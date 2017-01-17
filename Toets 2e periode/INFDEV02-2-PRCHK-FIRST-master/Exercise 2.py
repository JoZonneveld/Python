#Exercise 2
#The following program sums all the values of a list built with the Empty/Node data structure by means of a while loop.

class Empty:
  def __init__(self):
    self.IsEmpty = True
empty = Empty()
class Node:
  def __init__(self, value, tail):
    self.IsEmpty = False
    self.Value = value
    self.Tail = tail

lst = Node(5, Node(9, Node(1, empty)))
i = lst
sum = 0
while(not i.IsEmpty): #TODO: COMPLETE THE LINE (1 POINT)
  sum = sum + i.Value
  i = i.Tail #TODO: COMPLETE THE LINE (1 POINT)
print(sum)
