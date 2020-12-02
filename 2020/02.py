"""
AOC 2020
Day 2: Password Philosophy
Solution by 2xRon
"""

import re
from collections import namedtuple

Policy = namedtuple("Policy", ["low", "high", "letter", "password"])
policies = list()
with open("./input/02.input") as in_file:
    policypattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")
    for line in in_file.read().splitlines():
        match = policypattern.match(line)
        policies.append(Policy(int(match.groups(1)[0]), int(match.groups(2)[1]), match.groups(3)[2], match.groups(4)[3]))

def is_valid_policy_one(policy : Policy):
    count = policy.password.count(policy.letter)
    return (count >= policy.low) & (count <= policy.high)

print("Part 1:", sum(is_valid_policy_one(p) for p in policies))

def is_valid_policy_two(policy: Policy):
    return (policy.password[policy.low - 1] == policy.letter) ^ (policy.password[policy.high - 1] == policy.letter)

print("Part 2:", sum(is_valid_policy_two(p) for p in policies))