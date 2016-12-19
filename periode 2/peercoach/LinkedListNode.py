class IsEmpty:
    def __init__(self):
        self.IsEmpty = True

class LinkedListNode:
    def __init__(self, Node, Next):
        self.Node = Node
        self.Next = Next
        self.IsEmpty = False

def AddToLinkList(list, ElementToAdd):
    while CarList.IsEmpty == False:
        list = list.Next
    List.Next = LinkedListNode(ElementToAdd, IsEmpty())

def MapVehicleNumberAbove(carlist, HigherThan):
    tmpList = IsEmpty()
    while(carlist.IsEmpty == False):
        if(carlist.Node.Number > HigherThan):
            tmpList = AddToLinkList(tmpList, carlist.Node.Number):

    return tmpList
