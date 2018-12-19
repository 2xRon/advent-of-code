
'''
ADVENT OF CODE: 2018
Day 6: Chronal Coordinates
'''

in_file = open('inputs/06.input','r').readlines()
points = [tuple(map(int,l.replace(' ','').split(','))) for l in in_file]

max_x = max(points, key=lambda x: x[0])[0]
max_y = max(points, key=lambda y: y[1])[1]

def l1distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

L1dists = list()
for yc in range(max_y+1):
    xl = list()
    for xc in range(max_x+1):
        xl.append({pt:l1distance(pt,(xc,yc)) for pt in points})
    L1dists.append(xl)

area_counts = {pt:0 for pt in points}

