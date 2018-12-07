"""Code for part 1 of day 05.
"""
import pdb
import re

class Step():
    def __init__(self, name, dependency=None):
        self.name = name
        self.done = False
        if dependency is None:
            self.dependencies = []

        else:
            self.dependencies = [dependency]

    def __repr__(self):
        line = f"{self.name} <= [{', '.join(self.dependencies)}]"
        return line

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def can_begin(self, done):
        if self.done is True:
            return False

        return set(self.dependencies) <= set(done)


def next(steps, done):
    can_begin = []
    for name, step in steps.items():
        if step.can_begin(done) is True:
            can_begin.append(name)

    return sorted(can_begin)[0]

def all_steps_done(steps):
    return sum([not step.done for step in steps.values()]) == 0

def solution(sequences):
    """Solution to part one.
    """
    regex = re.compile(
        r'Step ([A-Z]) must be finished before step ([A-Z]) can begin.')

    steps = {}
    for line in sequences:
        matches = regex.match(line)
        before = matches.group(1)
        after = matches.group(2)

        if before not in steps:
            steps[before] = Step(before)

        if after not in steps:
            steps[after] = Step(after, before)

        else:
            steps[after].add_dependency(before)

    done = []
    while all_steps_done(steps) is False:
        next_step = next(steps, done)
        steps[next_step].done = True
        done.append(next_step)

    return "".join(done)
