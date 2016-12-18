x = int(input("Voer uw eerste getal in: \n"))
y = int(input("Voer uw tweede getal in: \n"))

if x > y:
    print("Het eerste getal is het grootst: ", x)
elif x < y:
    print("Het tweede getal is het grootst: ", y)
else:
    print("Getallen zijn gelijk: ", x," - ",y)
