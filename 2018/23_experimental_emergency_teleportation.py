"""
ADVENT OF CODE: 2018
Day 23: Experimental Emergency Teleportation
"""

from collections import namedtuple
import re
from itertools import product

Bot = namedtuple("Bot",["pos","radius"])

bot_pattern = re.compile(r"pos=<(-?\d+,-?\d+,-?\d+)>, r=(\d+)")
with open("./inputs/23.input") as in_file:
    bots = [re.match(bot_pattern, l) for l in in_file.readlines()]
    bots = [Bot(tuple(map(int, b.group(1).split(","))), int(b.group(2))) for b in bots]

largest_signal_radius_bot = max(bots, key=lambda x:x.radius)
def bot_dist(bot1,bot2):
    return sum(abs(x-y) for x,y in zip(bot1.pos, bot2.pos))

bots_in_range = [b for b in bots if bot_dist(largest_signal_radius_bot, b) <= largest_signal_radius_bot.radius]
print("Part 1:", len(bots_in_range))

mins = tuple(min(b.pos[coord] for b in bots) for coord in range(3))
maxs = tuple(max(b.pos[coord] for b in bots) for coord in range(3))

for coord in product(*(range(l,h+1) for l,h in zip(mins,maxs))):
    print(coord)
