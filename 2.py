import numpy as np
from operator import itemgetter as z

v = np.array([list(dict([(ord(t), 0) for t in 'rgb'] + sorted([(ord(b[0]), int(a))
             for a, b in np.reshape(f.split()[2:], (-1, 2))], key=z(1))).values()) for f in open('input.txt').readlines()])
print(sum(np.arange(1, len(v)+1)[(v <= (12, 13, 14)).all(axis=1)]))
print(sum(v.prod(axis=1)))
