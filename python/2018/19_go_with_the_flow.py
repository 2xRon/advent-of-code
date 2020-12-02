"""
ADVENT OF CODE: 2018
Day 19: Go with the Flow
"""

import re
from collections import Counter, namedtuple, deque
from copy import copy
from itertools import chain, combinations


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
        while 0 <= self.ip_val < prog_len:
            if verbose:
                print(self.mem)
            inst = program.instructions[self.ip_val]
            self.eval(inst.op, *inst.args)
        return self

    def iter_run_program(self, program):
        self.ip_reg = program.ip_reg
        prog_len = len(program.instructions)
        while 0 <= self.ip_val < prog_len:
            inst = program.instructions[self.ip_val]
            self.eval(inst.op, *inst.args)
            yield self

    def __repr__(self):
        return f"mem: {self.mem}, ip_reg: {self.ip_reg}, ip_val: {self.ip_val}"

    def __str__(self):
        return str(self.mem)

    def __eq__(self, other):
        if hasattr(other, "mem"):
            return self.mem == other.mem
        else:
            return self.mem == other


Program = namedtuple("Program", ["ip_reg", "instructions"])
Instruction = namedtuple("Instruction", ["op", "args"])
instruction_pattern = re.compile(r"(\w+) (\d+) (\d+) (\d+)")
with open("inputs/19.input") as in_file:
    ip_reg = re.match(r"#ip (\d)", in_file.readline()).group(1)
    instructions = [re.match(instruction_pattern, l) for l in in_file.readlines()]

instructions = [
    Instruction(m.group(1), list(map(int, m.group(2, 3, 4)))) for m in instructions
]

program = Program(int(ip_reg), instructions)

my_cpu = SIM()
my_cpu.run_program(program)
print("Part 1:", my_cpu.mem[0])

# find constant value and calc its factor sum
MEMORY_LEN = 100
register_memory = [deque(maxlen=MEMORY_LEN) for _ in range(6)]


def add_to_memory(register_memory, mem):
    for idx, val in enumerate(mem):
        register_memory[idx].append(val)


def get_repeating_val(register_memory):
    for last_register_vals in register_memory:
        if last_register_vals.count(last_register_vals[0]) == MEMORY_LEN:
            return last_register_vals[0]
    else:
        raise IndexError


add_to_memory(register_memory, [-1] * 6)  # initialize with nonsense value
for state in SIM([1, 0, 0, 0, 0, 0]).iter_run_program(program):
    add_to_memory(register_memory, state.mem)
    print(state)
    try:
        repeating_val = get_repeating_val(register_memory)
    except IndexError:
        continue
    break


def sieveE(n: int):
    """return a lit of primes below n"""
    prime = [False, False, False] + [True, False] * (n // 2)
    result = [2]
    append = result.append
    sqrt_n = (int(n ** 0.5) + 1) | 1
    for p in range(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            for i in range(p * p, n, 2 * p):
                prime[i] = False
    for p in range(sqrt_n, n, 2):
        if prime[p]:
            append(p)
    return result


primes_below_half = sieveE(repeating_val // 2 + 1)
prime_factorization = []
v = repeating_val
for p in primes_below_half:
    while v % p == 0:
        prime_factorization.append(p)
        v /= p


def product(seq):
    res = 1
    for x in seq:
        res *= x
    return res


factor_combinations = chain.from_iterable(
    combinations(prime_factorization, r) for r in range(len(prime_factorization) + 1)
)
factors = set(product(x) for x in factor_combinations)
print("Part 2:", sum(factors))
