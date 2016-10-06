getal = int(input("Voer een getal in: \n")) # 5

text = 1

for a in range(getal): #5 hoog
    output=""
    space = getal - (a+1) # space = 5 - 2 = 3
    for i in range(space):
        output += " "
    for x in range(text):
        output += "*"
    print(output)
    text += 2
