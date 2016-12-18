class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self, value, prevNode):
        self.IsEmpty = False
        self.Value = value
        self.PrevNode = prevNode

list = Empty()
for i in range(5):
    list = Node(i, list)


def som(willekeurigenaam):
    while not willekeurigenaam.IsEmpty:
        count += willekeurigenaam.Value
        willekeurigenaam = willekeurigenaam.PrevNode
    return count

print(som(list))
