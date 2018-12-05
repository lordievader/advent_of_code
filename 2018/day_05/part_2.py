import re
import concurrent.futures
import part_1


def find_length(letter, sequence):
    modified_sequence = re.sub(letter, '', sequence, flags=re.I)
    return part_1.solution(modified_sequence)


def remove_poly(sequence):
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
