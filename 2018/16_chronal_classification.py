"""
ADVENT OF CODE: 2018
Day 16: Chronal Classification
"""

import re
from collections import Counter, namedtuple
from copy import deepcopy, copy

observation_search = re.compile(
    r"Before: \[(\d, \d, \d, \d)\].(\d+ \d \d \d).After:  \[(\d, \d, \d, \d)\]",
    re.DOTALL,
)
with open("inputs/16_1.input") as in_file:
    observations_strs = re.findall(observation_search, in_file.read())

with open("inputs/16_2.input") as in_file:
    instructions = [list(map(int,x.split(" "))) for x in re.findall(r"\d+ \d \d \d", in_file.read())]

def split_int(seq, split_str=" "):
    return list(int(c) for c in seq.split(split_str))

observation = namedtuple("observation", ["before", "instruction", "after"])
observations = [
    observation(split_int(c[0], ", "), split_int(c[1]), split_int(c[2], ", "))
    for c in observations_strs
]


class CPU:
    def __init__(self, mem=[0, 0, 0, 0]):
        self.mem = copy(mem)

    def addr(self, A, B, C):
        self.mem[C] = self.mem[A] + self.mem[B]

    def addi(self, A, B, C):
        self.mem[C] = self.mem[A] + B

    def mulr(self, A, B, C):
        self.mem[C] = self.mem[A] * self.mem[B]

    def muli(self, A, B, C):
        self.mem[C] = self.mem[A] * B

    def banr(self, A, B, C):
        self.mem[C] = self.mem[A] & self.mem[B]

    def bani(self, A, B, C):
        self.mem[C] = self.mem[A] & B

    def borr(self, A, B, C):
        self.mem[C] = self.mem[A] | self.mem[B]

    def bori(self, A, B, C):
        self.mem[C] = self.mem[A] | B

    def setr(self, A, B, C):
        self.mem[C] = self.mem[A]

    def seti(self, A, B, C):
        self.mem[C] = A

    def gtir(self, A, B, C):
        self.mem[C] = int(A > self.mem[B])

    def gtri(self, A, B, C):
        self.mem[C] = int(self.mem[A] > B)

    def gtrr(self, A, B, C):
        self.mem[C] = int(self.mem[A] > self.mem[B])

    def eqir(self, A, B, C):
        self.mem[C] = int(A == self.mem[B])

    def eqri(self, A, B, C):
        self.mem[C] = int(self.mem[A] == B)

    def eqrr(self, A, B, C):
        self.mem[C] = int(self.mem[A] == self.mem[B])


operations = [
    func
    for func in dir(CPU)
    if callable(getattr(CPU, func)) and not func.startswith("__")
]


class SIM(CPU):
    def eval(self, op, A, B, C):
        getattr(self, op)(A, B, C)
        return self

    def test_eval(self, op, A, B, C):
        return SIM(self.mem).eval(op, A, B, C)

    def __repr__(self):
        return str(self.mem)

    def __eq__(self, other):
        if type(other) == list:
            return self.mem == other
        else:
            return self.mem == other.mem


matching_operations_per_observation = list()
matching_operations_per_opcode = {x:set(operations) for x in range(16)}
for obs in observations:
    matching_operations = [
            f
            for f in operations
            if SIM(obs.before).eval(f, *obs.instruction[1:]) == obs.after
        ]
    matching_operations_per_observation.append(matching_operations)
    matching_operations_per_opcode[obs.instruction[0]] &= set(matching_operations)

print("Part 1:", sum(len(x) >= 3 for x in matching_operations_per_observation))
print(matching_operations_per_opcode)
