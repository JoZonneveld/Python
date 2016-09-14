x = 0
while x == 0:
    CS = int(input("Voer het aantal Celsius in: \n"))

    if CS > -273.15:
        KL = CS + 273.15
        print(CS, "graden celcius is gelijk aan", "%.2f" % KL, "graden Kelvin")
    else:
        print("u kunt niet lager als -273.15")


