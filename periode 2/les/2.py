x = int(input("Voer uw eerste getal in: \n"))
y = int(input("Voer uw tweede getal in: \n"))

if (x > y and x % y == 0) or (y > x and y % x == 0):
    deelbaar = True
else:
    deelbaar =  False

if deelbaar == True:
    output = "Het is deelbaar"
else:
    output = "Het is niet deelbaar"

print(output)
