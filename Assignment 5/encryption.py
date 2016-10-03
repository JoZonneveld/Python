import re
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
