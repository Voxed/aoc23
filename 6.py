from math import *
from numpy import *
print(
    prod([[abs(floor(r[0])-ceil(r[1])+1) for r in [roots([-1, o[0], -o[1]-0.001])]][0] for o in zip(*[map(int, l[10:].strip().split()) for l in open('input.txt')])]), 
    *[[abs(floor(r[0])-ceil(r[1])+1) for r in [roots([-1, o[0], -o[1]-0.001])]][0] for o in [[int(l[10:].replace(' ', '').strip()) for l in open('input.txt')]]]
)
