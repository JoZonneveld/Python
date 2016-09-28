hoogte = int(input("Voer een getal in: \n"))

test = ""
for a in range(hoogte):
    test = ""
    for i in range(a + 1):
        test =  test + "*"
    print(test)
