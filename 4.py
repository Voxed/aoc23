from numpy import *
c = ([[[int(m) for m in n.split(' ') if m.isnumeric()]
     for n in f.strip().split('|')] for f in open('input.txt')])
w, x = {}, range(0, len(c))
r, t = 0, 0
while len(x) > 0:
    t, y, x = t+len(x), x, []
    for i in y:
        if i not in w:
            w[i] = [*(indices(intersect1d(*c[i]).shape)+1+i).flatten()]
            r += floor(pow(2, len(w[i])-1))
        x += w[i]
print(r, t)
