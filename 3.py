from numpy import *
map = [list(f.strip()) for f in open("input.txt")]
map2 = zeros((len(map), len(map[0])))+1
map3 = zeros((len(map), len(map[0])))
addto = []
print(map2)
sum = 0
sum2 = 0

def add_gear(x,y):
    print('add', x, y)

    map3[y][x] += 1
    addto.append((x,y))

for y, ys in enumerate(map):
    for x, xs in enumerate(ys):
        if xs.isdigit() and (x == 0 or not map[y][x-1].isdigit()):
            addto = []
            num = ""
            xc = x
            symbol = (x > 0 and map[y][x-1] != '.')
            symbol = symbol or (x > 0 and y > 0 and map[y-1][x-1] != '.') or (x > 0 and y < len(map)-1 and map[y+1][x-1] != '.')

            if (x > 0 and map[y][x-1] == '*'):
                add_gear(y,x-1) 
            if x > 0 and y > 0 and map[y-1][x-1] == '*':
                add_gear(y-1,x-1) 
            if (x > 0 and y < len(map)-1 and map[y+1][x-1] == '*'):
                add_gear(y+1,x-1) 

            while xc < len(map[0]) and map[y][xc].isdigit():
                num += map[y][xc]
                symbol = symbol or (y > 0 and map[y-1][xc] != '.') or (y < len(map)-1 and map[y+1][xc] != '.')

                if (y > 0 and map[y-1][xc] == '*'):
                    add_gear(y-1,xc) 
                if (y < len(map)-1 and map[y+1][xc] == '*'):
                    add_gear(y+1,xc) 

                xc += 1
            symbol = symbol or (xc < len(map[0]) and map[y][xc] != '.')
            symbol = symbol or (xc < len(map[0]) and y > 0 and map[y-1][xc] != '.') or (xc < len(map[0]) and y < len(map)-1 and map[y+1][xc] != '.')

            if (xc < len(map[0]) and map[y][xc] == '*'):
                add_gear(y,xc) 
            if (xc < len(map[0]) and y > 0 and map[y-1][xc] == '*'):
                add_gear(y-1,xc) 
            if (xc < len(map[0]) and y < len(map)-1 and map[y+1][xc] == '*'):
                add_gear(y+1,xc) 

            print(num)

            if symbol:
                sum += int(num)

            for (x2,y2) in addto:
                map2[y2][x2] *= int(num)



print((map2[map3 == 2]).sum())
print(sum)