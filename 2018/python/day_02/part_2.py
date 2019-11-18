"""Code for part 2 of day 2.
"""


def difference(compare_a, compare_b):
    """Checks the similarity between two words.
    """
    diff_count = 0
    for index, letter in enumerate(compare_a):
        if letter != compare_b[index]:
            diff_count += 1
            if diff_count == 2:
                break

    return diff_count


def solution(numbers):
    """Solution to part 2.
    """
    index = 0
    close = []
    while index != len(numbers) - 1:
        compare_a = numbers[index]
        for number in numbers[index + 1:]:
            compare_b = number
            diff_count = difference(compare_a, compare_b)
            if diff_count == 1:
                if compare_a not in close:
                    close.append(compare_a)

                if compare_b not in close:
                    close.append(compare_b)

        index += 1

    common_letters = []
    for index, letter in enumerate(close[0]):
        if letter == close[1][index]:
            common_letters.append(letter)

    return "".join(common_letters)
