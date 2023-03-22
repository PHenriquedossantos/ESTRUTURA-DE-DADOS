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
            pointer.next = Node(elem)
            self._size += 1
        else:
            self.head = Node(elem)
            self._size +=1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size
    
    def set(self, index, elem):
        # lista.set(5, 9)
        pass

    def get(self, index):
        # a = lista.get(6)
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

    def __setitem__(self, index, elem):
        #lista[2] = 20
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")
    
    def index(self, elem):
        """Retorna o índice do elemento na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise IndexError(f"{elem} is not in list")

x = LinkedList()
x.append(1)
x.append(2)
x.append(3)
x.append(4)
print(x.index(5))

