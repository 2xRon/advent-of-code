"""
AOC 2020
Day 9: Encoding Error
Solution by 2xRon
"""

from itertools import chain

with open("./input/09.input") as in_file:
    signal = [int(x) for x in in_file.readlines()]


def pin_low(idx):
    return max(idx, 0)

PREAMBLE = 25
available = []
for idx in range(len(signal)):
    x = signal[idx]
    if x not in chain(*(available[-PREAMBLE:])) and idx > PREAMBLE:
        break
    available.append([x + y for y in signal[pin_low(idx - PREAMBLE) : idx]])

print("Part 1:", x)
target = x
target_idx = idx
for start in range(len(signal)):
    for l in range(2, len(signal) - start):
        if sum(signal[start:start+l]) == target:
            break
    else:
        continue
    break
else:
    print("Part 2 Not Found")

print("Part 2:", max(signal[start:start+l]) + min(signal[start:start+l]))