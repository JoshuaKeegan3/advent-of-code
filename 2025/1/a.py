# modulo
cs = [0 for i in range(100)]
cs[50] += 1
with open("1/in.txt") as f:
    ls = f.readlines()
    n = 50
    for l in ls:
        a = int(l[1::])
        if l[0] == "L":
            n -= a
        else:
            n += a
        n %= 100
        cs[n] += 1
        print(n)
print("ans:\n", max(cs))
