from re import findall as a
from operator import itemgetter as b

c = 'one|two|three|four|five|six|seven|eight|nine'
print(sum([int(''.join([x if x.isdigit() else str(c.split('|').index(x)+1) for x in b(0,-1)(a(f"(?=([1-9]|{c}))", l))])) for l in open('input.txt').readlines()]))