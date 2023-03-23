from node import Node

class Stack:
    def __init__(self):
        self.head = None
        self._size = 0


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size
            
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()





