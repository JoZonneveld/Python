def add(x,y):
    return x + y

def even(x):
    if (x % 2 == 0): #even
        return True
    else:
        return False

def addAll(x,y):
    som = x
    for i in range(x+1,y,1):
        som = som + i
    som = som + y
    return som
