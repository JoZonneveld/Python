n = int(input("Vul een getal in: \n"))

mid = int(n / 2)

for x in range(n):
    output=""
    for y in range(n):
        if x == y or (x+y) == n-1:
            output += "*"
        elif x == mid:
            output += "*"
        elif y == mid:
            output += "*"
        else:
            output += " "
    print(output)
