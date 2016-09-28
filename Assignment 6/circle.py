from math import sqrt
diameter = int(input("Voer een diameter van 6 of groter in: \n"))
while diameter < 6:
    diameter = int(input("Voer een diameter van 6 of groter in: \n"))

for a in range(diameter + 1):
    text = ""
    d = int(2 * sqrt(0.25 * (pow(diameter, 2)) - pow((0.5 * diameter - a), 2)))
    if (d % 2 == 0): #even
        text = text
    else:
        d += 1
    space = (diameter - d) / 2
    for c in range(int(space)):
        text = text + " "
    for b in range(d):
        text = text + "*"
    print(text)
