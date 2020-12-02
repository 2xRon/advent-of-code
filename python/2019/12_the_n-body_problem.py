"""
AOC 2019
Day 12: The N-Body Problem
Solution by 2xRon
"""
import re

moon_re = re.compile(r"\-?\d+")
with open("./inputs/12.input") as in_file:
    moons_pos = [list(map(int,moon_re.findall(line))) for line in in_file.readlines()]
n_moons = len(moons_pos)
moons_vel = [[0]*3 for _ in range(n_moons)]

def one_zero_minusone(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
def ele_wise_sub(it1, it2):
    return [ one_zero_minusone( x2-x1 ) for x2,x1 in zip(it1,it2) ]
def ele_wise_list_sum(its):
    return [ sum(x) for x in zip(*its)]

MAXSTEP = 1000
for _ in range(MAXSTEP):
    # apply gravity
    for moon_idx in range(n_moons):
        moon = moons_pos[moon_idx]
        dv_by_moon = [ele_wise_sub(moon,moon2) for moon2 in moons_pos]
        moons_vel[moon_idx] = ele_wise_list_sum(moons_vel[moon_idx],dv_by_moon)
    # update position
