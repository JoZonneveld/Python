password = input("Vul uw wachtwoord in: \n")

i = len(password)

if i > 15:
    print("Strong")
elif i > 7 and i < 15:
    print("Medium")
elif i < 7:
    print("Weak")

