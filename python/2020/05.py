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
    seats = set(seat(s) for s in in_file.readlines())
    print("Part 1:", max(seats))
    missing_seat = seats.symmetric_difference(set(range(min(seats), max(seats)+1)))
    print("Part 2:", tuple(missing_seat)[0])
