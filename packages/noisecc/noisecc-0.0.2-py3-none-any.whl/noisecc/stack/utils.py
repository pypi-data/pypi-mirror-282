import math
import numpy as np

from scipy.signal import hilbert
from scipy.fftpack import fft, ifft, next_fast_len


########################################################################################
###                              Time domain
########################################################################################
def stacklib(data, dt, dist, dist_unit, method, config, device):
    if method == "linear":
        ngood = data.shape[0]
        info = {}
        if device == "cpu":
            stack_data = linear_cpu(data)
        elif device == "cuda":
            stack_data = linear_cuda(data)
    elif method == "snr":
        signal_win = config["signal_win"]
        noise_win = config["noise_win"]
        branch = config["branch"]
        func_snr = config["func_snr"]
        threshold = config["threshold"]
        weighting = config["weighting"]
        if device == "cpu":
            stack_data, ngood, nindex, snr = snr_cpu(
                data,
                dt,
                dist,
                dist_unit,
                signal_win,
                noise_win,
                branch,
                func_snr,
                threshold,
                weighting,
            )
            info = {"nindex": nindex, "snr": snr}
        elif device == "cuda":
            stack_data, ngood, nindex, snr = snr_cuda(
                data,
                dt,
                dist,
                dist_unit,
                signal_win,
                noise_win,
                branch,
                func_snr,
                threshold,
                weighting,
            )
            info = {"nindex": nindex, "snr": snr}
    elif method == "rms_ratio":
        threshold = config["threshold"]
        if device == "cpu":
            stack_data, ngood = rms_ratio_cpu(data, threshold)
        elif device == "cuda":
            stack_data, ngood = rms_ratio_cuda(data, threshold)
        info = {}
    elif method == "bayes":
        ngood = data.shape[0]
        info = {}
        signal_win = config["signal_win"]
        noise_win = config["noise_win"]
        func_snr = config["func_snr"]
        theta = config["theta"]
        stack_data = bayes_cpu(data)
    elif method == "select":
        nindex = config["index"]
        weight = config["weight"]
        ngood = len(nindex)
        info = {"nindex": nindex, "weight": weight}
        if device == "cpu":
            stack_data = select_cpu(data, nindex, weight)
        elif device == "cuda":
            stack_data = select_cuda(data, nindex, weight)
    elif method == "pws":
        ngood = data.shape[0]
        info = {}
        p = config["p"]
        if device == "cpu":
            stack_data = pws_cpu(data, p)
        elif device == "cuda":
            stack_data = pws_cuda(data, p)
    elif method == "robust":
        ngood = data.shape[0]
        info = {}
        epsilon = config["epsilon"]
        maxstep = config["maxstep"]
        win = config["win"]
        ref = config["ref"]
        stat = False
        if device == "cpu":
            stack_data = robust_cpu(data, epsilon, maxstep, win, ref, stat)
        elif device == "cuda":
            stack_data = robust_cuda(data, epsilon, maxstep, win, ref, stat)
    elif method == "acf":
        ngood = data.shape[0]
        info = {}
        g = config["g"]
        if device == "cpu":
            stack_data = adaptive_filter_cpu(data, g)
        elif device == "cuda":
            stack_data = adaptive_filter_cuda(data, g)

    return stack_data, ngood, info


# Bayesian sampling stack
def bayes_cpu(
    data,
    signal_win=[500, 5],  # [c, win]
    noise_win=None,  # [c, win]
    func_snr="max",  # 'max' or 'rms'
    theta=0.5,  # all pairs use the same theta
):
    c = []
    win = []


def linear_cpu(data):
    outdata = np.mean(data, axis=0)

    return outdata


def linear_cuda(data):
    pass


def select_cpu(data, nindex=None, weight=None):
    outdata = np.mean(data, axis=-1)


def select_cuda(data, nindex=None, weight=None):
    pass


