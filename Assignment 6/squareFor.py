breedte = int(input("Voer een breedte in: \n"))
hoogte = int(input("Voer een hoogte in: \n"))

for a in range(hoogte):
    output = ""
    for i in range(breedte):
        output = output + "*"
    print(output)
