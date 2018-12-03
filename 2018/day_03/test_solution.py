#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest

import part_1
import part_2


@pytest.mark.parametrize('arguments,output', [
    ([
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ], 4),
    ([
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 3,3: 2x2',
    ], 4),
])
def test_part_1(arguments, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    assert part_1.solution(arguments) == output
