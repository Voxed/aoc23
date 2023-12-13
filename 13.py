from numpy import *
s, t = 0, 0
for p in [array([*map(list, p.split('\n'))]) for p in open('input.txt').read().strip().split('\n\n')]:
    for c, p in (100, p), (1, p.transpose()):
        for r in range(0, p.shape[0]):
            h = min(r, p.shape[0] - r)
            a, b = p[r-1::-1][:h], p[r:][:h]
            s += (a == b).all() * r * c
            t += ((~(a == b)).sum() == 1) * r * c
print(s, t)
