from scipy.sparse import *
from numpy import *

m = [array(list(l.strip()), int) for l in open('input.txt')]
num_nodes = len(m[0]) * len(m) * 2


def shortest(minimum, maximum):
    indices = []
    data = []
    indptr = [0]

    for y, x in argwhere(m):
        for r in [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]:
            for d in r:
                c = 0
                for i in range(1, maximum+1):
                    if 0 <= x + d[0]*i < len(m[0]) and 0 <= y + d[1]*i < len(m[0]):
                        c += m[y+d[1]*i][x+d[0]*i]
                        if i >= minimum:
                            indices.append(
                                abs(d[1]) + (x + d[0]*i) * 2 + (y + d[1]*i) * 2 * len(m[0]))
                            data.append(c)
            indptr.append(len(indices))

    return min(csgraph.dijkstra(csr_matrix((data + [0, 0], indices + [0, 1], indptr +
                                            [len(indices) + 2]), (num_nodes + 1, num_nodes + 1)),
                                True, num_nodes)[-3:-1])


print(shortest(1, 3), shortest(4, 10))
