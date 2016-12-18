x = int(input("Voer uw eerste getal in: \n"))
y = int(input("Voer uw tweede getal in: \n"))

def avarage():
    totaal = 0
    count = 0
    for z in range(x, y +1):
        totaal += z
        count += 1
    return int(totaal / count)
print(avarage())
