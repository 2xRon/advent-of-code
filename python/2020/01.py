"""
AOC 2020
Day 1: 
Solution by 2xRon
"""

with open("./input/01.input") as in_file:
    nums = [int(x) for x in in_file.read().strip().splitlines()]
# assuming all distinct

num_diff_hash = dict()
for x in nums:
    diff = 2020 - x
    if diff in num_diff_hash:
        print("Part 1:", x * diff)
    else:
        num_diff_hash[x] = diff

found = False
for y in nums:
    diff1 = 2020 - y
    diff1_hash = dict()
    for x in nums:
        diff2 = diff1 - x
        if diff2 in diff1_hash:
            print("Part 2:", x * y * (2020 - x - y))
            found = True
            break
        else:
            diff1_hash[x] = diff2
    if found:
        break
