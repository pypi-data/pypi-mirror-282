import numpy as np

from obspy.core import UTCDateTime
from noisecc.stack.stackclass import StackClass
from noisecc.stack.stackdata import StackData

####################################################
#                     TIME                         #
####################################################
CONFIG = {
    "linear": {},
    "select": {
        "nindex": None,
        "weight": None,
    },
    "snr": {
        "signal_win": [300, 5],
        "noise_win": None,
        "branch": "all",
        "func_snr": "max",
        "threshold": 0.5,
        "weighting": False,
    },
    "rms_ratio": {
        "nindex": None,
        "weight": None,
    },
    "bayes": {},
    "pws": {
        "p": 2,
    },
    "robust": {
        "epsilon": 1e-5,
        "maxstep": 10,
        "win": None,
        "ref": None,
        "stat": False,
    },
    "acf": {"g": 1},
}


def stack(
    data,
    dt=1,
    win_time_interval=None,
    starttime=UTCDateTime("1970-01-01T00:00:00.0"),
    pairs=None,
    pairs_dist=None,
    dist_unit="m",
    stack_all=True,
    stack_len=1,
    stack_step=0,
    method="linear",
    config=None,
    device="cpu",
    jobs=1,
    flag=True,
):

    # check demision of data
    if data.ndim == 2:
        data = data.reshape(1, data.shape[0], data.shape[1])
        raise Warning(
            "data.ndim == 2, data.shape[0] will be treated as segments, and data.shape[1] will be treated as npts, and pair number will be set to 1."
        )

    # check win_time_interval
    if win_time_interval is None:
        win_time_interval = data.shape[2] * dt

    # check stack_all
    if stack_all:
        stack_len = data.shape[1]
        stack_step = 0

    # init pairs pairs_dist
    if pairs is None:
        pairs = np.full((data.shape[0], 2), np.nan)
    else:
        pairs = np.round(pairs).astype(int)

    # check demision of pairs
    if pairs.ndim == 1:
        pairs = pairs.reshape(1, -1)

    # check demision of pairs_dist
    if pairs_dist is None:
        pairs_dist = np.full(data.shape[0], np.nan)
    if pairs_dist.ndim == 2:
        pairs_dist = pairs_dist.reshape(-1)

    # check dist_unit
    if dist_unit not in ["m", "km", "degree"]:
        raise ValueError("'dist_unit' must be 'm', 'km', or 'degree'")

    # check stack_len
    if stack_len > data.shape[1]:
        raise ValueError(
            f"'stack_len' ({stack_len}) exceeds the maximum permissible value (data.shape[1]={data.shape[1]})"
        )

    # check stack_step
    if stack_step >= stack_len:
        raise ValueError(
            f"'stack_step' ({stack_step}) must be less than stack_len ({stack_len})"
        )

    # check method
    if method not in [
        "linear",
        "snr",
        "rms_ratio",
        "bayes",
        "select",
        "pws",
        "robust",
        "acf",
    ]:
        raise ValueError(
            "'method' must be 'linear', 'snr', 'rms_ratio', 'bayes', 'select', 'pws', 'robust', or 'acf'"
        )

    # check config
    if config is None:
        config = CONFIG[method]

    # check jobs
    if jobs < 1:
        raise ValueError("'jobs' must be >= 1")

    # run stack
    m = StackClass(
        data,
        dt,
        None,  # df
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
    m.run()
    output_data = m.output_data
    ngood = m.ngood
    info = m.info

    # generate StackData object
    Stack_Data = StackData(
        output_data,  # tdata
        None,  # fdata
        dt,  # dt
        None,  # df
        "time",  # domain
        ngood,
        info,
        win_time_interval,
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


####################################################
#                     FREQ                         #
####################################################
CONFIG_FREQ = {
    "linear": {},
    "select": {
        "nindex": None,
        "weight": None,
    },
    "pws": {
        "p": 2,
    },
}


def stack_freq(
    data,
    df=1,
    win_time_interval=None,
    starttime=UTCDateTime("1970-01-01T00:00:00.0"),
    pairs=None,
    pairs_dist=None,
    dist_unit="m",
    method="linear",
    stack_all=True,
    stack_len=1,
    stack_step=0,
    config=None,
    device="cpu",
    jobs=1,
    flag=True,
):

    # check demision of data
    if data.ndim == 2:
        data = data.reshape(1, data.shape[0], data.shape[1])
        raise Warning(
            "data.ndim == 2, data.shape[0] will be treated as segments, and data.shape[1] will be treated as npts, and pair number will be set to 1."
        )

    # check win_time_interval
    if win_time_interval is None:
        freq_npts = data.shape[2]
        time_npts = 2 * (freq_npts - 1)
        dt = 1 / (df * freq_npts)
        win_time_interval = time_npts * dt

    # check stack_all
    if stack_all:
        stack_len = data.shape[1]
        stack_step = 0

    # init pairs pairs_dist
    if pairs is None:
        pairs = np.full((data.shape[0], 2), np.nan)
    else:
        pairs = np.round(pairs).astype(int)

    # check demision of pairs
    if pairs.ndim == 1:
        pairs = pairs.reshape(1, -1)

    # check demision of pairs_dist
    if pairs_dist is None:
        pairs_dist = np.full(data.shape[0], np.nan)
    if pairs_dist.ndim == 2:
        pairs_dist = pairs_dist.reshape(-1)

    # check dist_unit
    if dist_unit not in ["m", "km", "degree"]:
        raise ValueError("'dist_unit' must be 'm', 'km', or 'degree'")

    # check stack_len
    if stack_len > data.shape[1]:
        raise ValueError(
            f"'stack_len' ({stack_len}) exceeds the maximum permissible value (data.shape[1]={data.shape[1]})"
        )

    # check stack_step
    if stack_step >= stack_len:
        raise ValueError(
            f"'stack_step' ({stack_step}) must be less than stack_len ({stack_len})"
        )

    # check method
    if method not in [
        "linear",
        "select",
        "pws",
    ]:
        raise ValueError("'method' must be 'linear', 'select', or 'pws'")

    # check config
    if config is None:
        config = CONFIG_FREQ[method]

    # check jobs
    if jobs < 1:
        raise ValueError("'jobs' must be >= 1")

    # run stack
    m = StackClass(
        data,
        None,  # dt
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
    )
    m.run()
    output_data = m.output_data
    ngood = m.ngood
    info = m.info

    # generate StackData object
    Stack_Data = StackData(
        None,  # tdata
        output_data,  # fdata
        None,  # dt
        df,  # df
        "freq",  # domain
        ngood,
        info,
        win_time_interval,
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
