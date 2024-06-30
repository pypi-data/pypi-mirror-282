import numpy as np


def time_linspace(start_time, end_time, num):
    t_min = 0
    t_max = end_time - start_time
    t_vector = np.linspace(t_min, t_max, num=num)
    date_vector = np.array([start_time + i for i in t_vector])

    return date_vector
