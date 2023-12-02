import numpy as n
from operator import itemgetter as z

v = n.array([list(dict([(ord(t), 0) for t in 'rgb'] + sorted([(ord(b[0]), int(a))
             for a, b in n.reshape(f.split()[2:], (-1, 2))], key=z(1))).values()) for f in open('inut.txt').readlines()])
print(sum(n.arange(len(v))[(v < (13, 14, 15)).all(1)]+1), sum(v.prod(1)))
