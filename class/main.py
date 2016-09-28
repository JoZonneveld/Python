from function import *

keuze = int(input("Selecteer functie: \n1. add \n2. even \n3. addAll \n"))
if keuze == 1 or keuze == 3:
    x = int(input("Voer een 1e getal in: \n"))
    y = int(input("Voer een 2e getal in: \n"))
elif keuze == 2:
    x = int(input("Voer een 1e getal in: \n"))


if keuze == 1:
    print(add(x,y))
elif keuze == 2:
    print(even(x))
elif keuze == 3:
    print(addAll(x,y))
