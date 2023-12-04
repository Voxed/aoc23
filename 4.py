from numpy import *
from itertools import *
from functools import *

c = array(list(zip_longest(*[[0]*(i+1) + [1]*len(a & b) for i, (a, b) in enumerate([[set([int(m)
          for m in n.split() if m.isnumeric()]) for n in f.strip().split('|')] for f in open('input.txt')])], fillvalue=0)))
print((1 << c.sum(0)-1).sum(), reduce(lambda a,
      b: vstack([a, c.dot(a[-1])]), range(len(c)), [[1]*len(c)]).sum())
