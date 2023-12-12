from numpy import *
import functools


def scan(arr):
    q = pad(arr, (0, 1)) != pad(arr, (1, 0))
    r = array([t.sum() for t in split(arr, where(q)[0])])
    return tuple([tuple(x[1:]) for x in split(r, where(r == 0)[0]) if x.shape != (0,)][:-1])


@functools.cache
def consume(v, g):
    while v > 0:
        if not g:
            return None
        e, g = g[0], g[1:]
        v -= abs(e)
        if (e > 0 and v < 0) or (e < 0 and v == 0 and g):
            return None
        if v == 0 and g:
            g = (g[0] + 1,) + g[1:]
        else:
            g = (v+1,)*(v < 0 and e < 0) + g
    return g


@functools.cache
def sols(comb, val):
    if len(comb) == 0:
        return len(val) == 0
    g = tuple([c for c in comb[0] if c != 0])
    if g == ():
        return sols(comb[1:], val)
    skip = sols(((comb[0][0] + 1,) + comb[0][1:],) +
                comb[1:], val) if g[0] < 0 else 0
    if len(val) == 0 or (g := consume(val[0], g)) is None:
        return skip
    return sols((g,) + comb[1:], val[1:]) + skip


i = [(scan(([{'.': 0, '?': -1, '#': 1}[c] for c in l.split()[0]] + [-1])*4 + [{'.': 0, '?': -1, '#': 1}[c]
      for c in l.split()[0]]), tuple(map(int, l.split()[1].strip().split(',')))*5) for l in open('input.txt')]
s = 0
q = len(i)
t = 0
for comb, val in i:
    s += sols(comb, val)
    t += 1
    print(str(t) + '/' + str(q))

print(s)
