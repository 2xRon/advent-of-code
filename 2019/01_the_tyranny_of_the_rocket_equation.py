

"""
ADVENT OF CODE: 2018
Day 01: The Tyranny of the Rocket Equation
"""

with open("inputs/01.input") as in_file:
    masses = [int(x) for x in in_file.readlines()]

fuel_required = [x//3-2 for x in masses]
print("Part 1:",sum(fuel_required))

def find_fuel(mass):
    fuel_required = 0
    addl_fuel_required = mass//3-2
    while addl_fuel_required > 0:
        fuel_required += addl_fuel_required
        addl_fuel_required = addl_fuel_required//3-2
    return fuel_required

real_fuel_req = [find_fuel(x) for x in masses]
print("Part 2:",sum(real_fuel_req))
