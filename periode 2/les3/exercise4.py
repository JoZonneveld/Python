class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self, value, prevNode):
        self.IsEmpty = False
        self.Value = value
        self.PrevNode = prevNode

list = Empty()
for i in range(1, 5):
    list = Node(i, list)
    print (list.Value)

tmplist = Empty()
while not list.IsEmpty:
    tmplist = Node(list.Value, tmplist)
    list = list.PrevNode
    print(tmplist.Value)
