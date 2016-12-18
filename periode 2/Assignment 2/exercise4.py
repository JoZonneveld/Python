class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

list = Empty()
for i in range(1, 5):
    list = Node(i, list)

def check(l):
    while not l.IsEmpty:
        print(l.Value)
        l = l.Tail
check(list)

def reverse(l):
    tmplist = Empty()
    while not l.IsEmpty:
        tmplist = Node(l.Value, tmplist)
        l = l.Tail
    while not tmplist.IsEmpty:
        print(tmplist.Value)
        tmplist = tmplist.Tail
reverse(list)
