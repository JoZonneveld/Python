import re
password = input("Vul uw wachtwoord in: \n")

i = len(password)

passwordstrenght = 0

if re.search(r'[A-Z]', password):
    passwordstrenght = passwordstrenght + 1

if re.search(r'[0-9_]', password):
    passwordstrenght = passwordstrenght + 1

if re.search(r'[a-z_]', password):
    passwordstrenght = passwordstrenght + 1

if re.search(r'[,_._@_#_$_%_^_&_*_!]', password):
    passwordstrenght = passwordstrenght + 2

if i > 7 and i < 12:
    passwordstrenght = passwordstrenght + 1
elif i >= 12:
    passwordstrenght = passwordstrenght + 2

print("Your password scored ", passwordstrenght, "points of 7")

if passwordstrenght > 5:
    print("Your password is strong")
elif passwordstrenght <= 5 and passwordstrenght > 3:
    print("Your password is medium")
elif passwordstrenght > 0 and passwordstrenght <= 3:
    print("Your password is weak")





