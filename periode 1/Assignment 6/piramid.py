hoogte = int(input("Voer een getal in: \n"))

last_row = 2 * hoogte -1

row = 0
mid = (last_row + 1) / 2

for a in range(hoogte):
    output = ""
    #make them empty again
    side = 1
    printbetweenmin = 0
    printbetweenmax = 0

    #fill then (again)
    printbetweenmin = mid - a
    printbetweenmax = mid + a
    for i in range(last_row +1):
        if i >= printbetweenmin and i <= printbetweenmax:
            output = output + "*"
        else:
            output = output + " "
    print(output)
