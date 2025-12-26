with open("2025/9/in.txt") as f:
    _in = f.readlines()

red_tile_coordinates = red_tile_coordinates = [
    tuple(map(int, line.split(","))) for line in _in
]

polygon_edges = [
    # make the coordinates easy to work with when checking the rectangle is valid
    (
        (min(x1, x2), min(y1, y2)),
        (max(x1, x2), max(y1, y2)),
    )
    for (x1, y1), (x2, y2) in sorted(
        # Shift all of the edges by one
        # This will collect all of the horizontal edges which is all that we care about
        zip(red_tile_coordinates, red_tile_coordinates[1:] + red_tile_coordinates[:1]),
    )
]


def is_rect_valid(p1, p2):
    min_x = min(p1[0], p2[0])
    max_x = max(p1[0], p2[0])
    min_y = min(p1[1], p2[1])
    max_y = max(p1[1], p2[1])

    for edge in polygon_edges:  # crossing edges
        (x1, y1), (x2, y2) = edge

        if x1 == x2:  # vertical line
            if min_x < x1 < max_x and y2 > min_y and y1 < max_y:
                return False
        else:  # horizontal
            if min_y < y1 < max_y and x2 > min_x and x1 < max_x:
                return False

    return True


best_area = 0
rectangle = None

for i in range(len(red_tile_coordinates)):
    for j in range(i + 1, len(red_tile_coordinates)):
        p1, p2 = list(sorted((red_tile_coordinates[j], red_tile_coordinates[i])))
        area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
        if area <= best_area:  # Small optimisation to not check the edges again
            continue

        if is_rect_valid(p1, p2):
            best_area = area
            rectangle = (p1, p2)

print(best_area, rectangle)
