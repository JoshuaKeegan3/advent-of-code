from collections import defaultdict

with open("2025/11/in.txt") as f:
    lines = f.readlines()

network = defaultdict(list)

for line in lines:
    line = line.split(":")
    node = line[0].replace(":", "")
    connections = line[1][1:].strip().split(" ")
    network[node] = connections


network["out"] = []


def countWaysToReach(end):
    counts = dict()
    newCounts = {node: (1 if node == end else 0) for node in network}

    while newCounts != counts:
        counts = newCounts
        newCounts = {
            node: (1 if node == end else sum(counts[child] for child in network[node]))
            for node in counts
        }

    return newCounts


print(countWaysToReach("out")["you"])

print(
    countWaysToReach("fft")["svr"]
    * countWaysToReach("dac")["fft"]
    * countWaysToReach("out")["dac"]
    + countWaysToReach("dac")["svr"]
    * countWaysToReach("fft")["dac"]
    * countWaysToReach("out")["fft"]
)
