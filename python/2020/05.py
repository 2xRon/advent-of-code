"""
AOC 2020
Day 5: Binary Boarding
Solution by 2xRon
"""

tr = str.maketrans("FBLR", "0101")

with open("./input/05.input") as in_file:
    seats = set(int(s.translate(tr), 2) for s in in_file.readlines())
    print("Part 1:", max(seats))
    missing_seat = set(range(min(seats), max(seats) + 1)).difference(seats)
    print("Part 2:", tuple(missing_seat)[0])
