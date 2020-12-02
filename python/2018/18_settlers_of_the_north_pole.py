"""
ADVENT OF CODE: 2018
Day 18: Settlers of the North Pole
"""

from itertools import product, chain
from copy import deepcopy


def replace_chars(char):
    if char == ".":  # open
        return 0
    if char == "|":  # tree
        return 1
    if char == "#":  # lumberyard
        return 10


def rev_replace_chars(char):
    if char == 0:  # open
        return "."
    if char == 1:  # tree
        return "|"
    if char == 10:  # lumberyard
        return "#"


with open("inputs/18.input") as in_file:
    init_grid = [
        [replace_chars(c) for c in line.strip()] for line in in_file.readlines()
    ]

YMAX = len(init_grid)
XMAX = len(init_grid[0])


def print_grid(grid):
    for l in grid:
        print(*map(rev_replace_chars, l), sep="")


def get_neighbor_sum(grid, x, y):
    total = 0
    for i, j in product((-1, 0, 1), (-1, 0, 1)):
        if i == j == 0:
            continue
        if (0 <= y + j < YMAX) and (0 <= x + i < XMAX):
            total += grid[y + j][x + i]
    return total


def get_new_acre(grid, x, y):
    nsum = get_neighbor_sum(grid, x, y)
    acre = grid[y][x]
    if acre == 0 and nsum % 10 >= 3:
        return 1
    if acre == 1 and nsum // 10 >= 3:
        return 10
    if acre == 10 and not (nsum % 10 >= 1 and nsum // 10 >= 1):
        return 0
    return acre


def get_resource_value(grid):
    n_trees = 0
    n_lumbers = 0
    for acre in chain(*grid):
        n_trees += int(acre == 1)
        n_lumbers += int(acre == 10)
    return n_trees * n_lumbers


def simulate(init_grid, n_minutes):
    last_grids = list()
    grid = deepcopy(init_grid)
    last_grids.append(grid)
    for minute in range(1, n_minutes + 1):
        new_grid = [
            [get_new_acre(grid, x, y) for x in range(XMAX)] for y in range(YMAX)
        ]
        grid = new_grid
        if grid in last_grids:
            break
        else:
            last_grids.append(grid)
    else:  # finished without finding cycle
        return get_resource_value(grid)
    repeat_found_at_min = minute
    min_until_term = n_minutes - repeat_found_at_min
    cycle_len = repeat_found_at_min - last_grids.index(grid)
    cycle = last_grids[repeat_found_at_min - cycle_len :]
    incomplete_cycle_index = min_until_term % cycle_len
    return get_resource_value(cycle[incomplete_cycle_index])


print("Part 1:", simulate(init_grid, 10))
print("Part 2:", simulate(init_grid, 1_000_000_000))
