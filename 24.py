from numpy import *

from numpy import *
from itertools import *

lines = array([[m.split(', ') for m in l.strip().split(' @ ')]
              for l in open('input.txt')], int)

answer_1 = 0

for l1, l2 in combinations(lines, 2):
    try:
        s, t = linalg.solve(
            array([l1[1][:-1], -l2[1][:-1]]).T, l2[0][:-1] - l1[0][:-1])
        x, y, z = l1[0] + l1[1]*s
        if s >= 0 and t >= 0:
            b = (200000000000000.0, 400000000000000.0)
            if b[0] <= x <= b[1] and b[0] <= y <= b[1]:
                answer_1 += 1
    except linalg.LinAlgError:
        pass

# I can't do it myself :(
from sympy.abc import s, t, u, v, w, x, y, z, h, j, k
from sympy import *

l = array([l.strip().replace(' @ ', ' , ').split(', ')
          for l in open('input.txt')], int)

answer_2 = sum(solve(
    (l[:, :3][:5] - array([x, y, z]) +
     array([[s, t, u, v, w]]).T * (l[:, 3:][:5] - array([h, j, k]))
     ).flatten(), (s, t, u, v, w, h, j, k, x, y, z))[0][-3:])

print(answer_1, answer_2)
