from numpy import *

import sys
sys.setrecursionlimit(100000)

m = pad([[{
    '|': set([(0,1), (0,-1)]),
    '-': set([(1,0), (-1,0)]),
    '7': set([(-1, 0), (0, 1)]),
    'F': set([(1, 0), (0, 1)]),
    'J': set([(-1, 0), (0, -1)]),
    'L': set([(1, 0), (0, -1)]),
    '.': set([(0, 0)]),
    'S': set([(1, 1)])
    }[s] for s in l.strip()] for l in open('input.txt')], pad_width=1, constant_values=(set([(0,0), (0,0)])))

minimum = {}

def search(o, x,y, done=[], steps = 1):
    for xl, yl in o:
        if (x + xl, y + yl) not in done:
            if (xl*-1, yl*-1) in m[y + yl][x + xl]:
                if (x + xl, y + yl) in minimum:
                    minimum[(x + xl, y + yl)] = min(minimum[(x + xl, y + yl)], steps) 
                else:
                    minimum[(x + xl, y + yl)] = steps
                search(m[y + yl][x + xl], x + xl, y + yl, done = done + [(x + xl, y + yl)], steps = steps + 1)

for y in range(len(m)):
    for x in range(len(m[0])):
        o = m[y][x]
        if (1,1) in o:
            search(set([(0,1), (1,0), (-1,0), (0, -1)]), x,y)
            minimum[(x,y)] = 0
            print(minimum)

his = sorted([(minimum[k], k) for k in minimum])

print(his[-1][0])
c = 0
for y in range(len(m)):
    inside = False
    u = False
    for x in range(len(m[0])):
        if (x, y) in minimum:
            if (1,1) in m[y][x]:
                if (-1, 0) in m[y][x+1]:
                    m[y][x].add((1,0))
                if (1, 0) in m[y][x-1]:
                    m[y][x].add((-1,0))
                if (0, -1) in m[y+1][x]:
                    m[y][x].add((0,1))
                if (0, 1) in m[y-1][x]:
                    m[y][x].add((0,-1))
            if (1, 0) not in m[y][x] or (-1,0) not in m[y][x]:
                if (0,1) in m[y][x] and (0,-1) in m[y][x]:
                    inside = not inside
                else:
                    if (1, 0) not in m[y][x]:
                        if ((0, 1) in m[y][x]) != u:
                            inside = not inside
                    else:
                        u = (0, 1) in m[y][x]
            print('#', end='')
        elif inside:
            c += 1
            print('I', end='')
        else:
            print('O', end='')
    print('')
print(c)