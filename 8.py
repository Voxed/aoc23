from functools import *
import os

sequence_raw, nodes_raw = open('input.txt').read().split('\n\n')
sequence = sequence_raw.strip()
nodes = [(l[:3], l[-9:-1].split(', ')) for l in nodes_raw.strip().split('\n')]
nodes_map = dict([(n, (i, {'L': p[0], 'R': p[1]})) for i, (n, p) in enumerate(nodes)])

sidx = 540

if os.path.exists('cache.txt'):
    cache_map = eval(open('cache.txt').read())
else:
    def steps(n):
        been_there_done_that = []
        btdtmap = {}
        pos = n
        idx = 0
        steps = 0
        goals = []
        while True:
            sidx = (idx, nodes_map[pos][0])
            if sidx in been_there_done_that:
                print(sidx, idx, node_ind)
                break
            been_there_done_that.append(sidx)
            btdtmap[sidx] = steps
            steps += 1

            node_ind, p = nodes_map[pos]
            pos = p[sequence[idx]]
            if pos[-1] == 'Z':
                goals.append(steps)
            idx = (idx + 1) % len(sequence)
        return ([g - btdtmap[sidx] for g in goals], steps - btdtmap[sidx], btdtmap[sidx])

    cache_map = dict([(n, steps(n)) for n, _ in nodes if n[-1] == 'A'])

    f = open('cache.txt', 'w')
    f.write(str(cache_map))
    f.close()


print(cache_map)



i = 7273579
while True:
    p = 20656 + 20659*i + 3

    t = []
    for k in cache_map:
        go, r, start = cache_map[k]
        for g in go:
            if ((p - g - start) % r) == 0:
                t.append(k)
    if len(t) > 4:
        print(t, i)
    if len(t) > 5:
        print(t, p, t, i)
        break
                

    i += 1

#poss = [n for n, d in nodes if n[-1] == 'A']
#steps = 0
#while any([pos[-1] != 'Z' for pos in poss]):
#routes = [[(len(p), n) for p, n in cache_map[p]] for p in poss]
#print(routes)

#print(steps)
