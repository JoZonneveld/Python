n = int(input("Vul een getal in: \n"))

prints = 1
for x in range(n):
    output = ""
    space = int((n-x)-1)
    for z in range(space):
        output += " "
    for y in range(prints):
        output += "*"
    prints+=2
    print(output)
