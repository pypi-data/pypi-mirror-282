import scipy
import numpy as np

from tqdm import tqdm
from joblib import Parallel, delayed
from noisecc.utils.whiten import moving_ave_cpu, moving_ave_cuda


def xcorr_cpu(source_data, receiver_data):
    rfft_corr_data = np.conj(source_data) * receiver_data

    return rfft_corr_data


def deconv_cpu(source_data, receiver_data, smoothspect_N):
    win_num = source_data.shape[0]
    rfft_npts = source_data.shape[1]
    ss_data = np.empty((win_num, rfft_npts), dtype=source_data.dtype)

    for i in range(win_num):
        ss = source_data[i, :]
        temp = moving_ave_cpu(np.abs(ss), smoothspect_N)
        temp = temp**2
        ss_data[i] = np.divide(
            ss, temp, out=np.zeros_like(ss, dtype=ss.dtype), where=temp != 0
        )

    rfft_corr_data = np.conj(ss_data) * receiver_data

    return rfft_corr_data


def coherency_cpu(source_data, receiver_data, smoothspect_N):
    win_num = source_data.shape[0]
    rfft_npts = source_data.shape[1]

    ss_data = np.empty((win_num, rfft_npts), dtype=source_data.dtype)
    rr_data = np.empty((win_num, rfft_npts), dtype=source_data.dtype)

    for i in range(win_num):
        ss = source_data[i, :]
        rr = receiver_data[i, :]
        ss_temp = moving_ave_cpu(np.abs(ss), smoothspect_N)
        rr_temp = moving_ave_cpu(np.abs(rr), smoothspect_N)
        ss_data[i] = np.divide(
            ss, ss_temp, out=np.zeros_like(ss, dtype=ss.dtype), where=ss_temp != 0
        )
        rr_data[i] = np.divide(
            rr, rr_temp, out=np.zeros_like(rr, dtype=rr.dtype), where=rr_temp != 0
        )

    rfft_corr_data = np.conj(ss_data) * rr_data

    return rfft_corr_data


class CorrClass(object):
    def __init__(
        self,
        data,
        dt,
        pairs,
        method,
        domain,
        maxlag,
        fstride,
        smoothspect_N,
        device,
        jobs,
        flag,
    ):
        # initialize parameters
        self.data = data
        self.dt = dt
        self.method = method
        self.pairs = pairs
        self.maxlag = maxlag
        self.fstride = fstride
        self.smoothspect_N = smoothspect_N
        self.domain = domain
        self.device = device
        self.jobs = jobs
        self.flag = flag

        # extract window info
        self.pairs_num = pairs.shape[0]
        self.win_num = data.shape[1]
        self.rfft_npts = data.shape[2]

        # compute domain parameters
        if self.domain == "time":
            # note that length of irfft is 2*(rfft_npts - 1), time rerange as: --maxlag---0---maxlag--, and will have 1 sampling ponit deviation
            t = np.arange(-self.rfft_npts + 1, self.rfft_npts - 1) * dt
            ind = np.where(np.abs(t) <= maxlag)[0]
            self.maxlag_npts = ind.size
            self.maxlag_start_npts = ind[0]
            self.maxlag_end_npts = ind[-1] + 1
        elif self.domain == "freq":
            self.output_freq_npts = len(np.arange(0, self.rfft_npts, fstride))

    def corr_cpu(self, source_data, receiver_data):
        if self.method == "xcorr":
            rfft_corr_data = xcorr_cpu(source_data, receiver_data)
        elif self.method == "deconv":
            rfft_corr_data = deconv_cpu(source_data, receiver_data, self.smoothspect_N)
        elif self.method == "coherency":
            rfft_corr_data = coherency_cpu(
                source_data, receiver_data, self.smoothspect_N
            )
        else:
            raise ValueError("method must be 'xcorr', 'coherency', or 'deconv'")

        return rfft_corr_data

    def corr_cuda(self, source_data, receiver_data):
        pass

    def irfft_cpu(self, rfft_corr_data):
        irfft_data = scipy.fft.irfft(rfft_corr_data, axis=-1)
        corr_data = np.roll(irfft_data, self.rfft_npts - 1, axis=-1)

        return corr_data

    def irfft_cuda(self, rfft_corr_data):
        pass

    def process_cpu(self, pair_index):
        # corr
        ss_index = int(self.pairs[pair_index, 0])
        rr_index = int(self.pairs[pair_index, 1])
        rfft_corr_data = self.corr_cpu(self.data[ss_index], self.data[rr_index])

        if self.domain == "time":
            # irfft
            time_corr_data = self.irfft_cpu(rfft_corr_data)
            # cut maxlag
            maxlag_corr_data = time_corr_data[
                :, self.maxlag_start_npts : self.maxlag_end_npts
            ]

            return maxlag_corr_data

        elif self.domain == "freq":
            fstride_corr_data = rfft_corr_data[:, :: self.fstride]

            return fstride_corr_data

    def process_cuda(self):
        pass

    def run(self):
        if self.device == "cpu":
            # initialize output_data
            if self.domain == "time":
                dtype_mapping = {np.complex64: np.float32, np.complex128: np.float64}
                try:
                    dtype = dtype_mapping[self.data.dtype.type]
                except KeyError:
                    raise ValueError(
                        f"Data type {self.data.dtype} is not supported for irfft."
                    )
                self.output_data = np.empty(
                    (self.pairs_num, self.win_num, self.maxlag_npts),
                    dtype=dtype,
                )
            elif self.domain == "freq":
                self.output_data = np.empty(
                    (self.pairs_num, self.win_num, self.output_freq_npts),
                    dtype=self.data.dtype,
                )

            # initialize pbar
            if self.flag:
                pbar = tqdm(
                    range(0, self.pairs_num),
                    desc=f"Corr via {self.jobs} jobs in CPU",
                )
            else:
                pbar = range(0, self.pairs_num)

            # serial processing
            if self.jobs == 1:
                for i in pbar:
                    self.output_data[i] = self.process_cpu(i)
            # parallel processing
            elif self.jobs > 1:
                results = Parallel(n_jobs=self.jobs, backend="loky")(
                    delayed(self.process_cpu)(i) for i in pbar
                )
                print("assembling results ...", flush=True) if self.flag else None
                for i, result in enumerate(results):
                    self.output_data[i] = result
                print("assembling results done", flush=True) if self.flag else None
            else:
                raise ValueError("'jobs' must be larger than 0.")

            # close pbar
            if self.flag:
                pbar.close()
        elif self.device == "cuda":
            self.output_data = self.process_cuda(self.data)
        else:
            raise ValueError("'device' must be 'cpu' or 'cuda'")
