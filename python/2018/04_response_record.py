"""
ADVENT OF CODE: 2018
Day 4: Response Record
"""
import parse
import datetime
from collections import defaultdict

guardlog = dict()
daylog = defaultdict(list)
for line in open("inputs/04.input", "r"):
    # for line in open('04_test.input','r'):
    if line:
        time, msgA, msgB = parse.parse("[{:ti}] {} {}", line)
        if msgA == "Guard":
            gid = parse.parse("#{:d} begins shift", msgB)[0]
            if time.hour == 23:
                guardlog[time.date() + datetime.timedelta(days=1)] = (gid, time)
            else:
                guardlog[time.date()] = (gid, time)
        if msgA == "wakes":
            daylog[time.date()].append(("wakes", time))
        if msgA == "falls":
            daylog[time.date()].append(("sleeps", time))
# part 1
sleep_record = defaultdict(dict)
HOUR_LEN = 60
for day, guard_start in guardlog.items():
    sleep_record[day]["guard_id"] = guard_start[0]
    sleep_record[day]["record"] = [0] * HOUR_LEN
    for entry in daylog[day]:
        minute = entry[1].minute
        # magic: XOR element after minute with 1 to flip record, works because each sleep has guaranteed
        # wake pair
        sleep_record[day]["record"][minute:] = [
            1 ^ x for x in sleep_record[day]["record"][minute:]
        ]

guard_stats = defaultdict(int)
for day, day_sleep_record in sleep_record.items():
    guard_stats[day_sleep_record["guard_id"]] += sum(day_sleep_record["record"])
gid_max = max(guard_stats, key=guard_stats.get)

minute_tracker = [0] * HOUR_LEN
for day, day_sleep_record in sleep_record.items():
    if day_sleep_record["guard_id"] == gid_max:
        minute_tracker = [
            a + b for a, b in zip(minute_tracker, day_sleep_record["record"])
        ]
minute_slept_most = minute_tracker.index(max(minute_tracker))
print(gid_max * minute_slept_most)

# part 2
minutewise_guard_stats = dict()
for day, day_sleep_record in sleep_record.items():
    gid = day_sleep_record["guard_id"]
    if gid not in minutewise_guard_stats:
        minutewise_guard_stats[gid] = day_sleep_record["record"]
    else:
        minutewise_guard_stats[gid] = [
            a + b
            for a, b in zip(minutewise_guard_stats[gid], day_sleep_record["record"])
        ]

maxed_min = 0
maxed_min_val = 0
maxed_gid = None
for gid, stats in minutewise_guard_stats.items():
    for minute, minute_val in enumerate(stats):
        if minute_val > maxed_min_val:
            maxed_min = minute
            maxed_min_val = minute_val
            maxed_gid = gid

print(maxed_min * maxed_gid)
