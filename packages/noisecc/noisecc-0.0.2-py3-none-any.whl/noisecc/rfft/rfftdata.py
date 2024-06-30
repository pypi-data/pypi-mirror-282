import h5py
import scipy
import textwrap
import numpy as np
import matplotlib.pyplot as plt

from noisecc.utils.timestamp import time_linspace
from obspy.imaging.spectrogram import spectrogram
from noisecc.utils.viz_tools import _get_ax


class RFFTData(object):
    def __init__(
        self,
        data,
        dt,
        df,
        win_time_interval,
        starttime,
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
        self.df = df
        self.win_time_interval = win_time_interval
        self.starttime = starttime
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
        self.freq_npts = data.shape[2]
        self.endtime = self.starttime + (self.win_num - 1) * self.win_time_interval

    def __str__(self):
        stats = f"* STATS:\n{textwrap.indent(str(self.print_stats()), '  ')}"

        def format_number(c):
            def format_part(num):
                formatted_num = f"{num:.3f}"
                return formatted_num if num < 0 else " " + formatted_num

            real_part = format_part(c.real)
            imag_part = format_part(c.imag)

            return f"{real_part} +{imag_part}j"

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
            f"       shape: {self.data.shape} || (channel_num, win_num, freq_npts)\n"
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
                "df": self.df,
                "win_time_interval": self.win_time_interval,
                "starttime": self.starttime,
                "endtime": self.endtime,
                "channel_num": self.channel_num,
                "win_num": self.win_num,
                "freq_npts": self.freq_npts,
                "freq_norm": self.freq_norm,
                "freqmin": self.freqmin,
                "freqmax": self.freqmax,
                "whiten_npad": self.whiten_npad,
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
            group.attrs["df"] = self.df
            group.attrs["win_time_interval"] = self.win_time_interval
            group.attrs["starttime"] = str(self.starttime)
            group.attrs["freq_norm"] = self.freq_norm
            group.attrs["freqmin"] = self.freqmin
            group.attrs["freqmax"] = self.freqmax
            group.attrs["whiten_npad"] = self.whiten_npad
            group.attrs["smoothspect_N"] = self.smoothspect_N
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

    # plot
    def plot(
        self,
        channel_index=0,
        win_index=0,
        raw_data=None,
        freq_start=None,
        freq_end=None,
        log=True,
        ax=None,
        figsize=(10, 4),
        show=True,
        save_path=None,
        dpi=100,
    ):
        ax = _get_ax(ax, figsize=figsize)
        freq_vector = np.arange(0, self.freq_npts) * self.df
        freq_data = np.abs(self.data[channel_index, win_index].copy())
        freq_data = freq_data / np.max(freq_data)
        if freq_start is None:
            freq_start = freq_vector[0]
        if freq_end is None:
            freq_end = freq_vector[-1]

        # plot
        ax.plot(freq_vector, freq_data, label="data", color="darkred")
        if raw_data is not None:
            win1 = int(win_index * self.win_time_interval / self.dt)
            win2 = win1 + 2 * (self.freq_npts - 1)
            raw_freq_data = np.abs(scipy.fft.rfft(raw_data[win1:win2]))
            raw_freq_data = raw_freq_data / np.max(raw_freq_data)
            raw_freq_vector = np.arange(0, len(raw_freq_data)) * self.df
            ax.plot(
                raw_freq_vector,
                raw_freq_data,
                label="raw_data",
                alpha=0.5,
                color="dimgray",
            )

        # format
        fig = ax.figure
        ax.legend()
        ax.set_xlim(freq_start, freq_end)
        ax.set_xlabel("Frequency(hz)")
        ax.set_ylabel("Normalized Amplitude")
        ax.set_title(
            f"RFFTData: channel_index={channel_index}, win_index={win_index}"
            f"\nfreq_norm={self.freq_norm}, freqband=[{self.freqmin:.3f}, {self.freqmax:.3f}] hz"
        )
        if log:
            ax.set_xscale("log")
        if show:
            plt.show()
        else:
            plt.close(fig)
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
        else:
            return ax

    # plot spectrum
    def spectrogram(
        self,
        channel_index=0,
        win_index=0,
        raw_data=None,
        dbscale=False,
        freq_start=None,
        freq_end=None,
        log=True,
        time_ticklabel_num=5,
        time_tick_rotation=0,
        figsize=(10, 4),
        show=True,
        save_path=None,
        dpi=100,
    ):
        cc_len = 2 * (self.freq_npts - 1) * self.dt
        time_ticks = np.linspace(0, cc_len, num=time_ticklabel_num)
        time_label_UTC = time_linspace(
            self.starttime + self.win_time_interval,
            self.starttime + self.win_time_interval + cc_len,
            num=time_ticklabel_num,
        )
        time_label = np.array(
            [i.strftime("%Y-%m-%d\n%H:%M:%S") for i in time_label_UTC]
        )
        if freq_start is None:
            freq_start = 0
        if freq_end is None:
            freq_end = self.freq_npts * self.df

        # plot
        if raw_data is None:
            win1 = int(win_index * self.win_time_interval / self.dt)
            win2 = win1 + 2 * (self.freq_npts - 1)
            rfft_whitedata = np.fft.irfft(
                self.data[channel_index, win_index].copy()
            ).real
            fig, ax = plt.subplots(figsize=figsize)
            _ = spectrogram(
                rfft_whitedata,
                1 / self.dt,
                axes=ax,
                dbscale=dbscale,
                log=log,
                show=show,
            )
            ax.plot(
                [0, cc_len],
                [self.freqmin, self.freqmin],
                "--",
                color="red",
                lw=3,
                alpha=0.7,
            )
            ax.plot(
                [0, cc_len],
                [self.freqmax, self.freqmax],
                "--",
                color="red",
                lw=3,
                alpha=0.7,
            )
            ax.set_title(
                f"RFFTData: channel_index={channel_index}, win_index={win_index}"
                f"\nfreq_norm={self.freq_norm}, freqband=[{self.freqmin:.3f}, {self.freqmax:.3f}] hz"
            )
            ax.set_xlim(0, cc_len)
            ax.set_ylim(freq_start, freq_end)
            ax.set_ylabel("Frequency(hz)")
            ax.set_xticks(time_ticks)
            ax.set_xticklabels(time_label, rotation=time_tick_rotation)
        else:
            win1 = int(win_index * self.win_time_interval / self.dt)
            win2 = win1 + 2 * (self.freq_npts - 1)
            rfft_whitedata = np.fft.irfft(
                self.data[channel_index, win_index].copy()
            ).real
            fig, ax = plt.subplots(2, 1, figsize=figsize)
            _ = spectrogram(
                raw_data[win1:win2],
                1 / self.dt,
                axes=ax[0],
                dbscale=dbscale,
                log=log,
                show=show,
            )
            _ = spectrogram(
                rfft_whitedata,
                1 / self.dt,
                axes=ax[1],
                dbscale=dbscale,
                log=log,
                show=show,
            )
            ax[0].plot(
                [0, cc_len],
                [self.freqmin, self.freqmin],
                "--",
                color="red",
                lw=3,
                alpha=0.7,
            )
            ax[0].plot(
                [0, cc_len],
                [self.freqmax, self.freqmax],
                "--",
                color="red",
                lw=3,
                alpha=0.7,
            )
            ax[1].plot(
                [0, cc_len],
                [self.freqmin, self.freqmin],
                "--",
                color="red",
                lw=3,
                alpha=0.7,
            )
            ax[1].plot(
                [0, cc_len],
                [self.freqmax, self.freqmax],
                "--",
                color="red",
                lw=3,
                alpha=0.7,
            )
            fig.suptitle(
                f"RFFTData: channel_index={channel_index}, win_index={win_index} "
                f"\nfreq_band=[{self.freqmin:.3f}, {self.freqmax:.3f}] hz"
            )
            ax[0].set_ylim(freq_start, freq_end)
            ax[0].set_xlim(0, cc_len)
            ax[0].set_ylabel("Frequency(hz)")
            ax[0].set_title("raw data")
            ax[0].set_xticks([])
            ax[1].set_ylim(freq_start, freq_end)
            ax[1].set_xlim(0, cc_len)
            ax[1].set_ylabel("Frequency(hz)")
            ax[1].set_title(f"freq_norm: {self.freq_norm}")
            ax[1].set_xticks(time_ticks)
            ax[1].set_xticklabels(time_label, rotation=time_tick_rotation)

        if show:
            plt.show()
        else:
            plt.close(fig)
        if save_path is not None:
            fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
        else:
            return ax
