from numpy import *
m = pad([[*f.strip()] for f in open("input.txt")], 1, constant_values='.')
s = ~char.isdigit(m) & (m != '.')
c = zeros(m.shape)
v = (m == '*').astype(int)
z = char.isdigit(m)
p = column_stack((column_stack(nonzero(~z[1:, :-1] & z[1:, 1:]))+1, column_stack(nonzero(z[1:, :-1] & ~z[1:, 1:]))+1))

sum = 0
for sx, sy, ex, ey in p:
    n = int(''.join(m[sx:ex+1, sy:ey].flatten()))
    sum += s[sx-1:ex+2,sy-1:ey+1].any()*n
    c[sx-1:ex+2,sy-1:ey+1][v[sx-1:ex+2,sy-1:ey+1] > 0] += 1
    v[sx-1:ex+2,sy-1:ey+1][v[sx-1:ex+2,sy-1:ey+1] > 0] *= n

print(sum, v[c == 2].sum())
