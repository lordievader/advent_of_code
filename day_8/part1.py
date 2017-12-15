#!/usr/bin/python3.5
import sys
import re
from collections import defaultdict

def update_registers(name, operation, amount, condition_name, condition,
                     registers):
    register_value = registers[condition_name]
    if condition[0] == '=':
        condition[0] = '=='

    if eval("{0} {1} {2}".format(register_value, condition[0], condition[1])):
        if operation == 'inc':
            registers[name] += int(amount)

        else:
            registers[name] -= int(amount)

    return registers


def process_data(data):
    name_regex = re.compile(r'^([a-z]+)')
    operation_regex = re.compile(r'(inc|dec)')
    amount_regex = re.compile(r'\ (-{0,1}[0-9]+)')
    condition_name_regex = re.compile(r'if\ ([a-z]+)')
    condition_regex = re.compile(r'([!><=]+)\ (-{0,1}[0-9]+)$')
    registers = defaultdict(int)
    max_value = 0
    for line in data:
        name = name_regex.search(line).group(1)
        operation = operation_regex.search(line).group(1)
        amount = amount_regex.search(line).group(1)
        condition_name = condition_name_regex.search(line).group(1)
        condition_string = condition_regex.search(line)
        condition = [condition_string.group(1), condition_string.group(2)]

        registers = update_registers(name, operation, amount, condition_name, 
                                     condition, registers)
        sub_max_value = max(registers.values())
        if sub_max_value > max_value:
            max_value = sub_max_value

    print(registers)
    print(max(registers.values()))
    print(max_value)

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.readlines()

    lines = [line.replace('\n', '') for line in data]
    return lines

def main():
    data = read_input(sys.argv[1])
    process_data(data)

if __name__ == '__main__':
    main()
