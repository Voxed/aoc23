from math import *
eps = 0.001
abc = lambda a, b, c: [(-b + r*(b**2 - 4*a*c)**0.5) / 2*a for r in [-1, 1]] # roots([a,b,c]) in numpy
record_combinations = lambda p: floor((r := abc(-1, p[0], -p[1]-eps))[0]) - ceil(r[1]) + 1
inp = [l[10:].strip() for l in open('input.txt')]
print(
    prod(map(record_combinations, zip(*[map(int, l.split()) for l in inp]))), 
    record_combinations([int(l.replace(' ', '')) for l in inp])
)
