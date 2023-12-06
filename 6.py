from math import *
from numpy import *
record_combinations = lambda p: abs(floor((r := roots([-1, p[0], -p[1]-0.001]))[0]) - ceil(r[1]) + 1)
print(
    prod([*map(record_combinations, zip(*[map(int, l[10:].strip().split()) for l in open('input.txt')]))]), 
    *map(record_combinations, [[int(l[10:].replace(' ', '').strip()) for l in open('input.txt')]])
)
