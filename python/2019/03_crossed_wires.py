"""
AOC 2019
Day 3: Crossed Wires
Solution by 2xRon
"""

with open("inputs/03.input") as in_file:
    wireA, wireB = [x.split(",") for x in in_file.readlines()]


def get_direction(step):
    if step.startswith("U"):
        return 1 + 0j
    elif step.startswith("D"):
        return -1 + 0j
    elif step.startswith("L"):
        return 0 + -1j
    elif step.startswith("R"):
        return 0 + 1j
    else:
        raise Exception("Bad get_direction")


def trace_wire_pos(wire_path):
    wire_pos = 0 + 0j
    wire_locs = []
    for step in wire_path:
        step_len = int(step[1:])
        step_dir = get_direction(step)
        for _ in range(step_len):
            wire_pos += step_dir
            wire_locs.append(wire_pos)
    return wire_locs


wireA_pos = trace_wire_pos(wireA)
wireB_pos = trace_wire_pos(wireB)

# find intersections
common_locs = set(wireA_pos).intersection(set(wireB_pos))
min_mhtn_dists_common = min(int(abs(x.real) + abs(x.imag)) for x in common_locs)
print("Part 1:", min_mhtn_dists_common)

# find shortest summed path to an intersection
path_len_to_intersections = []
for intersection in common_locs:
    wireA_intersection_len = wireA_pos.index(intersection) + 1  # removed origin
    wireB_intersection_len = wireB_pos.index(intersection) + 1
    path_len_to_intersections.append(wireA_intersection_len + wireB_intersection_len)
print("Part 2:", min(path_len_to_intersections))
