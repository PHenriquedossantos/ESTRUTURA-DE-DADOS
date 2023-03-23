from vetores import vetor
from linkedlist import linkedlist
from linkedlist import node

print(30 * "-", "MENU", 30*"-")
print("1. Vetores")
print("2. Listas Ligadas")

menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(0)
    vetor_teste.inserir_elemento_posicao(1, 0)
    vetor_teste.inserir_elemento_posicao(2, 1)
    vetor_teste.inserir_elemento_posicao(3, 2)
    vetor_teste.inserir_elemento_posicao(4, 2)

    print(vetor_teste.tamanho_vetor())
    print(vetor_teste)
    print(vetor_teste.contem(4))
    print(vetor_teste)
    print(vetor_teste.indice(3))
elif menu == 2:
    lista_ligada = linkedlist()
    lista_ligada.append(2)







    

