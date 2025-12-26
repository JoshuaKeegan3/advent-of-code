with open("2025/9/in.txt") as f:
    _in = f.readlines()

largest = 0

pairs = list()
for i in range(len(_in)):
    a = list(map(int, _in[i].split(",")))
    for j in range(i + 1, len(_in)):
        b = list(map(int, _in[j].split(",")))
        pairs.append([a, b])

m = max(pairs, key=lambda x: abs(x[0][0] - x[1][0]) * abs(x[0][1] - x[1][1]))
print((1 + abs(m[0][0] - m[1][0])) * (1 + abs(m[0][1] - m[1][1])))
