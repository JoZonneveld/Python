class Empty:
    def __init__(self):
        self.IsEmpty = True

class Node:
    def __init__(self, value, prevNode):
        self.IsEmpty = False
        self.Value = value
        self.PrevNode = prevNode

list = Empty()
for i in range(1,5):
    list = Node(i, list)


def keer(willekeurigenaam, x):
    while not willekeurigenaam.IsEmpty:
        uitkomst = willekeurigenaam.Value * x
        willekeurigenaam = willekeurigenaam.PrevNode
        print(uitkomst)

x = int(input("Voer een getal in: "))

keer(list, x)
