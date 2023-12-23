from collections import *
from numpy import *
from scipy.sparse import *

m = pad([list(l.strip()) for l in open('input.txt') if l.strip()], ((1,1),(1,1)), constant_values='#')

r = m == '.'
s = 'v^><'
e = (m == '>') | (m == '<') | (m == '^') | (m == 'v')
spot = r & ((array(pad(e, ((1,0), (0,0)))[:-1, :], int) + 
            array(pad(e, ((0,1), (0,0)))[1:, :], int) + 
            array(pad(e, ((0,0), (1,0)))[:, :-1], int) + 
            array(pad(e, ((0,0), (0,1)))[:, 1:], int)) > 1)

for y, ro in enumerate(spot):
    for x, co in enumerate(ro):
        print('X', end='') if co else print(m[y,x], end='')
    print('')

edges = defaultdict(lambda: [])
int_edges = defaultdict(lambda: [])

been_there = set()

locations = [(array([2, 1]), (2,1), 0)]
new_loc = True
while new_loc:
    new_loc = False
    new_locations = []
    for l, prev_intersection, dist in locations:
        for i, d in enumerate(array([(0,1), (0,-1), (1, 0), (-1, 0)])):
            l2 = tuple((l + d).tolist())
            if r[l2[1], l2[0]] or m[l2[1], l2[0]] == s[i]:
                if tuple(l.tolist()) not in edges[l2]:
                    edges[tuple(l.tolist())].append(l2)

                    if spot[l2[1], l2[0]]:
                        int_edges[prev_intersection].append((dist + 1, (l2[0], l2[1])))
                        prev_intersection = (l2[0], l2[1])
                        dist = -1

                    if l2 not in been_there:
                        new_locations.append((l + d, prev_intersection, dist + 1))
                        new_loc = True
                        been_there.add(l2)
    locations = new_locations

print(int_edges)
int_edges_real = defaultdict(lambda: [])
for k in int_edges:
    for v in int_edges[k]:
        int_edges_real[k].append(v)
        int_edges_real[v[1]].append((v[0], k))

def dumb_search(visited = [], curr = (2, 1), end= (134,136), len = 0):
    if curr == end:
        return [len]
    visited = visited + [curr]
    dist = []
    for d, p in int_edges_real[curr]:
        if p not in visited:
            dist += dumb_search(visited, p, end, len + d)
    
    return dist


print(max(dumb_search()) + 31)