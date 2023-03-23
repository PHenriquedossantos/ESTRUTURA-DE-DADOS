from node import Node

# inserir na pilha
# remover da pilha
# observar o topo da pilha

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        # insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size +=1
    def pop(self):
        # Remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -=1
            return node
        raise IndexError("The stack is empty")
    
    def peek(self):
        if self._size > 0:
            return self.top
        raise IndexError("The stack is empty")
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





