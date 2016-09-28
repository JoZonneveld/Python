def add(x,y):
    return x + y

def even(x):
    if (x % 2 == 0): #even
        return True
    else:
        return False

def addAll(x,y):
    som = 0
    for i in range(x,y):
        som += i
    som += y
    return som
