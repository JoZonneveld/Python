invoer = int(input("Vul een getal in: \n"))

mid = int(invoer / 2)
vulling = 1

def ramp(x, y, invoer, vulling):
    if x == invoer-1 or x == 0:
        uitvoer = True
    elif y == invoer-1 or y == 0:
        uitvoer = True
    elif y < vulling:
        uitvoer = True
    else:
        uitvoer = False

    return uitvoer

for x in range(invoer):
    output=""
    for y in range(invoer):
        uitvoer = ramp(x, y, invoer, vulling)

        if uitvoer == True:
            output += "*"
        else:
            output += " "
    vulling +=1


    print(output)
