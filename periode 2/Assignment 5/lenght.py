class Empty:
    def IsEmpty(self):
        return True
    def Length(self):
        return 0


class Node:
    def __init__(self, value, tail):
        self.Value = value
        self.Tail = tail

    def IsEmpty(self):
        return False

    def Length(self):
        return self.Tail.Length() + 1

l = Empty()
for i in range(0, 8):
    l = Node(i, l)

print(l.Length())
