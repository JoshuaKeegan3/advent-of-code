import math

import numpy as np


class DSU:
    """A Disjoint Set Union (DSU) data structure with path compression."""

    def __init__(self, n):
        self.parent = list(range(n))
        self.num_sets = n

    def find(self, i):
        """Finds the representative of the set containing element i."""
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """Merges the sets containing elements i and j."""
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_sets -= 1
            return True  # Returns True if a union was made
        return False  # Returns False if they were already in the same set


# --- Solution ---

FILE_PATH = "8/in.txt"

# 1. Read points from the input file.
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

# Kruskal's algorithm
dsu = DSU(num_points)
last_connection = None

for dist, u, v in dists:
    if dsu.union(u, v):
        if dsu.num_sets == 1:
            last_connection = (u, v)
            break

if last_connection:
    u, v = last_connection
    x1 = points[u][0]
    x2 = points[v][0]
    result = x1 * x2
    print(result)
else:
    pass
