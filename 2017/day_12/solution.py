#!/usr/bin/env python3.5
import sys
import logging
import re

FORMAT = '%(asctime)-15s: %(message)s'
logging.basicConfig(format=FORMAT, level='DEBUG')

class Node():
    def __init__(self, name, links, link_map):
        self.name = name
        self.links = links.replace(' ', '')
        self.link_map = link_map

    def __repr__(self):
        return "{0} <--> {1}".format(self.name, self.links)

    def __lt__(self, other):
        return self.name < other.name

    def link(self):
        links = []
        for link in self.links.split(','):
            if link != self.name:
                links.append(self.link_map[link])

        self.links = links

    def link_names(self):
        return [link.name for link in self.links]

    def connections(self):
        done = [self.name]
        todo = [link.name for link in self.links]
        while len(todo) > 0:
            link_name = todo.pop()
            done.append(link_name)
            todo.extend(self.link_map[link_name].link_names())
            todo = list(set(todo) - set(done))

        return done

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.readlines()
        
    return [line.replace('\n', '') for line in data]

def part1():
    data = read_input(sys.argv[1])
    link_map = {}
    for line in data:
        decoded = re.search(r'([0-9]+) <-> (.*)', line)
        node_name = decoded.group(1)
        links = decoded.group(2)
        node = Node(node_name, links, link_map)
        link_map[node_name] = node

    for name, node in link_map.items():
        node.link()

    groups = link_map['0'].connections()
    logging.info('group size of 0: %d', len(groups))

def part2():
    data = read_input(sys.argv[1])
    link_map = {}
    for line in data:
        decoded = re.search(r'([0-9]+) <-> (.*)', line)
        node_name = decoded.group(1)
        links = decoded.group(2)
        node = Node(node_name, links, link_map)
        link_map[node_name] = node

    for name, node in link_map.items():
        node.link()

    all_nodes = list(reversed(sorted(link_map.keys())))
    groups = []
    while len(all_nodes) > 0:
        node = all_nodes.pop()
        connections = link_map[node].connections()
        groups.append(connections)
        all_nodes = list(set(all_nodes) - set(connections))

    logging.info('number of different groups: %d', len(groups))

if __name__ == '__main__':
    part1()
    part2()
