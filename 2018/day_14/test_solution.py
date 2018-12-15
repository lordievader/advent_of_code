#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest

import part_1
import part_2


@pytest.mark.parametrize('number_recipes,output', [
    (5, '0124515891'),
    (9, '5158916779'),
    (18, '9251071085'),
    (2018, '5941429882'),
])
def test_part_1(number_recipes, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    assert part_1.solution(number_recipes) == output

@pytest.mark.parametrize('look_for,output', [
    ('51589', 9),
    ('01245', 5),
    ('92510', 18),
    ('59414', 2018),
])
def test_part_2(look_for, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    assert part_2.solution(look_for) == output
