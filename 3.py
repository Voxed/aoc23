from numpy import *
m = pad([[*f.strip()] for f in open("input.txt")], 1, constant_values='.')
v, o, x, e, d = ~(z := char.isdigit(m)) & (m != '.'), (w := column_stack)((w((g := nonzero)(z & ~(
    t := roll(z, 1, 1)))), w(g(~z & t)))), zeros(m.shape), array(m == '*', int), 0
for h, j, k, l in o:
    n = int(''.join(m[h:k+1, j:l].flatten()))
    (q := full(e.shape, False))[h-1:k+2, j-1:l+1] = True
    d += v[q].any()*n
    x += 1 * (q & e > 0)
    e *= q*n + ~q*1
print(d, e[x == 2].sum())
