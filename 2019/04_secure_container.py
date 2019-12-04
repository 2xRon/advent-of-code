"""
AOC 2019
Day 4: Secure Container
Solution by 2xRon
"""
a = 234208
b = 765869

from collections import Counter

meet = []


def has_adjacent_digits(n):
    return any(n[i] == n[i + 1] for i in range(len(n) - 1))


def is_non_decreasing(n):
    return not any(ns[i] < ns[i + 1] for i in range(len(n) - 1))


for n in range(a, b + 1):
    ns = [int(x) for x in str(n)]
    if has_adjacent_digits(ns) and is_non_decreasing(ns):
        meet.append(ns)

print("Part 1:", len(meet))

part2s = []
for ns in meet:
    c = Counter(ns)
    if 2 in c.values():
        part2s.append(c)


print("Part 2:", len(part2s))
