import math
hoogte = int(input("Voer een getal in van 6 of groter: \n"))

prints = 1
circlestart = int(hoogte / 3)
circledia = int(hoogte - (hoogte/3))

center_x = int(circledia/2)
center_y = int(circledia/2)

for x in range(hoogte):
    output = ""
    space = hoogte - x
    for y in range(space):
        output += " "
    for z in range(prints):
        distance = math.sqrt((center_x-x)**2 + (center_y-z)**2)
        distance = math.ceil(distance)
        if z == 0 or z == (prints - 1) or x == (hoogte-1):
            output += "*"
        elif (distance == math.floor(circledia/2)):
            output += "0"
        else:
            output += " "
    print(output)
    prints += 2
