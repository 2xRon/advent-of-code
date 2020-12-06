"""
AOC 2020
Day 6: Custom Customs
Solution by 2xRon
"""

with open("./input/06.input") as in_file:
    groups = [
        [set(p) for p in g.split("\n")] for g in in_file.read().split("\n\n")
    ]

print("Part 1:", sum(len(set.union(*g)) for g in groups))
print("Part 2:", sum(len(set.intersection(*g)) for g in groups))