"""
AOC 2019
Day 24: Planet of Discord
Solution by 2xRon
"""
from itertools import chain
from copy import deepcopy

# Pad outside of grid
GRID_SIZE = 5
initial_grid = list()
with open("./inputs/24.input") as in_file:
    for line in in_file.readlines():
        initial_grid.append([int(x == "#") for x in line.strip()])
print(initial_grid)


def print_grid(grid):
    for line in grid:
        print(*["🐛" if x else "  " for x in line], sep="")


print_grid(initial_grid)


def neighbor_score(grid):
    ns_grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            ns = 0
            if 0 <= y - 1:
                ns += grid[y - 1][x]
            if y + 1 < GRID_SIZE:
                ns += grid[y + 1][x]
            if 0 <= x - 1:
                ns += grid[y][x - 1]
            if x + 1 < GRID_SIZE:
                ns += grid[y][x + 1]

            ns_grid[y][x] = ns
    return ns_grid

def advance_life(grid):
    ns_grid = neighbor_score(grid)
    new_grid = list([0]* GRID_SIZE for _ in range(GRID_SIZE))
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x]:
                if ns_grid[y][x] == 1:
                    new_grid[y][x] = 1
            if not grid[y][x]:
                if ns_grid[y][x] == 1 or ns_grid[y][x] == 2:
                    new_grid[y][x] = 1
    return tuple(tuple(row) for row in new_grid)


print(neighbor_score(initial_grid))


biodiversity_index = [2 ** i for i in range(GRID_SIZE * GRID_SIZE)]
def biodiversity(grid):
    flat_grid = chain(*grid)
    return sum(x * biodiversity_index[idx] for idx, x in enumerate(flat_grid))

layouts = dict()
grid = tuple(tuple(row) for row in initial_grid)
print(type(grid))
layouts.update({grid:0})
while True:
    new_grid = advance_life(grid)
    print_grid(new_grid)
    print("----------")
    if new_grid in layouts:
        print("Part 1:",biodiversity(new_grid))
        break
    layouts.update({new_grid:0})
    grid = new_grid


