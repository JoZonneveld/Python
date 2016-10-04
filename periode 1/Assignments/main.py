from function import *
x =0
while x == 0:
    assignment = int(input("\n1. Assignment 4 \n2. Assignment 5 \n3. Assignment 6\n"))
    while assignment < 1  or assignment > 3:
        assignment = int(input("1. Assignment 4 \n2. Assignment 5 \n3. Assignment 6\n"))
    if assignment == 1: #Assignment 4

        assignment4 = int(input("\n1. Absolute \n2. Fahrenheit \n3. Kelvin\n4. RPS \n"))

        while assignment4 < 1  or assignment4 > 5:
            assignment4 = int(input("1. Absolute \n2. Fahrenheit \n3. Kelvin\n4. RPS \n"))

        if assignment4 == 1:
            print("U heeft gekozen voor Absolute.py")
            absolute()
        elif assignment4 == 2:
            print("U heeft gekozen voor fahrenheit.py")
            fahrenheit()
        elif assignment4 == 3:
            print("U heeft gekozen voor kelvin.py")
            kelvin()
        elif assignment4 == 4:
            print("U heeft gekozen voor rps.py")
            rps()

    elif assignment == 2: #Assignment 5
        assignment5 = int(input("1. Encryption \n2. Password \n3. Reverse\n"))

        while assignment5 < 1  or assignment5 > 3:
            assignment5 = int(input("1. Encryption \n2. Password \n3. Reverse\n"))

        if assignment5 == 1:
            print("U heeft gekozen voor encryption.py")
            encryption()
        elif assignment5 == 2:
            print("U heeft gekozen voor password.py")
            password()
        elif assignment5 == 3:
            print("U heeft gekozen voor reverse.py")
            reverse()

    elif assignment == 3: #Assignment 6
        assignment6 = int(input("1. Circle \n2. Smiley \n3. Square\n4. Hollow square \n5. Half piramid \n6. Piramid\n"))

        while assignment6 < 1  or assignment6 > 6:
            assignment6 = int(input("1. Circle \n2. Smiley \n3. Square\n4. Hollow square \n5. Half piramid \n6. Piramid\n"))


        if assignment6 == 1:
            print("U heeft gekozen voor Circle.py")
            circle()
        elif assignment6 == 2:
            print("U heeft gekozen voor Smiley.py")
            smiley()
        elif assignment6 == 3:
            print("U heeft gekozen voor square.py")
            square()
        elif assignment6 == 4:
            print("U heeft gekozen voor hollow_square.py")
            hollow_square()
        elif assignment6 == 5:
            print("U heeft gekozen voor half_piramid.py")
            half_piramid()
        elif assignment6 == 6:
            print("U heeft gekozen voor piramid.py")
            piramid()
