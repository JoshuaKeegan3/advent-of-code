# this is the same as a.py
# except we need to not use true and false
# This is because instead of the light being on or off, we need to get to a desired number of button presses
# To do this we can "Trim" the odd parity numbers from the desired configuration using the parity rules discovered in P1
# Then we half then repeat the puzzle

import itertools
from collections import defaultdict

with open("2025/10/in.txt") as f:
    _in = f.readlines()


def string_to_list(s):
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace("{", "")
    s = s.replace("}", "")
    return list(map(int, s.split(",")))


ans = 0
for p, line in enumerate(_in):
    line = line.strip().split(" ")
    combinations = defaultdict(dict)

    target_state = string_to_list(line[-1])
    buttons = list(map(string_to_list, line[1:-1]))

    for n_comb in range(len(buttons) + 1):
        for comb in itertools.combinations(buttons, n_comb):
            state = [0 for _ in target_state]
            for button in comb:
                for light in button:
                    state[light] += 1

            parity = [i % 2 for i in state]
            parity = sum((2**i) * x for i, x in enumerate(parity))

            state_tuple = tuple(state)
            cost = len(comb)

            if (
                state_tuple not in combinations[parity]
                or cost < combinations[parity][state_tuple]
            ):
                combinations[parity][state_tuple] = cost

    q = [[target_state, 0, 0]]  # [state, depth, accumulated_cost]

    visited = {tuple(target_state): 0}
    solution = 100000000

    while q:
        current_state, depth, cost = q.pop(0)

        if sum(current_state) == 0:
            solution = min(solution, cost)
            continue

        if cost >= solution:
            continue

        parity = [i % 2 for i in current_state]
        parity = sum((2**i) * x for i, x in enumerate(parity))

        for comb, length in combinations[parity].items():
            state_zip = list(zip(current_state, comb))

            if all([target >= curr for target, curr in state_zip]):
                output = [(target - curr) // 2 for target, curr in state_zip]

                new_cost = cost + length * (2**depth)

                output_tuple = tuple(output)
                if output_tuple not in visited or new_cost < visited[output_tuple]:
                    visited[output_tuple] = new_cost
                    q.append([output, depth + 1, new_cost])

    # Print(p, solution)
    ans += solution
print(ans)
