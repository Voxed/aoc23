from numpy import *
from itertools import *
m = array([[*l.strip()] for l in open('input.txt').readlines()])
er, ec = all(m == '.', 1), all(m.transpose() == '.', 1)
for d in (2, 1000000):
    p = [*combinations(vstack(nonzero(m == '#')).transpose(), 2)]
    print(int(sum([*map(float, [(er[y1:y2].sum() + ec[x1:x2].sum())*d + (~er)[y1:y2].sum() + (~ec)[x1:x2].sum()
                                for y1, x1, y2, x2 in hstack([amin(p, 1), amax(p, 1)])])])), end=' ')
print('')
