#!/usr/bin/python3
import sys

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.read().replace('\n', '').split('\t')

    memory = [int(char) for char in data]
    return memory

def check_states(states, memory):
    value = True
    if memory in states and len(states) > 1:
        value = False

    return value

def find_max(memory):
    max_value =  max(memory)
    for index, value in enumerate(memory):
        if value == max_value:
            break

    return index, value

def part1(memory):
    states = []
    length = len(memory)
    print(memory)
    count = 0
    while check_states(states, memory):
        states.append(memory.copy())
        max_index, max_value = find_max(memory)
        memory[max_index] = 0
        for index in range(1, max_value + 1):
            memory_index = (max_index + index) % length
            memory[memory_index] += 1

        print(memory)
        count += 1

    print("After {0} cycles the same state occured".format(count))
    cycle_length = len(states) - states.index(memory)
    print("Cycle length: {0}".format(cycle_length))

def main():
    data = read_input(sys.argv[1])
    part1(data)

if __name__ == '__main__':
    main()
