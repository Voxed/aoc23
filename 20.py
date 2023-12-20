from numpy import *
from math import *

# Cool network class
class Network:
    def __init__(self, conn_matrix, types, num_nodes):
        self.conn_matrix = conn_matrix
        self.types = types
        self.pulses = []
        self.broadcaster = where(types == 0)[0][0]
        self.num_nodes = num_nodes

        self.reset()

    def reset(self):
        self.states = zeros(self.num_nodes, dtype=bool)
        self.pulses = []

    def push_button(self):
        self.pulses += [(self.broadcaster, False)]

    def process_pulse(self):
        if not self.pulses:
            return None
        d, p = self.pulses.pop(0)
        match self.types[d]:
            case 0:  # Broadcaster
                self.pulses += [(nd, False)
                                for nd in where(self.conn_matrix[d])[0]]
                self.states[d] = False
            case 1:  # Flip-flop
                if not p:
                    self.states[d] = not self.states[d]
                    self.pulses += [(nd, self.states[d])
                                    for nd in where(self.conn_matrix[d])[0]]
            case 2:  # Conjunction
                if all(self.states[self.conn_matrix[:, d]]):
                    self.pulses += [(nd, False)
                                    for nd in where(self.conn_matrix[d])[0]]
                    self.states[d] = False
                else:
                    self.pulses += [(nd, True)
                                    for nd in where(self.conn_matrix[d])[0]]
                    self.states[d] = True
        return (d, p)

    def get_state(self, node):
        return self.states[node]

    def get_parents(self, node):
        return where(conn_matrix[:, node])[0]

# Parse input and create network
next_uid = 0
uid_mapping = {}

def uid(name):
    global next_uid
    if not name in uid_mapping:
        uid_mapping[name] = next_uid
        next_uid += 1
    return uid_mapping[name]

nodes = dict([
    (uid(name[1:] if name[0] == '%' or name[0] == '&' else name),
     (0 if name[0] == 'b' else (1 if name[0] == '%' else 2), list(map(uid, nodes.split(', ')))))
    for name, nodes in [l.strip().split(' -> ') for l in open('input.txt')]])

conn_matrix = zeros((next_uid, next_uid), dtype=bool)
types = zeros(next_uid)+3
for n in nodes:
    types[n] = nodes[n][0]
    if types[n] != 3:
        for conn in nodes[n][1]:
            conn_matrix[n][conn] = True

network = Network(conn_matrix, types, next_uid)

# Part 1
num_low_pulses = 0
num_high_pulses = 0

for i in range(1000):
    network.push_button()
    while (p := network.process_pulse()) is not None:
        num_low_pulses += not p[1]
        num_high_pulses += p[1]

# Part 2 utility
def get_until_high(query):
    network.reset()
    presses = 0
    while True:
        presses += 1
        network.push_button()
        while network.process_pulse() is not None:
            if network.get_state(query):
                return presses

# Answers
print(
    num_high_pulses * num_low_pulses,
    # This is insanely stupid... And it works!
    lcm(*map(get_until_high, network.get_parents(network.get_parents(uid('rx'))[0])))
)
