import numpy as np


def split(num, n_jobs):
    chunk_size = num // n_jobs
    results = []
    for i in range(0, n_jobs):
        chunk_start = i * chunk_size
        if i == n_jobs - 1:
            chunk_end = num
        else:
            chunk_end = (i + 1) * chunk_size
        results.append([chunk_start, chunk_end])

    return results


def slice_window(npts, segment_points, step_points):
    if segment_points < npts:
        slide_points = segment_points - step_points
        win_num = 0
        for i in range(0, int(npts / slide_points)):
            if (i * slide_points + segment_points) <= npts:
                win_num += 1
            else:
                break
        win_info = np.empty((win_num, 2), dtype=int)
        for i in range(win_num):
            win_info[i, 0] = i * slide_points
            win_info[i, 1] = i * slide_points + segment_points
    elif segment_points == npts:
        win_num = 1
        win_info = np.array([[0, npts]], dtype=int)
    else:
        raise ValueError(
            "error: segment-points length is larger than npts when slicing windows!"
        )

    return win_info
