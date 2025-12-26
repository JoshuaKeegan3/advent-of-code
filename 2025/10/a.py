with open("2025/10/in.txt") as f:
    _in = f.readlines()


def string_to_list(s):
    s = s.replace("(", "")
    s = s.replace(")", "")
    return list(map(int, s.split(",")))


machines = []
ans = 0
for line in _in:
    line = line.strip().split(" ")
    target_config = list(map(lambda x: x == "#", list(line[0])))[1:-1]
    joltage_requirements = line[-1]
    buttons = list(map(string_to_list, line[1:-1]))

    initial_configuration = [False for b in target_config]
    # ideally this would be a set with a good hash function for the list
    visited_state = [initial_configuration]
    queue = [(initial_configuration, 0)]

    found = False
    while queue and not found:
        config, i = queue.pop(0)
        for button in buttons:
            c = config.copy()
            for light in button:
                c[light] = not c[light]
            if c not in visited_state:
                visited_state.append(c)
                queue.append((c, i + 1))

            if c == target_config:
                ans += i + 1
                found = True
                break

print(ans)
