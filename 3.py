from numpy import *
m = pad([[*f.strip()] for f in open("input.txt")], 1, constant_values='.')
s = ~char.isdigit(m) & (m != '.')
c = zeros(m.shape)
v = (m == '*').astype(int)
z = char.isdigit(m)
p = column_stack((column_stack(nonzero(~z[:, :-1] & z[:, 1:]))+1, column_stack(nonzero(z[:, :-1] & ~z[:, 1:]))+1))
r = 0

for sx, sy, ex, ey in p:
    n = int(''.join(m[sx-1:ex, sy:ey].flatten()))
    r += s[sx-2:ex+1,sy-1:ey+1].any()*n
    c[sx-2:ex+1,sy-1:ey+1][v[sx-2:ex+1,sy-1:ey+1] > 0] += 1
    v[sx-2:ex+1,sy-1:ey+1][v[sx-2:ex+1,sy-1:ey+1] > 0] *= n

print(r, v[c == 2].sum())
