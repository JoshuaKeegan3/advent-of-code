with open("4/sample.txt") as f:
    map = f.readlines()


removed = 0
finished = False
while not finished:
    rolls = 0
    mapcp = map.copy()
    for i in range(len(map)):
        for j in range(len(map[i])):
            count = 0
            if map[i][j] != "@":
                continue

            for m in range(-1, 2):
                for n in range(-1, 2):
                    if (
                        i + m < 0
                        or i + m >= len(map)
                        or j + n < 0
                        or j + n >= len(map[i])
                    ):
                        continue
                    if m == 0 and n == 0:
                        continue
                    if map[i + m][j + n] == "@":
                        count += 1
            if count < 4:
                rolls += 1
                mapcp[i] = mapcp[i][:j] + "x" + mapcp[i][j + 1 :]
    map = mapcp
    removed += rolls
    if rolls == 0:
        finished = True
    for x in map:
        x.replace("x", ".")

print(removed)
