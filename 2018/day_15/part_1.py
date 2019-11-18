"""Code for part 1 of day 15.
"""
import logging
import copy
import pdb

logging.basicConfig(
    format='%(asctime)-23s %(funcName)15s: %(message)s',
    level=logging.DEBUG
)


class Cooordinates():
    """Cooordinates made easy ;)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x

        else:
            return self.y < other.y

    def is_same_location(self, other):
        return self.x == other.x and self.y == other.y

    def diff_x(self, other):
        return abs(self.x - other.x)

    def diff_y(self, other):
        return abs(self.y - other.y)

    def distance(self, other):
        diff_x = self.diff_x(other)
        diff_y = self.diff_y(other)
        return diff_x + diff_y


class Character():
    """Character representation
    """
    def __init__(self, faction, position_x, position_y, hp=200, attack_power=3):
        self.faction = faction
        self.coordinates = Cooordinates(position_x, position_y)
        self.hp = hp
        self.attack_power = attack_power

    def __repr__(self):
        line = f"{self.faction}: {self.coordinates}"
        return line

    def __lt__(self, other):
        return self.coordinates < other.coordinates

    def is_target(self, other):
        """A target is someone from another faction.
        """
        return not self.faction == other.faction

    def path(self, grid, characters, coordinates):
        """Traces a path to the coordinates.
        """
        split_grid = grid.split('\n')
        diff_x = self.coordinates.diff_x(coordinates)
        diff_y = self.coordinates.diff_y(coordinates)
        right = self.coordinates.x < coordinates.x
        down = self.coordinates.y < coordinates.y
        position = Cooordinates(self.coordinates.x, self.coordinates.y)
        reachable = True
        if down is True:
            previous_direction = '-'

        else:
            previous_direction = '|'

        history = [copy.copy(position)]
        while diff_x != 0 or diff_y != 0:
            if ((diff_x > 0 and previous_direction == '|')
                    or (diff_x > 0 and diff_y == 0)):
                previous_direction = '-'
                if right is True:
                    position.x += 1

                else:
                    position.x -= 1

                diff_x -= 1

            if ((diff_y > 0 and previous_direction == '-') or
                    (diff_y > 0 and diff_x == 0)):
                previous_direction = '|'
                if down is True:
                    position.y += 1

                else:
                    position.y -= 1

                diff_y -= 1

            symbol = split_grid[position.y][position.x]
            if symbol != '.':
                reachable = False
                break

            else:
                for character in characters:
                    if character.is_same_location(position):
                        reachable = False
                        break

            history.append(copy.copy(position))

        if reachable is True:
            return history

        else:
            return False

    def is_reachable(self, grid, characters, coordinates):
        """Determines if the coordinates are reachable.
        """
        reachable = False
        path = self.path(grid, characters, coordinates)
        if isinstance(path, list) is True:
            reachable = True

        return reachable

    def is_same_location(self, coordinates):
        return self.coordinates.is_same_location(coordinates)

    def distance(self, coordinates):
        return self.coordinates.distance(coordinates)

    def move_to(self, grid, characters, coordinates):
        """Moves the character.
        """
        path = self.path(grid, characters, coordinates)
        try:
            new_position = path[1]

        except IndexError:
            pdb.set_trace()

        logging.debug('%s -> %s', self.coordinates, new_position)
        self.coordinates = new_position

    def attack(self, character):
        """Attack another character.
        """
        character.hp -= self.attack_power


def print_grid(
        grid, characters,
        in_range=None, reachable=None,
        nearest=None, chosen=None,
        level='DEBUG'):
    """Prints the grid including the characters.

    :param grid: grid to print
    :type grid: str
    :param characters: characters to include
    :type characters: list
    :param in_range: squares in range
    :type in_range: list
    :param reachable: reachable squares
    :type reachable: list
    :param nearest: nearest squares
    :type nearest: list
    """
    lines = ['\n-------']
    for row_index, row in enumerate(grid.split('\n')):
        line = row
        for character in characters:
            if character.coordinates.y == row_index:
                line = (f"{line[:character.coordinates.x]}"
                        f"{character.faction}"
                        f"{line[character.coordinates.x + 1:]}"
                        f" {character.hp}")

        if in_range is not None:
            for coordinates in in_range:
                if coordinates.y == row_index:
                    line = (
                        f"{line[:coordinates.x]}"
                        "?"
                        f"{line[coordinates.x + 1:]}")

        if reachable is not None:
            for coordinates in reachable:
                if coordinates.y == row_index:
                    line = (
                        f"{line[:coordinates.x]}"
                        "@"
                        f"{line[coordinates.x + 1:]}")

        if nearest is not None:
            for coordinates in nearest:
                if coordinates.y == row_index:
                    line = (
                        f"{line[:coordinates.x]}"
                        "!"
                        f"{line[coordinates.x + 1:]}")

        if chosen is not None:
            if chosen.y == row_index:
                line = (
                    f"{line[:chosen.x]}"
                    "+"
                    f"{line[chosen.x + 1:]}")

        lines.append(line)

    line = "\n".join(lines)
    if level == 'DEBUG':
        logging.debug(line)

    else:
        logging.info(line)


def find_characters(problem_input):
    """Finds all the characters, build objects for them and removes them from
    the grid.

    :param problem_input: the problem_input
    :type problem_input: str
    :return: grid, characters
    """
    characters = []
    lines = []
    for row_index, row in enumerate(problem_input.split('\n')):
        line = row
        for column_index, column in enumerate(row):
            if column == 'E':
                characters.append(
                    Character(
                        'E',
                        column_index,
                        row_index
                    )
                )
                line = line[:column_index] + '.' + line[column_index + 1:]

            elif column == 'G':
                characters.append(
                    Character(
                        'G',
                        column_index,
                        row_index
                    )
                )
                line = line[:column_index] + '.' + line[column_index + 1:]

        lines.append(line)

    return "\n".join(lines), characters


def determine_targets(character, characters):
    """Determines who the targets are.

    :param character: character to act on
    :type character: Character
    :param characters: list of characters
    :type character: list
    :return: list of coordinates
    """
    return [other for other in characters if other.is_target(character)]


def in_range(grid, targets):
    """Determines which squares are in range of the targets.

    :param grid: grid to work with
    :type grid: str
    :param targets: list of targets
    :type targets: list
    :return: list of coordinates
    """
    split_grid = grid.split('\n')
    size_y = len(split_grid)
    size_x = len(split_grid[0])
    possible = []
    for character in targets:
        possibilities = [
            Cooordinates(
                character.coordinates.x - 1, character.coordinates.y),  # left
            Cooordinates(
                character.coordinates.x + 1, character.coordinates.y),  # right
            Cooordinates(
                character.coordinates.x, character.coordinates.y - 1),  # up
            Cooordinates(
                character.coordinates.x, character.coordinates.y + 1),  # down
        ]
        for possibility in possibilities:
            if (possibility.x > size_x or possibility.x < 0 or
                    possibility.y > size_y or possibility.y < 0):
                continue

            symbol = split_grid[possibility.y][possibility.x]
            if symbol == '.':
                possible.append(possibility)

    return possible


def reachable_targets(grid, characters, targets, character):
    """Checks if the targets are reachable for the character.

    :param grid: grid to work with
    :type grid: str
    :param targets: list of possible targets
    :type targets: list
    :param character: character to move
    :type character: Character
    :return: list of reachable targets
    """
    reachable = []
    for target in targets:
        if character.is_reachable(grid, characters, target):
            reachable.append(target)

    return reachable


def nearest_targets(character, targets):
    """Finds the nearest square.

    :param character: the character to move
    :type character: Character
    :param targets: target coordinates
    :type targets: list
    :return: list of nearest targets
    """
    distances = {}
    for target in targets:
        distance = character.distance(target)
        distances[target] = distance

    min_distance = min(distances.values())
    return [target
            for target in distances
            if distances[target] == min_distance]


def choose(nearest):
    """Choose a target.

    :param nearest: the nearest coordinates
    :type nearest: list
    :return: chosen coordinates
    """
    return sorted(nearest)[0]


def move_character(grid, characters, character):
    """Moves the character on the grid.

    :param grid: grid to use
    :type grid: str
    :param characters: characters to include
    :type characters: list
    :param character: character to move
    :type character: Character
    """
    logging.debug(character)
    targets = determine_targets(character, characters)
    logging.debug('targets of %s: %s', character, targets)
    if len(targets) == 0:
        return False

    possibilities = in_range(grid, targets)
    logging.debug('possibilities for %s: %s', character, possibilities)
    print_grid(grid, characters, in_range=possibilities)
    if len(possibilities) == 0:
        return False

    reachable = reachable_targets(grid, characters, possibilities, character)
    print_grid(grid, characters, reachable=reachable)
    if len(reachable) == 0:
        return False

    nearest = nearest_targets(character, reachable)
    print_grid(grid, characters, nearest=nearest)
    if len(nearest) == 0:
        return False

    chosen = choose(nearest)
    print_grid(grid, characters, chosen=chosen)

    character.move_to(grid, characters, chosen)
    print_grid(grid, characters, level='INFO')
    return True


def in_attack_range(grid, characters, character):
    """Determines which character is in attack range.

    :param grid: grid to use
    :type grid: str
    :param characters: characters to include
    :type characters: list
    :param character: character to move
    :type character: Character
    """
    possibilities = [target
                     for target in characters
                     if character.distance(target.coordinates) == 1]
    return possibilities


def choose_attack(targets):
    """Chooses who to attack.

    :param targets: list of targets
    :type targets: list
    :return: character to attack
    """
    logging.debug(targets)
    if len(targets) == 1:
        attack = targets[0]

    else:
        hp_map = {target: target.hp for target in targets}
        lowest_hp = min(hp_map.values())
        targets = [target for target in hp_map if hp_map[target] == lowest_hp]
        attack = sorted(targets)[0]

    return attack


def attack_character(grid, characters, character):
    """Attacks another character.
    """
    targets = determine_targets(character, characters)
    logging.debug('targets of %s: %s', character, targets)
    if len(targets) == 0:
        return False

    possibilities = in_attack_range(grid, targets, character)
    logging.debug('targets in range of %s: %s', character, possibilities)
    if len(possibilities) == 0:
        return False

    chosen = choose_attack(targets)
    character.attack(chosen)
    print_grid(grid, characters, level='INFO')
    return True


def advance_stage(grid, characters):
    """Advances to the next stage.

    :param grid: grid to print
    :type grid: str
    :param characters: characters to include
    :type characters: list
    """
    for character in sorted(characters):
        moved = move_character(grid, characters, character)
        if moved is False:
            break

        attacked = attack_character(grid, characters, character)


def solution(problem_input):
    """Solution to part one.

    :param problem_input: the problem input
    :type problem_input: str
    """
    grid, characters = find_characters(problem_input)
    print_grid(grid, characters)
    for _ in range(10):
        advance_stage(grid, characters)
