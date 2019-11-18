#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest

import part_1
import part_2


@pytest.mark.parametrize('arguments,output', [
    ("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2",
     138),
])
def test_part_1(arguments, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    # assert part_1.solution(arguments) == output
    assert part_1.solution(arguments) == output


@pytest.mark.parametrize('arguments,output', [
    ("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2",
     66),
])
def test_part_2(arguments, output):
    """Tests part 2 of the code with examples from the assignment.
    """
    assert part_2.solution(arguments) == output
