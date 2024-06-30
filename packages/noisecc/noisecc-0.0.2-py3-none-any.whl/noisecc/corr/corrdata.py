import h5py
import scipy
import textwrap
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.dates import date2num
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from obspy.signal.filter import bandpass
from noisecc.utils.viz_tools import _format_time_axis, _get_ax


class CorrData(object):
    def __init__(
        self,
        tdata,
        fdata,
        dt,
        df,
        win_time_interval,
        starttime,
        pairs,
        method,
        domain,
        maxlag,
        smoothspect_N,
        device,
        jobs,
        flag,
    ):
        # initialize parameters
        self.method = method
        self.pairs = pairs
        self.smoothspect_N = smoothspect_N
        self.domain = domain
        self.win_time_interval = win_time_interval
        self.starttime = starttime
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
            self.time_vector = np.arange(-maxlag, maxlag + dt, dt)
            self.maxlag = maxlag
            # freq
            self.fdata = None
            self.df = None
            self.freq_npts = None
            self.freq_vector = None
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
            self.time_vector = None
            self.maxlag = None
            # freq
            self.fdata = fdata
            self.df = df
            self.freq_npts = fdata.shape[2]
            self.freq_vector = df * np.arange(0, self.freq_npts)  # 0, df, 2df, ...
            self.maxfreq = self.freq_vector[-1]

        # compute endtime
        self.endtime = self.starttime + (self.win_num - 1) * self.win_time_interval

    def __str__(self):
        stats = f"* STATS:\n{textwrap.indent(str(self.print_stats()), '  ')}"
        pairs = (
            f"* PAIRS:\n"
            f"         pairs_num: {self.pairs.shape[0]}\n"
            f"{textwrap.indent(np.array2string(self.pairs, threshold=10), '                    ')}"
        )

        def format_number(num):
            formatted_num = f"{num:.6f}"
            return formatted_num if num < 0 else " " + formatted_num

        def format_data(domain):
            if domain == "time":
                dd = self.tdata
            elif domain == "freq":
                dd = self.fdata
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
            raise ValueError("'tdata' and 'fdata' are both None")

        info = "\n".join([stats, pairs, data])
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
                "pairs_num": self.pairs_num,
                "win_num": self.win_num,
                "method": self.method,
                "smoothspect_N": self.smoothspect_N,
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

    def calculate_timedata(self, workers=1):
        if self.t_mark is True:
            raise ValueError("'tdata' is already calculated")
        irfft_data = scipy.fft.irfft(self.fdata, axis=-1, workers=workers)
        self.tdata = np.roll(irfft_data, self.freq_npts - 1, axis=-1)
        self.dt = 1 / (2 * (self.freq_npts - 1) * self.df)
        self.maxlag = (self.freq_npts - 2) * self.dt
        self.time_vector = np.arange(-self.maxlag, self.maxlag + self.dt, self.dt)
        self.time_npts = len(self.time_vector)
        self.t_mark = True

    def calculate_freqdata(self, workers=1):
        if self.f_mark is True:
            raise ValueError("'fdata' is already calculated")
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
                group.attrs["domain"] = "time"
                group.attrs["dt"] = self.dt
                group.attrs["win_time_interval"] = self.win_time_interval
                group.attrs["starttime"] = str(self.starttime)
                group.attrs["method"] = self.method
                group.attrs["maxlag"] = self.maxlag
                group.attrs["smoothspect_N"] = self.smoothspect_N
                group.attrs["device"] = self.device
                group.attrs["jobs"] = self.jobs
                group.attrs["flag"] = self.flag
                group.create_dataset("pairs", data=self.pairs)
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
                group.attrs["domain"] = "freq"
                group.attrs["df"] = self.df
                group.attrs["win_time_interval"] = self.win_time_interval
                group.attrs["starttime"] = str(self.starttime)
                group.attrs["method"] = self.method
                group.attrs["maxlag"] = self.maxlag
                group.attrs["smoothspect_N"] = self.smoothspect_N
                group.attrs["device"] = self.device
                group.attrs["jobs"] = self.jobs
                group.attrs["flag"] = self.flag
                group.create_dataset("pairs", data=self.pairs)
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

        # set win times
        date2num_real_start = date2num(self.starttime.datetime)
        number_interval = 2
        date2num_internal = win_interval * self.win_time_interval * 1 / 86400
        win_start_datetime = (
            self.starttime + win_start * self.win_time_interval
        ).datetime
        win_end_datetime = (self.starttime + win_end * self.win_time_interval).datetime

        # select data
        win_index = np.arange(win_start, win_end, win_interval)
        if mean_win_interval:
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

        # plot
        ax = _get_ax(ax, figsize=figsize)
        if mode == "waveform":
            for i in range(0, data.shape[0]):
                number_real = data[i, :] * amp_scale + i * 2
                date2num_real = (
                    date2num_internal * number_real / number_interval
                    + date2num_real_start
                )
                if npts_axis == "x":
                    ax.plot(
                        lag_times,
                        date2num_real,
                        linewidth=linewidth,
                        color=color,
                        alpha=alpha,
                        linestyle=linestyle,
                    )
                elif npts_axis == "y":
                    ax.plot(
                        date2num_real,
                        lag_times,
                        linewidth=linewidth,
                        color=color,
                        alpha=alpha,
                        linestyle=linestyle,
                    )
        elif mode == "mat":
            if npts_axis == "x":
                im = ax.imshow(
                    data,
                    extent=[lag_start, lag_end, win_start_datetime, win_end_datetime],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            elif npts_axis == "y":
                im = ax.imshow(
                    data.T,
                    extent=[win_start_datetime, win_end_datetime, lag_start, lag_end],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )

            else:
                raise ValueError("'npts_axis' must be 'x' or 'y'")

            # plot cc mean
            cc_mean = np.mean(data, axis=0)
            y_offset = (date2num(win_end_datetime) + date2num(win_start_datetime)) / 2
            y_total = date2num(win_end_datetime) - date2num(win_start_datetime)
            if npts_axis == "x":
                ax.plot(
                    lag_times,
                    mean_amp_scale * y_total / 10 * cc_mean + y_offset,
                    linewidth=linewidth,
                    color=color,
                    alpha=alpha,
                    linestyle=linestyle,
                )
            elif npts_axis == "y":
                ax.plot(
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

        # format win_axis
        _format_time_axis(
            ax,
            axis=win_axis,
            tick_rotation=winstick_rotation,
            minticks=win_minticks,
            maxticks=win_maxticks,
            labelsize=winstick_labelsize,
        )
        # format
        fig = ax.figure
        ax.set_title(
            f"CorrData: pair=[{self.pairs[pair_index][0]}, {self.pairs[pair_index][1]}], filter=[{freqmin:.3f}, {freqmax:.3f}] hz"
        )
        if npts_axis == "x":
            ax.set_xlim(lag_start, lag_end)
            ax.set_xlabel("Time(s)")
        elif npts_axis == "y":
            ax.set_ylim(lag_start, lag_end)
            ax.set_ylabel("Time(s)")
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
            fig.savefig(
                save_path, dpi=dpi
            )  # bbox_inches="tight", which will change the colorbar location
        else:
            return ax

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
        win_end_datetime = (self.starttime + win_end * self.win_time_interval).datetime

        # select data
        win_index = np.arange(win_start, win_end, win_interval)
        if mean_win_interval:
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

        # plot
        ax = _get_ax(ax, figsize=figsize)
        if mode == "waveform":
            for i in range(0, data.shape[0]):
                number_real = data[i, :] * amp_scale + i * 2
                date2num_real = (
                    date2num_internal * number_real / number_interval
                    + date2num_real_start
                )
                if npts_axis == "x":
                    ax.plot(
                        lag_freqs,
                        date2num_real,
                        linewidth=linewidth,
                        color=color,
                        alpha=alpha,
                        linestyle=linestyle,
                    )
                elif npts_axis == "y":
                    ax.plot(
                        date2num_real,
                        lag_freqs,
                        linewidth=linewidth,
                        color=color,
                        alpha=alpha,
                        linestyle=linestyle,
                    )
        elif mode == "mat":
            if npts_axis == "x":
                im = ax.imshow(
                    data,
                    extent=[freq_start, freq_end, win_start_datetime, win_end_datetime],
                    aspect="auto",
                    cmap=cmap,
                    origin="lower",
                )
                im.set_clim(clip)
            elif npts_axis == "y":
                im = ax.imshow(
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
                ax.plot(
                    lag_freqs,
                    mean_amp_scale * y_total / 10 * cc_mean + y_offset,
                    linewidth=linewidth,
                    color=color,
                    alpha=alpha,
                    linestyle=linestyle,
                )
            elif npts_axis == "y":
                ax.plot(
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

        # format win_axis
        _format_time_axis(
            ax,
            axis=win_axis,
            tick_rotation=winstick_rotation,
            minticks=win_minticks,
            maxticks=win_maxticks,
            labelsize=winstick_labelsize,
        )
        # format
        fig = ax.figure
        ax.set_title(
            f"CorrData: pair=[{self.pairs[pair_index][0]}, {self.pairs[pair_index][1]}]"
        )
        if npts_axis == "x":
            if log:
                ax.set_xscale("log")
            ax.set_xlim(freq_start, freq_end)
            ax.set_xlabel("Freq(hz)")
        elif npts_axis == "y":
            if log:
                ax.set_yscale("log")
            ax.set_ylim(freq_start, freq_end)
            ax.set_ylabel("Freq(hz)")
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
            fig.savefig(
                save_path, dpi=dpi
            )  # bbox_inches="tight", which will change the colorbar location
        else:
            return ax
