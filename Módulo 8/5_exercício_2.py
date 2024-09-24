def soma_elementos (lista):

    inteiro = 0
    for i in lista:

        inteiro = inteiro + i
        i += 1

    return inteiro

#################################

n = int(input("Digite um número inteiro que corresponderá ao tamanho da sua lista: "))

i = 0
lista_inteiros = []

while i < n:

    elemento = int(input("Digite um número inteiro: "))
    lista_inteiros.append(elemento)
    i += 1

soma = soma_elementos (lista_inteiros)

print(soma)