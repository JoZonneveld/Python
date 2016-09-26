getal = int(input("Voer een getal in: \n"))
i = 0
j = 0
while i != getal:
    output = ""
    i += 1
    j = 0
    while j != getal:
        output = output + "*"
        j += 1
    print(output)
