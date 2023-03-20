from vetores import vetor

print(30 * "-", "MENU", 30*"-")
print("1. Vetores")
print("2. Listas Ligadas")

menu = int(input("Digite a opção desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(5)
    #vetor_teste.inserir_elemento_posicao(1, 0)
    #vetor_teste.inserir_elemento_posicao(22, 1)
    vetor_teste.inserir_elemento_final(2)
    vetor_teste.inserir_elemento_final(33)
    vetor_teste.inserir_elemento_final(44)
    print(vetor_teste.listar_elemento(0))
    print(vetor_teste.listar_elemento(1))
    print(vetor_teste.listar_elemento(2))
