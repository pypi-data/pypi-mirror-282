from obspy.core import UTCDateTime
from noisecc.chunk.chunkclass import ChunkClass
from noisecc.chunk.chunkdata import ChunkData


def chunk(
    data,
    dt,
    cc_len,
    cc_step=0.0,
    starttime=UTCDateTime("1970-01-01T00:00:00.0"),
    time_norm="no",
    clip_std=10,
    smooth_N=20,
    device="cpu",
    jobs=1,
    flag=True,
):
    # check demision of data
    if data.ndim == 1:
        data = data.reshape(1, -1)

    # check cc_len
    if cc_len > data.shape[1] * dt:
        data_duration = data.shape[1] * dt
        message = (
            f"Error: the value of 'cc_len' is too large.\n"
            f"'cc_len' should be less than or equal to the duration of the data,"
            f"which is {data_duration:.2f} seconds.\n"
            f"Please adjust the value of 'cc_len' and try again."
        )
        raise ValueError(message)

    # check cc_step
    if cc_step >= cc_len:
        message = (
            f"Error: the value of 'cc_step' is invalid.\n"
            f"'cc_step' should be strictly less than 'cc_len' (current 'cc_len' value is {cc_len}).\n"
            f"Please adjust the value of 'cc_step' and try again."
        )
        raise ValueError(message)

    # check time_norm
    if time_norm not in ["no", "onebit", "clip", "ramn"]:
        raise ValueError("'time_norm' must be 'no', 'onebit', 'clip', or 'ramn'")

    # check device
    if device not in ["cpu", "cuda"]:
        raise ValueError("'device' must be 'cpu' or 'cuda'")

    # check jobs
    if jobs < 1:
        raise ValueError("'jobs' must be >= 1")

    # run chunk
    m = ChunkClass(
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
    )
    m.run()
    output_data = m.output_data

    # generate ChunkData object
    Chunk_Data = ChunkData(
        output_data,
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
