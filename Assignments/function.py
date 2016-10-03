# ------------------------------------------------------------Assignment 4--------------------------------------------------------------
def absolute():
    i = int(input("Vul een getal in "))
    print("ingevoerde getal is", i)
    if i < 0:
        print ("uitkomst is", (i * -1))
    else:
        print("uitkomst is", i)

def fahrenheit():
    Fx = int(input("Voer het aantal fahrenheit in: \n"))
    CS = (Fx - 32) / 1.8
    print(Fx, "fahrenheit is gelijk aan", "%.2f" % CS, "graden Celsius")

def kelvin():
    CS = int(input("Voer het aantal Celsius in: \n"))

    if CS > -273.15:
        KL = CS + 273.15
        print(CS, "graden celcius is gelijk aan", "%.2f" % KL, "graden Kelvin")
    else:
        print("u kunt niet lager als -273.15")

def rps():
    import random

    stop = 0

    name = (input("whats your name? \n"))
    print("1. best of three \n2. best of five \n3. best of seven")
    modes = int((input("Select a game mode 1, 2 or 3? \n")))

    while modes >= 4:
        modes = int((input("Select a game mode 1, 2 or 3? \n")))

    if modes == 1:
        wins = 2
    elif modes == 2:
        wins = 3
    elif modes == 3:
        wins = 4

    playerwins = 0
    computerwins = 0

    print("Welcome ", name)

    while playerwins != wins and computerwins != wins:
        pick = (input("whats your pick? \n"))

        randompick = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        computer = (random.choice(randompick))

        if pick == computer:
            print("Draw!")
        else:
            if pick == "rock":
                if computer == "lizard":
                    print(pick, " crushes ", computer)
                    playerwins = playerwins + 1
                elif computer == "scissors":
                    print(pick, " crushes ", computer)
                    playerwins = playerwins + 1
                elif computer == "spock":
                    print(computer, " vaporizes ", pick)
                    computerwins = computerwins + 1
                elif computer == "paper":
                    print(computer, " covers ", pick)
                    computerwins = computerwins + 1

            if pick == "paper":
                if computer == "rock":
                    print(pick, " covers ", computer)
                    playerwins = playerwins + 1
                elif computer == "spock":
                    print(pick, " disaproves ", computer)
                    playerwins = playerwins + 1
                elif computer == "scissors":
                    print(computer, " cuts ", pick)
                    computerwins = computerwins + 1
                elif computer == "lizard":
                    print(computer, " eats ", pick)
                    computerwins = computerwins + 1

            if pick == "scissors":
                if computer == "paper":
                    print(pick, " cuts ", computer)
                    playerwins = playerwins + 1
                elif computer == "lizard":
                    print(pick, " decapitates ", computer)
                    playerwins = playerwins + 1
                elif computer == "spock":
                    print(computer, " smashes ", pick)
                    computerwins = computerwins + 1
                elif computer == "rock":
                    print(computer, " crushes ", pick)
                    computerwins = computerwins + 1

            if pick == "lizard":
                if computer == "paper":
                    print(pick, " eats ", computer)
                    playerwins = playerwins + 1
                elif computer == "spock":
                    print(pick, " poisens ", computer)
                    playerwins = playerwins + 1
                elif computer == "rock":
                    print(computer, " crushes ", pick)
                    computerwins = computerwins + 1
                elif computer == "scissors":
                    print(computer, " decapitates ", pick)
                    computerwins = computerwins + 1

            if pick == "spock":
                if computer == "scissors":
                    print(pick, " smashes ", computer)
                    playerwins = playerwins + 1
                elif computer == "rock":
                    print(pick, " vaporizes ", computer)
                    playerwins = playerwins + 1
                elif computer == "lizard":
                    print(computer, " poisens ", pick)
                    computerwins = computerwins + 1
                elif computer == "paper":
                    print(computer, " disaproves ", pick)
                    computerwins = computerwins + 1

        print("Standings ", playerwins, " - ", computerwins)

    if playerwins > computerwins:
        print(name, "wins")
    else:
        print("Computer wins")

# ------------------------------------------------------------Assignment 5--------------------------------------------------------------

def encryption():
    text = input("vul iets in\n")
    getal = 999 #raar getal om loop te triggeren
    while getal > 26 or getal < -26:
        getal = int(input("vul een getal in tussen -26 en 26 \n"))
    for i in text:
        a = (ord(i))
        if a >= 97 and a <= 122:#kleine letter controlle
            eind = a + getal
            if eind > 122:
                eind -= 26
            elif eind < 97:
                eind += 26
            print(chr(eind), end="")
        elif a >= 65 and a <= 90:#hoofdletter controlle
            eind = a + getal
            if eind > 90:
                eind -= 26
            elif eind < 65:
                eind += 26
            #A = 65 Z = 90
            print(chr(eind), end="")


