
"""
ADVENT OF CODE: 2018
Day 8: Chronal Change
"""

N = int(open("./inputs/11.input").read().strip())
N = 57
DIM = 300
grid = [[0]*DIM]*DIM
zone_power = [[0]*DIM]*DIM

for y in range(1,DIM+1):
    for x in range(1,DIM+1):
        y_idx = y-1
        x_idx = x-1
        rack_id = x+10
        power_level = rack_id * y
        power_level += N
        power_level *= rack_id
        power_level = power_level // 100
        power_level %= 10
        power_level -= 5
        grid[y_idx][x_idx] = power_level

print(grid[79][122])

max_power = -1000
max_power_x_idx = -1
max_power_y_idx = -1
for y in range(DIM-3):
    for x in range(DIM-3):
        power_sum = sum(sum(grid[y_c][x:x+3]) for y_c in range(y,y+3))
        if power_sum > max_power:
            max_power = power_sum
            max_power_x_idx = x
            max_power_y_idx = y

print(max_power_x_idx+1,max_power_y_idx+1)
