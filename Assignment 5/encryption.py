text = input("vul iets in\n")
getal = int(input("vul een getal in \n"))
for i in text:
    a = (ord(i))
    eind = a + getal
    print(chr(eind), end="")