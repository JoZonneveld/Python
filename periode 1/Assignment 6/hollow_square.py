breedte = int(input("Voer een breedte in: \n"))
hoogte = int(input("Voer een hoogte in: \n"))
for a in range(hoogte):
    output = ""
    if a == 0 or a == (hoogte - 1):
        for i in range(breedte):
            output = output + "*"
    else:
        for i in range(breedte):
            if i == 0 or i == (breedte - 1):
                output = output + "*"
            else:
                output = output + " "
    print(output)
