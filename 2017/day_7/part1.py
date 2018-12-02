#!/usr/bin/python3.5
import sys
import re
import collections

class Node():
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = int(weight)
        self.children = children

    def __repr__(self):
        lines = []
        lines.append("{name} ({weight} -- {summed_weight})".format(
            name=self.name, weight=self.weight,
            summed_weight=self.summed_weight))
        if self.children is not None:
            for child in self.children:
                for line in child.__repr__().split('\n'):
                    lines.append("\t{}".format(line))

        return "\n".join(lines)

    def link(self, node_map):
        if self.children is None:
            return

        children = []
        for child in self.children:
            node = node_map[child]
            children.append(node)

        self.children = children

    @property
    def summed_weight(self):
        weight = self.weight
        if self.children is not None:
            for child in self.children:
                weight += child.summed_weight

        return weight

def read_input(input_file):
    with open(input_file, 'r') as io_ref:
        data = io_ref.readlines()

    lines = [line.replace('\n', '') for line in data]
    return lines

def link_children(nodes):
    node_map = {node.name: node for node in nodes}
    for node in nodes:
        node.link(node_map)

    return nodes

def find_unbalance(root):
    weights = [child.summed_weight for child in root.children]
    counts = collections.Counter(weights)
    for weight, count in counts.items():
        if count == 1:
            break

    for child in root.children:
        if child.summed_weight == weight:
            break

    print(child)

def process_data(data):
    name_regex = re.compile(r'^[a-z]+')
    weight_regex = re.compile(r'\(([0-9]+)\)')
    children_regex = re.compile(r'-> (.*)')
    nodes = []
    for line in data:
        name = name_regex.search(line).group(0)
        weight = weight_regex.search(line).group(1)
        children = children_regex.search(line)
        if children is not None:
            children = children.group(1).split(', ')

        node = Node(name, weight, children)
        nodes.append(node)

    nodes = link_children(nodes)

    strings = [(node.__repr__(), node) for node in nodes]
    root = ("", None)
    for node_txt, node in strings:
        if len(node_txt) > len(root[0]):
            root = (node_txt, node)

    #print(root[0])
    find_unbalance(root[1])


def main():
    data = read_input(sys.argv[1])
    process_data(data)

if __name__ == '__main__':
    main()
