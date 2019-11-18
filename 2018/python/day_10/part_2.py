"""Code for part 1 of day 05.
"""
import pdb
import re
import collections
import logging

logging.basicConfig(
    format='%(asctime)-23s %(funcName)15s: %(message)s',
    level=logging.INFO
)

"""
Header: #children #metadata
"""
class Node():
    def __init__(self, num_children, children, num_metadata, metadata):
        self.num_children = num_children
        self.children = children
        self.num_metadata = num_metadata
        self.metadata = metadata

    def metadata_sum(self):
        metadata = 0
        if self.num_children == 0:
            metadata = sum(self.metadata)

        else:
            for index in self.metadata:
                if index == 0:
                    continue

                if index <= len(self.children):
                    metadata += self.children[index - 1].metadata_sum()

        return metadata


def add_child_node(sequence):
    num_children = sequence.popleft()
    num_metadata = sequence.popleft()
    logging.debug(
        "children: %2d, metadata: %2d",
        num_children, num_metadata)

    children = [add_child_node(sequence) for index_child in range(num_children)]
    metadata = [sequence.popleft() for index_metadata in range(num_metadata)]
    node = Node(num_children, children, num_metadata, metadata)
    return node

def add_root_node(sequence):
    num_children = sequence.popleft()
    num_metadata = sequence.popleft()
    logging.debug(
        "children: %2d, metadata: %2d",
        num_children, num_metadata)
    children = [add_child_node(sequence) for index_child in range(num_children)]
    metadata = [sequence.popleft() for index_metadata in range(num_metadata)]
    node = Node(num_children, children, num_metadata, metadata)
    return node



def solution(sequences):
    """Solution to part one.
    """
    sequence = collections.deque(
        [int(x) for x in re.findall(r'[0-9]+', sequences)]
    )
    node = add_root_node(sequence)
    return node.metadata_sum()
