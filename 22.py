from numpy import *
from itertools import *
import plotly.graph_objects as go

coords = array([l.strip().replace('~',',').split(',') for l in open('input.txt')], int)
bricks = [(vstack([*map(ravel, mgrid[x0:x1+1, y0:y1+1, z0:z1+1])])).transpose() for x0, y0, z0, x1, y1, z1 in coords]

new_bricks = bricks.copy()
moved = True
while moved:
    occupied = set(map(tuple, array([*chain(*new_bricks)]).tolist()))
    moved = False
    next_bricks = []

    for b in new_bricks:        
        if all(b[:, 2] > 1):
            new_brick = b - [0, 0, 1]
            move = True
            for c in new_brick:
                if tuple(c.tolist()) in occupied and c.tolist() not in b.tolist():
                    move = False
                    break
            if move:
                next_bricks.append(new_brick)
                moved = True
                continue
        next_bricks.append(b)
    new_bricks = next_bricks

pos_registry = {}
for i, b in enumerate(new_bricks):
    for c in b:
        pos_registry[tuple(c.tolist())] = (b, i)

s = 0
supported_by = {}
supporting = {}
for i, b in enumerate(new_bricks):
    good = False
    if i not in supporting:
        supporting[i] = set()
    if i not in supported_by:
        supported_by[i] = set()
    for c in (b + [0, 0, 1]):
        if tuple(c) in pos_registry:
            if c.tolist() not in b.tolist():
                falling, falling_idx = pos_registry[tuple(c)]
                supporting[i].add(falling_idx)
                if falling_idx not in supported_by:
                    supported_by[falling_idx] = set()
                supported_by[falling_idx].add(i)
                for c2 in falling - [0,0,1]:
                    if c2.tolist() not in falling.tolist() and c2.tolist() not in b.tolist() and tuple(c2) in pos_registry:
                        break
                else:
                    good = True
    if not good:
        s += 1

s2 = 0
colors = []
max_col = 0
for i, b in enumerate(new_bricks):
    more_falling = True
    currently_falling = set([i])
    while more_falling:
        more_falling = False
        for i in currently_falling.copy():
            for falling in supporting[i] - currently_falling:
                if len(currently_falling & supported_by[falling]) == len(supported_by[falling]):
                    currently_falling.add(falling)
                    more_falling = True
    s2 += len(currently_falling) - 1
    colors += [len(currently_falling) - 1]
    max_col = max(max_col, len(currently_falling) - 1)

print(s, s2)

# Warning this opens a browser window which lags alot on the big input :)
if False:
    def cubes(size, pos_x, pos_y, pos_z, color):
        x, y, z = meshgrid(
            linspace(pos_x-size/2, pos_x+size/2, 2), 
            linspace(pos_y-size/2, pos_y+size/2, 2), 
            linspace(pos_z-size/2, pos_z+size/2, 2),
        )
        x = x.flatten()
        y = y.flatten()
        z = z.flatten()
        xl = 350
        yl = 1000
        zl = 1000
        return go.Mesh3d(x=x, y=y, z=z, alphahull=1, flatshading=True, color=color, lighting={'diffuse': 1.0, 'ambient': 0.25, 'specular': 0, 'roughness': 1}, lightposition=dict(x=xl, y=yl, z=zl))

    fig = go.Figure()
    for i, b in enumerate(new_bricks):
        for c in b:
            fig.add_trace(cubes(1,c[0],c[1],c[2], f"rgba(250,{max(0, int(250-colors[i]/max_col*250.0))},{max(0, int(250-colors[i]/max_col*250.0))},1.0)"))
    fig.update_layout(scene_aspectmode='data')
    fig.show()