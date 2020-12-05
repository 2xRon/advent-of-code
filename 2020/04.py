"""
AOC 2020
Day 4: Passport Processing
Solution by 2xRon
"""

from typing import Dict

passports = list()
with open("./input/04.input") as in_file:
    pass_strings = in_file.read().strip().split("\n\n")

passports = [
    dict(tuple(e.split(":")) for e in p.replace("\n", " ").split(" "))
    for p in pass_strings
]

required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")


def is_present(p: Dict[str, str]) -> bool:
    return sum(k in p for k in required_keys) == len(required_keys)


valid_passports_one = sum(is_present(p) for p in passports)
print("Part 1:", valid_passports_one)

validations = {
    "byr": lambda x: x.isdigit() and 1920 <= int(x) <= 2002,
    "iyr": lambda x: x.isdigit() and 2010 <= int(x) <= 2020,
    "eyr": lambda x: x.isdigit() and 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and (150 <= int(x[:-2]) <= 193))
    or (x.endswith("in") and (59 <= int(x[:-2]) <= 76)),
    "hcl": lambda x: x.startswith("#")
    and len(x) == 7
    and all(c in "abcdef0123456789" for c in x[1:]),
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: len(x) == 9 and x.isdigit(),
}


def is_valid(p: Dict[str, str]) -> bool:
    return all(validations[k](p[k]) for k in validations.keys())


valid_passports_two = sum(is_present(p) and is_valid(p) for p in passports)
print("Part 2:", valid_passports_two)