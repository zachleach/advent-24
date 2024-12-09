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

line = read_s()
import pprint

def solve_1():
    arr = []
    cap = len(line) // 2
    for i in range(cap):
        idx = i * 2
        for _ in range(int(line[idx])):
            arr += [str(i)]
        for _ in range(int(line[idx + 1])):
            arr += '.'
    for _ in range(int(line[-1])):
        arr += [str(cap)]

    def find(val, arr, start):
        for i in range(start, len(arr)):
            if arr[i] == val:
                return i
        return -1

    l, r = 0, len(arr) - 1
    while True:
        l = find('.', arr, l)
        if not (l < r):
            break
        arr[l], arr[r] = arr[r], '.'
        r -= 1

    checksum = 0 
    for i in range(r):
        checksum += int(arr[i]) * i
    print(checksum)


solve_1()


































































