"""
AOC 2020
Day 3: Toboggan Trajectory
Solution by 2xRon
"""
from typing import List, Tuple
from itertools import count

with open("./input/03.input") as in_file:
    forest = [[c == "#" for c in line.strip()] for line in in_file.read().splitlines()]

def is_tree(forest: List[List[bool]], pos : Tuple[int, int]) -> bool:
    pattern_width = len(forest[0])
    return forest[pos[0]][pos[1] % pattern_width]

slope_one = (1, 3)
tree_count_one = sum(is_tree(forest, pos) for pos in zip(range(0,len(forest),slope_one[0]), count(0, slope_one[1])))
print("Part 1:", tree_count_one)

def tree_count(forest : List[List[bool]], slope : Tuple[int, int]) -> int:
    return sum(is_tree(forest, pos) for pos in zip(range(0,len(forest),slope[0]), count(0, slope[1])))

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
tot = 1
for s in slopes:
    tot *= tree_count(forest, s)
print("Part 2:", tot)
