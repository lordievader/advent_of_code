"""Code for part 1 of day 2
"""
import collections
import pandas

def repeats(sequence):
    """Checks if there are letters that apper twice or thrice.

    :param sequence: sequence of letters to check
    :type sequence: str
    :return: (bool, bool) (twice, trice present)
    """
    count = collections.Counter(sequence).values()
    return (2 in count, 3 in count)

def counts_dataframe(sequences):
    counts = []
    for sequence in sequences:
        counts.append(repeats(sequence))

    dataframe = pandas.DataFrame(
        counts,
        columns=['two', 'three'])
    return dataframe

def checksum(dataframe):
    return dataframe.two.sum() * dataframe.three.sum()

def solution(sequences):
    """Solution to part one.
    """
    dataframe = counts_dataframe(sequences)
    return checksum(dataframe)
