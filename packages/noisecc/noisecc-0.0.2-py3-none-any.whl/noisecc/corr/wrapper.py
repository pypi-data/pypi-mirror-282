import numpy as np

from obspy.core import UTCDateTime
from noisecc.corr.corrclass import CorrClass
from noisecc.corr.corrdata import CorrData


def corr(
    data,
    dt,
    df,
    win_time_interval=None,
    starttime=UTCDateTime("1970-01-01T00:00:00.0"),
    pairs=np.array([0, 0]),
    method="xcorr",
    domain="time",
    maxlag=None,
    fstride=1,
    smoothspect_N=10,
    device="cpu",
    jobs=1,
    flag=True,
):
    # check demision of data
    if data.ndim == 2:
        data = data.reshape(data.shape[0], 1, data.shape[1])
        raise Warning(
            "data.ndim == 2, data.shape[0] will be treated as pair number, and data.shape[1] will be treated as npts, and segment will be set to 1."
        )

    # check demision of pairs
    pairs = np.round(pairs).astype(int)
    if pairs.ndim == 1:
        pairs = pairs.reshape(1, -1)

    # check method
    if method not in ["xcorr", "coherency", "deconv"]:
        raise ValueError("'method' must be 'xcorr', 'coherency', or 'deconv'")

    # check domain
    if domain not in ["time", "freq"]:
        raise ValueError("'domain' must be 'time' or 'freq'")

    # check maxlag
    rfft_npts = data.shape[2]
    if maxlag == None:
        maxlag = dt * (rfft_npts - 2)
    elif maxlag < 0:
        raise ValueError("'maxlag' must be >= 0")
    elif maxlag > dt * (rfft_npts - 2):
        raise ValueError(
            f"""'maxlag' must be <= {dt * (data.shape[2]-2):.6f} (calculated from dt*(data.shape[2]-2)). 
Note that length of irfft is 2*(rfft_npts - 1), and consider that the center point as 0, 
so maxlag = dt*(data.shape[2]-2)  (--maxlag---0---maxlag--)."""
        )

    # check fstride
    if type(fstride) != int:
        raise ValueError("'fstride' must be an integer")
    if fstride < 1:
        raise ValueError("'fstride' must be >= 1")
    if domain == "time" and fstride != 1:
        raise ValueError("'fstride' must be 1 in time domain")

    # check win_interval
    if win_time_interval is None:
        win_time_interval = 2 * (rfft_npts - 1) * dt

    # check device
    if device not in ["cpu", "cuda"]:
        raise ValueError("'device' must be 'cpu' or 'cuda'")

    # check jobs
    if jobs < 1:
        raise ValueError("'jobs' must be >= 1")

    # run corr
    m = CorrClass(
        data,
        dt,
        pairs,
        method,
        domain,
        maxlag,
        fstride,
        smoothspect_N,
        device,
        jobs,
        flag,
    )
    m.run()
    if domain == "time":
        tdata = m.output_data
        fdata = None
    elif domain == "freq":
        tdata = None
        fdata = m.output_data

    # generate CorrData object
    Corr_Data = CorrData(
        tdata,
        fdata,
        dt,
        fstride * df,
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
