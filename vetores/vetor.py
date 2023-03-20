class Vetor():
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__elementos = tamanho * [None] # [None, None, None...]
        self.__posicao = 0


    def tamanho_vetor(self):
        return len(self.__elementos)
    
    def __str__(self):
        return ' '.join([str(i) for i in self.__elementos])

    def inserir_elemento_posicao(self, elemento, posicao):
        vetor_inicio = self.__elementos[:posicao] + [None] #Pega até uma posicao antes da variável posicao
        vetor_final = self.__elementos[posicao:] #pega tudo incluindo a variavel posicao
        vetor_inicio[-1] = elemento
        
        self.__elementos = vetor_inicio + vetor_final
        self.__posicao += 1
    
    def inserir_elemento_final(self, elemento):
        if self.__posicao >= self.tamanho_vetor():
            self.__elementos += [None]
        self.__elementos[self.__posicao] = elemento
        self.__posicao += 1

    def listar_elemento(self, posicao):
        return self.__elementos[posicao]
    


