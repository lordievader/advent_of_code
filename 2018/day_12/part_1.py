"""Code for part 1 of day 05.
"""
import logging
import numpy
import re
import pdb

logging.basicConfig(
    format='%(asctime)-23s %(funcName)15s: %(message)s',
    level=logging.INFO
)

option_regex = re.compile(r'([.#]+) => ([.#])')

class Option():
    def __init__(self, line):
        match = option_regex.match(line)
        self.name = to_numpy(match.group(1))
        self.replace = to_numpy(match.group(2))

    def __repr__(self):
        return ""

    def advance(self, state):
        new_state = numpy.ndarray(state.shape, dtype=numpy.int64)
        new_state[:] = 0
        window = rolling_window(state)
        locations = numpy.add(numpy.where(numpy.all(window == self.name, axis=1)), 2)
        new_state[locations] = self.replace
        return new_state


def rolling_window(a, window=5):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return numpy.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)

def collapse(new_states):
    state = new_states[0]
    for new_state in new_states[1:]:
        numpy.bitwise_or(state, new_state, out=state)

    return state

def to_numpy(state):
    return numpy.array(
        [int(char) for char in state.replace('.', '0').replace('#', '1')])

def extend(state, padding):
    new_state = numpy.ndarray(shape=(state.shape[0] + (padding * 2),), dtype=numpy.int64)
    new_state[:] = 0
    new_state[padding:-1*padding] = state
    return new_state

def print_state(generation, state):
    logging.debug(
        "%d: %s",
        generation,
        ("".join(state.astype(str)).replace('0', '.').replace('1', '#')))

def calculate_score(state, padding):
    return numpy.subtract(
        numpy.where(state == 1),
        padding).sum()

def solution(problem_input, generations=20):
    """Solution to part one.
    """
    padding = 2048
    problem = problem_input.split('\n')
    initial_state = problem[0].replace('initial state: ', '')
    state = extend(to_numpy(initial_state), padding)
    mutations = problem[2:-1]
    options = [Option(mutation) for mutation in mutations]

    generation = 0
    print_state(generation, state)
    for generation in range(generations):
        new_states = []
        for option in options:
            new_states.append(option.advance(state))

        state = collapse(new_states)
        print_state(generation + 1, state)

    return calculate_score(state, padding)
