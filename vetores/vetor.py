class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = tamanho * [None]
        self.__posicao = 0
