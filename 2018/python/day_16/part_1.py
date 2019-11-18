"""Code for part 1 of day 16.
"""
import logging
import pdb
import re

logging.basicConfig(
    format='%(asctime)-23s %(funcName)15s: %(message)s',
    level=logging.DEBUG
)


class Machine():
    """State machine
    """
    registers = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
    }

    def __init__(self, registers=None):
        self.__set_state__(registers)

    def __set_state__(self, registers=None):
        if registers is not None:
            for index, value in enumerate(registers):
                self.registers[index] = value

    @property
    def state(self):
        """Prints the current state of the registers.
        """
        registers = []
        for _, value in sorted(self.registers.items()):
            registers.append(value)

        return registers

    def addr(self, register_a, register_b, register_c):
        """Addr operation.

        :param register_a: first register to use
        :type register_a: int
        :param register_b: value to use
        :type register_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = (
            self.registers[register_a] + self.registers[register_b])

    def addi(self, register_a, value_b, register_c):
        """Addi operation.

        :param register_a: first register to use
        :type register_a: int
        :param value_b: value to use
        :type value_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = (
            self.registers[register_a] + value_b)

    def mulr(self, register_a, register_b, register_c):
        """Mulr operation.

        :param register_a: first register to use
        :type register_a: int
        :param register_b: value to use
        :type register_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = (
            self.registers[register_a] * self.registers[register_b])

    def muli(self, register_a, value_b, register_c):
        """Muli operation.

        :param register_a: first register to use
        :type register_a: int
        :param value_b: value to use
        :type value_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = (
            self.registers[register_a] * value_b)

    def banr(self, register_a, register_b, register_c):
        """Banr operation.

        :param register_a: first register to use
        :type register_a: int
        :param register_b: value to use
        :type register_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = (
            self.registers[register_a] & self.registers[register_b])

    def bani(self, register_a, value_b, register_c):
        """Bani operation.

        :param register_a: first register to use
        :type register_a: int
        :param value_b: value to use
        :type value_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = (
            self.registers[register_a] & value_b)

    def borr(self, register_a, register_b, register_c):
        """Borr operation.

        :param register_a: first register to use
        :type register_a: int
        :param register_b: value to use
        :type register_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = (
            self.registers[register_a] | self.registers[register_b])

    def bori(self, register_a, value_b, register_c):
        """Bori operation.

        :param register_a: first register to use
        :type register_a: int
        :param value_b: value to use
        :type value_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = (
            self.registers[register_a] | value_b)

    def setr(self, register_a, register_b, register_c):
        """Setr operation.

        :param register_a: first register to use
        :type register_a: int
        :param register_b: this register is ignored
        :type register_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = self.registers[register_a]

    def seti(self, value_a, value_b, register_c):
        """Seti operation.

        :param value_a: value to use
        :type value_a: int
        :param value_b: this value is ignored
        :type value_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        self.registers[register_c] = value_a

    def gtir(self, value_a, register_b, register_c):
        """Gtir operation.

        :param value_a: value to use
        :type value_a: int
        :param register_b: second register to use
        :type register_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        if value_a > self.registers[register_b]:
            value = 1

        else:
            value = 0

        self.registers[register_c] = value

    def gtri(self, register_a, value_b, register_c):
        """Gtir operation.

        :param register_a: first register to use
        :type register_a: int
        :param value_b: value to use
        :type value_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        if self.registers[register_a] > value_b:
            value = 1

        else:
            value = 0

        self.registers[register_c] = value

    def gtrr(self, register_a, register_b, register_c):
        """Gtrr operation.

        :param register_a: first register to use
        :type register_a: int
        :param register_b: second register to use
        :type register_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        if self.registers[register_a] > self.registers[register_b]:
            value = 1

        else:
            value = 0

        self.registers[register_c] = value

    def eqir(self, value_a, register_b, register_c):
        """Eqir operation.

        :param value_a: value to use
        :type value_a: int
        :param register_b: second register to use
        :type register_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        if value_a == self.registers[register_b]:
            value = 1

        else:
            value = 0

        self.registers[register_c] = value

    def eqri(self, register_a, value_b, register_c):
        """Eqri operation.

        :param register_a: first register to use
        :type register_a: int
        :param value_b: value to use
        :type value_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        if self.registers[register_a] == value_b:
            value = 1

        else:
            value = 0

        self.registers[register_c] = value

    def eqrr(self, register_a, register_b, register_c):
        """Eqrr operation.

        :param register_a: first register to use
        :type register_a: int
        :param register_b: second register to use
        :type register_b: int
        :param register_c: register to wite to
        :type register_c: int
        """
        if self.registers[register_a] == self.registers[register_b]:
            value = 1

        else:
            value = 0

        self.registers[register_c] = value

def decode_sample(problem_input):
    problem_input = problem_input.split('\n')
    before = [int(x) for x in re.findall(r'[0-9]+', problem_input[0])]
    instruction = [int(x) for x in re.findall(r'[0-9]+', problem_input[1])]
    after = [int(x) for x in re.findall(r'[0-9]+', problem_input[2])]
    return before, instruction, after

def opcodes(problem_input):
    """Find the possible opcodes for the sample.
    """
    before, instruction, after = decode_sample(problem_input)
    machine = Machine(before)
    functions = {
        name: getattr(machine, name)
        for name in dir(machine)
        if not name.startswith('__') and callable(getattr(machine, name))
    }
    valid = []
    for name, func in functions.items():
        func(instruction[1], instruction[2], instruction[3])
        if machine.state == after:
            valid.append(name)

        machine.__set_state__(before)

    return valid


def number_of_opcodes(problem_input):
    """Checks the possible opcodes for the given sample.
    """
    return len(opcodes(problem_input))


def split_samples(problem_input):
    """Splits the problem input into samples.
    """
    return re.split(r'\n\n', problem_input)


def solution(problem_input):
    """Solution to part one.
    """
    samples = split_samples(problem_input)
    count = 0
    for sample in samples:
        opcodes = number_of_opcodes(sample)
        if opcodes >= 3:
            count += 1

    return count
