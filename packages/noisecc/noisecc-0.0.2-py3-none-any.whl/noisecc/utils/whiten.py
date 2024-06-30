import numpy as np


def moving_ave_cpu(A, N):
    """
    moving average

    Parameters
    ----------
    A : 1-d array
        input array
    N : int
        window length

    Returns
    -------
    B1 : array
        output array


    Examples
    --------
    >>> import numpy as np
    >>> from noisecc.utils.whiten import moving_ave_cpu
    >>> A = np.array([1, 2, 3, 4, 5])
    >>> N = 3
    >>> B1 = moving_ave_cpu(A, N)
    >>> print(B1)
    [1. 2. 3. 4. 5.]

    """
    temp = np.zeros(A.shape[0] + 2 * N)

    temp_len = temp.shape[0]
    temp[N : temp_len - N] = A
    temp[0:N] = temp[N]
    temp[temp_len - N : temp_len] = temp[temp_len - N - 1]

    nn = np.ones(N) / N
    b1 = np.convolve(temp, nn, mode="full")

    n1 = N + (N - 1) // 2
    n2 = N + (N - 1 - (N - 1) // 2)
    B1 = b1[n1 : b1.shape[0] - n2]

    return B1


def moving_ave_cuda(A, N):
    pass


def whiten_cpu(
    rfft_data, dt, freq_norm_method, freqmin, freqmax, smoothspect_N, whiten_npad
):
    """
    whiten

    Parameters
    ----------
    rfft_data : 2-d array
        input array
    dt : float
        sampling interval
    freq_norm_method : str
        frequency normalization method
    freqmin : float
        minimum frequency
    freqmax : float
        maximum frequency
    smoothspect_N : int
        window length for smoothing spectrum
    whiten_npad : int
        number of points to pad at both ends

    Returns
    -------
    rfft_norm_data : array
        output array


    Examples
    --------
    >>> import numpy as np
    >>> from noisecc.utils.whiten import whiten_cpu
    >>> rfft_data = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
    >>> dt = 0.1
    >>> freq_norm_method = 'whiten'
    >>> freqmin = 1
    >>> freqmax = 2
    >>> smoothspect_N = 3
    >>> whiten_npad = 2
    >>> rfft_norm_data = whiten_cpu(rfft_data, dt, freq_norm_method, freqmin, freqmax, smoothspect_N, whiten_npad)
    >>> print(rfft_norm_data)
        [[1.+0.j 2.+0.j 3.+0.j 4.+0.j 5.+0.j]
        [1.+0.j 2.+0.j 3.+0.j 4.+0.j 5.+0.j]]

    """
    _i = 0.0 + 1.0j
    _i0 = 0.0 + 0.0j
    _pi = np.pi

    win_num = rfft_data.shape[0]
    rfft_npts = rfft_data.shape[1]

    freq_array = (
        np.arange(rfft_npts) / dt / 2.0 / (rfft_npts - 1)
    )  # note: must divide by 2.0, because rfft_npts is not npts.
    J = np.where((freq_array >= freqmin) & (freq_array <= freqmax))[0]

    low = J[0] - whiten_npad
    if low <= 0:
        low = 0
    left = J[0]
    right = J[-1]
    high = J[-1] + whiten_npad
    if high > rfft_npts:
        high = rfft_npts

    rfft_norm_data = _i0 * np.ones((win_num, rfft_npts))

    for i in range(0, win_num):
        ## left zero cut-off
        # rfft_norm_data[i, 0:low] = _i0*rfft_data[i, 0:low]

        # left tapering
        smo1 = np.power(np.cos(np.linspace(_pi / 2, _pi, left - low)), 2)
        exp1 = np.exp(_i * np.angle(rfft_data[i, low:left]))
        rfft_norm_data[i, low:left] = smo1 * exp1

        # pass band
        if freq_norm_method == "whiten":
            smo2 = np.ones((right - left))
            exp2 = np.exp(_i * np.angle(rfft_data[i, left:right]))
            rfft_norm_data[i, left:right] = smo2 * exp2
        elif freq_norm_method == "smooth_whiten":
            data = rfft_data[i, left:right]
            rfft_norm_data[i, left:right] = data / moving_ave_cpu(
                np.abs(data), smoothspect_N
            )

        # right tapering
        smo3 = np.power(np.cos(np.linspace(0, _pi / 2, high - right)), 2)
        exp3 = np.exp(_i * np.angle(rfft_data[i, right:high]))
        rfft_norm_data[i, right:high] = smo3 * exp3

        ## right zero cut-off
        # rfft_norm_data[i, high:rfft_npts] = _i0*rfft_data[i, high:rfft_npts]

    return rfft_norm_data


def whiten_cuda(
    rfft_data, dt, freq_norm_method, freqmin, freqmax, smoothspect_N, whiten_npad
):
    pass
