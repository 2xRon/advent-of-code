"""
AOC 2020
Day 5: Binary Boarding
Solution by 2xRon
"""

from typing import Tuple


def seat(row_string):
    return int(
        "0b"
        + row_string.replace("F", "0")
        .replace("B", "1")
        .replace("L", "0")
        .replace("R", "1"),
        2,
    )


with open("./input/05.input") as in_file:
    seats = [seat(s) for s in in_file.readlines()]
    max_seat = max(seats)
    print("Part 1:", max_seat)
    for ii in range(seat("FFFFFFFRRR"), seat("BBBBBBBLLL")):
        if ii not in seats:
            if (ii - 1 in seats) and (ii + 1 in seats):
                print("Part 2:", ii)
