import numpy


def to_int(numbers):
    """Converts the input strings to integers.

    :param numbers: list of frequencies
    :type numbers: list of strings
    :return: list of integers
    """
    return [int(number) for number in numbers]


def sum_freq(numbers):
    """Sums frequencies.

    :params numbers: list of frequencies
    :type numbers: list of integers
    :return: summed frequency
    """
    return numpy.sum(numbers)


def solution(numbers):
    """Solution to part one.
    """
    int_numbers = to_int(numbers)
    return sum_freq(int_numbers)
