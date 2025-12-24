with open("2/in.txt") as f:
    lines = f.readlines()

ranges = lines[0].split(",")
ans = 0
for r in ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])
    for id in range(start, end + 1):
        id_str = str(id)
        for incr in range(1, len(id_str) // 2 + 1):
            if len(id_str) % incr != 0:
                continue
            idx = 0
            while (idx + incr) < len(id_str) and id_str[idx : idx + incr] == id_str[
                idx + incr : idx + incr * 2
            ]:
                idx += incr
            if idx == len(id_str) - incr:
                ans += id
                break


print(ans)
