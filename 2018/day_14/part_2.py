"""Code for part 1 of day 05.
"""
import logging
import numpy
import re
import pdb

import part_1

logging.basicConfig(
    format='%(asctime)-23s %(funcName)15s: %(message)s',
    level=logging.DEBUG
)


def rolling_window(a, window=5):
    """Returns the array a in chunks of window size.

    :param a: numpy array
    :type a: numpy.ndarray
    :param window: window size
    :type window: int
    :return: numpy.ndarray
    """
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return numpy.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)


def found(problem_input, look_for, window=5):
    """Is the sequence to look for in the problem_input?

    :param problem_input: current state
    :type problem_input: numpy.ndarray
    :param look_for: what to look for
    :type look_for: numpy.ndarray
    :return: boolean
    """
    if len(problem_input) < window + 1:
        is_found = False

    elif problem_input[-window:] == look_for:
        is_found = True

    elif problem_input[-window-1:-1] == look_for:
        is_found = True

    else:
        is_found = False

    return is_found


def solution(look_for):
    """Solution to part one.
    """
    look_for = [int(x) for x in look_for]
    window = len(look_for)
    problem_input = [3, 7]
    elves = numpy.arange(2)
    while found(problem_input, look_for, window) is False:
        problem_input = part_1.next_generation(problem_input, elves)


    return len(problem_input) - window
