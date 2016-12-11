def repeat (symbol, n):
    res=""
    while((n>0)):
        res = (res + symbol)
        n = (n-1)
    return res

def draw_line(n):
    return repeat("*",n)

def draw_square(n):
    l = (draw_line(n) + "\n")
    return repeat(l, n)

def draw_empty_square(n):
    l = (draw_line(n) + "\n")
    empty_line=("*" + (repeat(" ", (n-2)) + "*\n"))
    return (l + empty_line + l)


res = draw_empty_square(3)

print(res)
