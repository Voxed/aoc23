from numpy import *
from itertools import * 
m = array([[*l.strip()] for l in open('input.txt').readlines()])
er, ec = all(m == '.', 1), all(m.transpose() == '.', 1)
distances = []
for d in (2, 1000000):
    s = 0.0
    p = [*combinations(vstack(nonzero(m == '#')).transpose(), 2)]
    for y1, x1, y2, x2 in hstack([amin(p, 1), amax(p, 1)]):
        s += (er[y1:y2].sum() + ec[x1:x2].sum())*d + (~er)[y1:y2].sum() + (~ec)[x1:x2].sum()
    distances.append(int(s))
print(*distances)