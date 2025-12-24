with open("2/in.txt") as f:
    lines = f.readlines()

ranges = lines[0].split(",")
ans = 0
for r in ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])
    for id in range(start, end + 1):
        id_str = str(id)
        a = id_str[: len(id_str) // 2]
        b = id_str[len(id_str) // 2 :]
        if a == b:
            ans += id


print(ans)
