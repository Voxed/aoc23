from collections import *
from networkx import *
from matplotlib import pyplot as plt

G = Graph(dict([(a, b.split()) for a, b in [l.strip().split(': ') for l in open('input.txt')]]))

# I drew the graph :^)
G.remove_edge('sph', 'rkh')
G.remove_edge('hrs', 'mnf')
G.remove_edge('nnl', 'kpc')

for i, c in enumerate(connected_components(G)):
    print(f"SiZZe: {len(c)}")

