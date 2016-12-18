x = int(input("Voer uw eerste getal in: \n"))
y = int(input("Voer uw tweede getal in: \n"))

def evengetal():
    oddnumbers = "De oneven nummers zijn: "
    evennumbers = "De even nummers zijn: "
    for z in range(x, y +1):
        if z % 2 == 0:
            if z == y - 1 or z == y:
                evennumbers += str(z)
            else:
                evennumbers += str(z) + ", "
        else:
            if z == y - 1 or z == y:
                oddnumbers += str(z)
            else:
                oddnumbers += str(z) + ", "
    print(evennumbers)
    print(oddnumbers)
evengetal()
