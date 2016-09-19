import re
text = input("vul iets in\n")
getal = int(input("vul een getal in \n"))
for i in text:
    a = (ord(i))
    if re.search(r'[a-z_]', i):
        eind = a + getal
        if eind > 122:
            eind -= 26
        elif eind < 97:
            eind += 26
        print(chr(eind), end="")

        #a = 97 z = 122
    elif re.search(r'[A-Z_]', i):
        eind = a + getal
        if eind > 90:
            eind -= 26
        elif eind < 65:
            eind += 26
        #A = 65 Z = 90
        print(chr(eind), end="")



