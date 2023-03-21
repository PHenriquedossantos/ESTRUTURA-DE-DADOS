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
            self.head = Node(elem)
            self._size +=1


    def __len__(self):
        return self._size
    
    def set(self, index, elem):
        pass

    def get(self, index):
        pass

    def __getitem__(self, index):
        # a = lista[6]
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")
    def __setitem__(self, index):
        pass

x = LinkedList()
x.append(22)
print(x.__len__())