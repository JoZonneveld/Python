from function import *

d = int(input("Voer een getal in \n"))

for x in range(d):
    output = ""
    for y in range(d):
        check = circle(d, x, y)
        if check == True:
            output += "*"
        else:
            output += " "
    print(output)
