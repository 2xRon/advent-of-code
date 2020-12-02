"""
AOC 2019
Day 5: Sunny with a Chance of Asteroids
Solution by 2xRon
"""
from math import prod
from copy import copy

with open("./inputs/05.input") as in_file:
    program = [int(x) for x in in_file.read().strip().split(",")]

# program = [1002,4,3,4,33]
# program = [1101,100,-1,4,0]


class IntcodeComputer:

    ip = 0  # instruction pointer
    op_paramater_count = dict([(1, 3), (2, 3), (3, 1), (4, 1), (5,2), (6,2), (7,3), (8,3), (99, 0)])

    def __init__(self, program, input_parameter=1):
        self.program = copy(program)
        self.input_parameter = input_parameter

    def _get_values(self, value_codes, parameter_modes):
        ret = list()
        for vc, pm in zip(value_codes, parameter_modes):
            if pm == 0:
                ret.append(self.program[vc])
            elif pm == 1:
                ret.append(vc)
            else:
                raise Exception(f"Invalid parameter mode at ip {self.ip}")
        return ret

    def _get_value(self, vc, pm):
        if pm == 0:
            return self.program[vc]
        elif pm == 1:
            return vc
        else:
            raise Exception(f"Invalid parameter mode at ip {self.ip}")

    def op_01(self, parameters, parameter_modes):
        # SUM
        result = sum(self._get_values(parameters[:2], parameter_modes[:2]))
        self.program[parameters[-1]] = result
        self.ip += 4

    def op_02(self, parameters, parameter_modes):
        # PRODUCT
        result = prod(self._get_values(parameters[:2], parameter_modes[:2]))
        self.program[parameters[-1]] = result
        self.ip += 4

    def op_03(self, parameters, parameter_modes):
        # INPUT
        self.program[parameters[0]] = self.input_parameter
        self.ip += 2

    def op_04(self, parameters, parameter_modes):
        # OUTPUT
        print(f"OUTPUT VAL: {self.program[parameters[0]]}")
        self.ip += 2

    def op_05(self, parameters, parameter_modes):
        # JUMP_IF_TRUE
        if self._get_value(parameters[0], parameter_modes[0]):
            self.ip = self._get_value(parameters[1], parameter_modes[1])
        else:
            self.ip += 3

    def op_06(self, parameters, parameter_modes):
        # JUMP_IF_FALSe
        if not self._get_value(parameters[0], parameter_modes[0]):
            self.ip = self._get_value(parameters[1], parameter_modes[1])
        else:
            self.ip += 3

    def op_07(self, parameters, parameter_modes):
        # LESS_THAN
        if self._get_value(parameters[0], parameter_modes[0]) < self._get_value(
            parameters[1], parameter_modes[1]
        ):
            self.program[parameters[2]] = 1
        else:
            self.program[parameters[2]] = 0
        self.ip += 4

    def op_08(self, parameters, parameter_modes):
        # EQUAL_TO
        if self._get_value(parameters[0], parameter_modes[0]) == self._get_value(
            parameters[1], parameter_modes[1]
        ):
            self.program[parameters[2]] = 1
        else:
            self.program[parameters[2]] = 0
        self.ip += 4

    def op_99(self, parameters, parameter_modes):
        # HALT
        print("PROGRAM HALT")
        raise StopIteration("Reached halt instruction")


class IntcodeSimulator(IntcodeComputer):
    operations = {
        int(func[-2:]): func
        for func in dir(IntcodeComputer)
        if callable(getattr(IntcodeComputer, func)) and not func.startswith("_")
    }

    def parse_instruction(self, instruction):
        opcode = instruction % 100
        parameter_modes_int = instruction / 100
        # first p has first p_mode in list
        parameter_modes = [(parameter_modes_int // 10 ** i) % 10 for i in range(4)]
        return opcode, parameter_modes

    def exe_instruction(self, instruction):
        opcode, parameter_modes = self.parse_instruction(instruction)
        value_codes = self.program[
            self.ip + 1 : self.ip + self.op_paramater_count[opcode] + 1
        ]
        getattr(self, self.operations[opcode])(value_codes, parameter_modes)

    def run_program(self):
        while True:
            # print(self.ip, self.program)
            try:
                self.exe_instruction(self.program[self.ip])
            except StopIteration:
                # print(f"final program state {self.program}")
                break
            except IndexError as e:
                print("Ran off the end of the tape (probably)")
                print(e)
                break


print("Part 1")
part1simulation = IntcodeSimulator(program, 1)
part1simulation.run_program()

print("Part 2")
part2simulation = IntcodeSimulator(program, 5)
part2simulation.run_program()
