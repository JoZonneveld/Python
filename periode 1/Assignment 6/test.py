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





'''
getal = int(input("Voer een getal in: \n")) # input

text = 1 # hoeveel ga je uitprinten

for a in range(getal):
    output=""
    space = getal - (a - 1)
    for i in range(space):
        output += "/"
    for x in range(text):
        output += "*"
    print(output)
    text += 2
'''
>>>>>>> origin/master
>>>>>>> origin/master
