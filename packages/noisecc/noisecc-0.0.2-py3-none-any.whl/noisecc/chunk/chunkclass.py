import numpy as np

from tqdm import tqdm
from joblib import Parallel, delayed
from noisecc.utils.split import slice_window
from noisecc.utils.whiten import moving_ave_cpu, moving_ave_cuda


def onebit_cpu(data):
    time_norm_data = np.sign(data)

    return time_norm_data


def onebit_cuda(data):
    pass


def clip_cpu(data, clip_std):
    lim = clip_std * np.std(data)
    time_norm_data = np.clip(data, -lim, lim)

    return time_norm_data


def clip_cuda(data, clip_std):
    pass


def ramn_cpu(data, smooth_N):
    # running absolute mean normalization
    temp = moving_ave_cpu(np.abs(data), smooth_N)
    time_norm_data = np.divide(
        data, temp, out=np.zeros_like(data, dtype=data.dtype), where=temp != 0
    )

    return time_norm_data


def ramn_cuda(data, smooth_N):
    temp = moving_ave_cuda(np.abs(data), smooth_N)
    pass


class ChunkClass(object):
    def __init__(
        self,
        data,
        dt,
        cc_len,
        cc_step,
        time_norm,
        clip_std,
        smooth_N,
        device,
        jobs,
        flag,
    ):
        # initialize parameters
        self.data = data
        self.dt = dt
        self.cc_len = cc_len
        self.cc_step = cc_step
        self.time_norm = time_norm
        self.clip_std = clip_std
        self.smooth_N = smooth_N
        self.device = device
        self.jobs = jobs
        self.flag = flag

        # convert time to npts
        self.cc_len_npts = round(cc_len / dt)
        self.cc_step_npts = round(cc_step / dt)
        self.npts = data.shape[1]
        self.channel_num = data.shape[0]

        # slice_window --> win_num, win_info
        self.win_info = slice_window(self.npts, self.cc_len_npts, self.cc_step_npts)
        self.win_num = self.win_info.shape[0]

    def time_norm_cpu(self, data):
        time_norm_data = None
        if self.time_norm == "no":
            time_norm_data = data
        elif self.time_norm == "onebit":
            time_norm_data = onebit_cpu(data)
        elif self.time_norm == "clip":
            time_norm_data = clip_cpu(data, self.clip_std)
        elif self.time_norm == "ramn":
            time_norm_data = ramn_cpu(data, self.smooth_N)
        else:
            raise ValueError("'time_norm' must be 'no', 'clip', 'onebit', or 'ramn'.")

        return time_norm_data

    def time_norm_cuda(self, data):
        pass

    def slide_cpu(self, time_norm_data):
        slide_data = np.empty((self.win_num, self.cc_len_npts), dtype=self.data.dtype)
        for i in range(self.win_num):
            slide_data[i] = time_norm_data[self.win_info[i, 0] : self.win_info[i, 1]]

        return slide_data

    def slide_cuda(self, time_norm_data):
        pass

    def process_cpu(self, channel):
        time_norm_data = self.time_norm_cpu(self.data[channel])
        slide_data = self.slide_cpu(time_norm_data)

        return slide_data

    def process_cuda(self):
        pass

    def run(self):
        if self.device == "cpu":
            # initialize output_data
            self.output_data = np.empty(
                (self.channel_num, self.win_num, self.cc_len_npts),
                dtype=self.data.dtype,
            )

            # initialize pbar
            if self.flag:
                pbar = tqdm(
                    range(0, self.channel_num),
                    desc=f"Chunk via {self.jobs} jobs in CPU",
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
