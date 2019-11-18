#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest

import part_1
import part_2

@pytest.mark.parametrize('arguments,output', [
    (['+1', '+1', '+1'], [1, 1, 1]),
    (['+0', '-0', '-1'], [0, 0, -1]),
    (['-2', '-10', '-1'], [-2, -10, -1]),
])
def test_to_int(arguments, output):
    """Test the to_int function.
    """
    assert part_1.to_int(arguments) == output


@pytest.mark.parametrize('arguments,output', [
    ([1, 1, 1], 3),
    ([0, 0, -1], -1),
    ([-2, -10, -1], -13),
])
def test_sum_freq(arguments, output):
    """Tests the sum_freq function.
    """
    assert part_1.sum_freq(arguments) == output


@pytest.mark.parametrize('arguments,output', [
    (['+1', '+1', '+1'], 3),
    (['+1', '+1', '-2'], 0),
    (['-1', '-2', '-3'], -6)])
def test_part_1(arguments, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    assert part_1.solution(arguments) == output


@pytest.mark.parametrize('arguments,output', [
    (['+1', '-1'], 0),
    (['+3', '+3', '+4', '-2', '-4'], 10),
    (['-6', '+3', '+8', '+5', '-6'], 5),
    (['+7', '+7', '-2', '-7', '-4'], 14),
])
def test_part_2(arguments, output):
    """Tests the solution of part 2 against the examples.
    """
    assert part_2.solution(arguments) == output
