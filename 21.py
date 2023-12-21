from numpy import *
from matplotlib import pyplot as plt

m = array([list(l.strip()) for l in open('input.txt') if l.strip()])

m = hstack((m, m, m, m, m, m, m, m, m))
m = vstack((m, m, m, m, m, m, m, m, m))

s = (m.shape[0]//2, m.shape[1]//2) #argwhere(m == 'S')[0]

state = zeros(m.shape, dtype=bool)
state[s[0], s[1]] = True

#
#    ^
#   <X>
#    v
#
#    ^
#   /X\
#  <XOX>
#   \X/
#    v
#
# O = 7651
# X = 7699
#
# spikes = 34700 - X = 27001
#
# diagonals = 96215 - spikes - X*4 - O = 30767
#
#
#    ^
#   /X\
#  /XOX\
# <XOXOX>
#  \XOX/
#   \X/
#    V
#
# O*4 + X*9 + diagonals*2 + spikes = 
#
#     ^
#    /X\
#   /XOX\
#  /XOXOX\
# <XOXOXOX>
#  \XOXOX/
#   \XOX/
#    \X/
#     V
#
#
# (26501365 - 65)/131 = 202300
# 
# 202300 is even so center is O amount of O:
#    1 + 8 + 16 + 24 + 32...
#    num_x = ((x+1)/4)*(((x+1)/2-1)*8)+1 = 40925290000
#    num_o = (x/4)*((x/2-1)*8)+1         = 40924885401
#
# outer layer increases by 4 diagonals each step > 1 so "diagonals*4*(202300-1) + spikes"
#
# 40925290000 * 7699 + 40924885401 * 7651 + 27001 + 202299 * 30767
#
#
# 16*O + 11*X + diagonals*4*(4-1) + spikes = 

print(40925290000 * 7699 + 40924885401 * 7651 + 27001 + 202299 * 30767)

for i in range(65 + 131*4):
    d = pad(state, ((0,1),(0,0)))[1:]
    u = pad(state, ((1,0),(0,0)))[:-1]
    l = pad(state, ((0,0),(1,0)))[:,:-1]
    r = pad(state, ((0,0),(0,1)))[:,1:]
    adj = d | u | l | r
    state = (m != '#') & adj

print(state.sum())

print(state[131*4:131*5, 131*4:131*5].sum())