with open("5/in.txt") as f:
    _in = f.readlines()

ranges = []
for line in _in:
    if line == "\n":
        break
    ranges.append(list(map(int, line.strip().split("-"))))

ranges.sort(key=lambda r: r[0])

merged_ranges = [ranges[0]]
for current_range in ranges[1:]:
    last_merged_range = merged_ranges[-1]

    if current_range[0] <= last_merged_range[1] + 1:
        last_merged_range[1] = max(last_merged_range[1], current_range[1])
    else:
        merged_ranges.append(current_range)

total_fresh_ids = 0
for r in merged_ranges:
    total_fresh_ids += r[1] - r[0] + 1

print(total_fresh_ids)
