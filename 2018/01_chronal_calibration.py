#!/usr/bin/python
'''
ADVENT OF CODE: 2018
Day 1: Chronal Calibration
'''

output1 = []
for line in open('01_input','r'):
    if line.strip():
        output1.append(int(line))
    

maxiter = 2000
cumsum = []
last = 0
freqsum = [sum(output1[0:x+1]) for x in range(len(output1))]

for i in range(maxiter):
    cumsum += [a+b for a,b in zip(freqsum, [last]*len(freqsum))] 
    last = cumsum[-1]

def firstDuplicate(a):
    set_ = set()
    for item in a:
        if item in set_:
            return item
        set_.add(item)
    return None

print(firstDuplicate(cumsum))
