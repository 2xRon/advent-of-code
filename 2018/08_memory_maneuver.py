"""
ADVENT OF CODE: 2018
Day 8: Memory Maneuver
"""

from typing import List
from dataclasses import dataclass

@dataclass
class Node():
    n_children : int
    n_metadata : int
    metadata : List[int]
    children : List['Node']

in_file = open("inputs/08.input", "r").read().strip()
in_file = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
license = list(map(int, in_file.split(" ")))


def read_node(license):
    n_children = license[0]
    n_metadata = license[1]
    metadata = license[-1*n_metadata:]
    if n_children == 0:
        return Node(n_children,n_metadata,metadata,[])
    else:
        pass

    new_node = Node(n_children,n_metadata,metadata,)
