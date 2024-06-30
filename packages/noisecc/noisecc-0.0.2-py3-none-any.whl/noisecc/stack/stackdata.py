import h5py
import json
import scipy
import textwrap
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from matplotlib.dates import date2num
from obspy.signal.filter import bandpass
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from noisecc.utils.viz_tools import (
    _format_time_axis,
    _get_ax,
    get_color_gradient,
)


class StackData(object):
    def __init__(
        self,
        tdata,
        fdata,
        dt,
        df,
        domain,
        ngood,
        info,
        ccwin_time_interval,
        starttime,
        pairs,
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
        self.domain = domain
        self.ngood = ngood
        self.info = info
        self.ccwin_time_interval = ccwin_time_interval
        self.starttime = starttime
        self.pairs = pairs
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
        if domain == "time":
            self.t_mark = True
            self.f_mark = False
            # share
            self.pairs_num = tdata.shape[0]
            self.win_num = tdata.shape[1]
            # time
            self.tdata = tdata
            self.dt = dt
            self.time_npts = tdata.shape[2]
            self.maxlag = dt * (self.time_npts - 1) / 2  # -dt, avoid float-point error
            self.time_vector = np.arange(-self.maxlag, self.maxlag + dt, dt)
            # freq
            self.fdata = None
            self.df = None
            self.freq_npts = None
            self.maxfreq = None
        elif domain == "freq":
            self.t_mark = False
            self.f_mark = True
            # share
            self.pairs_num = fdata.shape[0]
            self.win_num = fdata.shape[1]
            # time
            self.tdata = None
            self.dt = None
            self.time_npts = None
            self.maxlag = None
            # freq
            self.fdata = fdata
            self.df = df
            self.freq_npts = fdata.shape[2]
            self.freq_vector = df * np.arange(0, self.freq_npts)
            self.maxfreq = self.freq_vector[-1]  # or df * (self.freq_npts - 1)

        # compute win_time_interval and endtime
        self.win_time_interval = (stack_len - stack_step) * ccwin_time_interval
        self.endtime = self.starttime + (self.win_num - 1) * self.win_time_interval

    def __str__(self):
        stats = f"* STATS:\n{textwrap.indent(str(self.print_stats()), '  ')}"

        config = f"* CONFIG:\n{textwrap.indent(str(self.print_config()), '  ')}"

        pairs = (
            f"* PAIRS:\n"
            f"         pairs_num: {self.pairs.shape[0]}\n"
            f"{textwrap.indent(np.array2string(self.pairs, threshold=10), '                    ')}"
        )

        pairs_dist = (
            f"* PAIRS DIST:\n"
            f"         pairs_num: {self.pairs.shape[0]}\n"
            f"{textwrap.indent(np.array2string(self.pairs_dist, threshold=10), '                    ')}"
        )

        def format_number(num):
            formatted_num = f"{num:.6f}"
            return formatted_num if num < 0 else " " + formatted_num

        def format_data(domain):
            if domain == "time":
                dd = self.tdata
            elif domain == "freq":
                dd = self.fdata

            if self.stack_all or dd.shape[1] <= 2:
                data_string = (
                    f"[[[{format_number(dd[0,0,0])} {format_number(dd[0,0,1])} ... {format_number(dd[0,0,-2])} {format_number(dd[0,0,-1])}]],\n"
                    f"  ...\n"
                    f" [[{format_number(dd[-1,0,0])} {format_number(dd[-1,0,1])} ... {format_number(dd[-1,0,-2])} {format_number(dd[-1,0,-1])}]]]\n"
                )
            else:
                data_string = (
                    f"[[[{format_number(dd[0,0,0])} {format_number(dd[0,0,1])} ... {format_number(dd[0,0,-2])} {format_number(dd[0,0,-1])}]\n"
                    f"  [{format_number(dd[0,1,0])} {format_number(dd[0,1,1])} ... {format_number(dd[0,1,-2])} {format_number(dd[0,1,-1])}]\n"
                    f"   ...\n"
                    f"  [{format_number(dd[0,-2,0])} {format_number(dd[0,-2,1])} ... {format_number(dd[0,-2,-2])} {format_number(dd[0,-2,-1])}]\n"
                    f"  [{format_number(dd[0,-1,0])} {format_number(dd[0,-1,1])} ... {format_number(dd[0,-1,-2])} {format_number(dd[0,-1,-1])}]],\n"
                    f"  ...\n"
                    f" [[{format_number(dd[-1,0,0])} {format_number(dd[-1,0,1])} ... {format_number(dd[-1,0,-2])} {format_number(dd[-1,0,-1])}]\n"
                    f"  [{format_number(dd[-1,1,0])} {format_number(dd[-1,1,1])} ... {format_number(dd[-1,1,-2])} {format_number(dd[-1,1,-1])}]\n"
                    f"   ...\n"
                    f"  [{format_number(dd[-1,-2,0])} {format_number(dd[-1,-2,1])} ... {format_number(dd[-1,-2,-2])} {format_number(dd[-1,-2,-1])}]\n"
                    f"  [{format_number(dd[-1,-1,0])} {format_number(dd[-1,-1,1])} ... {format_number(dd[-1,-1,-2])} {format_number(dd[-1,-1,-1])}]]]\n"
                )
            return data_string

        if self.t_mark is True and self.f_mark is not True:
            data_string = format_data("time")
            data = (
                "* TDATA:\n"
                f"       shape: {self.tdata.shape} || (pairs_num, win_num, time_npts)\n"
                f"       dtype: {self.tdata.dtype}\n"
                f"      masked: {np.ma.isMaskedArray(self.tdata)}\n"
                f"{textwrap.indent(data_string, '      ')}"
                f"* FDATA: None\n"
            )
        elif self.t_mark is not True and self.f_mark is True:
            data_string = format_data("freq")
            data = (
                "* TDATA: None\n"
                f"* FDATA:\n"
                f"       shape: {self.fdata.shape} || (pairs_num, win_num, freq_npts)\n"
                f"       dtype: {self.fdata.dtype}\n"
                f"      masked: {np.ma.isMaskedArray(self.fdata)}\n"
                f"{textwrap.indent(data_string, '      ')}"
            )
        elif self.t_mark is True and self.f_mark is True:
            tdata_string = format_data("time")
            fdata_string = format_data("freq")
            data = (
                "* TDATA:\n"
                f"       shape: {self.tdata.shape} || (pairs_num, win_num, time_npts)\n"
                f"       dtype: {self.tdata.dtype}\n"
                f"      masked: {np.ma.isMaskedArray(self.tdata)}\n"
                f"{textwrap.indent(tdata_string, '      ')}"
                f"* FDATA:\n"
                f"       shape: {self.fdata.shape} || (pairs_num, win_num, freq_npts)\n"
                f"       dtype: {self.fdata.dtype}\n"
                f"      masked: {np.ma.isMaskedArray(self.fdata)}\n"
                f"{textwrap.indent(fdata_string, '      ')}"
            )
        else:
            raise ValueError("tdata and fdata are both None")

        info = "\n".join([stats, config, pairs, pairs_dist, data])
        return info

    def __repr__(self):
        return str(self)

    @property
    def stats(self):
        stats = dict(
            {
                "domain": self.domain,
                # time
                "dt": self.dt,
                "maxlag": self.maxlag,
                "time_npts": self.time_npts,
                # freq
                "df": self.df,
                "maxfreq": self.maxfreq,
                "freq_npts": self.freq_npts,
                # timeinfo
                "starttime": self.starttime,
                "endtime": self.endtime,
                "win_time_interval": self.win_time_interval,
                "win_num": self.win_num,
                "pairs_num": self.pairs_num,
                "dist_unit": self.dist_unit,
                "stack_all": self.stack_all,
                "stack_len": self.stack_len,
                "stack_step": self.stack_step,
                "method": self.method,
                "device": self.device,
                "jobs": self.jobs,
                "flag": self.flag,
                "ngood": "(maybe too long to display)",
                "info": "(maybe too long to display)",
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

    def print_config(self, min_label_length=16):
        keys = list(self.config.keys())
        if len(keys) == 0:
            return "\t None"
        else:
            i = max(max([len(k) for k in keys]), min_label_length)
            pattern = "%%%ds: %%s" % (i)
            head = []
            for k in keys:
                head.append(pattern % (k, self.config[k]))

            return "\n".join(head)

    def calculate_timedata(self, workers=1):
        if self.t_mark is True:
            raise ValueError("tdata is already calculated")
        irfft_data = scipy.fft.irfft(self.fdata, axis=-1, workers=workers)
        self.tdata = np.roll(irfft_data, self.freq_npts - 1, axis=-1)
        self.dt = 1 / (2 * (self.freq_npts - 1) * self.df)
        self.maxlag = (self.freq_npts - 2) * self.dt
        self.time_vector = np.arange(-self.maxlag, self.maxlag + self.dt, self.dt)
        self.time_npts = len(self.time_vector)
        self.t_mark = True

    def calculate_freqdata(self, workers=1):
        if self.f_mark is True:
            raise ValueError("fdata is already calculated")
        tdata = np.roll(self.tdata, self.time_npts // 2, axis=-1)
        self.fdata = scipy.fft.rfft(tdata, axis=-1, workers=workers)
        self.df = 1 / (self.time_npts * self.dt)
        self.freq_vector = scipy.fft.rfftfreq(self.time_npts, self.dt)
        self.freq_npts = len(self.freq_vector)
        self.maxfreq = self.freq_vector[-1]
        self.f_mark = True

    def save(
        self,
        save_path,
        type="time",
        compression=False,
        compression_format="gzip",
        compression_opts=3,
    ):
        if type == "time":
            with h5py.File(save_path, "w") as f:
                group = f.create_group("noisecc")
                group.attrs["dt"] = self.dt
                group.attrs["domain"] = "time"
                group.create_dataset("ngood", data=self.ngood)
                group.attrs["ccwin_time_interval"] = self.ccwin_time_interval
                group.attrs["starttime"] = str(self.starttime)
                group.create_dataset("pairs", data=self.pairs)
                group.create_dataset("pairs_dist", data=self.pairs_dist)
                group.attrs["dist_unit"] = self.dist_unit
                group.attrs["stack_all"] = self.stack_all
                group.attrs["stack_len"] = self.stack_len
                group.attrs["stack_step"] = self.stack_step
                group.attrs["method"] = self.method
                group.attrs["config"] = json.dumps(self.config)
                group.attrs["device"] = self.device
                group.attrs["jobs"] = self.jobs
                group.attrs["flag"] = self.flag
                if compression:
                    group.create_dataset(
                        "data",
                        data=self.tdata,
                        compression=compression_format,
                        compression_opts=compression_opts,
                    )
                else:
                    group.create_dataset("data", data=self.tdata)

        elif type == "freq":
            with h5py.File(save_path, "w") as f:
                group = f.create_group("noisecc")
                group.attrs["df"] = self.df
                group.attrs["domain"] = "freq"
                group.create_dataset("ngood", data=self.ngood)
                group.attrs["ccwin_time_interval"] = self.ccwin_time_interval
                group.attrs["starttime"] = str(self.starttime)
                group.create_dataset("pairs", data=self.pairs)
                group.create_dataset("pairs_dist", data=self.pairs_dist)
                group.attrs["dist_unit"] = self.dist_unit
                group.attrs["stack_all"] = self.stack_all
                group.attrs["stack_len"] = self.stack_len
                group.attrs["stack_step"] = self.stack_step
                group.attrs["method"] = self.method
                group.attrs["config"] = json.dumps(self.config)
                group.attrs["device"] = self.device
                group.attrs["jobs"] = self.jobs
                group.attrs["flag"] = self.flag
                if compression:
                    group.create_dataset(
                        "data",
                        data=self.fdata,
                        compression=compression_format,
                        compression_opts=compression_opts,
                    )
                else:
                    group.create_dataset("data", data=self.fdata)

    # plot
    def plot(
        self,
        pair_index=0,
        win_start=None,
        win_end=None,
        win_interval=1,
        mean_win_interval=False,
        lag_start=None,
        lag_end=None,
        amp_normalize=True,
        amp_scale=1,
        mean_amp_scale=1,
        filter=False,
        freqmin=0.0,
        freqmax=0.1,
        corners=4,
        zerophase=True,
        mode="waveform",
        npts_axis="x",
        colorbar=True,
        invert_x=False,
        invert_y=False,
        win_minticks=5,
        win_maxticks=None,
        winstick_rotation=0,
        winstick_labelsize=10,
        color="k",
        linewidth=1,
        linestyle="-",
        alpha=1,
        cmap="seismic",
        clip=[-1.0, 1.0],
        ngood=False,
        ngood_label=True,
        figsize=(10, 6),
        show=True,
        save_path=None,
        dpi=100,
    ):
        # check mark
        if self.t_mark is not True:
            raise ValueError("'tdata' is not calculated")

        # check pair_index
        if pair_index >= self.pairs_num:
            raise ValueError(f"'pair_index' must be <= {self.pairs_num}")

        # init win_axis
        if npts_axis == "x":
            win_axis = "y"
        elif npts_axis == "y":
            win_axis = "x"
        else:
            raise ValueError("'npts_axis' must be 'x' or 'y'")

        # check win_start and win_end
        if win_start is None:
            win_start = int(0)
        if win_end is None:
            win_end = int(self.win_num)

        # init lag_start
        if lag_start is None:
            lag_start = -self.maxlag
        if lag_start < -self.maxlag:
            raise ValueError(f"'lag_start' must be larger than -maxlag=-{self.maxlag}")

        # init lag_end
        if lag_end is None:
            lag_end = self.maxlag - self.dt
        if lag_end > self.maxlag:
            raise ValueError(f"'lag_end' must be smaller than maxlag={self.maxlag}")

        # set lag times
        lag_times = np.arange(lag_start, lag_end + self.dt, self.dt)
        lag_times_npts_start = round((lag_start + self.maxlag) / self.dt)
        lag_times_npts_end = lag_times_npts_start + len(lag_times)

        # set win times
        date2num_real_start = date2num(self.starttime.datetime)
        number_interval = 2
        date2num_internal = win_interval * self.win_time_interval * 1 / 86400
        win_start_datetime = (
            self.starttime + win_start * self.win_time_interval
        ).datetime
        win_end_datetime = (
            self.starttime + (win_end - 1) * self.win_time_interval
        ).datetime

        # select data
        win_index = np.arange(win_start, win_end, win_interval)
        if mean_win_interval and len(win_index) > 1:
            data = np.empty((len(win_index) - 1, len(lag_times)))
            for i in range(0, len(win_index) - 1):
                data[i, :] = np.mean(
                    self.tdata[
                        pair_index,
                        win_index[i] : win_index[i + 1],
                        lag_times_npts_start:lag_times_npts_end,
                    ].copy(),
                    axis=0,
                )
            data = data.astype(np.float64)
        else:
            data = self.tdata[
                pair_index, win_index, lag_times_npts_start:lag_times_npts_end
            ].copy()
            data = data.astype(np.float64)

        # check data dim
        if data.ndim == 1:
            data = data.reshape(1, -1)

        # filter
        if filter:
            sampling_rate = 1 / self.dt
            for i in range(0, data.shape[0]):
                data[i] = bandpass(
                    data[i],
                    freqmin,
                    freqmax,
                    sampling_rate,
                    corners=corners,
                    zerophase=zerophase,
                )

        # normalize
        if amp_normalize:
            scale = np.max(np.abs(data), axis=1)[:, None]
            for i in range(0, data.shape[0]):
                if scale[i] == 0:
                    data[i] = 0
                else:
                    data[i] = data[i] / scale[i]
        else:
            scale = np.max(np.abs(data))
            if scale != 0:
                data = data / scale
            else:
                raise ValueError("data is all zeros in amp_normalize=False")

        # init figure
        if ngood:
            ngood_axis_size = 1
        else:
            ngood_axis_size = 0
        if npts_axis == "x":
            fig, ax = plt.subplots(
                1,
                2,
                gridspec_kw=dict(width_ratios=[5, ngood_axis_size]),
                sharey="row",
                figsize=figsize,
            )
            fig.subplots_adjust(wspace=0.0)
        elif npts_axis == "y":
            fig, ax = plt.subplots(
                2,
                1,
                gridspec_kw=dict(height_ratios=[ngood_axis_size, 5]),
                sharex="col",
                figsize=figsize,
            )
            fig.subplots_adjust(hspace=0.0)

        # plot
        if mode == "waveform":
            for i in range(0, data.shape[0]):
                number_real = data[i, :] * amp_scale + i * 2
                date2num_real = (
                    date2num_internal * number_real / number_interval
                    + date2num_real_start
                )
                if npts_axis == "x":
                    ax[0].plot(
                        lag_times,
                        date2num_real,
                        linewidth=linewidth,
                        color=color,
                        alpha=alpha,
                        linestyle=linestyle,
                    )
                elif npts_axis == "y":
                    ax[1].plot(
                        date2num_real,
                        lag_times,
                        linewidth=linewidth,
                        color=color,
                        alpha=alpha,
                        linestyle=linestyle,
                    )
        elif mode == "mat":
            if npts_axis == "x":
                im = ax[0].imshow(
                    data,
                    extent=[lag_start, lag_end, win_start_datetime, win_end_datetime],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            elif npts_axis == "y":
                im = ax[1].imshow(
                    data.T,
                    extent=[win_start_datetime, win_end_datetime, lag_start, lag_end],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            else:
                raise ValueError("'npts_axis' must be 'x' or 'y'")

            # plot cc mean
            cc_mean = np.mean(data, axis=0)
            y_offset = (date2num(win_end_datetime) + date2num(win_start_datetime)) / 2
            y_total = date2num(win_end_datetime) - date2num(win_start_datetime)
            if npts_axis == "x":
                ax[0].plot(
                    lag_times,
                    mean_amp_scale * y_total / 10 * cc_mean + y_offset,
                    linewidth=linewidth,
                    color=color,
                    alpha=alpha,
                    linestyle=linestyle,
                )
            elif npts_axis == "y":
                ax[1].plot(
                    mean_amp_scale * y_total / 10 * cc_mean + y_offset,
                    lag_times,
                    linewidth=linewidth,
                    color=color,
                    alpha=alpha,
                    linestyle=linestyle,
                )
            else:
                raise ValueError("'npts_axis' must be 'x' or 'y'")
        else:
            raise ValueError("'mode' must be 'waveform' or 'mat'")

        # plot ngood
        if ngood:
            color1 = "#8A5AC2"
            color2 = "#3575D5"
            goods = self.ngood[pair_index, win_start:win_end]
            win_times = np.linspace(
                date2num(win_start_datetime), date2num(win_end_datetime), len(goods)
            )
            if npts_axis == "x":
                ax[1].barh(
                    win_times,
                    goods,
                    height=self.win_time_interval / 86400 / 1.2,
                    color=get_color_gradient(color1, color2, goods.shape[0]),
                )
                ax[1].set_xlabel("Ngood")
                ax[1].xaxis.set_major_locator(plt.MaxNLocator(integer=True, nbins=4))
                if not ngood_label:
                    ax[1].spines["top"].set_visible(False)
                    ax[1].spines["right"].set_visible(False)
                    ax[1].spines["bottom"].set_visible(False)
                    ax[1].spines["left"].set_visible(True)
                    ax[1].set_xticks([])
                    ax[1].set_yticks([])
            elif npts_axis == "y":
                ax[0].bar(
                    win_times,
                    goods,
                    width=self.win_time_interval / 86400 / 1.2,
                    color=get_color_gradient(color1, color2, goods.shape[0]),
                )
                ax[0].set_ylabel("Ngood")
                ax[0].yaxis.set_major_locator(plt.MaxNLocator(integer=True, nbins=4))
                if not ngood_label:
                    ax[0].spines["top"].set_visible(False)
                    ax[0].spines["right"].set_visible(False)
                    ax[0].spines["bottom"].set_visible(True)
                    ax[0].spines["left"].set_visible(False)
                    ax[0].set_xticks([])
                    ax[0].set_yticks([])
            else:
                raise ValueError("npts_axis must be 'x' or 'y'")
        else:
            if npts_axis == "x":
                ax[1].spines["top"].set_visible(False)
                ax[1].spines["right"].set_visible(False)
                ax[1].spines["bottom"].set_visible(False)
                ax[1].spines["left"].set_visible(True)
                ax[1].set_xticks([])
                ax[1].set_yticks([])
            elif npts_axis == "y":
                ax[0].spines["top"].set_visible(False)
                ax[0].spines["right"].set_visible(False)
                ax[0].spines["bottom"].set_visible(True)
                ax[0].spines["left"].set_visible(False)
                ax[0].set_xticks([])
                ax[0].set_yticks([])
            else:
                raise ValueError("'npts_axis' must be 'x' or 'y'")

        # format
        if npts_axis == "x":
            ax[0].set_title(
                f"StackData: pair=[{self.pairs[pair_index][0]}, {self.pairs[pair_index][1]}], filter=[{freqmin:.3f}, {freqmax:.3f}] hz"
            )
            _format_time_axis(
                ax[0],
                axis=win_axis,
                tick_rotation=winstick_rotation,
                minticks=win_minticks,
                maxticks=win_maxticks,
                labelsize=winstick_labelsize,
            )
            ax[0].set_xlim(lag_start, lag_end)
            ax[0].set_xlabel("Time(s)")
            if colorbar and mode == "mat":
                cbaxes = inset_axes(
                    ax[0], width="15%", height="4%", loc="upper right", borderpad=0.5
                )
                plt.colorbar(im, cax=cbaxes, orientation="horizontal")
            if invert_x:
                ax[0].invert_xaxis()
            if invert_y:
                ax[0].invert_yaxis()
                # ax[1].invert_yaxis() # don't need, cuz sharey="row" in plt.subplots
        elif npts_axis == "y":
            ax[0].set_title(
                f"StackData: pair=[{self.pairs[pair_index][0]}, {self.pairs[pair_index][1]}], filter=[{freqmin:.3f}, {freqmax:.3f}] hz"
            )
            _format_time_axis(
                ax[1],
                axis=win_axis,
                tick_rotation=winstick_rotation,
                minticks=win_minticks,
                maxticks=win_maxticks,
                labelsize=winstick_labelsize,
            )
            ax[1].set_ylim(lag_start, lag_end)
            ax[1].set_ylabel("Time(s)")
            if colorbar and mode == "mat":
                cbaxes = inset_axes(
                    ax[1], width="15%", height="4%", loc="upper right", borderpad=0.5
                )
                plt.colorbar(im, cax=cbaxes, orientation="horizontal")
            if invert_x:
                # ax[0].invert_xaxis() # don't need, cuz sharex="col" in plt.subplots
                ax[1].invert_xaxis()
            if invert_y:
                ax[1].invert_yaxis()
        if show:
            plt.show()
        else:
            plt.close(fig)
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi)  # bbox_inches="tight"
        else:
            return ax

    # plot
    def fplot(
        self,
        pair_index=0,
        win_start=None,
        win_end=None,
        win_interval=1,
        mean_win_interval=False,
        freq_start=None,
        freq_end=None,
        amp="real",  # 'real', 'imag', 'abs'
        amp_normalize=True,
        amp_scale=1,
        mean_amp_scale=1,
        mode="waveform",
        npts_axis="x",
        log=False,
        colorbar=True,
        invert_x=False,
        invert_y=False,
        win_minticks=5,
        win_maxticks=None,
        winstick_rotation=0,
        winstick_labelsize=10,
        color="k",
        linewidth=1,
        linestyle="-",
        alpha=1,
        cmap="seismic",
        clip=[-1.0, 1.0],
        ngood=False,
        ngood_label=True,
        figsize=(10, 6),
        show=True,
        save_path=None,
        dpi=100,
    ):
        # check mark
        if self.f_mark is not True:
            raise ValueError("'fdata' is not calculated")

        # check pair_index
        if pair_index >= self.pairs_num:
            raise ValueError(f"'pair_index' must be <= {self.pairs_num}")

        # init win_axis
        if npts_axis == "x":
            win_axis = "y"
        elif npts_axis == "y":
            win_axis = "x"
        else:
            raise ValueError("'npts_axis' must be 'x' or 'y'")

        # check win_start and win_end
        if win_start is None:
            win_start = int(0)
        if win_end is None:
            win_end = int(self.win_num)

        # init lag_start
        if freq_start is None:
            freq_start = 0
        if freq_start < 0:
            raise ValueError("'freq_start' must be >= 0")

        # init lag_end
        if freq_end is None:
            freq_end = self.maxfreq
        if freq_end > self.maxfreq:
            raise ValueError(f"'freq_end' must be <= (maxfreq={self.maxfreq})")

        # set lag freqs
        lag_freqs = np.arange(freq_start, freq_end + self.df, self.df)
        lag_freqs_npts_start = round(lag_freqs[0] / self.df)
        lag_freqs_npts_end = round(lag_freqs[-1] / self.df) + 1

        # set win times
        date2num_real_start = date2num(self.starttime.datetime)
        number_interval = 2
        date2num_internal = win_interval * self.win_time_interval * 1 / 86400
        win_start_datetime = (
            self.starttime + win_start * self.win_time_interval
        ).datetime
        win_end_datetime = (
            self.starttime + (win_end - 1) * self.win_time_interval
        ).datetime

        # select data
        win_index = np.arange(win_start, win_end, win_interval)
        if mean_win_interval and len(win_index) > 1:
            data = np.empty((len(win_index) - 1, len(lag_freqs)))
            for i in range(0, len(win_index) - 1):
                freq_data = self.fdata[
                    pair_index,
                    win_index[i] : win_index[i + 1],
                    lag_freqs_npts_start:lag_freqs_npts_end,
                ].copy()
                if amp == "real":
                    data[i, :] = np.mean(np.real(freq_data), axis=0)
                elif amp == "imag":
                    data[i, :] = np.mean(np.imag(freq_data), axis=0)
                elif amp == "abs":
                    data[i, :] = np.mean(np.abs(freq_data), axis=0)
        else:
            data = self.fdata[
                pair_index, win_index, lag_freqs_npts_start:lag_freqs_npts_end
            ].copy()
            if amp == "real":
                data = np.real(data)
            elif amp == "imag":
                data = np.imag(data)
            elif amp == "abs":
                data = np.abs(data)

        # normalize
        if amp_normalize:
            scale = np.max(np.abs(data), axis=1)[:, None]
            for i in range(0, data.shape[0]):
                if scale[i] == 0:
                    data[i] = 0
                else:
                    data[i] = data[i] / scale[i]
        else:
            scale = np.max(np.abs(data))
            if scale != 0:
                data = data / scale
            else:
                raise ValueError("data is all zeros in amp_normalize=False")

        # init figure
        if ngood:
            ngood_axis_size = 1
        else:
            ngood_axis_size = 0
        if npts_axis == "x":
            fig, ax = plt.subplots(
                1,
                2,
                gridspec_kw=dict(width_ratios=[5, ngood_axis_size]),
                sharey="row",
                figsize=figsize,
            )
            fig.subplots_adjust(wspace=0.0)
        elif npts_axis == "y":
            fig, ax = plt.subplots(
                2,
                1,
                gridspec_kw=dict(height_ratios=[ngood_axis_size, 5]),
                sharex="col",
                figsize=figsize,
            )
            fig.subplots_adjust(hspace=0.0)

        # plot
        if mode == "waveform":
            for i in range(0, data.shape[0]):
                number_real = data[i, :] * amp_scale + i * 2
                date2num_real = (
                    date2num_internal * number_real / number_interval
                    + date2num_real_start
                )
                if npts_axis == "x":
                    ax[0].plot(
                        lag_freqs,
                        date2num_real,
                        linewidth=linewidth,
                        color=color,
                        alpha=alpha,
                        linestyle=linestyle,
                    )
                elif npts_axis == "y":
                    ax[1].plot(
                        date2num_real,
                        lag_freqs,
                        linewidth=linewidth,
                        color=color,
                        alpha=alpha,
                        linestyle=linestyle,
                    )
        elif mode == "mat":
            if npts_axis == "x":
                im = ax[0].imshow(
                    data,
                    extent=[freq_start, freq_end, win_start_datetime, win_end_datetime],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            elif npts_axis == "y":
                im = ax[1].imshow(
                    data.T,
                    extent=[win_start_datetime, win_end_datetime, freq_start, freq_end],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            else:
                raise ValueError("'npts_axis' must be 'x' or 'y'")

            # plot cc mean
            cc_mean = np.mean(data, axis=0)
            y_offset = (date2num(win_end_datetime) + date2num(win_start_datetime)) / 2
            y_total = date2num(win_end_datetime) - date2num(win_start_datetime)
            if npts_axis == "x":
                ax[0].plot(
                    lag_freqs,
                    mean_amp_scale * y_total / 10 * cc_mean + y_offset,
                    linewidth=linewidth,
                    color=color,
                    alpha=alpha,
                    linestyle=linestyle,
                )
            elif npts_axis == "y":
                ax[1].plot(
                    mean_amp_scale * y_total / 10 * cc_mean + y_offset,
                    lag_freqs,
                    linewidth=linewidth,
                    color=color,
                    alpha=alpha,
                    linestyle=linestyle,
                )
            else:
                raise ValueError("'npts_axis' must be 'x' or 'y'")
        else:
            raise ValueError("'mode' must be 'waveform' or 'mat'")

        # plot ngood
        if ngood:
            color1 = "#8A5AC2"
            color2 = "#3575D5"
            goods = self.ngood[pair_index, win_start:win_end]
            win_times = np.linspace(
                date2num(win_start_datetime), date2num(win_end_datetime), len(goods)
            )
            if npts_axis == "x":
                ax[1].barh(
                    win_times,
                    goods,
                    height=self.win_time_interval / 86400 / 1.2,
                    color=get_color_gradient(color1, color2, goods.shape[0]),
                )
                ax[1].set_xlabel("Ngood")
                ax[1].xaxis.set_major_locator(plt.MaxNLocator(integer=True, nbins=4))
                if not ngood_label:
                    ax[1].spines["top"].set_visible(False)
                    ax[1].spines["right"].set_visible(False)
                    ax[1].spines["bottom"].set_visible(False)
                    ax[1].spines["left"].set_visible(True)
                    ax[1].set_xticks([])
                    ax[1].set_yticks([])
            elif npts_axis == "y":
                ax[0].bar(
                    win_times,
                    goods,
                    width=self.win_time_interval / 86400 / 1.2,
                    color=get_color_gradient(color1, color2, goods.shape[0]),
                )
                ax[0].set_ylabel("Ngood")
                ax[0].yaxis.set_major_locator(plt.MaxNLocator(integer=True, nbins=4))
                if not ngood_label:
                    ax[0].spines["top"].set_visible(False)
                    ax[0].spines["right"].set_visible(False)
                    ax[0].spines["bottom"].set_visible(True)
                    ax[0].spines["left"].set_visible(False)
                    ax[0].set_xticks([])
                    ax[0].set_yticks([])
            else:
                raise ValueError("'npts_axis' must be 'x' or 'y'")
        else:
            if npts_axis == "x":
                ax[1].spines["top"].set_visible(False)
                ax[1].spines["right"].set_visible(False)
                ax[1].spines["bottom"].set_visible(False)
                ax[1].spines["left"].set_visible(True)
                ax[1].set_xticks([])
                ax[1].set_yticks([])
            elif npts_axis == "y":
                ax[0].spines["top"].set_visible(False)
                ax[0].spines["right"].set_visible(False)
                ax[0].spines["bottom"].set_visible(True)
                ax[0].spines["left"].set_visible(False)
                ax[0].set_xticks([])
                ax[0].set_yticks([])
            else:
                raise ValueError("npts_axis must be 'x' or 'y'")

        # format

        # plt.colorbar(im, orientation="vertical", shrink=0.4)
        if npts_axis == "x":
            ax[0].set_title(
                f"StackData: pair=[{self.pairs[pair_index][0]}, {self.pairs[pair_index][1]}]"
            )
            _format_time_axis(
                ax[0],
                axis=win_axis,
                tick_rotation=winstick_rotation,
                minticks=win_minticks,
                maxticks=win_maxticks,
                labelsize=winstick_labelsize,
            )
            if log:
                ax[0].set_xscale("log")
            if colorbar and mode == "mat":
                cbaxes = inset_axes(
                    ax[0], width="15%", height="4%", loc="upper right", borderpad=0.5
                )
                plt.colorbar(im, cax=cbaxes, orientation="horizontal")
            ax[0].set_xlim(freq_start, freq_end)
            ax[0].set_xlabel("Freq(hz)")
            if invert_x:
                ax[0].invert_xaxis()
            if invert_y:
                ax[0].invert_yaxis()
                # ax[1].invert_yaxis() # don't need, cuz sharey="row" in plt.subplots
        elif npts_axis == "y":
            ax[0].set_title(
                f"StackData: pair=[{self.pairs[pair_index][0]}, {self.pairs[pair_index][1]}]"
            )
            _format_time_axis(
                ax[1],
                axis=win_axis,
                tick_rotation=winstick_rotation,
                minticks=win_minticks,
                maxticks=win_maxticks,
                labelsize=winstick_labelsize,
            )
            if log:
                ax[1].set_yscale("log")
            if colorbar and mode == "mat":
                cbaxes = inset_axes(
                    ax[1], width="15%", height="4%", loc="upper right", borderpad=0.5
                )
                plt.colorbar(im, cax=cbaxes, orientation="horizontal")
            ax[1].set_ylim(freq_start, freq_end)
            ax[1].set_ylabel("Freq(hz)")
            if invert_x:
                # ax[0].invert_xaxis() # don't need, cuz sharex="col" in plt.subplots
                ax[1].invert_xaxis()
            if invert_y:
                ax[1].invert_yaxis()
        if show:
            plt.show()
        else:
            plt.close(fig)
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi)  # bbox_inches="tight"
        else:
            return ax

    def plot_moveout(
        self,
        win_index=0,
        velocity=[],
        source_index=None,
        receiver_index=None,
        dist_start=None,
        dist_end=None,
        dist_interval=None,
        mean_dist_interval=False,
        amp_scale=1,
        amp_normalize=True,
        lag_start=None,
        lag_end=None,
        filter=False,
        freqmin=0.0,
        freqmax=0.1,
        corners=4,
        zerophase=True,
        mode="waveform",
        npts_axis="x",
        colorbar=True,
        invert_x=False,
        invert_y=False,
        ax=None,
        color="k",
        linewidth=1,
        linestyle="-",
        alpha=1,
        cmap="seismic",
        clip=[-1.0, 1.0],
        figsize=(10, 6),
        show=True,
        save_path=None,
        dpi=100,
    ):
        # check source_index and receiver_index
        if source_index is not None and receiver_index is not None:
            raise ValueError(
                "'source_index' and 'receiver_index' cannot be specified at the same time"
            )
        elif source_index is not None:
            if source_index not in self.pairs[:, 0]:
                raise ValueError("'source_index' must be in pairs[:,0]")
        elif receiver_index is not None:
            if receiver_index not in self.pairs[:, 1]:
                raise ValueError("'receiver_index' must be in pairs[:,1]")
        else:
            raise ValueError("'source_index' or 'receiver_index' must be specified")

        # init dist_start
        if dist_start is None:
            dist_start = np.min(self.pairs_dist)
        if dist_start < np.min(self.pairs_dist):
            raise ValueError(
                f"'dist_start' must be >= (np.min(pairs_dist)={np.min(self.pairs_dist)})"
            )

        # init dist_end
        if dist_end is None:
            dist_end = np.max(self.pairs_dist)
        if dist_end > np.max(self.pairs_dist):
            raise ValueError(
                f"'dist_end' must be <= (np.max(pairs_dist)={np.max(self.pairs_dist)})"
            )

        # init lag_start
        if lag_start is None:
            lag_start = -self.maxlag
        if lag_start < -self.maxlag:
            raise ValueError(f"'lag_start' must be >= (-maxlag=-{self.maxlag})")

        # init lag_end
        if lag_end is None:
            lag_end = self.maxlag
        if lag_end > self.maxlag:
            raise ValueError(f"'lag_end' must be <= (maxlag={self.maxlag})")

        # set lag times
        lag_times = np.arange(lag_start, lag_end + self.dt, self.dt)
        lag_times_npts_start = round((lag_start + self.maxlag) / self.dt)
        lag_times_npts_end = lag_times_npts_start + len(lag_times)

        # select if from dist_start and dist_end
        if source_index is not None:
            a_id = np.where((self.pairs[:, 0] == source_index))[0]
            b_id = np.where(
                (self.pairs_dist >= dist_start) & (self.pairs_dist <= dist_end)
            )[0]
            id = np.intersect1d(a_id, b_id)
        elif receiver_index is not None:
            a_id = np.where((self.pairs[:, 1] == receiver_index))[0]
            b_id = np.where(
                (self.pairs_dist >= dist_start) & (self.pairs_dist <= dist_end)
            )[0]
            id = np.intersect1d(a_id, b_id)
        else:
            raise ValueError("'source_index' or 'receiver_index' must be specified")

        # init dist_interval and update dist_start and dist_end
        dist = self.pairs_dist[id]
        dist_start = np.min(dist)
        dist_end = np.max(dist)
        if dist_interval is None:
            dist_interval = np.diff(np.sort(dist)).min()
        elif dist_interval < np.diff(np.sort(dist)).min():
            dist_interval = np.diff(np.sort(dist)).min()
        elif dist_interval > np.diff(np.sort(dist)).max():
            dist_interval = np.diff(np.sort(dist)).max()

        # select data
        if mean_dist_interval or mode == "mat":
            data_all = self.tdata[
                id, win_index, lag_times_npts_start:lag_times_npts_end
            ].copy()
            ntrace = int((dist_end - dist_start) / dist_interval)
            data = np.zeros((ntrace, len(lag_times)))
            for i in range(0, ntrace):
                tindx = np.where(
                    ((dist - dist_start) >= i * dist_interval)
                    & ((dist - dist_start) < (i + 1) * dist_interval)
                )[0]
                if tindx.size > 0:
                    data[i] = np.mean(data_all[tindx], axis=0)
            dist = np.linspace(dist_start, dist_end, ntrace)
        else:
            data = self.tdata[
                id, win_index, lag_times_npts_start:lag_times_npts_end
            ].copy()

        # filter
        if filter:
            sampling_rate = 1 / self.dt
            for i in range(0, data.shape[0]):
                data[i] = bandpass(
                    data[i],
                    freqmin,
                    freqmax,
                    sampling_rate,
                    corners=corners,
                    zerophase=zerophase,
                )

        # normalize data
        if amp_normalize:
            scale = np.max(np.abs(data), axis=1)
            for i in range(0, data.shape[0]):
                if scale[i] == 0:
                    data[i] = 0
                else:
                    data[i] = data[i] / scale[i]
        else:
            scale = np.max(np.abs(data))
            if scale != 0:
                data = data / scale
            else:
                raise ValueError("data is all zeros in amp_normalize=False")

        # plot
        ax = _get_ax(ax, figsize=figsize)
        colors = list(mcolors.TABLEAU_COLORS.keys())
        if mode == "waveform":
            for i in range(0, data.shape[0]):
                if not np.all(data[i].astype(float) == 0.0):
                    if npts_axis == "x":
                        ax.plot(
                            lag_times,
                            amp_scale * dist_interval * data[i] + dist[i],
                            color=color,
                            alpha=alpha,
                            linewidth=linewidth,
                            linestyle=linestyle,
                        )
                    elif npts_axis == "y":
                        ax.plot(
                            amp_scale * dist_interval * data[i] + dist[i],
                            lag_times,
                            color=color,
                            alpha=alpha,
                            linewidth=linewidth,
                            linestyle=linestyle,
                        )
        elif mode == "mat":
            if npts_axis == "x":
                im = ax.imshow(
                    data,
                    extent=[lag_start, lag_end, np.min(dist), np.max(dist)],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            elif npts_axis == "y":
                im = ax.imshow(
                    data.T,
                    extent=[np.min(dist), np.max(dist), lag_start, lag_end],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
        else:
            raise ValueError("'mode' must be 'waveform' or 'mat'")

        # plot velocity
        for i in range(0, len(velocity)):
            x0 = 0
            y0 = 0
            if self.dist_unit == "m":
                x1 = (dist_end - dist_start) / velocity[i]
                y1 = dist_end
            elif self.dist_unit == "km":
                x1 = (dist_end - dist_start) * 1000 / velocity[i]
                y1 = dist_end
            elif self.dist_unit == "degree":
                x1 = (dist_end - dist_start) * (111.2 * 1000) / velocity[i]
                y1 = dist_end
            else:
                raise ValueError("'dist_unit' must be 'm', 'km', or 'degree'")
            if npts_axis == "x":
                ax.plot(
                    [x0, x1],
                    [y0, y1],
                    color=colors[i],
                    linestyle="--",
                    linewidth=1.5,
                    label=str(velocity[i]) + "m/s",
                )
                ax.plot(
                    [x0, -x1],
                    [y0, y1],
                    color=colors[i],
                    linestyle="--",
                    linewidth=1.5,
                )
            elif npts_axis == "y":
                ax.plot(
                    [y0, y1],
                    [x0, x1],
                    color=colors[i],
                    linestyle="--",
                    linewidth=1.5,
                    label=str(velocity[i]) + "m/s",
                )
                ax.plot(
                    [y0, y1],
                    [x0, -x1],
                    color=colors[i],
                    linestyle="--",
                    linewidth=1.5,
                )

        # set title
        fig = ax.figure
        starttime_win_index = self.starttime + self.win_time_interval * win_index
        endtime_win_index = starttime_win_index + self.win_time_interval
        if source_index is not None:
            ax.set_title(
                f"StackData: source_index={source_index}, win_index={win_index}, filter=[{freqmin:.3f}, {freqmax:.3f}] hz\n"
                + f"{starttime_win_index} ~ {endtime_win_index}"
            )
        elif receiver_index is not None:
            ax.set_title(
                f"StackData: receiver_index={receiver_index}, win_index={win_index}, filter=[{freqmin:.3f}, {freqmax:.3f}] hz\n"
                + f"{starttime_win_index} ~ {endtime_win_index}"
            )
        else:
            raise ValueError("'source_index' or 'receiver_index' must be specified")

        # format
        if len(velocity) != 0:
            ax.legend(loc="upper left", fontsize=8, shadow=False)
        if npts_axis == "x":
            if mode == "waveform":
                deviation = 1.2 * amp_scale * dist_interval
                ax.set_ylim(dist_start - deviation, dist_end + deviation)
            elif mode == "mat":
                ax.set_ylim(dist_start, dist_end)
            ax.set_xlim(lag_start, lag_end)
            ax.set_xlabel("Time(s)")
            ax.set_ylabel(f"Distance({self.dist_unit})")
        elif npts_axis == "y":
            if mode == "waveform":
                deviation = 1.2 * amp_scale * dist_interval
                ax.set_xlim(dist_start - deviation, dist_end + deviation)
            elif mode == "mat":
                ax.set_xlim(dist_start, dist_end)
            ax.set_ylim(lag_start, lag_end)
            ax.set_ylabel("Time(s)")
            ax.set_xlabel(f"Distance({self.dist_unit})")
        if colorbar and mode == "mat":
            cbaxes = inset_axes(
                ax, width="15%", height="4%", loc="upper right", borderpad=0.5
            )
            plt.colorbar(im, cax=cbaxes, orientation="horizontal")
        if invert_x:
            ax.invert_xaxis()
        if invert_y:
            ax.invert_yaxis()
        if show:
            plt.show()
        else:
            plt.close(fig)
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi)  # bbox_inches="tight"
        else:
            return ax

    def fplot_moveout(
        self,
        win_index=0,
        source_index=None,
        receiver_index=None,
        dist_start=None,
        dist_end=None,
        dist_interval=None,
        mean_dist_interval=False,
        freq_start=None,
        freq_end=None,
        amp="real",  # 'real', 'imag', 'abs'
        amp_scale=1,
        amp_normalize=True,
        mode="waveform",
        npts_axis="x",
        log=False,
        colorbar=True,
        invert_x=False,
        invert_y=False,
        ax=None,
        color="k",
        linewidth=1,
        linestyle="-",
        alpha=1,
        cmap="seismic",
        clip=[-1.0, 1.0],
        figsize=(10, 6),
        show=True,
        save_path=None,
        dpi=100,
    ):
        # check mark
        if self.f_mark is not True:
            raise ValueError("'fdata' is not calculated")

        # check source_index and receiver_index
        if source_index is not None and receiver_index is not None:
            raise ValueError(
                "'source_index' and 'receiver_index' cannot be specified at the same time"
            )
        elif source_index is not None:
            if source_index not in self.pairs[:, 0]:
                raise ValueError("'source_index' must be in pairs[:,0]")
        elif receiver_index is not None:
            if receiver_index not in self.pairs[:, 1]:
                raise ValueError("'receiver_index' must be in pairs[:,1]")
        else:
            raise ValueError("'source_index' or 'receiver_index' must be specified")

        # init dist_start
        if dist_start is None:
            dist_start = np.min(self.pairs_dist)
        if dist_start < np.min(self.pairs_dist):
            raise ValueError(
                f"'dist_start' must be >= (np.min(pairs_dist)= {np.min(self.pairs_dist)})"
            )

        # init dist_end
        if dist_end is None:
            dist_end = np.max(self.pairs_dist)
        if dist_end > np.max(self.pairs_dist):
            raise ValueError(
                f"'dist_end' must be <= (np.max(pairs_dist)= {np.max(self.pairs_dist)})"
            )

        # init lag_start
        if freq_start is None:
            freq_start = 0
        if freq_start < 0:
            raise ValueError("'freq_start' must be >= 0")

        # init lag_end
        if freq_end is None:
            freq_end = self.maxfreq
        if freq_end > self.maxfreq:
            raise ValueError(f"'freq_end' must be <= (maxfreq={self.maxfreq})")

        # set lag freqs
        lag_freqs = np.arange(freq_start, freq_end + self.df, self.df)
        lag_freqs_npts_start = round(lag_freqs[0] / self.df)
        lag_freqs_npts_end = round(lag_freqs[-1] / self.df) + 1

        # select if from dist_start and dist_end
        if source_index is not None:
            a_id = np.where((self.pairs[:, 0] == source_index))[0]
            b_id = np.where(
                (self.pairs_dist >= dist_start) & (self.pairs_dist <= dist_end)
            )[0]
            id = np.intersect1d(a_id, b_id)
        elif receiver_index is not None:
            a_id = np.where((self.pairs[:, 1] == receiver_index))[0]
            b_id = np.where(
                (self.pairs_dist >= dist_start) & (self.pairs_dist <= dist_end)
            )[0]
            id = np.intersect1d(a_id, b_id)
        else:
            raise ValueError("'source_index' or 'receiver_index' must be specified")

        # init dist_interval and update dist_start and dist_end
        dist = self.pairs_dist[id]
        dist_start = np.min(dist)
        dist_end = np.max(dist)
        if dist_interval is None:
            dist_interval = np.diff(np.sort(dist)).min()
        elif dist_interval < np.diff(np.sort(dist)).min():
            dist_interval = np.diff(np.sort(dist)).min()
        elif dist_interval > np.diff(np.sort(dist)).max():
            dist_interval = np.diff(np.sort(dist)).max()

        # select data
        if mean_dist_interval or mode == "mat":
            data_all = self.fdata[
                id, win_index, lag_freqs_npts_start:lag_freqs_npts_end
            ].copy()
            ntrace = int((dist_end - dist_start) / dist_interval)
            data = np.zeros((ntrace, len(lag_freqs)))
            for i in range(0, ntrace):
                tindx = np.where(
                    ((dist - dist_start) >= i * dist_interval)
                    & ((dist - dist_start) < (i + 1) * dist_interval)
                )[0]
                if tindx.size > 0:
                    if amp == "real":
                        data[i] = np.mean(np.real(data_all[tindx]), axis=0)
                    elif amp == "imag":
                        data[i] = np.mean(np.imag(data_all[tindx]), axis=0)
                    elif amp == "abs":
                        data[i] = np.mean(np.abs(data_all[tindx]), axis=0)
            dist = np.linspace(dist_start, dist_end, ntrace)
        else:
            data = self.fdata[
                id, win_index, lag_freqs_npts_start:lag_freqs_npts_end
            ].copy()
            if amp == "real":
                data = np.real(data)
            elif amp == "imag":
                data = np.imag(data)
            elif amp == "abs":
                data = np.abs(data)

        # normalize data
        if amp_normalize:
            scale = np.max(np.abs(data), axis=1)
            for i in range(0, data.shape[0]):
                if scale[i] == 0:
                    data[i] = 0
                else:
                    data[i] = data[i] / scale[i]
        else:
            scale = np.max(np.abs(data))
            if scale != 0:
                data = data / scale
            else:
                raise ValueError("data is all zeros in amp_normalize=False")

        # plot
        ax = _get_ax(ax, figsize=figsize)
        if mode == "waveform":
            for i in range(0, data.shape[0]):
                if not np.all(data[i].astype(float) == 0.0):
                    if npts_axis == "x":
                        ax.plot(
                            lag_freqs,
                            amp_scale * dist_interval * data[i] + dist[i],
                            color=color,
                            alpha=alpha,
                            linewidth=linewidth,
                            linestyle=linestyle,
                        )
                    elif npts_axis == "y":
                        ax.plot(
                            amp_scale * dist_interval * data[i] + dist[i],
                            lag_freqs,
                            color=color,
                            alpha=alpha,
                            linewidth=linewidth,
                            linestyle=linestyle,
                        )
        elif mode == "mat":
            if npts_axis == "x":
                im = ax.imshow(
                    data,
                    extent=[freq_start, freq_end, np.min(dist), np.max(dist)],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            elif npts_axis == "y":
                im = ax.imshow(
                    data.T,
                    extent=[np.min(dist), np.max(dist), freq_start, freq_end],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
        else:
            raise ValueError("'mode' must be 'waveform' or 'mat'")

        # set title
        fig = ax.figure
        starttime_win_index = self.starttime + self.win_time_interval * win_index
        endtime_win_index = starttime_win_index + self.win_time_interval
        if source_index is not None:
            ax.set_title(
                f"StackData: source_index={source_index}, win_index={win_index}\n"
                + f"{starttime_win_index} ~ {endtime_win_index}"
            )
        elif receiver_index is not None:
            ax.set_title(
                f"StackData: receiver_index={receiver_index}, win_index={win_index}\n"
                + f"{starttime_win_index} ~ {endtime_win_index}"
            )
        else:
            raise ValueError("'source_index' or 'receiver_index' must be specified")

        # format
        if npts_axis == "x":
            if log:
                ax.set_xscale("log")
            if mode == "waveform":
                deviation = 1.2 * amp_scale * dist_interval
                ax.set_ylim(dist_start - deviation, dist_end + deviation)
            elif mode == "mat":
                ax.set_ylim(dist_start, dist_end)
            ax.set_xlim(freq_start, freq_end)
            ax.set_xlabel("Freq(hz)")
            ax.set_ylabel(f"Distance({self.dist_unit})")
        elif npts_axis == "y":
            if log:
                ax.set_yscale("log")
            if mode == "waveform":
                deviation = 1.2 * amp_scale * dist_interval
                ax.set_xlim(dist_start - deviation, dist_end + deviation)
            elif mode == "mat":
                ax.set_xlim(dist_start, dist_end)
            ax.set_ylim(freq_start, freq_end)
            ax.set_ylabel("Freq(hz)")
            ax.set_xlabel(f"Distance({self.dist_unit})")
        if colorbar and mode == "mat":
            cbaxes = inset_axes(
                ax, width="15%", height="4%", loc="upper right", borderpad=0.5
            )
            plt.colorbar(im, cax=cbaxes, orientation="horizontal")
        if invert_x:
            ax.invert_xaxis()
        if invert_y:
            ax.invert_yaxis()
        if show:
            plt.show()
        else:
            plt.close(fig)
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi)  # bbox_inches="tight"
        else:
            return ax

    def plot_bin(
        self,
        win_index=0,
        velocity=[],
        dist_start=None,
        dist_end=None,
        dist_interval=None,
        mean_dist_interval=False,
        amp_scale=1,
        amp_normalize=True,
        lag_start=None,
        lag_end=None,
        filter=False,
        freqmin=0.0,
        freqmax=0.1,
        corners=4,
        zerophase=True,
        mode="waveform",
        npts_axis="x",
        colorbar=True,
        invert_x=False,
        invert_y=False,
        ax=None,
        color="k",
        linewidth=1,
        linestyle="-",
        alpha=1,
        cmap="seismic",
        clip=[-1.0, 1.0],
        figsize=(10, 6),
        show=True,
        save_path=None,
        dpi=100,
    ):
        # init dist_start
        if dist_start is None:
            dist_start = np.min(self.pairs_dist)
        if dist_start < np.min(self.pairs_dist):
            raise ValueError(
                f"'dist_start' must be >= (np.min(pairs_dist)= {np.min(self.pairs_dist)})"
            )

        # init dist_end
        if dist_end is None:
            dist_end = np.max(self.pairs_dist)
        if dist_end > np.max(self.pairs_dist):
            raise ValueError(
                f"'dist_end' must be <= (np.max(pairs_dist)= {np.max(self.pairs_dist)})"
            )

        # init lag_start
        if lag_start is None:
            lag_start = -self.maxlag
        if lag_start < -self.maxlag:
            raise ValueError(f"'lag_start' must be >= (-maxlag=-{self.maxlag})")

        # init lag_end
        if lag_end is None:
            lag_end = self.maxlag
        if lag_end > self.maxlag:
            raise ValueError(f"'lag_end' must be <= (maxlag={self.maxlag})")

        # set lag times
        lag_times = np.arange(lag_start, lag_end + self.dt, self.dt)
        lag_times_npts_start = round((lag_start + self.maxlag) / self.dt)
        lag_times_npts_end = lag_times_npts_start + len(lag_times)

        # select id from dist_start and dist_end
        id = np.where((self.pairs_dist >= dist_start) & (self.pairs_dist <= dist_end))[
            0
        ]

        # init dist_interval and update dist_start and dist_end
        dist = self.pairs_dist[id]
        dist_start = np.min(dist)
        dist_end = np.max(dist)
        if dist_interval is None:
            dist_interval = np.diff(np.sort(dist)).min()
        elif dist_interval < np.diff(np.sort(dist)).min():
            dist_interval = np.diff(np.sort(dist)).min()
        elif dist_interval > np.diff(np.sort(dist)).max():
            dist_interval = np.diff(np.sort(dist)).max()

        if dist_interval == 0:
            raise ValueError("'dist_interval' must be larger than 0")

        # select data
        if mean_dist_interval or mode == "mat":
            data_all = self.tdata[
                id, win_index, lag_times_npts_start:lag_times_npts_end
            ].copy()
            ntrace = int((dist_end - dist_start) / dist_interval)
            data = np.zeros((ntrace, len(lag_times)))
            for i in range(0, ntrace):
                tindx = np.where(
                    ((dist - dist_start) >= i * dist_interval)
                    & ((dist - dist_start) < (i + 1) * dist_interval)
                )[0]
                if tindx.size > 0:
                    data[i] = np.mean(data_all[tindx], axis=0)
            dist = np.linspace(dist_start, dist_end, ntrace)
        else:
            data = self.tdata[
                id, win_index, lag_times_npts_start:lag_times_npts_end
            ].copy()

        # filter
        if filter:
            sampling_rate = 1 / self.dt
            for i in range(0, data.shape[0]):
                data[i] = bandpass(
                    data[i],
                    freqmin,
                    freqmax,
                    sampling_rate,
                    corners=corners,
                    zerophase=zerophase,
                )

        # normalize data
        if amp_normalize:
            scale = np.max(np.abs(data), axis=1)
            for i in range(0, data.shape[0]):
                if scale[i] == 0:
                    data[i] = 0
                else:
                    data[i] = data[i] / scale[i]
        else:
            scale = np.max(np.abs(data))
            if scale != 0:
                data = data / scale
            else:
                raise ValueError("data is all zeros in amp_normalize=False")

        # plot
        ax = _get_ax(ax, figsize=figsize)
        colors = list(mcolors.TABLEAU_COLORS.keys())
        if mode == "waveform":
            for i in range(0, data.shape[0]):
                if not np.all(data[i].astype(float) == 0.0):
                    if npts_axis == "x":
                        ax.plot(
                            lag_times,
                            amp_scale * dist_interval * data[i] + dist[i],
                            color=color,
                            alpha=alpha,
                            linewidth=linewidth,
                            linestyle=linestyle,
                        )
                    elif npts_axis == "y":
                        ax.plot(
                            amp_scale * dist_interval * data[i] + dist[i],
                            lag_times,
                            color=color,
                            alpha=alpha,
                            linewidth=linewidth,
                            linestyle=linestyle,
                        )
        elif mode == "mat":
            if npts_axis == "x":
                im = ax.imshow(
                    data,
                    extent=[lag_start, lag_end, np.min(dist), np.max(dist)],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            elif npts_axis == "y":
                im = ax.imshow(
                    data.T,
                    extent=[np.min(dist), np.max(dist), lag_start, lag_end],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
        else:
            raise ValueError("'mode' must be 'waveform' or 'mat'")

        # plot velocity
        for i in range(0, len(velocity)):
            x0 = 0
            y0 = 0
            if self.dist_unit == "m":
                x1 = (dist_end - dist_start) / velocity[i]
                y1 = dist_end
            elif self.dist_unit == "km":
                x1 = (dist_end - dist_start) * 1000 / velocity[i]
                y1 = dist_end
            elif self.dist_unit == "degree":
                x1 = (dist_end - dist_start) * (111.2 * 1000) / velocity[i]
                y1 = dist_end
            else:
                raise ValueError("'dist_unit' must be 'm', 'km', or 'degree'")
            if npts_axis == "x":
                ax.plot(
                    [x0, x1],
                    [y0, y1],
                    color=colors[i],
                    linestyle="--",
                    linewidth=1.5,
                    label=str(velocity[i]) + "m/s",
                )
                ax.plot(
                    [x0, -x1],
                    [y0, y1],
                    color=colors[i],
                    linestyle="--",
                    linewidth=1.5,
                )
            elif npts_axis == "y":
                ax.plot(
                    [y0, y1],
                    [x0, x1],
                    color=colors[i],
                    linestyle="--",
                    linewidth=1.5,
                    label=str(velocity[i]) + "m/s",
                )
                ax.plot(
                    [y0, y1],
                    [x0, -x1],
                    color=colors[i],
                    linestyle="--",
                    linewidth=1.5,
                )

        # set title
        fig = ax.figure
        starttime_win_index = self.starttime + self.win_time_interval * win_index
        endtime_win_index = starttime_win_index + self.win_time_interval
        ax.set_title(
            f"StackData: win_index={win_index}, filter=[{freqmin:.3f}, {freqmax:.3f}] hz\n"
            + f"{starttime_win_index} ~ {endtime_win_index}"
        )

        # format
        if len(velocity) != 0:
            ax.legend(loc="upper left", fontsize=8, shadow=False)
        if npts_axis == "x":
            if mode == "waveform":
                deviation = 1.2 * amp_scale * dist_interval
                ax.set_ylim(dist_start - deviation, dist_end + deviation)
            elif mode == "mat":
                ax.set_ylim(dist_start, dist_end)
            ax.set_xlim(lag_start, lag_end)
            ax.set_xlabel("Time(s)")
            ax.set_ylabel(f"Distance({self.dist_unit})")
        elif npts_axis == "y":
            if mode == "waveform":
                deviation = 1.2 * amp_scale * dist_interval
                ax.set_xlim(dist_start - deviation, dist_end + deviation)
            elif mode == "mat":
                ax.set_xlim(dist_start, dist_end)
            ax.set_ylim(lag_start, lag_end)
            ax.set_ylabel("Time(s)")
            ax.set_xlabel(f"Distance({self.dist_unit})")
        if colorbar and mode == "mat":
            cbaxes = inset_axes(
                ax, width="15%", height="4%", loc="upper right", borderpad=0.5
            )
            plt.colorbar(im, cax=cbaxes, orientation="horizontal")
        if invert_x:
            ax.invert_xaxis()
        if invert_y:
            ax.invert_yaxis()
        if show:
            plt.show()
        else:
            plt.close(fig)
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi)  # bbox_inches="tight"
        else:
            return ax

    def fplot_bin(
        self,
        win_index=0,
        dist_start=None,
        dist_end=None,
        dist_interval=None,
        mean_dist_interval=False,
        freq_start=None,
        freq_end=None,
        amp="real",  # 'real', 'imag', 'abs'
        amp_scale=1,
        amp_normalize=True,
        mode="waveform",
        npts_axis="x",
        log=False,
        colorbar=True,
        invert_x=False,
        invert_y=False,
        ax=None,
        color="k",
        linewidth=1,
        linestyle="-",
        alpha=1,
        cmap="seismic",
        clip=[-1.0, 1.0],
        figsize=(10, 6),
        show=True,
        save_path=None,
        dpi=100,
    ):
        # check mark
        if self.f_mark is not True:
            raise ValueError("'fdata' is not calculated")

        # init dist_start
        if dist_start is None:
            dist_start = np.min(self.pairs_dist)
        if dist_start < np.min(self.pairs_dist):
            raise ValueError(
                f"'dist_start' must be >= (np.min(pairs_dist)= {np.min(self.pairs_dist)})"
            )

        # init dist_end
        if dist_end is None:
            dist_end = np.max(self.pairs_dist)
        if dist_end > np.max(self.pairs_dist):
            raise ValueError(
                f"'dist_end' must be <= (np.max(pairs_dist)= {np.max(self.pairs_dist)})"
            )

        # init lag_start
        if freq_start is None:
            freq_start = 0
        if freq_start < 0:
            raise ValueError("'freq_start' must be >= 0")

        # init lag_end
        if freq_end is None:
            freq_end = self.maxfreq
        if freq_end > self.maxfreq:
            raise ValueError(f"'freq_end' must be <= (maxfreq={self.maxfreq})")

        # set lag freqs
        lag_freqs = np.arange(freq_start, freq_end + self.df, self.df)
        lag_freqs_npts_start = round(lag_freqs[0] / self.df)
        lag_freqs_npts_end = round(lag_freqs[-1] / self.df) + 1

        # select id from dist_start and dist_end
        id = np.where((self.pairs_dist >= dist_start) & (self.pairs_dist <= dist_end))[
            0
        ]

        # init dist_interval and update dist_start and dist_end
        dist = self.pairs_dist[id]
        dist_start = np.min(dist)
        dist_end = np.max(dist)
        if dist_interval is None:
            dist_interval = np.diff(np.sort(dist)).min()
        elif dist_interval < np.diff(np.sort(dist)).min():
            dist_interval = np.diff(np.sort(dist)).min()
        elif dist_interval > np.diff(np.sort(dist)).max():
            dist_interval = np.diff(np.sort(dist)).max()

        if dist_interval == 0:
            raise ValueError("'dist_interval' must be larger than 0")

        # select data
        if mean_dist_interval or mode == "mat":
            data_all = self.fdata[
                id, win_index, lag_freqs_npts_start:lag_freqs_npts_end
            ].copy()
            ntrace = int((dist_end - dist_start) / dist_interval)
            data = np.zeros((ntrace, len(lag_freqs)))
            for i in range(0, ntrace):
                tindx = np.where(
                    ((dist - dist_start) >= i * dist_interval)
                    & ((dist - dist_start) < (i + 1) * dist_interval)
                )[0]
                if tindx.size > 0:
                    if amp == "real":
                        data[i] = np.mean(np.real(data_all[tindx]), axis=0)
                    elif amp == "imag":
                        data[i] = np.mean(np.imag(data_all[tindx]), axis=0)
                    elif amp == "abs":
                        data[i] = np.mean(np.abs(data_all[tindx]), axis=0)
            dist = np.linspace(dist_start, dist_end, ntrace)
        else:
            data = self.fdata[
                id, win_index, lag_freqs_npts_start:lag_freqs_npts_end
            ].copy()
            if amp == "real":
                data = np.real(data)
            elif amp == "imag":
                data = np.imag(data)
            elif amp == "abs":
                data = np.abs(data)

        # normalize data
        if amp_normalize:
            scale = np.max(np.abs(data), axis=1)
            for i in range(0, data.shape[0]):
                if scale[i] == 0:
                    data[i] = 0
                else:
                    data[i] = data[i] / scale[i]
        else:
            scale = np.max(np.abs(data))
            if scale != 0:
                data = data / scale
            else:
                raise ValueError("data is all zeros in amp_normalize=False")

        # plot
        ax = _get_ax(ax, figsize=figsize)
        if mode == "waveform":
            for i in range(0, data.shape[0]):
                if not np.all(data[i].astype(float) == 0.0):
                    if npts_axis == "x":
                        ax.plot(
                            lag_freqs,
                            amp_scale * dist_interval * data[i] + dist[i],
                            color=color,
                            alpha=alpha,
                            linewidth=linewidth,
                            linestyle=linestyle,
                        )
                    elif npts_axis == "y":
                        ax.plot(
                            amp_scale * dist_interval * data[i] + dist[i],
                            lag_freqs,
                            color=color,
                            alpha=alpha,
                            linewidth=linewidth,
                            linestyle=linestyle,
                        )
        elif mode == "mat":
            if npts_axis == "x":
                im = ax.imshow(
                    data,
                    extent=[freq_start, freq_end, np.min(dist), np.max(dist)],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            elif npts_axis == "y":
                im = ax.imshow(
                    data.T,
                    extent=[np.min(dist), np.max(dist), freq_start, freq_end],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
        else:
            raise ValueError("'mode' must be 'waveform' or 'mat'")

        # set title
        fig = ax.figure
        starttime_win_index = self.starttime + self.win_time_interval * win_index
        endtime_win_index = starttime_win_index + self.win_time_interval
        ax.set_title(
            f"StackData: win_index={win_index}\n"
            + f"{starttime_win_index} ~ {endtime_win_index}"
        )

        # format
        if npts_axis == "x":
            if log:
                ax.set_xscale("log")
            if mode == "waveform":
                deviation = 1.2 * amp_scale * dist_interval
                ax.set_ylim(dist_start - deviation, dist_end + deviation)
            elif mode == "mat":
                ax.set_ylim(dist_start, dist_end)
            ax.set_xlim(freq_start, freq_end)
            ax.set_xlabel("Freq(hz)")
            ax.set_ylabel(f"Distance({self.dist_unit})")
        elif npts_axis == "y":
            if log:
                ax.set_yscale("log")
            if mode == "waveform":
                deviation = 1.2 * amp_scale * dist_interval
                ax.set_xlim(dist_start - deviation, dist_end + deviation)
            elif mode == "mat":
                ax.set_xlim(dist_start, dist_end)
            ax.set_ylim(freq_start, freq_end)
            ax.set_ylabel("Freq(hz)")
            ax.set_xlabel(f"Distance({self.dist_unit})")
        if colorbar and mode == "mat":
            cbaxes = inset_axes(
                ax, width="15%", height="4%", loc="upper right", borderpad=0.5
            )
            plt.colorbar(im, cax=cbaxes, orientation="horizontal")
        if invert_x:
            ax.invert_xaxis()
        if invert_y:
            ax.invert_yaxis()
        if show:
            plt.show()
        else:
            plt.close(fig)
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi)  # bbox_inches="tight"
        else:
            return ax

    def stack_bin(self, dist_interval, domain="time"):
        dist = np.empty(0)
        data = np.empty(0)
        return data, dist  # take those parameters to the plotting function

    def stack_dbf(self, domain="time"):  # double beamforming
        pass
