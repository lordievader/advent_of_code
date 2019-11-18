#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest

import part_1

# ((
#     '#######\n'
#     '#G..#E#\n'
#     '#E#E.E#\n'
#     '#G.##.#\n'
#     '#...#E#\n'
#     '#...E.#\n'
#     '#######\n'
# ), 36334)

@pytest.mark.parametrize('problem_input,output', [
    ((
        '#######\n'
        '#E..G.#\n'
        '#...#.#\n'
        '#.G.#G#\n'
        '#######\n'
    ), 36334),

])
def test_part_1(problem_input, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    assert part_1.solution(problem_input) == output
