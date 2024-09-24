def maior_elemento (lista):

    maximo = max (lista)
    
    return maximo

#################################

n = int(input("Digite um número inteiro que corresponderá ao tamanho da sua lista: "))

i = 0
lista_inteiros = []

while i < n:

    elemento = int(input("Digite um número inteiro: "))
    lista_inteiros.append(elemento)
    i += 1

inteiro_maximo = maior_elemento (lista_inteiros)

print(inteiro_maximo)