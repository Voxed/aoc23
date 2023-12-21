from numpy import *

m = array([list(l.strip()) for l in open('input.txt') if l.strip()])

# For deducing values in part 2
#
# m = hstack((m, m, m, m, m, m, m, m, m))
# m = vstack((m, m, m, m, m, m, m, m, m))

# Part 1:
s = (m.shape[0]//2, m.shape[1]//2)

state = zeros(m.shape, dtype=bool)
state[s[0], s[1]] = True

for i in range(64):
    d = pad(state, ((0,1),(0,0)))[1:]
    u = pad(state, ((1,0),(0,0)))[:-1]
    l = pad(state, ((0,0),(1,0)))[:,:-1]
    r = pad(state, ((0,0),(0,1)))[:,1:]
    adj = d | u | l | r
    state = (m != '#') & adj

# Part 2:
#
# Deductions:
#
#   O = 7651
#   X = 7699 
#
#    ^
#   <X> = 34700
#    v
#
#     ^
#    /X\
#   <XOX> = 96215
#    \X/
#     v
# 
# Calculations:
#
#   spikes = 34700 - X = 27001                     # Sum of the four tips
#   diagonals = 96215 - spikes - X*4 - O = 30767   # Sum of 4 diagonals on each side, this is the delta in the outer layer between each radia increase
#
#   radia = (26501365 - 65)/131 = 202300
#   num_x = ((radia+1)/4)*(((radia+1)/2-1)*8)+1 = 40925290000   # Arthimetic sequence
#   num_o = (radia/4)*((radia/2-1)*8)+1         = 40924885401   # Arthimetic sequence
#   outer_layer = diagonals*(radia-1) + spikes
#
#   ANSWER = num_x * X + num_o * O + outer_layer = 40925290000 * 7699 + 40924885401 * 7651 + 202299 * 30767 + 27001
#
print(state.sum(), 40925290000 * 7699 + 40924885401 * 7651 + 202299 * 30767 + 27001) # Part 2