import re
import concurrent.futures
import part_1


def find_length(letter, sequence):
    """Removes the letter and runs the solution of part 1 to find the
    resulting length.

    :param letter: letter to remove
    :type letter: str
    :param sequence: input sequence
    :type sequence: str
    :return: length of the output
    """
    modified_sequence = re.sub(letter, '', sequence, flags=re.I)
    return part_1.solution(modified_sequence)


def remove_poly(sequence):
    """Finds the shortest output by removing a letter and trying to
    collapse the poly.

    :param sequence: input sequence
    :type sequence: str
    :return: shortest length
    """
    letters = set(list(sequence.lower()))
    length = None
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(find_length, letter, sequence)
                   for letter in letters]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if length is None or result < length:
                length = result

    return length


def solution(sequences):
    """Solution to part one.
    """
    return remove_poly(sequences)
