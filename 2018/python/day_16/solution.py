#!/usr/bin/env python3
"""Author:      Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:    Solution for AoC day 02.
"""
import re
import pdb

import part_1
import part_2


def main():
    """Main function.
    """
    with open('part_1_input', 'r') as input_file:
        problem_input = input_file.read()


    problem_input_part_1 = re.split(r'\n\n\n', problem_input)[0]
    problem_input_part_2 = re.split(r'\n\n\n', problem_input)[1]
    part_1_solution = part_1.solution(problem_input_part_1)
    part_2_solution = part_2.solution(problem_input_part_1, problem_input_part_2)
    print(f"Solution to part one: {part_1_solution}\nSolution to part two: {part_2_solution}")


if __name__ == '__main__':
    main()
