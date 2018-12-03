#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest

import part_1
import part_2


@pytest.mark.parametrize('arguments,output', [
    ('abcdef', (False, False)),
    ('bababc', (True, True)),
    ('abbcde', (True, False)),
    ('abcccd', (False, True)),
    ('aabcdd', (True, False)),
    ('abcdee', (True, False)),
    ('ababab', (False, True))
])
def test_repeats(arguments, output):
    """Tests the counts function.
    """
    assert part_1.repeats(arguments) == output


@pytest.mark.parametrize('arguments,output', [
    ([
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabcdd',
        'abcdee',
        'ababab'
    ], 12),
])
def test_part_1(arguments, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    assert part_1.solution(arguments) == output


@pytest.mark.parametrize('a,b,output', [
    ('abcde', 'abcdf', 1),
    ('abcde', 'gbcdf', 2),
])
def test_difference(a, b, output):
    """Tests the diffrence function.
    """
    assert part_2.difference(a, b) == output


@pytest.mark.parametrize('arguments,output', [
    ([
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz'
    ], 'fgij'),
])
def test_part_2(arguments, output):
    """Tests part 2 solution.
    """
    assert part_2.solution(arguments) == output
