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
    (q := full(v.shape, False))[sx-2:ex+1,sy-1:ey+1] = True
    r += s[q].any()*n
    c += 1 * (q & v > 0)
    v *= q*n + ~q*1

print(r, v[c == 2].sum())
