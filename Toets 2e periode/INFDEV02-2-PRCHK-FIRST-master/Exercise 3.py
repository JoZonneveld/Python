#Exercise 3
#The following program computes the length of a list built with the Empty/Node data structure by means of recursive methods.

class Empty:
  def __init__(self):
    self.IsEmpty = True

  def Length(self): #TODO: COMPLETE THE MISSING LINES (1.5 POINT)
      return 0

empty = Empty()
class Node:
  def __init__(self, value, tail):
    self.IsEmpty = False
    self.Value = value
    self.Tail = tail

  def Length(self):
    return 1 + self.Tail.Length() #TODO: COMPLETE THE LINE (1.5 POINT)

lst = Node(5, Node(9, Node(1, empty)))
lst_length = lst.Length()
print(lst_length)
