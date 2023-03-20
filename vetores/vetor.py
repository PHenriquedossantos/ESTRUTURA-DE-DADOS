class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = tamanho * [None] # [None, None, None...]
        self.__posicao = 0

    def inserir_elemento_posicao(self, elemento, posicao):
        self.__elementos[posicao] = elemento
    
    def inserir_elemento_final(self, elemento):
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]
    


