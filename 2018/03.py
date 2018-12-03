# AOC 3
import numpy as np

in_lines = []
for line in open('03.input','r'):
    if line:
        in_lines.append(line.strip().split(' '))

zip_flip = list(map(list,zip(*in_lines)))
claim_nos = [int(x[1:]) for x in zip_flip[0]]
coords = [tuple(map(int,cpair.rstrip(':').split(',')))  for cpair in zip_flip[2]]
dims = [tuple(map(int,dim.split('x'))) for dim in zip_flip[3]]

# Part 1
fabric_edge = 1000
overlap_count = 0
occupy_count = np.array([[0]*fabric_edge]*fabric_edge)
for coord, dim in zip(coords,dims):
    occupy_count[ coord[1]:coord[1]+dim[1], coord[0]:coord[0]+dim[0] ] += 1

for row in occupy_count:
    for cell in row:
        if cell > 1:
            overlap_count += 1

print(overlap_count)

# part 2
dc = {a: b for a,b in zip(claim_nos,coords)}
dd = {a: b for a,b in zip(claim_nos,dims)}
ot = np.array([[0]*fabric_edge]*fabric_edge)
overlapped = {a: b for a,b in zip(claim_nos,[False]*len(claim_nos))}
overlapped[0]=False
for claim in claim_nos:
    # chk claim for existing claims, write to overlapped, write claim
    claim_region = ot[dc[claim][1]:dc[claim][1]+dd[claim][1], dc[claim][0]:dc[claim][0]+dd[claim][0]]
    for underlap_row in claim_region:
        for underlap_cell in underlap_row:
            overlapped[underlap_cell] = True
            if underlap_cell != 0:
                overlapped[claim] = True
    ot[dc[claim][1]:dc[claim][1]+dd[claim][1], dc[claim][0]:dc[claim][0]+dd[claim][0]] = claim

for k,v in overlapped.items():
    if not v:
        print(k)

