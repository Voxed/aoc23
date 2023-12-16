from numpy import *

import sys
sys.setrecursionlimit(5000)

m = array([list(l.strip()) for l in open('input.txt')])

n = 0

for i in ([((-1, y), (1, 0)) for y in range(0, m.shape[0])] + [((m.shape[1], y), (-1, 0)) for y in range(0, m.shape[0])] +
          [((x, -1), (0, 1)) for x in range(0, m.shape[1])] + [((x, m.shape[0]), (0, -1)) for x in range(0, m.shape[1])]):
    print(i)
    s = []

    def steps(p, d):
        dx, dy = d
        px, py = p
        px += dx
        py += dy
        p = (px, py)
        if px < 0 or px >= m.shape[1] or py < 0 or py >= m.shape[0]:
            return 0
        if (p, d) in s:
            return 0
        s.append((p,d))

        if dx > 0 and m[py, px] == '\\':
            dy = 1
            return steps(p, (0, 1))
        if dx < 0 and m[py, px] == '\\':
            return steps(p, (0, -1))
        if dy > 0 and m[py, px] == '\\':
            return steps(p, (1, 0))
        if dy < 0 and m[py, px] == '\\':
            return steps(p, (-1, 0))

        if dx > 0 and m[py, px] == '/':
            return steps(p, (0, -1)) 
        if dx < 0 and m[py, px] == '/':
            return steps(p, (0, 1)) 
        if dy > 0 and m[py, px] == '/':
            return steps(p, (-1, 0)) 
        if dy < 0 and m[py, px] == '/':
            return steps(p, (1, 0))

        if dx == 0 and m[py, px] == '-':
            return steps(p, (1, 0)) + steps(p, (-1, 0))
        #print(dx, dy)
        if dy == 0 and m[py, px] == '|':
            return steps(p, (0, 1)) + steps(p, (0, -1))
        
        return steps(p, d) + 1

    print(steps(*i))
    un = set([a[0] for a in s])
    print(len(un))
    n = max(n, len(un))
print(n)