from shapely import *

i = [l.strip().split() for l in open('input.txt')]

a = [(0, 0)]
b = [(0, 0)]
r = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

for d, l, c in i:
    d = r[d]
    a += [(a[-1][0] + d[0]*int(l), a[-1][1] + d[1]*int(l))]
    d = [*r.values()][int(c[-2], 16)]
    l = int(c[-7:-2], 16)
    b += [(b[-1][0] + d[0]*int(l), b[-1][1] + d[1]*int(l))]

print(
    int(Polygon(a).buffer(0.5, join_style=2).area),
    int(Polygon(b).buffer(0.5, join_style=2).area)
)
