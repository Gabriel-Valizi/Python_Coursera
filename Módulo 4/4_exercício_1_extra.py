n = int(input("Digite o valor de n: "))

# Verifica se o número é não-negativo
if n < 0:

    print("Tem que ser um número positivo!!")

else:
    
    divisor = 2
    resto = 1

    if n == 2:

        print("primo")

    else:

        while resto != 0 and divisor != n:

            resto = n % divisor
            divisor = divisor + 1

            if resto == 0:

                print("não primo")

            elif divisor == n:

                print("primo")