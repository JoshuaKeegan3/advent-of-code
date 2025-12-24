import numpy as np

with open("6/in.txt") as f:
    _in = f.readlines()

line_operations = []
for line in _in:
    line = line.strip().split()
    line_operations.append(line)


line_operations = np.transpose(line_operations)
ans = 0
for line in line_operations:
    op = line[-1]
    line = line[:-1]

    print(line)
    line = list(map(int, line))

    s = 0
    if op == "*":
        s = 1
        for i in line:
            s *= i

    elif op == "+":
        for i in line:
            s += i
    ans += s
print(ans)
