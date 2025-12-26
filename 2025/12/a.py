data = open("2025/12/in.txt").readlines()[30:]
P1 = 0
for line in data:
    str1, str2 = line.split(": ")
    L, H = map(int, str1.split("x"))
    available = L * H
    if available >= 9 * sum((list(map(int, str2.split(" "))))):
        P1 += 1
print(P1)
