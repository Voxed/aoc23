from numpy import *

pattern = [array(list(map(list, p.split('\n')))) for p in open('input.txt').read().split('\n\n')]

s = 0
t = 0

for p in pattern:
    for r in range(0, p.shape[0]):
        a, b = flipud(p[:r,:]), p[r:,:]
        h = min(a.shape[0], b.shape[0])
        a, b = a[:h, :], b[:h, :]
        a = a[:h, :]
        s += (a == b).all() * r * 100
        t += ((~(a == b)).sum() == 1) * r * 100

    for r in range(0, p.shape[1]):
        a, b = fliplr(p[:,:r]), p[:,r:]
        w = min(a.shape[1], b.shape[1])
        a, b = a[:, :w], b[:, :w]
        s += (a == b).all() * r
        t += ((~(a == b)).sum() == 1) * r

print(s, t)