from collections import *


def hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v


sequences = open('input.txt').read().replace('\n', '').split(',')
boxes = defaultdict(lambda: {})

for s in sequences:
    h = s.split('=')[0].split('-')[0]
    v = hash(h)
    if '=' in s:
        boxes[v][h] = int(s.split('=')[1])
    elif h in boxes[v]:
        del boxes[v][h]

print(sum(map(hash, sequences)),
      sum([sum([(b+1)*(i+1)*boxes[b][s] for i, s in enumerate(boxes[b])]) for b in boxes]))
