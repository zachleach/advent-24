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


result = 0
for _ in range(1000):
	line = read_ints()

	# increasing
	if (line[0] - line[1] < 0):
		unsafe, flag = 0, 0
		for i in range(len(line) - 1):
			a, b = line[i], line[i + 1]
			if not (a - b < 0) or not (abs(a - b) < 4 and abs(a - b) > 0):
				if i + 2 >= len(line):
					unsafe = 1
				else:
					c = line[i + 2]
					if flag == 0 and not (a - c < 0) or not (abs(a - c) < 4 and abs(a - c) > 0):
						flag = 1
					else:
						unsafe = 1

		if not unsafe:
			result += 1

	# decreasing
	else:
		unsafe, flag = 0, 0
		for i in range(len(line) - 1):
			a, b = line[i], line[i + 1]
			if not (a - b > 0) or not (abs(a - b) < 4 and abs(a - b) > 0):
				if i + 2 >= len(line):
					unsafe = 1
				else:
					c = line[i + 2]
					if flag == 0 and not (a - c > 0) or not (abs(a - c) < 4 and abs(a - c) > 0):
						flag = 1
					else:
						unsafe = 1

		if not unsafe:
			result += 1

print(result)



