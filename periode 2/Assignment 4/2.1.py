up = lambda x, y: (y == 0)
left = lambda x, y: (x == 0)

OR = lambda p1, p2: lambda p1,p2: (up(p1,p2) or left(p1,p2))


top_or_left = OR(up, left)

a = top_or_left(0,0)
b = top_or_left(0,1)
c = top_or_left(1,0)
d = top_or_left(1,1)

print(a)
print(b)
print(c)
print(d)
