breedte = int(input("Voer een breedte in: \n"))
hoogte = int(input("Voer een hoogte in: \n"))
row = 0
for a in range(hoogte):
    side = 0
    row = row + 1
    output = ""
    if row == 1 or row == hoogte:
        for i in range(breedte):
            output = output + "*"
    else:
        for i in range(breedte):
            side = side + 1
            if side == 1 or side == breedte:
                output = output + "*"
            else:
                output = output + " "
    print(output)
