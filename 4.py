from numpy import *
from itertools import *
from functools import *
p = enumerate([[set([int(m) for m in n.split()]) for n in f.strip().split(':')[1].split('|')] for f in open('input.txt')])
c = array([*zip_longest(*[[0]*(i+1) + [1]*len(a & b) for i, (a, b) in p], fillvalue=0)])
print((1 << c.sum(0)-1).sum(), reduce(lambda a, _: vstack([a, dot(c, a[-1])]), c, [[1]*len(c)]).sum())
