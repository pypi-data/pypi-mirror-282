import h5py
import json
import numpy as np

from obspy import UTCDateTime
from noisecc.chunk.chunkdata import ChunkData
from noisecc.rfft.rfftdata import RFFTData
from noisecc.corr.corrdata import CorrData
from noisecc.stack.stackdata import StackData


def load_chunk(filename, only_header=False):
    with h5py.File(filename, "r") as f:
        group = f["noisecc"]
        if only_header:
            data = None
        else:
            data = group["data"][:]

        dt = group.attrs["dt"]
        cc_len = group.attrs["cc_len"]
        cc_step = group.attrs["cc_step"]
        starttime = UTCDateTime(group.attrs["starttime"])
        time_norm = group.attrs["time_norm"]
        clip_std = group.attrs["clip_std"]
        smooth_N = group.attrs["smooth_N"]
        device = group.attrs["device"]
        flag = group.attrs["flag"]
        jobs = group.attrs["jobs"]

    Chunk_Data = ChunkData(
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
    )

    return Chunk_Data


def load_rfft(filename, only_header=False):

    with h5py.File(filename, "r") as f:
        group = f["noisecc"]
        if only_header:
            data = None
        else:
            data = group["data"][:]

        dt = group.attrs["dt"]
        df = group.attrs["df"]
        win_time_interval = group.attrs["win_time_interval"]
        starttime = UTCDateTime(group.attrs["starttime"])
        freq_norm = group.attrs["freq_norm"]
        freqmin = group.attrs["freqmin"]
        freqmax = group.attrs["freqmax"]
        whiten_npad = group.attrs["whiten_npad"]
        smoothspect_N = group.attrs["smoothspect_N"]
        device = group.attrs["device"]
        flag = group.attrs["flag"]
        jobs = group.attrs["jobs"]

    RFFT_Data = RFFTData(
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
    )

    return RFFT_Data


def load_corr(filename, type="time", only_header=False):

    if type == "time":
        with h5py.File(filename, "r") as f:
            group = f["noisecc"]
            if only_header:
                tdata = None
            else:
                tdata = group["data"][:]
            domain = group.attrs["domain"]
            dt = group.attrs["dt"]
            win_time_interval = group.attrs["win_time_interval"]
            starttime = UTCDateTime(group.attrs["starttime"])
            method = group.attrs["method"]
            maxlag = group.attrs["maxlag"]
            smoothspect_N = group.attrs["smoothspect_N"]
            device = group.attrs["device"]
            flag = group.attrs["flag"]
            jobs = group.attrs["jobs"]
            pairs = group["pairs"][:]

        Corr_Data = CorrData(
            tdata,
            None,
            dt,
            None,
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
        )

    elif type == "freq":
        with h5py.File(filename, "r") as f:
            group = f["noisecc"]
            if only_header:
                fdata = None
            else:
                fdata = group["data"][:]
            domain = group.attrs["domain"]
            df = group.attrs["df"]
            win_time_interval = group.attrs["win_time_interval"]
            starttime = UTCDateTime(group.attrs["starttime"])
            method = group.attrs["method"]
            maxlag = group.attrs["maxlag"]
            smoothspect_N = group.attrs["smoothspect_N"]
            device = group.attrs["device"]
            flag = group.attrs["flag"]
            jobs = group.attrs["jobs"]
            pairs = group["pairs"][:]

        Corr_Data = CorrData(
            None,
            fdata,
            None,
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
        )

    return Corr_Data


def load_stack(
    filename,
    pairs=None,
    type="time",
    only_header=False,
):

    if type == "time":
        with h5py.File(filename, "r") as f:
            group = f["noisecc"]
            dt = group.attrs["dt"]
            domain = group.attrs["domain"]
            info = {}
            ccwin_time_interval = group.attrs["ccwin_time_interval"]
            starttime = UTCDateTime(group.attrs["starttime"])
            raw_pairs = group["pairs"][:]
            if pairs is None:
                pairs = raw_pairs
                index = np.arange(0, pairs.shape[0])
            else:
                index = []
                for row in pairs:
                    match = np.where((raw_pairs == row).all(axis=1))
                    if match[0].size > 0:
                        index.append(match[0][0])
                    else:
                        index.append(-1)  # if not found, append -1
                        raise Warning(
                            f"{row} not found in the pairs database, and will be removed."
                        )
                index = np.array(index)
                index = index[index != -1]  # remove the unmatched pairs
                pairs = raw_pairs[index]

            ngood = group["ngood"][:][index]
            pairs_dist = group["pairs_dist"][:][index]
            dist_unit = group.attrs["dist_unit"]
            stack_all = group.attrs["stack_all"]
            stack_len = group.attrs["stack_len"]
            stack_step = group.attrs["stack_step"]
            method = group.attrs["method"]
            config = json.loads(group.attrs["config"])
            device = group.attrs["device"]
            flag = group.attrs["flag"]
            jobs = group.attrs["jobs"]

            if only_header:
                data = None
            else:
                # read index rows of the data
                data = group["data"][:][index, :, :]

        info = {}
        Stack_Data = StackData(
            data,  # tdata
            None,  # fdata
            dt,  # dt
            None,  # df
            "time",  # domain
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
        )
    elif type == "freq":
        with h5py.File(filename, "r") as f:
            group = f["noisecc"]
            df = group.attrs["df"]
            domain = group.attrs["domain"]
            info = {}
            ccwin_time_interval = group.attrs["ccwin_time_interval"]
            starttime = UTCDateTime(group.attrs["starttime"])
            raw_pairs = group["pairs"][:]
            if pairs is None:
                pairs = raw_pairs
                index = np.arange(0, pairs.shape[0])
            else:
                index = []
                for row in pairs:
                    match = np.where((raw_pairs == row).all(axis=1))
                    if match[0].size > 0:
                        index.append(match[0][0])
                    else:
                        index.append(-1)  # if not found, append -1
                        raise Warning(
                            f"{row} not found in the pairs database, and will be removed."
                        )
                index = np.array(index)
                index = index[index != -1]  # remove the unmatched pairs
                pairs = raw_pairs[index]

            ngood = group["ngood"][:][index]
            pairs_dist = group["pairs_dist"][:][index]
            dist_unit = group.attrs["dist_unit"]
            stack_all = group.attrs["stack_all"]
            stack_len = group.attrs["stack_len"]
            stack_step = group.attrs["stack_step"]
            method = group.attrs["method"]
            config = json.loads(group.attrs["config"])
            device = group.attrs["device"]
            flag = group.attrs["flag"]
            jobs = group.attrs["jobs"]

            if only_header:
                data = None
            else:
                # read index rows of the data
                data = group["data"][:][index, :, :]

        info = {}
        Stack_Data = StackData(
            None,  # tdata
            data,  # fdata
            None,  # dt
            df,  # df
            "freq",  # domain
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
        )
    return Stack_Data
