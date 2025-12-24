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

    line = list(map(int, line))

    # get the lengths of items in a line
    ls = []
    for i in line:
        ls.append(len(str(i)))

    # zip and sort by length
    z = list(zip(ls, line))

    # get max len
    ml = max(z)[0]

    base_n = 1 if op == "*" else 0

    for l in range(0, ml, 1):
        n = ""
        if op == "*":
            for i in z:
                if ml - l <= i[0]:
                    n += str(i[1])[-ml + l + i[0]]
            if n == "":
                continue
            base_n *= int(n)
        elif op == "+":
            for i in z:
                if l < i[0]:
                    n += str(i[1])[l]
            if n == "":
                continue
            print(n)
            base_n += int(n)

    ans += base_n
print(ans)  # < 6028582941185
