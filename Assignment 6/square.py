breedte = int(input("Voer een getal in: \n"))
hoogte = int(input("Voer een getal in: \n"))

for a in range(hoogte):
    output = ""
    for i in range(breedte):
        output = output + "*"

    print(output)
