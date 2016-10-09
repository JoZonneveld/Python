from function import *

d = int(input("Voer een getal in \n"))

for x in range(d):
    output = ""
    for y in range(d):
        check = hollow_circle(d, x, y)
        if check == 1: #standaart
            output += " "
        elif check == 2: #ogen
            output += "O"
        elif check == 3: #neus
            output += "7"
        elif check == 4: #mondhoek
            output += "\\"
        elif check == 5: #mondhoek
            output += "/"
        elif check == 6: #mond
            output += "_"
        else:
            output += " "
    print(output)
