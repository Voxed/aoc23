from numpy import *

maps = []
nm = {}
inn = [r.split('\n') for r in open('input.txt').read().split('\n\n')]

seeds = [('seed', p[0], p[0] + p[1]) for p in list(reshape([int(e) for e in inn[0][0].split()[1:]], (-1, 2)))]
print('SEEDS:')
print(seeds)

for l in inn[1:]:
    f, _, t = l[0].split()[0].split('-')
    nm[f] = t
    for r in l[1:]:
        if r != '':
            d, s, r = map(int, r.split())
            maps.append((f, t, s, s+r, d-s))

dest = []
m = None



for o, os, oe in seeds:
    while o != 'location':
        for f, t, rs, re, s in maps:
            if f == o and rs <= os and re > os:
                old = oe
                if oe > re:
                    old = re
                    seeds.append((o, re, re + (oe - re)))
                o, os, oe = t, os + s, old + s
                break
        else:
            o, os, oe = nm[o], os, oe            
    if m is None:
        m = os
    elif m > os:
        m = os

print(m)
