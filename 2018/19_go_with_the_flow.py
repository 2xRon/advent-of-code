"""
ADVENT OF CODE: 2018
Day 19: Go with the Flow
"""

import re
from collections import Counter, namedtuple
from copy import copy


class CPU:
    def __init__(self, mem=[0, 0, 0, 0, 0, 0], *, ip_reg=0, ip_val=0):
        self.mem = copy(mem)
        self.ip_reg = ip_reg
        self.ip_val = ip_val

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
        self.mem[self.ip_reg] = self.ip_val
        getattr(self, op)(A, B, C)
        self.ip_val = self.mem[self.ip_reg]
        self.ip_val += 1
        return self

    def test_eval(self, op, A, B, C):
        return SIM(self.mem, self.ip_reg, self.ip_val).eval(op, A, B, C)

    def run_program(self, program, verbose=False):
        self.ip_reg = program.ip_reg
        prog_len = len(program.instructions)
        while self.ip_val < prog_len:
            if verbose:
                print(self.mem)
            inst = program.instructions[self.ip_val]
            self.eval(inst.op, *inst.args)
        return self

    def __repr__(self):
        return f"mem: {self.mem}, ip_reg: {self.ip_reg}, ip_val: {self.ip_val}"

    def __str__(self):
        return str(self.mem)

    def __eq__(self, other):
        if hasattr(other, "mem"):
            return self.mem == other.mem
        else:
            return self.mem == other

Program = namedtuple('Program',['ip_reg','instructions'])
Instruction = namedtuple('Instruction',['op','args'])
instruction_pattern = re.compile(r"(\w+) (\d+) (\d+) (\d+)")
with open("inputs/19.input") as in_file:
    ip_reg = re.match(r"#ip (\d)",in_file.readline()).group(1)
    instructions = [re.match(instruction_pattern, l) for l in in_file.readlines()]

instructions = [Instruction(m.group(1),list(map(int,m.group(2,3,4)))) for m in instructions]

program = Program(int(ip_reg),instructions)

my_cpu = SIM()
my_cpu.run_program(program)
print("Part 1:", my_cpu.mem[0])

my_cpu = SIM([1,0,0,0,0,0])
my_cpu.run_program(program, verbose=True)
print("Part 2:", my_cpu)

