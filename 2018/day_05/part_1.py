"""Code for part 1 of day 05.
"""
import re


def replace(sequence, poly):
    """Removes the first poly from the sequence.

    :param sequence: input string
    :type sequence: str
    :param poly: poly to remove
    :type poly: str:
    :return: modified sequence
    """
    sequence = re.sub(poly, '', sequence, count=1)
    return sequence


def find_match(sequence):
    """Tries the find a poly to react. If it is found the poly is removed.

    :param sequence: input string
    :type sequence: str
    :return: changed, modified sequence
    """
    changed = False
    for match in re.finditer(r'([a-z])\1', sequence, flags=re.I):
        if (match.group(0).lower() != match.group(0) and
                match.group(0).upper() != match.group(0)):
            sequence = re.sub(match.group(0), '', sequence, count=1)
            changed = True
            break

    return changed, sequence

def solution(sequences):
    """Solution to part one.
    """
    changed, sequences = find_match(sequences)
    while changed is True:
        changed, sequences = find_match(sequences)

    return len(sequences)
