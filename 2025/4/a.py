with open("4/in.txt") as f:
    map = f.readlines()

mapcp = map.copy()

rolls = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        count = 0

        if map[i][j] != "@":
            continue

        for m in range(-1, 2):
            for n in range(-1, 2):
                if i + m < 0 or i + m >= len(map) or j + n < 0 or j + n >= len(map[i]):
                    continue
                if m == 0 and n == 0:
                    continue
                if map[i + m][j + n] == "@":
                    count += 1
        if count < 4:
            rolls += 1
            mapcp[i] = mapcp[i][:j] + "x" + mapcp[i][j + 1 :]

print("\n".join(mapcp))
print(rolls)
