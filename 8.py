import math

sequence, nodes = [(s, dict([(n[:3], n[-9:-1].split(', ')) for n in n.split('\n')]))
                   for s, n in [open('input.txt').read().strip().split('\n\n')]][0]

def steps(pos):
    steps = 0
    while pos[-1] != 'Z':
        pos = nodes[pos][sequence[steps % len(sequence)] == 'R']
        steps += 1
    return steps

print(steps('AAA'), math.lcm(*[steps(n) for n in nodes if n[-1] == 'A']))