def snr_cpu(
    data,
    dt,
    dist,
    dist_unit,
    signal_win=[300, 5],  # [c: m/s, win: s]
    noise_win=None,  # [c, win]
    branch="all",  # 'all', 'positive', or 'negative'
    func_snr="max",  # 'max' or 'rms'
    threshold=0.5,
    weighting=False,
):
    win_num = data.shape[0]
    npts = data.shape[1]
    mid_npts = math.ceil(npts / 2)

    # compute distance
    if dist_unit == "m":
        dist = dist
    elif dist_unit == "km":
        dist = dist * 1e3
    elif dist_unit == "deg":
        dist = dist * 111.2 * 1000

    # check siganl win
    c = signal_win[0]
    win_npts = int(signal_win[1] / dt)
    dist_npts = int(dist / c / dt)

    # construct signal and noise data
    signal_data = []
    noise_data = []
    for i in range(win_num):
        if branch == "all":
            positive_start = mid_npts + dist_npts
            positive_end = mid_npts + (dist_npts + win_npts)
            negative_end = mid_npts - dist_npts
            negative_start = mid_npts - (dist_npts + win_npts)
            signal_index = np.concatenate(
                (
                    np.arange(negative_start, negative_end),
                    np.arange(positive_start, positive_end),
                )
            )
        elif branch == "positive":
            positive_start = mid_npts + dist_npts
            positive_end = mid_npts + (dist_npts + win_npts)
            signal_index = np.arange(positive_start, positive_end)
        elif branch == "negative":
            negative_end = mid_npts - dist_npts
            negative_start = mid_npts - (dist_npts + win_npts)
            signal_index = np.arange(negative_start, negative_end)

        signal_data.append(data[i, signal_index])

        # check noise win
        if noise_win is not None:
            c = noise_win[0]
            win_npts = int(noise_win[1] / dt)
            if branch == "all":
                positive_start = mid_npts + dist_npts
                positive_end = mid_npts + (dist_npts + win_npts)
                negative_end = mid_npts - dist_npts
                negative_start = mid_npts - (dist_npts + win_npts)
                noise_index = np.concatenate(
                    (
                        np.arange(negative_start, negative_end),
                        np.arange(positive_start, positive_end),
                    )
                )
            elif branch == "positive":
                positive_start = mid_npts + dist_npts
                positive_end = mid_npts + (dist_npts + win_npts)
                noise_index = np.arange(positive_start, positive_end)
            elif branch == "negative":
                negative_end = mid_npts - dist_npts
                negative_start = mid_npts - (dist_npts + win_npts)
                noise_index = np.arange(negative_start, negative_end)
        else:
            if branch == "all":
                noise_index = np.setdiff1d(np.arange(npts), signal_index)
            elif branch == "positive":
                noise_index = np.setdiff1d(np.arange(mid_npts, npts), signal_index)
            elif branch == "negative":
                noise_index = np.setdiff1d(np.arange(0, mid_npts), signal_index)

        noise_data.append(data[i, noise_index])

    # convert to numpy array
    signal_data = np.array(signal_data)
    noise_data = np.array(noise_data)

    # compute snr
    if func_snr == "max":
        snr = np.max(np.abs(signal_data), axis=-1) / np.sqrt(
            np.mean(noise_data**2, axis=-1)
        )
    elif func_snr == "rms":
        snr = np.sqrt(np.mean(signal_data**2, axis=-1)) / np.sqrt(
            np.mean(noise_data**2, axis=-1)
        )
    snr = snr / np.max(snr)

    # check ngood
    ngood = np.sum(snr > threshold)
    nindex = np.array(np.where(snr > threshold)[0], dtype=int)

    # stack
    if weighting:
        outdata = np.mean(snr[nindex, np.newaxis] * data[nindex], axis=0)
    else:
        outdata = np.mean(data[nindex], axis=0)

    return outdata, ngood, nindex, snr


def snr_cuda(
    data,
    dt,
    pairs_dist,
    dist_unit,
    signal_win=[300, 5],
    noise_win=None,
    branch="all",
    func_snr="max",
    threshold=0.5,
    weighting=False,
):
    pass


def rms_ratio_cpu(data, threshold=0.5):
    pass


def rms_ratio_cuda(data, threshold=0.5):
    pass


def robust_cpu(data, epsilon=1e-5, maxstep=10, win=None, ref=None, stat=False):
    """
    this is a robust stacking algorithm described in Pavlis and Vernon 2010. Generalized
    by Xiaotao Yang.

    PARAMETERS:
    ----------------------
    data: numpy.ndarray contains the 2D cross correlation matrix
    epsilon: residual threhold to quit the iteration (a small number). Default 1E-5
    maxstep: maximum iterations. default 10.
    win: [start_index,end_index] used to compute the weight, instead of the entire trace. Default None.
            When None, use the entire trace.
    ref: reference stack, with the same length as individual data. Default: None. Use median().
    RETURNS:
    ----------------------
    outdata: numpy vector contains the stacked cross correlation

    Written by Marine Denolle
    Modified by Xiaotao Yang
    """
    if data.ndim == 1:
        print("2D matrix is needed")
        return data
    N, M = data.shape
    res = 9e9  # residuals
    w = np.ones(data.shape[0])
    small_number = 1e-15
    nstep = 0
    if N >= 2:
        if ref is None:
            outdata = np.median(data, axis=0)
        else:
            outdata = ref
        if win is None:
            win = [0, -1]
        while res > epsilon and nstep <= maxstep:
            stack = outdata
            for i in range(data.shape[0]):
                dtemp = data[i, win[0] : win[1]]
                crap = np.multiply(stack[win[0] : win[1]], dtemp.T)
                crap_dot = np.sum(crap)
                di_norm = np.linalg.norm(dtemp)
                ri_norm = np.linalg.norm(dtemp - crap_dot * stack[win[0] : win[1]])
                if ri_norm < small_number:
                    w[i] = 0
                else:
                    w[i] = np.abs(crap_dot) / di_norm / ri_norm
            w = w / np.sum(w)
            outdata = np.sum((w * data.T).T, axis=0)  # /len(cc_array[:,1])
            res = (
                np.linalg.norm(outdata - stack, ord=1)
                / np.linalg.norm(outdata)
                / len(data[:, 1])
            )
            nstep += 1
    else:
        outdata = data[0].copy()
    if stat:
        return outdata, w, nstep
    else:
        return outdata


