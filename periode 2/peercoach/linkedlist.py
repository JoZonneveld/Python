import random
import math
from LinkedListNode import *

MYLIST = LinkedListNode(80, LinkedListNode(50, IsEmpty()))

while MYLIST.IsEmpty == False:
    print(str(MYLIST.Node))
    MYLIST = MYLIST.Next
