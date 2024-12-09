import sys
getline = sys.stdin.readline
 
def read_int():
    return int(getline())
 
def read_ints():
    return list(map(int, getline().split()))
 
def read_s():
    return str(getline().strip())
 
def read_ss():
    return list(map(str, getline().strip().split()))

file = open('3.txt', 'r')
getline = file.readline

import re

result = 0
line = read_s()

i, a, n = 0, 0, len(line)
valid = []
while -1 < i < n:
    a = line.find("don't()", i)
    if a == -1:
        valid += [line[i:n]]
        break
    valid += [line[i:a]]
    i = line.find("do()", a)

for s in valid:
    matches = re.findall(r"mul\((\d+),(\d+)\)", s)
    result += sum([int(x) * int(y) for x, y in matches])

print(result)





























































