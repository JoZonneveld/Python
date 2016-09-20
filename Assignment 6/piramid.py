hoogte = int(input("Voer een getal in: \n"))

last_row = 2 * hoogte -1

aantal = 1

row = 0
mid = (last_row + 1) / 2

for a in range(hoogte):
    output = ""
    #make them empty again
    side = 1
    printbetweenmin = 0
    printbetweenmax = 0

    #fill then (again)
    printbetweenmin = mid - row
    printbetweenmax = mid + row
    row = row + 1
    for i in range(last_row):
        if side >= printbetweenmin and side <= printbetweenmax:
            output = output + "*"
        else:
            output = output + " "
        side = side + 1
    print(output)
