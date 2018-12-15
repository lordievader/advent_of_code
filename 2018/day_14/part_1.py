"""Code for part 1 of day 05.
"""
import logging
import numpy
import re
import pdb

logging.basicConfig(
    format='%(asctime)-23s %(funcName)15s: %(message)s',
    level=logging.DEBUG
)


def next_generation(problem_input, elves):
    """Determines the next generation of recipes.
    """
    current = [problem_input[elves[0]], problem_input[elves[1]]]
    summed = sum(current)
    values = [summed // 10, summed % 10]
    if values[0] != 0:
        problem_input.extend(values)

    else:
        problem_input.append(values[1])

    numpy.mod(numpy.add(elves, numpy.array(current) + 1), len(problem_input), out=elves)
    return problem_input


def solution(number_recipes):
    """Solution to part one.
    """
    problem_input = [3, 7]
    required_length = number_recipes + 10
    elves = numpy.arange(2)
    while len(problem_input) < required_length:
        problem_input = next_generation(
            problem_input, elves)

    answer = problem_input[number_recipes:number_recipes + 10]
    return "".join([str(x) for x in answer])
