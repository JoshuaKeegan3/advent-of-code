import math

position = 50
zeros = 0

with open("1/in.txt") as f:
    lines = f.readlines()

for line in lines:
    amount = int(line[1:])
    direction = line[0]

    prev_position = position

    if direction == "L":
        position -= amount
        zeros += math.ceil(prev_position / 100) - math.ceil(position / 100)

    elif direction == "R":
        position += amount
        zeros += position // 100 - prev_position // 100

print(f"answer: {zeros}")
