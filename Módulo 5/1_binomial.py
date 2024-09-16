def fatorial (n):

    resultado = 1
    contador = 1

    while contador <= n:

        resultado *= contador
        contador += 1

    return resultado

# Função main

n = int(input("Digite o valor de n: "))

if n < 0:

    print("O fatorial não está definido para números negativos.")

else:

    fat = fatorial(n)
    print(fat)
