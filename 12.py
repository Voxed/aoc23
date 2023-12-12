from numpy import *
import functools

def segscan(arr, reset_on): # not actually segscan
    rs = 0
    rs2 = 0
    finsums = []
    sums = []
    for e in arr:
        if e == reset_on:
            if rs != 0:
                sums.append(rs)
                rs = 0
            if rs2 != 0:
                sums.append(rs2)
                rs2 = 0
            if len(sums) != 0:
                finsums.append(tuple(sums))
                sums = []
        if e == 1:
            rs += e
            if rs2 != 0:
                sums.append(rs2)
                rs2 = 0
        if e == -1:
            rs2 -= 1 
            if rs != 0:
                sums.append(rs)
                rs = 0
    if rs != 0:
        sums.append(rs)
    if rs2 != 0:
        sums.append(rs2)
    if len(sums) > 0:
        finsums.append(tuple(sums))
    return tuple(finsums)

@functools.cache
def sols(comb, val):
    if len(comb) == 0:
        return 1 if len(val) == 0 else 0

    g = comb[0]
    if len(g) > 0 and g[0] == 0:
        g = g[1:]

    if g == ():
        return sols(comb[1:], val)

    skip = 0
    if comb[0][0] < 0:
            skip = sols(((comb[0][0] + 1,) + comb[0][1:],) + comb[1:], val)

    if len(val) == 0:
        return skip
    
    v = val[0]
    while v > 0:
        if g == ():
            return skip
        e = g[0]
        if e == 0:
            g = g[1:]
        elif e > 0:
            if e <= v:
                if e == v and len(g) > 1 and g[1] != 0:
                    g = (g[0], g[1] + 1) + g[2:]
                v -= e
            else:
                return skip
            g = g[1:]
        elif e < 0:
            e *= -1
            if e == v and len(g) == 1:
                v -= e
                g = g[1:]
            elif e > v:
                v -= e
                g = (v+1,) + g[1:]
            elif e < v:
                v -= e
                g = g[1:]
            else:
                return skip

    rest = sols((g,) + comb[1:], val[1:])

    return rest + skip


i = [(segscan(([{'.': 0, '?': -1, '#': 1}[c] for c in l.split()[0]] + [-1])*4 + [{'.': 0, '?': -1, '#': 1}[c] for c in l.split()[0]], 0), tuple(map(int, l.split()[1].strip().split(',')))*5) for l in open('input.txt')]
s = 0
q = len(i)
t = 0
for comb, val in i:
    s += sols(comb, val)
    t += 1
    print(str(t) + '/' + str(q))

print(s)
