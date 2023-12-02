from numpy import *
v = array([[*dict([*ndindex(3, 1), *sorted([(ord(b[0]) % 3, int(a)) for a, b in reshape(f.split()[2:], (-1, 2))])]).values()] for f in open('input.txt')])
print(sum(argwhere((v-13 < range(3)).all(1))+1), sum(v.prod(1)))
