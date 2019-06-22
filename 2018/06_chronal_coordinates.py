"""
ADVENT OF CODE: 2018
Day 6: Chronal Coordinates
"""
from operator import sub, add
from itertools import product
from collections import Counter


def l1distance(c1, c2):
    return sum(map(abs, map(sub, c1, c2)))  # d = |c1_0 - c2_0| + |c1_1 - c2_1|


in_file = open("inputs/06.input", "r").read().strip()

coords = [tuple(map(int, c.split(", "))) for c in in_file.split("\n")]
n_coords = len(coords)
dims = len(coords[0])

edges = tuple(map(add, map(max, zip(*coords)), tuple(1 for _ in range(dims))))
grid = {indices: -1 for indices in product(*map(range, edges))}
dist_grid = {indices: -1 for indices in product(*map(range, edges))}
coords_with_edge_neighbor = set()


def is_on_edge(coord_index):
    return any(
        idx_1 >= idx_2 - 1 or idx_1 == 0 for idx_1, idx_2 in zip(coord_index, edges)
    )


for loc in product(*map(range, edges)):
    distances = [l1distance(loc, c) for c in coords]
    dist_grid[loc] = sum(distances)
    nearest_coord_indexs = [
        idx for idx, dist in enumerate(distances) if dist == min(distances)
    ]
    if len(nearest_coord_indexs) > 1:
        grid[loc] = None
    else:
        grid[loc] = nearest_coord_indexs[0]
    if is_on_edge(loc):
        coords_with_edge_neighbor.add(nearest_coord_indexs[0])

nearest_coord_index_counter = Counter(grid.values())

non_edge_areas = sorted(
    (count, idx)
    for idx, count in nearest_coord_index_counter.items()
    if idx not in coords_with_edge_neighbor
)
print("Part A:", non_edge_areas[-1][0])
highly_proximal_locations = [loc for loc, dist in dist_grid.items() if dist < 10000]
print("Part B:", len(highly_proximal_locations))
