import numpy as np

from tqdm import tqdm
from joblib import Parallel, delayed
from noisecc.stack.utils import stacklib, stacklib_freq
from noisecc.utils.split import slice_window


class StackClass(object):
    def __init__(
        self,
        data,
        dt,
        df,
        pairs_dist,
        dist_unit,
        stack_all,
        stack_len,
        stack_step,
        method,
        config,
        device,
        jobs,
        flag,
    ):
        # initialize parameters
        self.data = data
        self.dt = dt
        self.df = df
        self.pairs_dist = pairs_dist
        self.dist_unit = dist_unit
        self.stack_all = stack_all
        self.stack_len = stack_len
        self.stack_step = stack_step
        self.method = method
        self.config = config
        self.device = device
        self.jobs = jobs
        self.flag = flag

        # extract window info
        self.pairs_num = data.shape[0]
        self.corr_win_num = data.shape[1]
        self.npts = data.shape[2]

        # slice_window --> stack_win_num, win_info
        if stack_all:
            self.win_info = np.array([[0, self.corr_win_num]])
            self.stack_win_num = 1
        else:
            self.win_info = slice_window(self.corr_win_num, stack_len, stack_step)
            self.stack_win_num = int(self.win_info.shape[0])

    def process_cpu(self, pair_index):
        info = np.empty(self.stack_win_num, dtype=object)
        ngood = np.empty(self.stack_win_num)
        stack_data = np.empty((self.stack_win_num, self.npts), dtype=self.data.dtype)
        for i in range(0, self.stack_win_num):
            pick_index = np.arange(self.win_info[i, 0], self.win_info[i, 1])
            if len(pick_index) == 0:
                stack_data[i, :] = np.zeros(self.npts)
            else:
                pick_data = self.data[pair_index, pick_index, :]
                if self.dt != None and self.df == None:
                    stack_data[i, :], ngood[i], info[i] = stacklib(
                        pick_data,
                        self.dt,
                        self.pairs_dist[pair_index],
                        self.dist_unit,
                        self.method,
                        self.config,
                        "cpu",
                    )
                elif self.dt == None and self.df != None:
                    stack_data[i, :], ngood[i], info[i] = stacklib_freq(
                        pick_data,
                        self.df,
                        self.pairs_dist[pair_index],
                        self.dist_unit,
                        self.method,
                        self.config,
                        "cpu",
                    )

        return stack_data, ngood, info

    def process_cuda(self):
        pass

    def run(self):
        if self.device == "cpu":
            # initialize ngood and output_data
            self.info = np.empty((self.pairs_num, self.stack_win_num), dtype=object)
            self.ngood = np.empty((self.pairs_num, self.stack_win_num))
            self.output_data = np.empty(
                (self.pairs_num, self.stack_win_num, self.npts),
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
                    self.output_data[i], self.ngood[i], self.info[i] = self.process_cpu(
                        i
                    )
            # parallel processing
            elif self.jobs > 1:
                results = Parallel(n_jobs=self.jobs, backend="loky")(
                    delayed(self.process_cpu)(i) for i in pbar
                )
                print("assembling results ...", flush=True) if self.flag else None
                for i, result in enumerate(results):
                    self.output_data[i], self.ngood[i], self.info[i] = result
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
