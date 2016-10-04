x = input("Vul uw antwoord in: \n")

for c in range(len(x), 0, -1):
    print(x[c-1], end="")
