import scipy
import numpy as np

from tqdm import tqdm
from joblib import Parallel, delayed
from noisecc.utils.whiten import whiten_cpu, whiten_cuda


class RFFTClass(object):
    def __init__(
        self,
        data,
        dt,
        freq_norm,
        freqmin,
        freqmax,
        whiten_npad,
        smoothspect_N,
        device,
        jobs,
        flag,
    ):
        # initialize parameters
        self.data = data
        self.dt = dt
        self.freq_norm = freq_norm
        self.freqmin = freqmin
        self.freqmax = freqmax
        self.whiten_npad = whiten_npad
        self.smoothspect_N = smoothspect_N
        self.device = device
        self.jobs = jobs
        self.flag = flag

        # extract window info
        self.channel_num = data.shape[0]
        self.win_num = data.shape[1]
        self.cc_len_npts = data.shape[2]
        self.rfft_npts = self.cc_len_npts // 2 + 1
        self.df = 1 / (self.cc_len_npts * dt)

    def rfft_cpu(self, data):
        rfft_data = scipy.fft.rfft(data, axis=-1)

        return rfft_data

    def rfft_cuda(self, data):
        pass

    def freq_norm_cpu(self, rfft_data):
        freq_norm_data = None
        if self.freq_norm == "no":
            freq_norm_data = rfft_data
        else:
            freq_norm_data = whiten_cpu(
                rfft_data,
                self.dt,
                self.freq_norm,
                self.freqmin,
                self.freqmax,
                self.smoothspect_N,
                self.whiten_npad,
            )

        return freq_norm_data

    def freq_norm_cuda(self, rfft_data):
        pass

    def process_cpu(self, channel):
        rfft_data = self.rfft_cpu(self.data[channel])
        freq_norm_rfft_data = self.freq_norm_cpu(rfft_data)

        return freq_norm_rfft_data

    def process_cuda(self):
        pass

    def run(self):
        if self.device == "cpu":
            # initialize output_data
            dtype_mapping = {np.float32: np.complex64, np.float64: np.complex128}
            try:
                complex_dtype = dtype_mapping[self.data.dtype.type]
            except KeyError:
                raise ValueError(
                    f"Data type {self.data.dtype} is not supported for RFFT."
                )
            self.output_data = np.empty(
                (self.channel_num, self.win_num, self.rfft_npts),
                dtype=complex_dtype,
            )

            # initialize pbar
            if self.flag:
                pbar = tqdm(
                    range(0, self.channel_num),
                    desc=f"RFFT via {self.jobs} jobs in CPU",
                )
            else:
                pbar = range(0, self.channel_num)

            # serial processing
            if self.jobs == 1:
                for i in pbar:
                    self.output_data[i] = self.process_cpu(i)
            # parallel processing
            elif self.jobs > 1:
                results = Parallel(n_jobs=self.jobs, backend="loky")(
                    delayed(self.process_cpu)(channel) for channel in pbar
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
