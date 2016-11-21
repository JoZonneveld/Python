hoogte = int(input("Voer een getal in: \n"))

for a in range(hoogte):
    output = ""
    for i in range(a + 1):
        output += "*"
    print(output)
