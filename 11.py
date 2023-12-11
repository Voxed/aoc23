from numpy import *
from itertools import * 
m = array([list(l.strip()) for l in open('input.txt').readlines()])
er = all(m == '.', 1)
ec = all(m.transpose() == '.', 1)
distances = []
for d in (2, 1000000):
    s = 0.0
    p = list(combinations(list(vstack(nonzero(m == '#')).transpose()), 2))
    for y1, x1, y2, x2 in hstack([amin(p, 1), amax(p, 1)]):
        s += er[y1:y2].sum()*d + (~er)[y1:y2].sum() + ec[x1:x2].sum()*d + (~ec)[x1:x2].sum()
    distances.append(s)
print(*distances)