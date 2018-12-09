"""Code for part 1 of day 05.
"""
import collections
import logging
import numpy

logging.basicConfig(
    format='%(asctime)-23s %(funcName)15s: %(message)s',
    level=logging.INFO
)

class Circle():
    def __init__(self):
        self.circle = collections.deque()

    def __repr__(self):
        line = 'None'
        self.current = (self.circle.index(0) * -1) % self.length
        self.circle.rotate(self.current)
        if self.current is not None:
            before = [str(x) for index, x in enumerate(self.circle)
                      if index < self.current]
            current = str(self.circle[self.current])
            after = [str(x) for index, x in enumerate(self.circle)
                     if index > self.current]
            line = f"{' '.join(before)} ({current}) {' '.join(after)}"

        self.circle.rotate(-1 * self.current)
        return line

    @property
    def length(self):
        return len(self.circle)

    def add(self, marble):
        self.circle.insert(2, marble)
        self.circle.rotate(-2)

    def popleft(self):
        return self.circle.popleft()


class Player():
    def __init__(self, name):
        self.name = name + 1
        self.points = 0

    def add_points(self, points):
        self.points += points


def cash_points(player, points, circle):
    circle.circle.rotate(7)
    marble = circle.popleft()
    player.add_points(marble + points)


def add_marble(player, marbles, circle):
    marble = marbles.popleft()
    if marble % 23 == 0 and marble != 0:
        cash_points(player, marble, circle)

    else:
        circle.add(marble)


def solution(num_players, num_rounds):
    """Solution to part one.
    """
    circle = Circle()
    marbles = collections.deque([index for index in range(num_rounds + 1)])
    add_marble(Player(-1), marbles, circle)

    players = [Player(index) for index in range(num_players)]

    current_round = 0
    while current_round < num_rounds:
        player = players[current_round % num_players]
        add_marble(player, marbles, circle)
        current_round += 1

    return max([player.points for player in players])
