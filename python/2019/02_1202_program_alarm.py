""" AOC 2019
Day 2: 1202 Program Alarm
Solution by 2xRon"""

from copy import copy
from itertools import product

with open("inputs/02.input") as in_file:
    program = [int(x) for x in in_file.readline().rstrip().split(",")]


def run_program(p, noun, verb, verbose=False):
    p[1] = noun
    p[2] = verb
    ip = 0
    prog_len = len(p)
    while ip < prog_len:
        if p[ip] == 1:
            p[p[ip + 3]] = p[p[ip + 1]] + p[p[ip + 2]]
        elif p[ip] == 2:
            p[p[ip + 3]] = p[p[ip + 1]] * p[p[ip + 2]]
        elif p[ip] == 99:
            break
        else:
            break
        if verbose:
            print(p)
        ip += 4
    return p[0]


print("Part 1:", run_program(copy(program), 12, 2))

target = 19690720
for noun, verb in product(range(100), range(100)):
    result = run_program(copy(program), noun, verb)
    if result == target:
        print("Part 2:", 100 * noun + verb)
