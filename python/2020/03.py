"""
AOC 2020
Day 3: Toboggan Trajectory
Solution by 2xRon
"""
from typing import List, Tuple
from math import gcd
from itertools import count

with open("./input/03.input") as in_file:
    forest = [[c == "#" for c in line.strip()] for line in in_file.read().splitlines()]


def is_tree(forest: List[List[bool]], pos: Tuple[int, int]) -> bool:
    pattern_width = len(forest[0])
    return forest[pos[0]][pos[1] % pattern_width]


def tree_count(forest: List[List[bool]], slope: Tuple[int, int]) -> int:
    return sum(
        is_tree(forest, pos)
        for pos in zip(range(0, len(forest), slope[0]), count(0, slope[1]))
    )


slope_one = (1, 3)
print("Part 1:", tree_count(forest, slope_one))

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
tot = 1
for s in slopes:
    f = gcd(s[0], s[1])
    tot *= tree_count(forest, (s[0] // f, s[1] // f))
print("Part 2:", tot)
