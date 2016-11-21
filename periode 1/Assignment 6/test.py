diameter = int(input("Voer een diameter in: \n"))

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
