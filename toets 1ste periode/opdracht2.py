n = int(input("Vul een getal in: \n"))

output = ""
for i in range(2, 10):
    output += str(i)
    if i % n == 0:
        output += "V"
print(output)