def password():
    password = input("Vul uw wachtwoord in: \n")

    passwordstrenght = 0
    L = len(password) #lengte password
    kl  = False #bevat kleine letter?
    hl  = False #bevat hoofdletter?
    sp  = False #bevat speciaal teken?
    g   = False #bevat getal?

    for i in password:
        a = (ord(i))
        if a >= 97 and a <= 122:#kleine letter controlle
            kl = True
        elif a >= 65 and a <= 90:#hoofdletter controlle
            hl = True
        elif (a >= 35 and a <= 47) or (a >= 58 and a <= 64) or (a >= 91 and a <= 96) or (a >= 123 and a <= 126): #speciale caracter controlle
            sp = True
        elif a >= 48 and a <= 57: # getal controlle
            g = True

    if kl == True:
        passwordstrenght += 1
    if hl == True:
        passwordstrenght += 1
    if sp == True:
        passwordstrenght += 2
    if g == True:
        passwordstrenght += 1

    if L > 7 and L < 12:
        passwordstrenght = passwordstrenght + 1
    elif L >= 12:
        passwordstrenght = passwordstrenght + 2

    print("Your password scored ", passwordstrenght, "points of 7")

    if passwordstrenght > 5:
        print("Your password is strong")
    elif passwordstrenght <= 5 and passwordstrenght > 3:
        print("Your password is medium")
    elif passwordstrenght > 0 and passwordstrenght <= 3:
        print("Your password is weak")


def reverse():
    x = input("Vul uw antwoord in: \n")

    for c in range(len(x), 0, -1):
        print(x[c-1], end="")

# ------------------------------------------------------------Assignment 6--------------------------------------------------------------
def circle():
    from math import sqrt
    diameter = int(input("Voer een diameter van 6 of groter in: \n"))
    while diameter < 6:
        diameter = int(input("Voer een diameter van 6 of groter in: \n"))

    for a in range(diameter + 1):
        text = ""
        d = int(2 * sqrt(0.25 * (pow(diameter, 2)) - pow((0.5 * diameter - a), 2)))
        if (d % 2 == 0): #even
            text = text
        else:
            d += 1
        space = (diameter - d) / 2
        for c in range(int(space)):
            text = text + " "
        for b in range(d):
            text = text + "*"
        print(text)

def smiley():
    from math import sqrt
    diameter = int(input("Voer een diameter van 6 of groter in: \n"))
    while diameter < 6:
        diameter = int(input("Voer een diameter van 6 of groter in: \n"))

    row = 0
    eyes = True
    nose = True
    Mouth = True
    for a in range(diameter):
        text = ""
        side = 0
        row += 1
        d = int(2 * sqrt(0.25 * (pow(diameter, 2)) - pow((0.5 * diameter - row), 2)))
        if (d % 2 == 0): #even
            text = text
        else:
            d += 1

        space = (diameter - d) / 2
        if row == 1 or row == (diameter - 1):
            for c in range(int(space)):
                text = text + " "
            for b in range(d):
                text = text + "*"
        else:
            for c in range(int(space)):
                text = text + " "

            if (d == diameter or d == (diameter - 1)) and eyes == True:
                placeEye1 = int(diameter / 3)
                placeEye2 = int(diameter / 3 * 2)
                for b in range(d):
                    side += 1
                    if side == 1 or side == d:
                        text = text + "*"
                    elif side == placeEye1 or side == placeEye2:
                        text = text + "#"
                    else:
                        text = text + " "
                eyes = False
            else:
                for b in range(d):
                    side += 1
                    if side == 1 or side == d:
                        text = text + "*"
                    else:
                        text = text + " "

        print(text)


def square():
    getal = int(input("Voer een getal in: \n"))
    for a in range(getal):
        output = ""
        for i in range(getal):
            output = output + "*"
        print(output)

def hollow_square():
    getal = int(input("Voer een getal in: \n"))
    for a in range(getal):
        output = ""
        if a == 0 or a == (getal - 1):
            for i in range(getal):
                output = output + "*"
        else:
            for i in range(getal):
                if i == 0 or i == (getal - 1):
                    output = output + "*"
                else:
                    output = output + " "
        print(output)

def half_piramid():
    hoogte = int(input("Voer een getal in: \n"))

    test = ""
    for a in range(hoogte):
        test = ""
        for i in range(a + 1):
            test =  test + "*"
        print(test)

def piramid():
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
