"""
AOC 2019
Day 16: Flawed Frequency Transmission
Solution by 2xRon
"""

from itertools import cycle, chain
from copy import copy

with open("./inputs/16.input") as in_file:
    signal = [int(x) for x in in_file.read().strip()]

test_signal = 80871224585914546619083218645595
signal = [int(x) for x in str(test_signal)]
signal = signal*10000
signal_len = len(signal)
msg_offset = int("".join(str(x) for x in signal[:7]))

def apply_FFT(signal,index):
    offset = index+1
    p0 = [0]*offset
    p1 = [1]*offset
    p2 = [0]*offset
    p3 = [-1]*offset

    pattern = cycle(chain(p0,p1,p2,p3))
    next(pattern) # skip first 0

    return abs(sum(x*y for x,y in zip(signal,pattern)) ) % 10

for step in range(100):
    print("phase:",step)
    next_signal = [apply_FFT(signal,idx) for idx in range(signal_len)]
    signal = next_signal

# print("Part 1:", "".join(str(x) for x in signal[:8]))

print("Part 2:",signal[msg_offset:msg_offset+8])
