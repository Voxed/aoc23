from numpy import *
map = pad(array([[*f.strip()] for f in open("input.txt")]), 1, constant_values='.')
symbols = ~char.isdigit(map) & (map != '.')
gear_mask = map == '*'
gear_count = zeros(map.shape)
gear_val = gear_count + 1

z = char.isdigit(map)
p = column_stack((column_stack(nonzero(~z[1:, :-1] & z[1:, 1:]))+1, column_stack(nonzero(z[1:, :-1] & ~z[1:, 1:]))+1))
sum = 0
for sx, sy, ex, ey in p:
    n = int(''.join(map[sx:ex+1, sy:ey].flatten()))
    if symbols[sx-1:ex+2,sy-1:ey+1].any():
        sum += n
    gear_count[sx-1:ex+2,sy-1:ey+1][gear_mask[sx-1:ex+2,sy-1:ey+1]] += 1
    gear_val[sx-1:ex+2,sy-1:ey+1][gear_mask[sx-1:ex+2,sy-1:ey+1]] *= n

print(sum, gear_val[gear_count == 2].sum())
