from math import pi, sqrt, ceil
text = ""
diameter = int(input("Voer een diameter: \n"))
row = 0
for a in range(diameter):
    row += 1
    d = int(2 * sqrt(0.25 * (pow(diameter, 2)) - pow((0.5 * diameter - row), 2)))
    for b in range(d):
        text = text + "*"


radius = ceil(sqrt(len(text)/pi))
text_iter = iter(text)

for i in range(-radius, radius+1):
    num = ceil(sqrt(radius**2 - i**2))
    print("{:^{}}".format("".join(next(text_iter, "*") for _ in range(2*num)), 2*radius))
