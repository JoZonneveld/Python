class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self, value, prevNode):
        self.IsEmpty = False
        self.Value = value
        self.PrevNode = prevNode

list = Empty()
for i in range(4):
    list = Node(i, list)


def count(willekeurigenaam):
    count=0
    while not willekeurigenaam.IsEmpty:
        count +=1
        willekeurigenaam = willekeurigenaam.PrevNode
    return count

print(count(list))
