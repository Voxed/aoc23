from shapely import *
from numpy import *
from functools import *
i = [(a, int(b), int(c[-7:-2], 16), int(c[-2], 16)) for a,b,c in [l.strip().split() for l in open('input.txt')]]
s, t = array([[0, 1], [1, 0], [0, -1], [-1, 0]]), array([0, 0])
print(*[int(Polygon(u).buffer(0.5, join_style=2).area) for u in [
    reduce(lambda u, i: u + [u[-1] + s['RDLU'.index(i[0])]*i[1]], i, [t]), 
    reduce(lambda u, i: u + [u[-1] + s[i[3]]*i[2]], i, [t])
]])