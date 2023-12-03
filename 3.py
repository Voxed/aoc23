from numpy import *
m = pad([[*f.strip()] for f in open("input.txt")], 1, constant_values='.')
s = ~char.isdigit(m) & (m != '.')
c = zeros(m.shape)
v = (m == '*').astype(int)
z = char.isdigit(m)
p = column_stack((column_stack(nonzero(z & ~(t := roll(z, 1, 1)))), column_stack(nonzero(~z & t))))
r = 0

for h, j, k, l in p:
    n = int(''.join(m[h:k+1, j:l].flatten()))
    (q := full(v.shape, False))[h-1:k+2,j-1:l+1] = True
    r += s[q].any()*n
    c += 1 * (q & v > 0)
    v *= q*n + ~q*1


print(r, v[c == 2].sum())
