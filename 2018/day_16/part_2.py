"""Code for part 1 of day 05.
"""
import logging
import pdb
import re
import collections

import part_1

logging.basicConfig(
    format='%(asctime)-23s %(funcName)15s: %(message)s',
    level=logging.DEBUG
)


def map_opcodes(problem_input):
    samples = part_1.split_samples(problem_input)
    sample_map = {}
    for sample in samples:
        before, instruction, after = part_1.decode_sample(sample)
        opcode = instruction[0]
        if opcode in sample_map:
            sample_map[opcode].append((before, instruction, after))

        else:
            sample_map[opcode] = [(before, instruction, after)]

    machine = part_1.Machine()
    functions = {
        name: getattr(machine, name)
        for name in dir(machine)
        if not name.startswith('__') and callable(getattr(machine, name))
    }
    function_map = {}
    for key, samples in sample_map.items():
        valid_functions = []
        for sample in samples:
            before, instruction, after = sample
            machine.__set_state__(before)
            valid = []
            for name, func in functions.items():
                func(instruction[1], instruction[2], instruction[3])
                if machine.state == after:
                    valid.append(name)

                machine.__set_state__(before)

            valid_functions.append(set(valid))

        valid = valid_functions[0]
        for test in valid_functions[1:]:
            valid = valid & test

        function_map[key] = valid

    opcode_map = {}
    while len(function_map) > 0:
        min_value = min([len(values) for values in function_map.values()])
        for key, values in function_map.copy().items():
            if len(values) == min_value:
                opcode = list(values)[0]
                opcode_map[key] = opcode
                del function_map[key]

                for name, opcodes in function_map.items():
                    opcodes = opcodes ^ set([opcode])
                    function_map[name] = opcodes

                break

    return opcode_map


def run_instruction(machine, opcode_map, instruction):
    opcode = instruction[0]
    func_name = opcode_map[opcode]
    getattr(machine, func_name)(instruction[1], instruction[2], instruction[3])


def solution(problem_input_part_1, problem_input_part_2):
    """Solution to part one.
    """
    program_part_1 = part_1.split_samples(problem_input_part_1)
    program_part_1 = [
        part_1.decode_sample(sample)[1] for sample in program_part_1]

    program_part_2 = problem_input_part_2.split('\n')[1:-1]
    program_part_2 = [
        [int(x) for x in re.findall(r'[0-9]+', line)]
        for line in program_part_2]

    return

    machine = part_1.Machine()
    opcode_map = map_opcodes(problem_input_part_1)
    for line in program:
        run_instruction(machine, opcode_map, line)

    logging.debug(machine.registers[0])
