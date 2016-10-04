password = input("Vul uw wachtwoord in: \n")

passwordstrength = 0
L = len(password) #lengte password
kl  = False #bevat kleine letter?
hl  = False #bevat hoofdletter?
sp  = False #bevat speciaal teken?
g   = False #bevat getal?

for i in password:
    a = (ord(i))
    if a >= 97 and a <= 122: #kleine letter controlle
        kl = True
    elif a >= 65 and a <= 90: #hoofdletter controlle
        hl = True
    elif (a >= 33 and a <= 47) or (a >= 58 and a <= 64) or (a >= 91 and a <= 96) or (a >= 123 and a <= 126): #speciale caracter controlle
        sp = True
    elif a >= 48 and a <= 57: # getal controlle
        g = True

if kl == True:
    passwordstrength += 1
if hl == True:
    passwordstrength += 1
if sp == True:
    passwordstrength += 2
if g == True:
    passwordstrength += 1

if L > 7 and L < 12:
    passwordstrength = passwordstrength + 1
elif L >= 12:
    passwordstrength = passwordstrength + 2

print("Your password scored ", passwordstrength, "points of 7")

if passwordstrength > 5:
    print("Your password is strong")
elif passwordstrength <= 5 and passwordstrength > 3:
    print("Your password is medium")
elif passwordstrength > 0 and passwordstrength <= 3:
    print("Your password is weak")
