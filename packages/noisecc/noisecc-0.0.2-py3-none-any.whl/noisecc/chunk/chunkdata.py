import h5py
import warnings
import textwrap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.dates import date2num
from noisecc.utils.viz_tools import _format_time_axis, _get_ax


class ChunkData(object):
    def __init__(
        self,
        data,
        dt,
        cc_len,
        cc_step,
        starttime,
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
        self.starttime = starttime
        self.time_norm = time_norm
        self.clip_std = clip_std
        self.smooth_N = smooth_N
        self.device = device
        self.jobs = jobs
        self.flag = flag

        # extract window info
        self.channel_num = data.shape[0]
        self.win_num = data.shape[1]
        self.npts = data.shape[2]
        self.win_time_interval = self.cc_len - self.cc_step
        self.endtime = self.starttime + (self.win_num - 1) * self.win_time_interval

    def __str__(self):
        stats = f"* STATS:\n{textwrap.indent(str(self.print_stats()), '  ')}"

        def format_number(num):
            formatted_num = f"{num:.6f}"
            return formatted_num if num < 0 else " " + formatted_num

        data_string = (
            f"[[[{format_number(self.data[0,0,0])} {format_number(self.data[0,0,1])} ... {format_number(self.data[0,0,-2])} {format_number(self.data[0,0,-1])}]\n"
            f"  [{format_number(self.data[0,1,0])} {format_number(self.data[0,1,1])} ... {format_number(self.data[0,1,-2])} {format_number(self.data[0,1,-1])}]\n"
            f"   ...\n"
            f"  [{format_number(self.data[0,-2,0])} {format_number(self.data[0,-2,1])} ... {format_number(self.data[0,-2,-2])} {format_number(self.data[0,-2,-1])}]\n"
            f"  [{format_number(self.data[0,-1,0])} {format_number(self.data[0,-1,1])} ... {format_number(self.data[0,-1,-2])} {format_number(self.data[0,-1,-1])}]],\n"
            f"  ...\n"
            f" [[{format_number(self.data[-1,0,0])} {format_number(self.data[-1,0,1])} ... {format_number(self.data[-1,0,-2])} {format_number(self.data[-1,0,-1])}]\n"
            f"  [{format_number(self.data[-1,1,0])} {format_number(self.data[-1,1,1])} ... {format_number(self.data[-1,1,-2])} {format_number(self.data[-1,1,-1])}]\n"
            f"   ...\n"
            f"  [{format_number(self.data[-1,-2,0])} {format_number(self.data[-1,-2,1])} ... {format_number(self.data[-1,-2,-2])} {format_number(self.data[-1,-2,-1])}]\n"
            f"  [{format_number(self.data[-1,-1,0])} {format_number(self.data[-1,-1,1])} ... {format_number(self.data[-1,-1,-2])} {format_number(self.data[-1,-1,-1])}]]]\n"
        )

        data = (
            "* DATA:\n"
            f"       shape: {self.data.shape} || (channel_num, win_num, npts)\n"
            f"       dtype: {self.data.dtype}\n"
            f"      masked: {np.ma.isMaskedArray(self.data)}\n"
            f"{textwrap.indent(data_string, '      ')}"
        )
        info = "\n".join([stats, data])
        return info

    def __repr__(self):
        return str(self)

    @property
    def stats(self):
        stats = dict(
            {
                "dt": self.dt,
                "cc_len": self.cc_len,
                "cc_step": self.cc_step,
                "starttime": self.starttime,
                "endtime": self.endtime,
                "channel_num": self.channel_num,
                "win_num": self.win_num,
                "npts": self.npts,
                "time_norm": self.time_norm,
                "clip_std": self.clip_std,
                "smooth_N": self.smooth_N,
                "device": self.device,
                "jobs": self.jobs,
                "flag": self.flag,
            }
        )
        return stats

    def print_stats(self, min_label_length=16):
        keys = list(self.stats.keys())
        i = max(max([len(k) for k in keys]), min_label_length)
        pattern = "%%%ds: %%s" % (i)
        head = []
        for k in keys:
            head.append(pattern % (k, self.stats[k]))

        return "\n".join(head)

    def save(
        self,
        save_path,
        compression=False,
        compression_format="gzip",
        compression_opts=3,
    ):
        with h5py.File(save_path, "w") as f:
            group = f.create_group("noisecc")
            group.attrs["dt"] = self.dt
            group.attrs["cc_len"] = self.cc_len
            group.attrs["cc_step"] = self.cc_step
            group.attrs["starttime"] = str(self.starttime)
            group.attrs["time_norm"] = self.time_norm
            group.attrs["clip_std"] = self.clip_std
            group.attrs["smooth_N"] = self.smooth_N
            group.attrs["device"] = self.device
            group.attrs["jobs"] = self.jobs
            group.attrs["flag"] = self.flag
            if compression:
                group.create_dataset(
                    "data",
                    data=self.data,
                    compression=compression_format,
                    compression_opts=compression_opts,
                )
            else:
                group.create_dataset("data", data=self.data)

    def plot(
        self,
        channel_index=0,
        win_start=None,
        win_end=None,
        win_interval=1,
        amp_scale=1,
        npts_axis="x",
        invert_x=False,
        invert_y=False,
        npts_minticks=5,
        npts_maxticks=None,
        win_minticks=5,
        win_maxticks=None,
        nptstick_rotation=0,
        nptstick_labelsize=10,
        winstick_rotation=0,
        winstick_labelsize=10,
        ax=None,
        color=None,
        linewidth=1,
        linestyle="-",
        alpha=1,
        figsize=(10, 5),
        show=True,
        save_path=None,
        dpi=100,
    ):
        # check data memory [cpu or gpu]
        if self.device == "cuda":
            pass

        # check win_start and win_end
        if win_start is None:
            win_start = int(0)
        if win_end is None:
            win_end = int(self.win_num)

        # init win_axis
        if npts_axis == "x":
            win_axis = "y"
        elif npts_axis == "y":
            win_axis = "x"
        else:
            raise ValueError("'npts_axis' must be 'x' or 'y'")

        # normalize data
        data = (
            self.data[channel_index, :, :].copy()
            / np.max(np.abs(self.data[channel_index, :, :]))
            / 2
        ).astype(np.float64)

        # set times
        npts_times_ns = (1e9 * np.arange(self.npts) * self.dt).astype(np.int64)
        time_deltas_timedelta64 = npts_times_ns * np.timedelta64(1, "ns")
        datenpts_times = (
            np.datetime64(self.starttime.datetime) + time_deltas_timedelta64
        )
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", FutureWarning)
            npts_times = pd.Series(datenpts_times).dt.to_pydatetime()
            npts_times = np.array(npts_times)
        npts_times_start = npts_times[0]
        npts_times_end = npts_times[-1]

        # set win times
        date2num_real_start = float(date2num(self.starttime.datetime))
        number_interval = float(win_interval)
        date2num_internal = float(self.win_time_interval * win_interval * 1 / 86400)

        # set color
        if color is None:
            color = ["#B2000F", "#004C12", "#847200", "#0E01FF"]
        elif type(color) is str:
            color = [color]

        # set ax
        ax = _get_ax(ax, figsize=figsize)

        # plot data
        for i, chan in enumerate(range(win_start, win_end, win_interval)):
            number_real = data[chan, :] * win_interval * amp_scale + chan
            date2num_real = (
                date2num_internal * number_real / number_interval + date2num_real_start
            )
            if npts_axis == "x":
                ax.plot(
                    npts_times,
                    date2num_real,
                    linewidth=linewidth,
                    color=color[i % len(color)],
                    alpha=alpha,
                    linestyle=linestyle,
                )
            elif npts_axis == "y":
                ax.plot(
                    date2num_real,
                    npts_times,
                    linewidth=linewidth,
                    color=color[i % len(color)],
                    alpha=alpha,
                    linestyle=linestyle,
                )

        _format_time_axis(
            ax,
            axis=npts_axis,
            tick_rotation=nptstick_rotation,
            minticks=npts_minticks,
            maxticks=npts_maxticks,
            labelsize=nptstick_labelsize,
        )

        _format_time_axis(
            ax,
            axis=win_axis,
            tick_rotation=winstick_rotation,
            minticks=win_minticks,
            maxticks=win_maxticks,
            labelsize=winstick_labelsize,
        )

        fig = ax.figure
        if npts_axis == "x":
            ax.set_xlim(npts_times_start, npts_times_end)
        elif npts_axis == "y":
            ax.set_ylim(npts_times_start, npts_times_end)
        if invert_x:
            ax.invert_xaxis()
        if invert_y:
            ax.invert_yaxis()
        if show:
            plt.show()
        else:
            plt.close(fig)
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
        else:
            return ax
