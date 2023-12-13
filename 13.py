from numpy import *

s, t = 0, 0
for p in [array(list(map(list, p.split('\n')))) for p in open('input.txt').read().strip().split('\n\n')]:
    for r in range(0, p.shape[0]):
        a, b = flipud(p[:r, :]), p[r:, :]
        h = min(a.shape[0], b.shape[0])
        a, b = a[:h, :], b[:h, :]
        s += (a == b).all() * r * 100
        t += ((~(a == b)).sum() == 1) * r * 100
    for c in range(0, p.shape[1]):
        a, b = fliplr(p[:, :c]), p[:, c:]
        w = min(a.shape[1], b.shape[1])
        a, b = a[:, :w], b[:, :w]
        s += (a == b).all() * c
        t += ((~(a == b)).sum() == 1) * c

print(s, t)
