#!/usr/bin/env pypy3
import sys
import re
import logging
import queue

INSTRUCTION_REGEX =re.compile(r'([a-z]+)\s([0-9a-z]+)(\s[-0-9a-z]+){0,1}')

def read_input():
    with open(sys.argv[1], 'r') as input_ref:
        data = input_ref.readlines()

    data = [line.replace('\n', '') for line in data]
    return data

def instructions_to_registers(instructions):
    registers = []
    for instruction in instructions:
        try:
            register = INSTRUCTION_REGEX.search(instruction).group(2)

        except AttributeError:
            continue

        registers.append(register)

    return set(registers)

def part1():
    instructions = read_input()
    registers = {register: 0 for register in instructions_to_registers(instructions)}
    logging.debug(registers)
    last_played = -1

    position = 0
    length = len(instructions)
    while position < length:
        instruction = instructions[position]
        decoded = INSTRUCTION_REGEX.search(instruction)
        try:
            func = decoded.group(1)
            register = decoded.group(2)
            if decoded.lastindex == 3:
                argument = decoded.group(3).replace(' ', '')
                try:
                    argument = int(argument)

                except ValueError:
                    argument = registers[argument]

            else:
                argument = None

        except AttributeError:
            print(instruction)
            raise

        if func == 'snd':
            last_played = registers[register]

        elif func == 'set':
            registers[register] = argument

        elif func == 'add':
            registers[register] += argument

        elif func == 'mul':
            registers[register] *= argument

        elif func == 'mod':
            registers[register] %= argument

        elif func == 'rcv':
            if registers[register] != 0:
                registers[register] = last_played
                break

        elif func == 'jgz':
            if registers[register] > 0:
                position += (argument - 1)

        position += 1

    logging.info('last played frequency: %d', last_played)

class Program():
    def __init__(self, registers, value, tx_queue, rx_queue, instructions):
        self.value = value
        self.registers = registers.copy()
        self.registers['p'] = value
        self.tx = tx_queue
        self.rx = rx_queue
        self.send_count = 0
        self.position = 0
        self.instructions = instructions
        self.dead_lock = False
        self.dead_lock_count = 0
        self.rcv = None

    def decode(self, instruction):
        decoded = INSTRUCTION_REGEX.search(instruction)
        try:
            func = decoded.group(1)
            register = decoded.group(2)
            if decoded.lastindex == 3:
                argument = decoded.group(3).replace(' ', '')
                try:
                    argument = int(argument)

                except ValueError:
                    argument = self.registers[argument]

            else:
                argument = None

        except AttributeError:
            print(instruction)
            raise

        return (func, register, argument)

    def advance(self):
        if self.dead_lock is True:
            if self.rx.empty() is False and self.dead_lock_count < 5:
                self.registers[self.rcv] = self.rx.get()
                self.dead_lock = False
                self.dead_lock_count += 1

            return

        instruction = self.instructions[self.position]
        func, register, argument = self.decode(instruction)
        if func == 'snd':
            self.send_count += 1
            value = self.registers[register]
            if isinstance(argument, int):
                value = argument

            self.tx.put(value)

        elif func == 'set':
            self.registers[register] = argument

        elif func == 'add':
            self.registers[register] += argument

        elif func == 'mul':
            self.registers[register] *= argument

        elif func == 'mod':
            self.registers[register] %= argument

        elif func == 'rcv':
            if self.rx.empty() is True:
                self.dead_lock = True
                self.rcv = register
                self.dead_lock_count = 0

            else:
                self.registers[register] = self.rx.get()

        elif func == 'jgz':
            jump = False
            try:
                register = int(register)
                if register > 0:
                    jump = True

            except ValueError:
                if self.registers[register] > 0:
                    jump = True

            if jump is True:
                self.position += (argument - 1)

        self.position += 1
        if self.position >= len(self.instructions):
            self.dead_lock = True
            self.dead_lock_count = 10

def part2():
    instructions = read_input()
    registers = {register: 0 for register in instructions_to_registers(instructions)}
    tx_queue = queue.Queue()
    rx_queue = queue.Queue()
    program_0 = Program(registers, 0, tx_queue, rx_queue, instructions)
    program_1 = Program(registers, 1, rx_queue, tx_queue, instructions)

    count = 0
    while not (program_0.dead_lock is True and program_1.dead_lock is True):
        program_0.advance()
        program_1.advance()
        count += 1

    logging.info('program_1 send %d times', program_1.send_count)

if __name__ == '__main__':
    FORMAT = '%(asctime)-15s: %(message)s'
    logging.basicConfig(format=FORMAT, level='DEBUG')
    #part1()
    part2()
