from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            self.next = Node(elem)
        else:
            #primeira insercao
            self.head = Node(elem)
            self._size +=1


    def __len__(self):
        return self._size

x = LinkedList()
x.append(22)
print(x.__len__())