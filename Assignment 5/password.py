password = input("Vul uw wachtwoord in: \n")

passwordstrenght = 0
L = len(password) #lengte password
kl  = False #bevat kleine letter?
hl  = False #bevat hoofdletter?
sp  = False #bevat speciaal teken?
g   = False #bevat getal?

for i in password:
    a = (ord(i))
    if a >= 97 and a <= 122:#kleine letter controlle
        kl = True
    elif a >= 65 and a <= 90:#hoofdletter controlle
        hl = True
    elif (a >= 35 and a <= 47) or (a >= 58 and a <= 64) or (a >= 91 and a <= 96) or (a >= 123 and a <= 126): #speciale caracter controlle
        sp = True
    elif a >= 48 and a <= 57: # getal controlle
        g = True

if kl == True:
    passwordstrenght += 1
if hl == True:
    passwordstrenght += 1
if sp == True:
    passwordstrenght += 2
if g == True:
    passwordstrenght += 1

if L > 7 and L < 12:
    passwordstrenght = passwordstrenght + 1
elif L >= 12:
    passwordstrenght = passwordstrenght + 2

print("Your password scored ", passwordstrenght, "points of 7")

if passwordstrenght > 5:
    print("Your password is strong")
elif passwordstrenght <= 5 and passwordstrenght > 3:
    print("Your password is medium")
elif passwordstrenght > 0 and passwordstrenght <= 3:
    print("Your password is weak")
