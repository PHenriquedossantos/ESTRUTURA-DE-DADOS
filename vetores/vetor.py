class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = tamanho * [None] # [None, None, None...]
        self.__posicao = 0

    def inserir_elemento_posicao(self, elemento, posicao):
        self.__elementos[posicao] = elemento