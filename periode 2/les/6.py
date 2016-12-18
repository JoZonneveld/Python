x = int(input("Hoe breed mag hij worden: \n"))
y = int(input("Hoeveel steren wilt u: \n"))

def rij(x, y):
    output = ""
    if x > y:
        for z in range(x+1):
            aantalhash = x - y
            if z <= aantalhash -1:
                output += "#"
            elif z > aantalhash:
                output += "*"
    else:
        output = False
    print(output)
rij(x,y)
