hoogte = int(input("Voer een getal in: \n"))

last_row = 2 * hoogte -1

mid = hoogte

for a in range(hoogte):
    output = ""
    #make them empty again
    printbetweenmin = 0
    printbetweenmax = 0

    #fill then (again)
    printbetweenmin = mid - a # 3 - 1 = 1
    printbetweenmax = mid + a # 3 + 1 = 5
    for i in range(last_row +1):
        if i >= printbetweenmin and i <= printbetweenmax:
            output = output + "*"
        else:
            output = output + " "
    print(output)
