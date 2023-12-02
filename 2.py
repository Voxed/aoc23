import numpy as np
from operator import itemgetter as z

v = np.array([list(dict([(ord(t), 0) for t in 'rgb'] + sorted([(ord(b[0]), int(a))
             for a, b in np.reshape(f.split()[2:], (-1, 2))], key=z(1))).values()) for f in open('input.txt').readlines()])
print(sum(np.arange(len(v))[(v < (13, 14, 15)).all(1)]+1), sum(v.prod(1)))
