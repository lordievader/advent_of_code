"""Code for part 1 of day 2
"""
import numpy
import re

import part_1

def sleepy_guard(guards):
    stats = {}
    for tag, guard in sorted(guards.items()):
        minute, amount = guard.max_minute()
        stats[amount] = (tag, minute)

    suspect = stats[max(stats.keys())]
    return suspect

def solution(sequences):
    """Solution to part one.
    """
    sorted_log = part_1.sort_log(sequences)
    guards = part_1.log(sorted_log)
    tag, minute = sleepy_guard(guards)
    return tag * minute
