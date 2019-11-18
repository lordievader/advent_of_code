#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest

import part_1
import part_2

@pytest.mark.parametrize('arguments,output', [
    ([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up",
    ], 240),
])
def test_part_1(arguments, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    # assert part_1.solution(arguments) == output
    assert part_1.solution(arguments) == output

@pytest.mark.parametrize('arguments,output', [
    ([
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up",
    ], 4455),
])
def test_part_2(arguments, output):
    """Tests part 2 of the code with examples from the assignment.
    """
    # assert part_1.solution(arguments) == output
    assert part_2.solution(arguments) == output