def robust_cuda(data, epsilon=1e-5, maxstep=10, win=None, ref=None, stat=False):
    pass


def pws_cpu(data, p=2):
    """
    Performs phase-weighted stack on array of time series. Modified on the noise function by Tim Climents.
    Follows methods of Schimmel and Paulssen, 1997.
    If s(t) is time series data (seismogram, or cross-correlation),
    S(t) = s(t) + i*H(s(t)), where H(s(t)) is Hilbert transform of s(t)
    S(t) = s(t) + i*H(s(t)) = A(t)*exp(i*phi(t)), where
    A(t) is envelope of s(t) and phi(t) is phase of s(t)
    Phase-weighted stack, g(t), is then:
    g(t) = 1/N sum j = 1:N s_j(t) * | 1/N sum k = 1:N exp[i * phi_k(t)]|^v
    where N is number of traces used, v is sharpness of phase-weighted stack

    PARAMETERS:
    ---------------------
    data: N length array of time series data (numpy.ndarray)
    p: exponent for phase stack (int). default is 2

    RETURNS:
    ---------------------
    outdata: Phase weighted stack of time series data (numpy.ndarray)
    """

    if data.ndim == 1:
        print("2D matrix is needed")
        return data
    N, M = data.shape
    if N >= 2:
        analytic = hilbert(data, axis=1, N=next_fast_len(M))[:, :M]
        phase = np.angle(analytic)
        phase_stack = np.mean(np.exp(1j * phase), axis=0)
        phase_stack = np.abs(phase_stack) ** (p)

        weighted = np.multiply(data, phase_stack)

        outdata = np.mean(weighted, axis=0)
    else:
        outdata = data[0].copy()
    return outdata


def pws_cuda(data, p=2):
    pass


def adaptive_filter_cpu(data, g=1):
    """
    the adaptive covariance filter to enhance coherent signals. Fellows the method of
    Nakata et al., 2015 (Appendix B)

    the filtered signal [x1] is given by x1 = ifft(P*x1(w)) where x1 is the ffted spectra
    and P is the filter. P is constructed by using the temporal covariance matrix.

    PARAMETERS:
    ----------------------
    data: numpy.ndarray contains the 2D traces of daily/hourly cross-correlation functions
    g: a positive number to adjust the filter harshness [default is 1]
    RETURNS:
    ----------------------
    outdata: numpy vector contains the stacked cross correlation function
    """
    if data.ndim == 1:
        print("2D matrix is needed")
        return data
    N, M = data.shape
    if N >= 2:
        Nfft = next_fast_len(M)

        # fft the 2D array
        spec = fft(data, axis=1, n=Nfft)[:, :M]

        # make cross-spectrm matrix
        cspec = np.zeros(shape=(N * N, M), dtype=np.complex64)
        for ii in range(N):
            for jj in range(N):
                kk = ii * N + jj
                cspec[kk] = spec[ii] * np.conjugate(spec[jj])

        S1 = np.zeros(M, dtype=np.complex64)
        S2 = np.zeros(M, dtype=np.complex64)
        # construct the filter P
        for ii in range(N):
            mm = ii * N + ii
            S2 += cspec[mm]
            for jj in range(N):
                kk = ii * N + jj
                S1 += cspec[kk]

        p = np.power((S1 - S2) / (S2 * (N - 1)), g)

        # make ifft
        narr = np.real(ifft(np.multiply(p, spec), Nfft, axis=1)[:, :M])
        outdata = np.mean(narr, axis=0)
    else:
        outdata = data[0].copy()

    return outdata


def adaptive_filter_cuda(data, g=1):
    pass


########################################################################################
###                              Frequency domain
########################################################################################
def stacklib_freq(data, df, pairs_dist, dist_unit, method, config, device):
    if method == "linear":
        ngood = data.shape[0]
        info = {}
        if device == "cpu":
            stack_data = linear_freq_cpu(data)
        elif device == "cuda":
            stack_data = linear_freq_cuda(data)
    elif method == "select":
        nindex = config["index"]
        weight = config["weight"]
        ngood = len(nindex)
        info = {"nindex": nindex, "weight": weight}
        if device == "cpu":
            stack_data = select_freq_cpu(data, nindex, weight)
        elif device == "cuda":
            stack_data = select_freq_cuda(data, nindex, weight)
    elif method == "pws":
        ngood = data.shape[0]
        info = {}
        p = config["p"]
        if device == "cpu":
            stack_data = pws_freq_cpu(data, p)
        elif device == "cuda":
            stack_data = pws_freq_cuda(data, p)

    return stack_data, ngood, info


def linear_freq_cpu(data):
    outdata = np.mean(data, axis=0)

    return outdata


def linear_freq_cuda(data):
    pass


def select_freq_cpu(data, nindex=None, weight=None):
    pass


def select_freq_cuda(data, nindex=None, weight=None):
    pass


def pws_freq_cpu(data, p):
    pass


def pws_freq_cuda(data, p):
    pass
