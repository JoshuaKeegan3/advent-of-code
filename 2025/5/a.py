with open("5/in.txt") as f:
    _in = f.readlines()

ranges = []
ids = []
setting = "ranges"
fresh = 0
for line in _in:
    if line == "\n":
        setting = "ids"
        continue

    if setting == "ranges":
        ranges.append(list(map(int, line.strip().split("-"))))

    if setting == "ids":
        for range in ranges:
            if range[0] <= int(line) and range[1] >= int(line):
                fresh += 1
                break

print(fresh)
