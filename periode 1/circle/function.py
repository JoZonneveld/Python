def smiley(d, x, y, check):
    placeEye1 = int(d / 3)
    placeEye2 = int(d / 3 * 2)
    placeNose = int(d / 2)
    mouthwidthmin = int(d / 3)
    mouthwidthmax = int(d / 3 * 2)
    placeMouth = int(d / 3 * 2)
    if check != 1:
        if y == placeEye1 and x == placeEye1 or y == placeEye2 and x == placeEye1:
            check = 2
        elif y == placeNose and x ==  placeNose:
            check = 3
        elif x == mouthwidthmax and y == mouthwidthmin:
            check = 4
        elif x == mouthwidthmax and y == mouthwidthmax:
            check = 5
        elif x == mouthwidthmax and y > mouthwidthmin and y < mouthwidthmax:
            check = 6
    return check

def hollow(d, x, y):
    check = 0
    if x == 0 or x == d - 1:
        check = 1
    if y == 0 or y == d - 1:
        check = 1
    check = smiley(d, x, y, check)
    return check

def circle(d, x, y):
    import math

    center_x = d/2
    center_y = d/2

    distance = math.sqrt((center_x-x)**2 + (center_y-y)**2)
    distance = math.ceil(distance)

    if(distance <= d/2):
        return True
    else:
        return False

def hollow_circle(d, x, y):
    import math

    center_x = d/2
    center_y = d/2

    distance = math.sqrt((center_x-x)**2 + (center_y-y)**2)
    distance = math.ceil(distance)
    check = 0

    if(distance == math.floor(d/2)):
        check = 1
    else:
        check = 0
    check = smiley(d, x, y, check)
    return check
