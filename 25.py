from networkx import *
from math import *

print(prod(map(len, community.greedy_modularity_communities(
    Graph(dict([(a, b.split()) for a, b in [l.strip().split(': ')
          for l in open('input.txt')]])),
    best_n=2))))
