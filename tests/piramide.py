hoogte = int(input("Voer een getal in van 6 of groter: \n"))

prints = 1
for x in range(hoogte):
    output = ""
    space = hoogte - x
    for y in range(space):
        output += " "
    for z in range(prints):
        output += "*"
    print(output)
    prints += 2
