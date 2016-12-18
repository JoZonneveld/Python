def repeat(symbol, n):
    res=""
    while((n>0)):
        res = (res + symbol)
        n = (n-1)
    return res

def draw_pyramid_AUX(num_spaces, num_stars):
    if(num_spaces < 0):
        return ""
    else:
        spaces = repeat(" ", num_spaces)
        stars = repeat("*", num_stars)
        return(spaces+(stars+("\n"+draw_pyramid_AUX((num_spaces - 1), (num_stars + 2)))))

def draw_pyramid(n):
    return draw_pyramid_AUX((n-1), 1)

res = draw_pyramid(5)

print(res)
