import re

def to_num(letters):
    if letters.isdigit():
        return letters
    return str({'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}[letters])

sum = 0
for line in open('input.txt').readlines():
    matches = re.findall('(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))', line)
    sum += int(str(to_num(matches[0])) + str(to_num(matches[-1])))
