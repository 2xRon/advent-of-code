"""
AOC 2020
Day 3: Toboggan Trajectory
Solution by 2xRon
"""

from typing import Dict

passports = list()
with open("./input/04.input") as in_file:
    pass_strings = in_file.read().strip().split("\n\n")

passports = [
    {
        e.split(":")[0].strip(): e.split(":")[1].strip()
        for e in p.replace("\n", " ").split(" ")
    }
    for p in pass_strings
]

required_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

def is_present(p: Dict[str, str]) -> bool:
    return sum(k in p for k in required_keys) == len(required_keys)

valid_passports_one = sum(is_present(p) for p in passports)
print("Part 1:", valid_passports_one)

valid_ecl = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
validations = dict(
    [
        ("byr", lambda x: 1920 <= int(x) <= 2002),
        ("iyr", lambda x: 2010 <= int(x) <= 2020),
        ("eyr", lambda x: 2020 <= int(x) <= 2030),
        (
            "hgt",
            lambda x: (len(x) > 2)
            and (
                (x.endswith("cm") and (150 <= int(x[:-2]) <= 193))
                or (x.endswith("in") and (59 <= int(x[:-2]) <= 76))
            ),
        ),
        (
            "hcl",
            lambda x: x.startswith("#") & len(x)
            == 7 & all(ord(c) < 103 for c in x[1:]),
        ),
        ("ecl", lambda x: x in valid_ecl),
        ("pid", lambda x: len(x) == 9 and all(48 <= ord(c) <= 57 for c in x)),
    ]
)


def is_valid(p: Dict[str, str]) -> bool:
    return all(validations[k](p[k]) for k in validations.keys())

valid_passports_two = sum(is_present(p) and is_valid(p) for p in passports)
print("Part 2:", valid_passports_two)