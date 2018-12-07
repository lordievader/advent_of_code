#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest

import part_1
import part_2

@pytest.mark.parametrize('arguments,output', [
    ([
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.'
     ], 'CABDFE'),
])
def test_part_1(arguments, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    # assert part_1.solution(arguments) == output
    assert part_1.solution(arguments) == output


@pytest.mark.parametrize('arguments,duration,output', [
    ([
        'Step C must be finished before step A can begin.',
        'Step C must be finished before step F can begin.',
        'Step A must be finished before step B can begin.',
        'Step A must be finished before step D can begin.',
        'Step B must be finished before step E can begin.',
        'Step D must be finished before step E can begin.',
        'Step F must be finished before step E can begin.'
     ], 0, 15),
])
def test_part_2(arguments, duration, output):
    """Tests part 2 of the code with examples from the assignment.
    """
    assert part_2.solution(arguments, duration) == output
