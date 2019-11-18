#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Test solution for AoC day 01.
"""
import pytest

import part_1
import part_2


@pytest.mark.parametrize('problem_input,output', [
    ((
        '/->-\        \n'
        '|   |  /----\\\n'
        '| /-+--+-\  |\n'
        '| | |  | v  |\n'
        '\-+-/  \-+--/\n'
        '  \------/   \n'
      ), '7,3'),
])
def test_part_1(problem_input, output):
    """Tests part 1 of the code with examples from the assignment.
    """
    assert part_1.solution(problem_input) == output

@pytest.mark.parametrize('problem_input,output', [
    ((
      '/>-<\  \n'
      '|   |  \n'
      '| /<+-\\\n'
      '| | | v\n'
      '\>+</ |\n'
      '  |   ^\n'
      '  \<->/\n'
      ), '6,4'),
])
def test_part_2(problem_input, output):
    """Tests part 2 of the code with examples from the assignment.
    """
    assert part_2.solution(problem_input) == output
