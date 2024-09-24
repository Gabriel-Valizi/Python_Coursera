def remove_repetidos(lista):

    lista.sort()  # Ordena a lista in-place
    lista_sem_repetidos = []  # Lista para armazenar os elementos sem repetição

    # Percorre a lista e adiciona os elementos únicos à nova lista
    for i in lista:

        if i not in lista_sem_repetidos:

            lista_sem_repetidos.append(i)

    return lista_sem_repetidos

##############################

n = int(input("Digite um número inteiro que corresponderá ao tamanho da sua lista: "))

i = 0
lista_inteiros = []

while i < n:

    elemento = int(input("Digite um número inteiro: "))
    lista_inteiros.append(elemento)
    i += 1

lista_sem_repetição = remove_repetidos(lista_inteiros)

print(lista_sem_repetição)
