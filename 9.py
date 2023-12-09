from numpy import *
n = lambda h: 0 if not any(h) else h[-1] + n(diff(h))
h = array([l.split() for l in open('input.txt')], int)
print(sum([*map(n, h)]), sum([*map(n, flip(h))]))