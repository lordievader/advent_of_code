"""Code for part 1 of day 05.
"""
import pdb
import re
from string import ascii_uppercase

class Step():
    def __init__(self, name, duration=60, dependency=None):
        self.name = name
        self.duration = ascii_uppercase.index(self.name) + 1 + duration
        self.done_at = None
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
        if self.done_at is not None:
            return False

        return set(self.dependencies) <= set(done)

    def start(self, seconds):
        self.done_at = self.duration + seconds
        return self.done_at

    def done(self, seconds):
        return seconds >= self.done_at

class Worker():
    def __init__(self, name):
        self.name = name
        self.step = None

    def __repr__(self):
        if self.step is None:
            job = '.'

        else:
            job = self.step.name

        line = f"{self.name}: {job}"
        return line

    def assign(self, step, seconds):
        self.step = step
        self.step.start(seconds)

    def done(self, seconds):
        if self.step is None:
            return None, True

        return_data = (self.step.name, self.step.done(seconds))
        if return_data[1] is True:
            self.step = None

        return return_data


def next(steps, done):
    can_begin = []
    for name, step in steps.items():
        if step.can_begin(done) is True:
            can_begin.append(name)

    return sorted(can_begin)

def all_steps_done(workers, seconds):
    return sum([not worker.done(seconds)[1] for worker in workers]) == 0

def solution(sequences, duration):
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
            steps[before] = Step(before, duration)

        if after not in steps:
            steps[after] = Step(after, duration, before)

        else:
            steps[after].add_dependency(before)

    done = []

    num_workers = 5
    workers = [Worker(index) for index in range(num_workers)]

    seconds = 0
    while True:
        available_workers = []
        for worker in workers:
            name, is_done = worker.done(seconds)
            if is_done is True:
                available_workers.append(worker)
                if name is not None:
                    done.append(name)

        next_steps = next(steps, done)
        if len(next_steps) < len(available_workers):
            for index, step in enumerate(next_steps):
                available_workers[index].assign(steps[step], seconds)

        else:
            for index, worker in enumerate(available_workers):
                step = steps[next_steps[index]]
                worker.assign(step, seconds)

        worker_status = ", ".join([str(worker) for worker in workers])
        status = f"seconds: {seconds:2d} -- {worker_status} -- {''.join(done)}"
        if all_steps_done(workers, seconds) is True:
            break

        seconds += 1

    return seconds
