from numpy import *

m = [[{
    '|': [(0,1), (0,-1)],
    '-': [(1,0), (-1,0)],
    '7': [(-1, 0), (0, 1)],
    'F': [(1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    'L': [(1, 0), (0, -1)],
    '.': [(0, 0)],
    'S': [(1,1), (1, 0), (-1, 0), (0, 1), (0, -1)]
    }[s] for s in l.strip()] for l in open('input.txt')]

def search(x,y, done=[], steps = 1):
    done = [(x,y)]
    xd, yd = m[y][x][0]
    x, y = x+xd, y+yd
    steps += 1
    while (x,y) not in done:
        done += [(x, y)]
        for xd, yd in set(m[y][x]):
            if (x + xd, y + yd) not in done:
                x, y = x + xd, y + yd
                steps += 1
                break
    return steps, done

start_x, start_y = 0, 0
for y in range(len(m)):
    for x in range(len(m[0])):
        o = m[y][x]
        if (1,1) in o:
            m[y][x] = [d for d in o if (d[0]*-1, d[1]*-1) in m[y+d[1]][x+d[0]]]
            start_x = x
            start_y = y

r, cycle = search(start_x,start_y)

c = 0
for y in range(len(m)):
    inside = False
    u = False
    for x in range(len(m[0])):
        if (x, y) in cycle:
            if (1, 0) not in m[y][x] or (-1,0) not in m[y][x]:
                if (0,1) in m[y][x] and (0,-1) in m[y][x]:
                    inside = not inside
                else:
                    if (1, 0) not in m[y][x]:
                        if ((0, 1) in m[y][x]) != u:
                            inside = not inside
                    else:
                        u = (0, 1) in m[y][x]
        elif inside:
            c += 1
print(int(ceil(r/2)), c)