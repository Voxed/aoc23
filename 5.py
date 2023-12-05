from numpy import *

maps = {}
nm = {}
inn = [r.split('\n') for r in open('input.txt').read().split('\n\n')]

seeds = [('seed', p[0], p[1]) for p in list(reshape([int(e) for e in inn[0][0].split()[1:]], (-1, 2)))]
print('SEEDS:')
print(seeds)

for l in inn[1:]:
    f, _, t = l[0].split()[0].split('-')
    nm[f] = t
    if f not in maps:
        maps[f] = []
    for r in l[1:]:
        if r != '':
            d, s, r = map(int, r.split())
            maps[f].append((s, s+r, d-s, r))

print(maps)

dest = []
m = None



for k in seeds:
    while k[0] != 'location':
        for rs, re, s, le in maps[k[0]]:
            if rs <= k[1] and re > k[1]:
                old = k[2]
                if k[1] + k[2] > re:
                    old = re - k[1]
                    ns = (k[0], re, k[1] + k[2] - re)
                    seeds.append(ns)
                k = (nm[k[0]], k[1] + s, old)
                break
        else:
            k = (nm[k[0]], k[1], k[2])
    print(k)
            
    if m is None:
        m = k[1]
    elif m > k[1]:
        m = k[1]

print(m)
