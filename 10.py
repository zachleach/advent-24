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


'''
    trailhead is a 0
    trailhead score is the number of 9's reachable from a trailhead
    path defined as 0, 1, 2, ..., 8, 9
    paths can only be up, down, left, right

'''

grid = []
while line := read_s():
    grid.append(line)

def oob(grid, y, x):
    return y < 0 or x < 0 or y == len(grid) or x == len(grid[0])

result = 0

'''
    you're trying to count the number of 9's reachable from a 0

'''

def dfs(grid, y, x, visited):
    count = 1 if grid[y][x] == '9' else 0
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        yy, xx = y + dy, x + dx
        if yy < 0 or xx < 0:
            continue
        if yy == len(grid) or xx == len(grid[0]):
            continue
        if grid[yy][xx] == '.':
            continue
        if (yy, xx) in visited:
            continue
        if int(grid[yy][xx]) != int(grid[y][x]) + 1:
            continue

        visited.add((yy, xx))
        count += dfs(grid, yy, xx, visited)

    return count



result = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == '0':
            result += dfs(grid, y, x, set())

print(result)


    




























































