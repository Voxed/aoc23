from numpy import *
dish = array([list(r.strip()) for r in open('input.txt').readlines()])
rocks = dish == 'O'
blocks = dish == '#'

prevcycles = []
cyc = 0
skipped = False
while cyc < 1000000000:
    if not skipped:
        for i, c in enumerate(prevcycles):
            if (rocks == c).all():
                a = 1000000000 - cyc
                n = a // (cyc - i)
                cyc = cyc + (cyc - i)*n
                skipped = True
        prevcycles.append(rocks)
    for r1, r2 in [((1, 0), (0,0)), 
                    ((0,0), (1, 0)), 
                    ((0, 1), (0, 0)), 
                    ((0, 0), (0, 1))]:
        prevrocks = zeros(rocks.shape)
        while (prevrocks != rocks).any():
            prevrocks = rocks
            blocked = (pad(blocks | rocks, (r1, r2), constant_values=True) & pad(rocks, (r1[::-1], r2[::-1]), constant_values=True))
            blocked = blocked[r1[1]:blocked.shape[0] - r1[0]]
            blocked = blocked[:, r2[1]:blocked.shape[1] - r2[0]]
            rocks = (pad(blocked, (r1, r2), constant_values=True) | pad(rocks & ~blocked, (r1[::-1], r2[::-1]), constant_values=False))
            rocks = rocks[r1[0]:rocks.shape[0] - r1[1]]
            rocks = rocks[:, r2[0]:rocks.shape[1] - r2[1]]
    cyc += 1

s = 0
for i, r in enumerate(rocks):
    s += r.sum()*(dish.shape[0]-i)

print(s)