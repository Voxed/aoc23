workflow_raw, items_raw = open('input.txt').read().split('\n\n')
items =  [eval(it.replace('{', '{"').replace(',', ',"').replace('=', '":')) for it in items_raw.split('\n')] 
    
def split_range(xr, mr, ar, sr, cond):
    arg, val = cond.replace('<', '>').split('>')
    val = int(val)
    rxr, rmr, rar, rsr = xr, mr, ar, sr
    if '<' in cond:
        match arg:
            case 'x':
                xr = (xr[0], min(xr[1], val - 1))
                rxr = (max(rxr[0], val), rxr[1])
            case 'm':
                mr = (mr[0], min(mr[1], val - 1))
                rmr = (max(rmr[0], val), rmr[1])
            case 'a':
                ar = (ar[0], min(ar[1], val - 1))
                rar = (max(rar[0], val), rar[1])
            case 's':
                sr = (sr[0], min(sr[1], val - 1))
                rsr = (max(rsr[0], val), rsr[1])
    else:
        match arg:
            case 'x':
                rxr = (rxr[0], min(rxr[1], val))
                xr = (max(xr[0], val+1), xr[1])
            case 'm':
                rmr = (rmr[0], min(rmr[1], val))
                mr = (max(mr[0], val+1), mr[1])
            case 'a':
                rar = (rar[0], min(rar[1], val))
                ar = (max(ar[0], val+1), ar[1])
            case 's':
                rsr = (rsr[0], min(rsr[1], val))
                sr = (max(sr[0], val+1), sr[1])
    return (xr, mr, ar, sr), (rxr, rmr, rar, rsr)

workflow = {}

for r in workflow_raw.split('\n'):
    name, rules = r[:-1].split('{')
    if name not in workflow:
        workflow[name] = []
    for f in rules.split(',')[:-1]:
        workflow[name].append(f.split(':'))
    workflow[name].append(['x>-1', rules.split(',')[-1]])

accepted_ranges = []
queue = [('in', ((1, 4000), (1, 4000), (1, 4000), (1, 4000)))]
for w, r in queue:
    for c in workflow[w]:
        nr, r = split_range(*r, c[0])
        if c[1] == 'A':
            accepted_ranges += [nr]
        elif c[1] != 'R':
            queue += [(c[1], nr)]

sum1 = 0
for i in items:
    x, m, a, s = i['x'], i['m'], i['a'], i['s']
    for xr, mr, ar, sr in accepted_ranges:
        if x >= xr[0] and x <= xr[1] and m >= mr[0] and m <= mr[1] and a >= ar[0] and a <= ar[1] and s >= sr[0] and s <= sr[1]:
            sum1 += x + m + a + s
            break

sum2 = 0
for xr, mr, ar ,sr in accepted_ranges:
    sum2 += (xr[1] - xr[0] + 1)*(mr[1] - mr[0] + 1)*(ar[1] - ar[0] + 1)*(sr[1] - sr[0] + 1)

print(sum1, sum2)