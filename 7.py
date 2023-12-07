from itertools import *
from functools import *

def hand_value(h):
    return sum([10**v for v in dict((i, h.count(i)) for i in h).values()])

def digit_value(h):
    return reduce(lambda a, b: (a + VALUE_CHART.index(b)) << 4, list(h), 0)

def perm(hand):
    match list(hand):
        case []:
            return [[]]
        case ['J', *_]:
            return chain(*[[[b, *q] for b in VALUE_CHART] for q in perm(hand[1:])])
        case [c, *_]:
            return [[c, *q] for q in perm(hand[1:])]

VALUE_CHART = ['2', '3', '4', '5', '6',
               '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

hands = [l.strip().split() for l in open('input.txt')]

sorted_hands_p1 = [(hand_value(hand), digit_value(hand), int(points))
                   for (hand, points) in hands]

VALUE_CHART = ['J', '2', '3', '4', '5', '6',
               '7', '8', '9', 'T', 'Q', 'K', 'A']

sorted_hands_p2 = [sorted([(hand_value(p), digit_value(hand), int(points))
                           for p in perm(hand)])[-1] for (hand, points) in hands]

print(sum([(i+1)*p for i, (_, _, p) in enumerate(sorted(sorted_hands_p1))]),
      sum([(i+1)*p for i, (_, _, p) in enumerate(sorted(sorted_hands_p2))]))
