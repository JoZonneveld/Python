<<<<<<< HEAD
diameter = int(input("Voer een diameter in: \n"))
=======
<<<<<<< HEAD
output = ""
for i in range(0, 4):
    for j in range(0, 4):
        if (i + j) % 2 == 0:
            output += "0"
        else:
            output += "="
    output += "\n"
print(output)
=======
<<<<<<< HEAD
x = "i am" * str(2016 - 1995)

print(x)
=======
import math
diameter = int(input("Voer een getal in: \n")) # input
center_x = diameter/2
center_y = diameter/2
for x in range(diameter+1):
    output = ""
    for y in range(diameter+1):
        distance = math.sqrt((center_x-x)**2 + (center_y-y)**2)
        distance = math.ceil(distance)
        if(distance <= diameter/2):
            output += "#"
        else:
            output += " "
    print(output)
>>>>>>> origin/master

oog1            =   int(diameter/3)
oog2            =   int((diameter/3) * 2)
oogLocatie      =   int(diameter/3)

neus_locatie    =   int(diameter/2)

mondhoek1       =   int(diameter/3)
mondhoek2       =   int((diameter/3) * 2)
mond_locatie    =   int((diameter/3) * 2)


for a in range(diameter):
    output = ""
    if a == 0 or a == (diameter - 1):
        for i in range(diameter):
            output = output + "*"
    else:
        for i in range(diameter):
            if i == 0 or i == (diameter - 1):
                output = output + "*"
            elif a == oogLocatie and i == oog1:
                output = output + "O"
            elif a == oogLocatie and i == oog2:
                output = output + "O"
            elif a == neus_locatie and i == neus_locatie:
                output = output + "7"
            elif (a-1) == mond_locatie and i == mondhoek1:
                output = output + "/"
            elif (a-1) == mond_locatie and i == mondhoek2:
                output = output + "\\"
            elif a == mond_locatie and i > mondhoek1 and i < mondhoek2:
                output += "_"
            else:
                output = output + " "
    print(output)
<<<<<<< HEAD
=======
    text += 2
'''
>>>>>>> origin/master
>>>>>>> origin/master
>>>>>>> origin/master
