from math import sqrt
diameter = int(input("Voer een diameter van 6 of groter in: \n"))
while diameter < 6:
    diameter = int(input("Voer een diameter van 6 of groter in: \n"))

row = 0

for a in range(diameter):
    text = ""
    side = 0
    row += 1
    d = int(2 * sqrt(0.25 * (pow(diameter, 2)) - pow((0.5 * diameter - row), 2)))
    if (d % 2 == 0): #even
        text = text
    else:
        d += 1
    space = (diameter - d) / 2
    if row == 1 or row == (diameter - 1):
        for c in range(int(space)):
            text = text + " "
        for b in range(d):
            text = text + "*"
    else:
        for c in range(int(space)):
            text = text + " "
        for b in range(d):
            side += 1
            if side == 1 or side == d:
                text = text + "*"
            else:
                text = text + " "

    print(text)
