from function import *

d = int(input("Voer een getal in \n"))

for x in range(d):
    output = ""
    for y in range(d):
        check = hollow(d, x, y)
        if check == 1:
            output += "*"
        elif check == 2:
            output += "O"
        elif check == 3:
            output += "7"
        elif check == 4:
            output += "\\"
        elif check == 5:
            output += "/"
        elif check == 6:
            output += "_"
        else:
            output += " "
    print(output)
