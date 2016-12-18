class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

list = Empty()
for i in range(6):
    list = Node(i, list)

def rec_count(l):
    if l.IsEmpty:
        return 0
    else:
        return rec_count(l.Tail) +1

print(rec_count(list))
