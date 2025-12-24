import math

import numpy as np

FILE_PATH = "8/in.txt"
N = 1000

with open(FILE_PATH) as f:
    lines = f.readlines()

points = [list(map(int, line.strip().split(","))) for line in lines]
num_points = len(points)

dists = []
for i in range(num_points):
    for j in range(i + 1, num_points):
        dist = math.dist(points[i], points[j])
        dists.append((dist, i, j))

dists.sort()

connections = {}
for i in range(N):
    dist, u, v = dists[i]

    if u not in connections:
        connections[u] = []
    if v not in connections:
        connections[v] = []

    connections[u].append(v)
    connections[v].append(u)

islands = []
visited = set()
for i in range(num_points):
    if i in visited:
        continue

    current_island = []
    q = [i]
    visited.add(i)

    head = 0
    while head < len(q):
        current_node = q[head]
        head += 1
        current_island.append(current_node)

        if current_node in connections:
            for neighbor in connections[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

    islands.append(current_island)

island_sizes = [len(island) for island in islands]
island_sizes.sort(reverse=True)

three_largest_sizes = island_sizes[:3]
result = int(np.prod(three_largest_sizes))
print(result)
