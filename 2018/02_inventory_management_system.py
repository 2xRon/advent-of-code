'''
ADVENT OF CODE: 2018
Day 2: Inventory Management System
'''

from collections import Counter

linesin = []
for line in open('02_input','r'):
    if line.strip():
        linesin.append(line.strip())

lettercounts = [Counter(x) for x in linesin]

count3 = 0
count2 = 0
for id_count in lettercounts:
    if 2 in id_count.values():
        count2 += 1
    if 3 in id_count.values():
        count3 += 1

print(count2*count3)


unique_modified_ids = set()
for id in linesin:
    for c_pos in range(len(id)):
        t = ''.join(id[0:c_pos]+'_'+id[c_pos+1:])
        if t in unique_modified_ids:
            # found duplicate
            result = ''.join(id[0:c_pos]+id[c_pos+1:])
        else:
            unique_modified_ids.add(t)
print(result)
