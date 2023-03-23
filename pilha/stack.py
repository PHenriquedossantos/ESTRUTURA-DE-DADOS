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

        self.top = node
        node.next = self.top
    def pop(self):
        # Remove o elemento do topo da pilha
        ...
    def peek(self):
        # retorna o topo da pilha sem remover
        ...
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





