import re
password = input("Vul uw wachtwoord in: \n")

i = len(password)

if re.match("^[a-z0-9_]*$", password):
    uppercase = 0
    special = 0
elif re.match("^[A-Z_]*$", password):
    uppercase = 1
else:
    special = 1

if i < 8 and uppercase == 1 or special == 1:
    print("kleiner dan 8 en uppercase is used")
elif i < 8 and special == 1:
    print("kleiner dan 8 en special is used")