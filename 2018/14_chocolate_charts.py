"""
ADVENT OF CODE: 2018
Day 14: Chocolate Charts
"""

input_val = open("inputs/14.input", "r").read().strip()

scoreboard = "37"
elfA = 0
elfB = 1

while input_val not in scoreboard[-10:]:
    # create new recipies
    scoreboard += str(int(scoreboard[elfA])+int(scoreboard[elfB]))
    # advance elves
    elfA = (elfA + 1 + int(scoreboard[elfA])) % len(scoreboard)
    elfB = (elfB + 1 + int(scoreboard[elfB])) % len(scoreboard)

answerA = scoreboard[int(input_val):int(input_val)+10]
answerB = scoreboard.index(input_val)
print("Part A: " + answerA)
print("Part B: " + str(answerB))

