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

list1, list2 = [], []
for i in range(1000):
    a, b = read_ints()
    list1 += [a]
    list2 += [b]

from collections import Counter
counts = Counter(list2)

score = 0
for x in list1:
    score += (x * counts[x])

print(score)


