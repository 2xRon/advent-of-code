"""
AOC 2020
Day 6: Custom Customs
Solution by 2xRon
"""

with open("./input/06.input") as in_file:
    groups = in_file.read().split("\n\n")

yeses = [set(s.replace(" ","").replace("\n","")) for s in groups]
print("Part 1:", sum(len(y) for y in yeses))

person_groups = [[set(p.strip()) for p in g.split("\n")] for g in groups]
counts = [len(set.intersection(*g)) for g in person_groups]
print("Part 2:", sum(counts))