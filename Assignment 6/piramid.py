hoogte = int(input("Voer een getal in: \n"))

aantal = 0
test = ""
for a in range(hoogte):
    test = ""
    aantal = aantal + 1

    for i in range(aantal):
        test =  test + "*"
    print(test)
