from math import sqrt
diameter = 10

radius = diameter / 2
center_x = diameter / 2
center_y = diameter / 2

for x in range(diameter):
    for y in range(diameter):
        distance = sqrt(pow((center_x - x), 2) + pow((center_y - y), 2))

        if distance == radius:
            print("#")
