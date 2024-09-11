n = int(input("Digite o valor de n: "))

# Verifica se o número é não-negativo
if n < 0:

    print("O fatorial não está definido para números negativos.")

else:

    resultado = 1
    contador = 1

    # Calcula o fatorial usando um loop while
    while contador <= n:
        resultado *= contador
        contador += 1

    #print(f"O fatorial de {n} é {resultado}.")
    print(resultado)