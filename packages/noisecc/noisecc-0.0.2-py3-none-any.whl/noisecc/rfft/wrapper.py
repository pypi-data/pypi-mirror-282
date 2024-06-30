from obspy.core import UTCDateTime
from noisecc.rfft.rfftclass import RFFTClass
from noisecc.rfft.rfftdata import RFFTData


def rfft(
    data,
    dt,
    win_time_interval=None,
    starttime=UTCDateTime("1970-01-01T00:00:00.0"),
    freq_norm="no",
    freqmin=None,
    freqmax=None,
    whiten_npad=50,
    smoothspect_N=20,
    device="cpu",
    jobs=1,
    flag=True,
):
    # check demision of data
    if data.ndim == 2:
        data = data.reshape(data.shape[0], 1, data.shape[1])
        raise Warning(
            "data.ndim == 2, data.shape[0] will be treated as channel number, and data.shape[1] will be treated as npts, and segment will be set to 1."
        )

    # check win_interval
    if win_time_interval is None:
        win_time_interval = data.shape[2] * dt

    # check freq
    if freqmin is None:
        freqmin = 0.0
    elif freqmin < 0:
        raise ValueError("'freqmin' must be >= 0.0")
    nyquist_freq = 1 / (2 * dt)
    if freqmax is None:
        freqmax = nyquist_freq
    elif freqmax > nyquist_freq:
        raise ValueError(
            f"'freqmax' must be <= {nyquist_freq:.4f}Hz (Nyquist frequency)."
        )

    # check freqmin
    if freqmin >= freqmax:
        raise ValueError("'freqmin' must be strictly less than 'freqmax'")

    # check freq_norm
    if freq_norm not in ["no", "whiten", "smooth_whiten"]:
        raise ValueError("'freq_norm' must be 'no', 'whiten', or 'smooth_whiten'")

    # check device
    if device not in ["cpu", "cuda"]:
        raise ValueError("'device' must be 'cpu' or 'cuda'")

    # check jobs
    if jobs < 1:
        raise ValueError("'jobs' must be >= 1")

    # run rfft
    m = RFFTClass(
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
    )
    m.run()
    df = m.df
    output_data = m.output_data

    # generate RFFTData
    RFFT_Data = RFFTData(
        output_data,
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
