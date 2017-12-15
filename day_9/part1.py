#!/usr/bin/env python3.5
import sys
import re
import logging

FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT, level='INFO')

GARBAGE = re.compile(r'<.*?[^!]>')
FILTER = re.compile(r',')
GROUP = re.compile(r'{(.*)}')

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.readlines()

    codes = [line.replace('\n', '') for line in data]
    return codes

def parse(line):
    level = 0
    score = 0
    garbage = False
    skip = False
    list_of_garbage = []
    logging.info('Begin')
    for character in line:
        logging.debug('state: score %d, level %d, garbage %s, skip %s',
            score, level, garbage, skip)
        if skip is True:
            skip = False
            continue

        if character == '!':
            skip = True
            continue

        if garbage is True:
            if character == '>':
                garbage = False

            else:
                list_of_garbage.append(character)

            continue

        if character == '<':
            garbage = True

        if character == '{':
            level += 1
            continue

        if character == '}':
            score += level
            level -= 1
            continue

    logging.info('End: score %d\n', score)
    logging.debug('Garbage:\n%s', ''.join(list_of_garbage))
    logging.info('number of garbage characters: %d', len(list_of_garbage))

def main():
    data = read_input(sys.argv[1])
    for line in data:
        parse(line)

if __name__ == '__main__':
    main()
