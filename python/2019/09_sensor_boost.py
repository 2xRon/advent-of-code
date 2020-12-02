"""
AOC 2019
Day 9: Sensor Boost
Solution by 2xRon
"""

from math import prod
from copy import copy
from collections import namedtuple


with open("./inputs/09.input") as in_file:
    program = [int(x) for x in in_file.read().strip().split(",")]

# program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# program = [1102,34915192,34915192,7,4,7,99,0]
# program = [104,1125899906842624,99]


class IntcodeComputer:

    ip = 0  # instruction pointer
    rb = 0  # relative base
    op_paramater_count = dict(
        [
            (1, 3),
            (2, 3),
            (3, 1),
            (4, 1),
            (5, 2),
            (6, 2),
            (7, 3),
            (8, 3),
            (9, 1),
            (99, 0),
        ]
    )

    def __init__(self, program, input_parameter=1):
        self.program = copy(program) + [0] * 2048  # memory padding
        self.input_parameter = input_parameter

    def _get_values(self, value_codes, parameter_modes):
        ret = list()
        for vc, pm in zip(value_codes, parameter_modes):
            if pm == 0:
                ret.append(self.program[vc])
            elif pm == 1:
                ret.append(vc)
            elif pm == 2:
                ret.append(self.program[vc + self.rb])
            else:
                raise Exception(f"Invalid parameter mode,{pm}, at ip {self.ip}")
        return ret

    def _get_value(self, vc, pm):
        if pm == 0:
            return self.program[vc]
        elif pm == 1:
            return vc
        elif pm == 2:
            return self.program[vc + self.rb]
        else:
            raise Exception(f"Invalid parameter mode at ip {self.ip}")

    def _write_value(self, value, location_parameter, parameter_mode):
        location = self._get_value(location_parameter, parameter_mode)
        self.program[location] = value

    def op_01(self, parameters, parameter_modes):
        # SUM
        result = sum(self._get_values(parameters[:2], parameter_modes[:2]))
        self._write_value(result, parameters[-1], parameter_modes[-1])
        self.ip += 4

    def op_02(self, parameters, parameter_modes):
        # PRODUCT
        result = prod(self._get_values(parameters[:2], parameter_modes[:2]))
        self._write_value(result, parameters[-1], parameter_modes[-1])
        self.ip += 4

    def op_03(self, parameters, parameter_modes):
        # INPUT
        print(parameters, parameter_modes)
        self._write_value(self.input_parameter, parameters[0], parameter_modes[0])
        self.ip += 2

    def op_04(self, parameters, parameter_modes):
        # OUTPUT
        print(f"OUTPUT VAL: {self._get_value(parameters[0],parameter_modes[0])}")
        self.ip += 2

    def op_05(self, parameters, parameter_modes):
        # JUMP_IF_TRUE
        if self._get_value(parameters[0], parameter_modes[0]):
            self.ip = self._get_value(parameters[1], parameter_modes[1])
        else:
            self.ip += 3

    def op_06(self, parameters, parameter_modes):
        # JUMP_IF_FALSE
        if not self._get_value(parameters[0], parameter_modes[0]):
            self.ip = self._get_value(parameters[1], parameter_modes[1])
        else:
            self.ip += 3

    def op_07(self, parameters, parameter_modes):
        # LESS_THAN
        if self._get_value(parameters[0], parameter_modes[0]) < self._get_value(
            parameters[1], parameter_modes[1]
        ):
            self._write_value(1, parameters[2], parameter_modes[2])
        else:
            self._write_value(0, parameters[2], parameter_modes[2])
        self.ip += 4

    def op_08(self, parameters, parameter_modes):
        # EQUAL_TO
        if self._get_value(parameters[0], parameter_modes[0]) == self._get_value(
            parameters[1], parameter_modes[1]
        ):
            self._write_value(1, parameters[2], parameter_modes[2])
        else:
            self._write_value(0, parameters[2], parameter_modes[2])
        self.ip += 4

    def op_09(self, parameters, parameter_modes):
        # ADJUST_RELATIVE_BASE
        self.rb += self._get_value(parameters[0], parameter_modes[0])
        self.ip += 2

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
