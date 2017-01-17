#Exercise 4
#The following program computes the average of the values of a list built with the Empty/Node data structure by means of recursive methods.

class Empty:
  def __init__(self): self.IsEmpty = True
  def Sum(self): return 0
  def Average(self): return 0
  def Length(self): return 0 #TODO: COMPLETE THE MISSING LINES (1.5 POINT)

empty = Empty()
class Node:
  def __init__(self, value, tail):
    self.IsEmpty = False
    self.Value = value
    self.Tail = tail

  def Length(self):
    return 1 + self.Tail.Length()

  def Sum(self):
      return self.Value + self.Tail.Sum() #TODO: COMPLETE THE MISSING LINES (1.5 POINT)


  def Average(self):
      return self.Sum() / self.Length()

lst = Node(5, Node(9, Node(1, empty)))
lst_avg = lst.Average()
print(lst_avg)
