from numpy import *
v = array([list(dict([(ord(t), 0) for t in 'rgb'] + sorted([(ord(b[0]), int(a))
             for a, b in reshape(f.split()[2:], (-1, 2))], key=sum)).values()) for f in open('input.txt').readlines()])
print(sum(arange(len(v))[(v-13 < range(3)).all(1)]+1), sum(v.prod(1)))
                              