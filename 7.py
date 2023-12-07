from itertools import *
from functools import *

hand_value = lambda h: sum([10**v for v in dict((i, h.count(i)) for i in h).values()])
digit_value = lambda h, value_chart: reduce(lambda a, b: (a + value_chart.index(b)) << 4, h, 0)

def perm(hand, values):
    match hand:
        case []:
            return [[]]
        case ['J', *r]:
            return chain(*[[[b, *q] for b in values] for q in perm(r, values)])
        case [c, *r]:
            return [[c, *q] for q in perm(r, values)]

hands = [(list(a), int(b)) for a, b in [l.strip().split() for l in open('input.txt')]]

p1 = [(hand_value(h), digit_value(h, '23456789TJQKA'), p) for (h, p) in hands]

value_chart = 'J23456789TQKA'
p2 = [sorted([(hand_value(p), digit_value(hand, value_chart), points) for p in perm(hand, value_chart)])[-1] 
      for (hand, points) in hands]

print(*[sum([(i+1)*p for i, (_, _, p) in enumerate(sorted(hands))]) for hands in [p1, p2]])
