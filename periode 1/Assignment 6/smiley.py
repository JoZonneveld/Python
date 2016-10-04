from math import sqrt
diameter = int(input("Voer een diameter van 10 of groter in: \n"))
while diameter < 10:
    diameter = int(input("Voer een diameter van 10 of groter in: \n"))

row = 0
eyes = True
nose = True
Mouth = True

placeEye1 = int(diameter / 3)
placeEye2 = int(diameter / 3 * 2)
placeNose = int(diameter / 2)
mouthwidthmin = int(diameter / 3)
mouthwidthmax = int(diameter / 3 * 2)
placeMouth = int(diameter / 3 * 2)


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

        if row == placeNose and nose == True:
            for b in range(d):
                side += 1
                if side == 1 or side == d:
                    text = text + "*"
                elif side == placeNose:
                    text = text + "7"
                else:
                    text = text + " "
            nose = False
        elif row == placeMouth and Mouth == True:
            for b in range(d):
                side += 1
                if side == 1 or side == d:
                    text = text + "*"
                elif side == mouthwidthmin:
                    text = text + "\\"
                elif side == mouthwidthmax:
                    text = text + "/"
                elif side > mouthwidthmin and side < mouthwidthmax:
                    text = text + "_"
                else:
                    text = text + " "
        elif (d == diameter or d == (diameter - 1)) and eyes == True:
            for b in range(d):
                side += 1
                if side == placeEye1 or side == placeEye2:
                    text = text + "O"
                elif side == 1 or side == d:
                    text = text + "*"
                else:
                    text = text + " "
            eyes = False
        else:
            for b in range(d):
                side += 1
                if side == 1 or side == d:
                    text = text + "*"
                else:
                    text = text + " "

    print(text)

#smiley done
