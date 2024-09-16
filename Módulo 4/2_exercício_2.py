n = int(input("Digite o valor de n: "))

# Verifica se o número é não-negativo
if n < 0:

    print("Tem que ser um número positivo!!")

else:

    contador = 1

    while contador <= n:

        print(2*contador - 1)
        contador = contador + 1