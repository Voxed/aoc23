from numpy import *
f, g = column_stack, nonzero
m = pad([[*f.strip()] for f in open("input.txt")], 1, constant_values='.')
z = char.isdigit(m)
t = roll(z, 1, 1)
v, o, x, e, d = ~z & (m != '.'), f((f(g(z & ~t)), f(g(~z & t)))), zeros(m.shape), array(m == '*', int), 0
for h, j, k, l in o:
    n = int(''.join(m[h:k+1, j:l].flatten()))
    (q := full(e.shape, False))[h-1:k+2, j-1:l+1] = True
    d += v[q].any()*n
    x += q*e > 0
    e *= q*n+~q
print(d, e[x == 2].sum())
