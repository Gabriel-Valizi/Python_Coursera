import math

def é_hipotenusa (hipotenusa):

    # um lado do triângulo não pode ser 0
    i = j = 1

    # enquanto o cateto i for menor que a hipotenusa "hipotenusa"
    while i < hipotenusa:

        # enquanto o cateto j for menor que a hipotenusa "hipotenusa"
        while j < hipotenusa:

            # calcula a raiz quadrada da soma dos quadrados dos catetos = "teste" = hipotenusa desses catetos
            teste = math.sqrt((i**2)+(j**2))

            # se teste for igual ao nosso numero inputado "hipotenusa"
            if hipotenusa == teste:

                # retorna hipotenusa, ou seja, é hipotenusa
                return hipotenusa
        
            j = j + 1

        j = 1
        i = i + 1

    return "Não é hipotenusa"

################################################################

def soma_hipotenusas (n):

    contador = 1
    soma = 0
    while contador <= n:

        testeeee = é_hipotenusa(contador)

        if testeeee == contador:

            soma = soma + testeeee
            #print("Aqui, contador =", contador, "e teste =", testeeee)
            #print("Aqui, soma =", soma)
            contador += 1

        else:

            #print("Aqui, contador =", contador, "e teste =", testeeee)
            #print("Aqui, soma =", soma)
            contador += 1

    return soma

################################################################

n = int(input("Digite um número inteiro positivo: "))

if n <= 0:

    print("Número inválido! Deve ser >= a 0!!")

else:

    #soma_hipotenusas (n)
    soma_das_hipotenusas = soma_hipotenusas(n)
    print(soma_das_hipotenusas)