top = lambda x, y: (y == 0)
left = lambda x, y: (x == 0)

AND = lambda p1, p2: lambda p1, p2: (top

(p1,p2) and left(p1,p2))


left_and_top = AND(left, top)

a = left_and_top(0,0)
b = left_and_top(0,1)
c = left_and_top(1,0)
d = left_and_top(1,1)

print(a)
print(b)
print(c)
print(d)
