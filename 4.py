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

grid = []
while line := read_s():
    grid += [line]

def solve_1():
    def check(grid, start, d):
        y, x = start[0], start[1]
        string = "XMAS"
        for i in range(4):
            yy, xx = y + (i * d[0]), x + (i * d[1])
            if yy < 0 or xx < 0 or yy == len(grid) or xx == len(grid[0]):
                return False
            if grid[yy][xx] != string[i]:
                return False

        return True

    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                result += check(grid, (y, x), d)

    print(result)


def solve_2():
    def oob(grid, s):
        return s[0] < 0 or s[1] < 0 or s[0] == len(grid) or s[1] == len(grid[0])

    def diag_1(grid, s):
        a = s[0] - 1, s[1] - 1
        b = s[0] + 1, s[1] + 1

        if oob(grid, a) or oob(grid, b):
            return False
        if grid[a[0]][a[1]] == 'M' and grid[b[0]][b[1]] == 'S':
            return True
        if grid[a[0]][a[1]] == 'S' and grid[b[0]][b[1]] == 'M':
            return True
        
        print(s, a, b)
        return False

    def diag_2(grid, s):
        a = s[0] - 1, s[1] + 1
        b = s[0] + 1, s[1] - 1

        if oob(grid, a) or oob(grid, b):
            return False
        if grid[a[0]][a[1]] == 'M' and grid[b[0]][b[1]] == 'S':
            return True
        if grid[a[0]][a[1]] == 'S' and grid[b[0]][b[1]] == 'M':
            return True
        
        print(s, a, b)
        return False

    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'A':
                result += (diag_1(grid, (y, x)) and diag_2(grid, (y, x)))

    print(result)







































































