"""
AOC 2019
Day 10: Monitoring Station
Solution by 2xRon
"""

from math import atan2, pi
from collections import Counter, defaultdict

asteroids = list()
with open("./inputs/10.input") as infile:
    for row, line in enumerate(infile.readlines()):
        asteroids.extend(
            [(col, row) for col, x in enumerate(list(line.strip())) if x == "#"]
        )


def sq_dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def slope_angle(p1, p2):
    return atan2((p2[1] - p1[1]), (p2[0] - p1[0]))


visble_asteroids = Counter()
for ast1 in asteroids:
    ast1_angles_to_ast2 = [slope_angle(ast1, ast2) for ast2 in asteroids]
    # colinear stars will have non-unique slope angles, so only count one star from each angle
    visble_asteroids.update({ast1: len(set(ast1_angles_to_ast2))})
print("Part 1: ", visble_asteroids.most_common(1)[0][1])


station_addr = visble_asteroids.most_common(1)[0][0]
station_idx = asteroids.index(station_addr)
asteroids_by_angle_dict = defaultdict(list)
for ast in asteroids:
    if ast != station_addr:
        # left = -pi
        sa = slope_angle(station_addr, ast)
        asteroids_by_angle_dict[sa].append(ast)
        # closest asteroid = rightmost in list
        asteroids_by_angle_dict[sa].sort(key=lambda x: sq_dist(station_addr, x))
living_asteroids_by_angle = [
    (ang, asts) for ang, asts in asteroids_by_angle_dict.items()
]
living_asteroids_by_angle.sort(key=lambda x: x[0],)

n_angles = len(living_asteroids_by_angle)
# assume there is at least one asteroid striaght up
start_angle_index = [x[0] for x in living_asteroids_by_angle].index(-pi / 2)
angle_idx = start_angle_index
for exploded_asts in range(200):
    if len(living_asteroids_by_angle[angle_idx][1]) > 0:
        last_chopped = living_asteroids_by_angle[angle_idx][1].pop()
    angle_idx = (angle_idx + 1) % n_angles
print("Part 2:", last_chopped[0] * 100 + last_chopped[1])
