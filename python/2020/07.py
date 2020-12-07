"""
AOC 2020
Day 7: Handy Haversacks
Solution by 2xRon
"""

from collections import defaultdict
import re

rules = dict()
with open("./input/07.input") as in_file:
    outer_pattern = re.compile(r"^(.+?) bags contain")
    inner_pattern = re.compile(r"(\d+) (.+?) bags?[,.]")
    for l in in_file.readlines():
        ##for l in t.split("\n"):
        rules.update(
            {
                outer_pattern.match(l).group(1): [
                    (int(c[0]), c[1]) for c in inner_pattern.findall(l)
                ],
            }
        )

contained = defaultdict(set)
for c in rules.keys():
    for i in rules[c]:
        contained[i[1]].add(c)

contains_gold = set()


def find_containers(color):
    for c in contained[color]:
        contains_gold.add(c)
        find_containers(c)


find_containers("shiny gold")

print("Part 1:", len(contains_gold))
print(rules["shiny gold"])


def count_inners(color):
    return sum(c[0] for c in rules[color]) + sum(
        c[0] * count_inners(c[1]) for c in rules[color]
    )


print("Part 2:", count_inners("shiny gold"))
