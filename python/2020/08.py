"""
AOC 2020
Day 8: Handheld Halting
Solution by 2xRon
"""

from copy import copy


class TwoIntTwoCode:
    def __init__(self, program):
        self.acc = 0
        self.program = program
        self.program_base = copy(program)
        self.ptr = 0
        self.instruction_history = []

    def Reset(self):
        self.ptr = 0
        self.acc = 0
        self.instruction_history = []
        self.program = copy(self.program_base)

    def Run(self):
        while True:
            pass

    def SolveOne(self):
        while True:
            self._executeInstruction(self.program[self.ptr])
            if self.ptr in self.instruction_history:
                break
            self.instruction_history.append(self.ptr)
        print("Part 1:", self.acc)

    def _breaks(self):
        while True:
            if self.ptr >= len(self.program):
                return True
            self._executeInstruction(self.program[self.ptr])
            if self.ptr in self.instruction_history:
                return False
            self.instruction_history.append(self.ptr)

    def SolveTwo(self):
        for i in range(len(self.program_base)):
            self.Reset()
            if self.program_base[i][0] == "jmp":
                self.program = copy(self.program_base)
                self.program[i] = ("nop", self.program_base[i][1])
            elif self.program_base[i][0] == "nop":
                self.program = copy(self.program_base)
                self.program[i] = ("jmp", self.program_base[i][1])
            else:
                continue
            if self._breaks():
                print("Part 2", self.acc)

    def _executeInstruction(self, instruction):
        op = instruction[0]
        param = instruction[1]
        # getattr(TwoIntTwoCode, "_" + op)(self, param)
        self.__dict__["_" + op](self, param)

    def _acc(self, param):
        self.acc += param
        self.ptr += 1

    def _jmp(self, param):
        self.ptr += param

    def _nop(self, param):
        self.ptr += 1


if __name__ == "__main__":
    with open("./input/08.input") as in_file:
        program = [ tuple(l.split(" ")) for l in in_file.readlines() ]
        program = [ (i[0], int(i[1])) for i in program ]

    Halterator = TwoIntTwoCode(program)
    Halterator.SolveOne()
    Halterator.SolveTwo()
