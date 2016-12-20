class Empty:
    def IsEmpty(self):
        return True
    def Length(self):
        return 0
    def Sum(self):
        return 0
    def Map(self, f):
        return 0
    def Filter(self, p):
        return 0
    def Fold(self, f, z):
        return 0

class Node:
    def IsEmpty (self):
        return False

    def Head (self):
        return self.Value

    def Tail (self):
        return self.Tail

    def __init__(self, value, tail):
        self.Value = value
        self.Tail = tail

    def __rlshift__ (self , v):
        return Node (v, self)

    def __str__ (self):
        return str(self.Value ) + " <<" + str (self.Tail)

    def IsEmpty(self):
        return False

    def Length(self):
        return self.Tail.Length() + 1

    def Sum(self):
        return self.Value + self.Tail.Sum()

    def Map (self, f):
        return Node(f(self.Value), self.Tail.Map(f))

    def Filter (self ,p) :
        xs = self.Tail.Filter( p)
        if p(self.Value):
            return Node(self.Value, xs)
        else:
            return xs

    def Fold (self ,f ,z) :
        return f(self.Value , self.Tail.Fold(f , z))



l = Node(5, Node(9, Node(-1, Empty())))

print(l.Length())
print(l.Sum())
print(l.Map(lambda x: x+2))
print(l.Filter(lambda x: x % 3))
# print(l.Fold())
