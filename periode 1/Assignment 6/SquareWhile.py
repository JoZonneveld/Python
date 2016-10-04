getal = int(input("Voer een getal in: \n"))
i = 0
while i != getal:
    i += 1
    j = 0
    output = ""
    while j != getal:
        output = output + "*"
        j += 1
    print(output)
