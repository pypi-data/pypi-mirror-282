import numpy as np
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


def _get_cmap(cmap):
    """Return a color map from a colormap or string."""
    if isinstance(cmap, str):  # get color map if a string was passed
        cmap = plt.get_cmap(cmap)
    return cmap


def _get_ax(ax, figsize=None, **kwargs):
    """Get an axis if ax is None"""
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=figsize, **kwargs)
    return ax


def _format_time_axis(
    ax, axis="x", tick_rotation=0, minticks=5, maxticks=None, labelsize=10
):
    locator = mdates.AutoDateLocator(tz="UTC", minticks=minticks, maxticks=maxticks)
    formatter = mdates.ConciseDateFormatter(locator)
    formatter.formats = [
        "%y",  # ticks are mostly years
        "%b",  # ticks are mostly months
        "%d",  # ticks are mostly days
        "%H:%M",  # hrs
        "%H:%M",  # min
        "%H:%M:%S.%f",
    ]  # secs

    formatter.zero_formats = [
        "",
        "%Y",
        "%b",
        "%b-%d",
        "%H:%M",
        "%H:%M:%S.%f",
    ]

    formatter.offset_formats = [
        "",
        "%Y",
        "%Y-%m",
        "%Y-%m-%d",
        "%Y-%m-%d",
        "%Y-%m-%dT%H:%M:%S",
    ]
    if axis.lower() == "x":
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
    elif axis.lower() == "y":
        ax.yaxis.set_major_locator(locator)
        ax.yaxis.set_major_formatter(formatter)
    ax.tick_params(axis=axis.lower(), rotation=tick_rotation, labelsize=labelsize)


def _format_trace_axis(
    ax,
    start=0,
    end=1,
    axis="y",
    tick_rotation=0,
    ticks=5,
    labelsize=10,
):
    # ---- [Get the current axis limit, deperated] ----#
    # start, end = ax.get_xlim() if axis.lower() == "x" else ax.get_ylim()

    # Define the ticks spacing
    if ticks > (end - start):
        spacing = 1
    else:
        spacing = (end - start) // (ticks - 1)

    # Generate ticks values
    ticks_values = np.arange(start, end + 1, spacing)

    # Set the ticks
    ax.set_xticks(ticks_values) if axis.lower() == "x" else ax.set_yticks(ticks_values)

    # Set the rotation
    ax.tick_params(axis=axis, rotation=tick_rotation, labelsize=labelsize)


def hex_to_RGB(hex_str):
    """#FFFFFF -> [255,255,255]"""
    # Pass 16 to the integer function for change of base
    return [int(hex_str[i : i + 2], 16) for i in range(1, 6, 2)]


def get_color_gradient(c1, c2, n):
    """
    Given two hex colors, returns a color gradient
    with n colors.
    """
    if n == 1:
        return [c1]
    else:
        c1_rgb = np.array(hex_to_RGB(c1)) / 255
        c2_rgb = np.array(hex_to_RGB(c2)) / 255
        mix_pcts = [x / (n - 1) for x in range(n)]
        rgb_colors = [((1 - mix) * c1_rgb + (mix * c2_rgb)) for mix in mix_pcts]
        return [
            "#" + "".join([format(int(round(val * 255)), "02x") for val in item])
            for item in rgb_colors
        ]
