#Exercise 1
#The following program returns the sum of all numbers between a range of two numbers by means of a recursive function.

def add_range(i,n):
  if(i < n): #TODO: COMPLETE THE LINE (0.5 POINT)
    return i + add_range((i+1), n) #TODO: COMPLETE THE MISSING LINE (1.5 POINT)
  else:
    return 0

print(add_range(5,10))
