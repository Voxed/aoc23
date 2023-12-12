from numpy import *
import functools


def scan(arr):
    q = pad(arr, (0, 1)) != pad(arr, (1, 0))
    r = array([t.sum() for t in split(arr, where(q)[0])])
    return tuple([tuple(x[1:]) for x in split(r, where(r == 0)[0]) if x.shape != (0,)][:-1])

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


i = [(scan(([{'.': 0, '?': -1, '#': 1}[c] for c in l.split()[0]] + [-1])*4 + [{'.': 0, '?': -1, '#': 1}[c] for c in l.split()[0]]), tuple(map(int, l.split()[1].strip().split(',')))*5) for l in open('input.txt')]
s = 0
q = len(i)
t = 0
for comb, val in i:
    s += sols(comb, val)
    t += 1
    print(str(t) + '/' + str(q))

print(s)
