from sympy import *
from numpy import *
from itertools import *
from sympy.abc import s, t, u, v, w, x, y, z, h, j, k

l = array([l.strip().replace(' @ ', ' , ').split(', ')
          for l in open('input.txt')], int)

# Part 1
a1 = 0
for l1, l2 in combinations(l, 2):
    try:
        r = linalg.solve(array([l1[3:5], -l2[3:5]]).T, l2[:2] - l1[:2])
        i = l1[:2] + l1[3:5]*r[0]
        a1 += (r[0] >= 0 <= r[1]) * all((i >= 2*10**14) & (i <= 4*10**14))
    except linalg.LinAlgError:
        pass

# Part 2
a2 = sum(solve(
    (l[:, :3][:5] - [x, y, z] +
     array([[s, t, u, v, w]]).T * (l[:, 3:][:5] - [h, j, k])
     ).flatten(), (s, t, u, v, w, h, j, k, x, y, z))[0][-3:])

print(a1, a2)
