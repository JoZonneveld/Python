output = ""
for i in range(0, 4):
    for j in range(0, 4):
        if (i + j) % 2 == 0:
            output += "0"
        else:
            output += "="
    output += "\n"
print(output)
