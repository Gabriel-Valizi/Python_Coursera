def n_primos (inteiro):

    # inteiro = 2 --> quantidade = 1
    if inteiro == 2:

        return 1
    
    # inteiro > 2 --> quantidade > 1
    # exemplo:
    # inteiro = 3  -->  quantidade  =  2 (2 e 3)
    # inteiro = 4  -->  quantidade  =  2 (2 e 3)
    # inteiro = 5  -->  quantidade  =  3 (2, 3 e 5)
    # inteiro = 10 -->  quantidade  =  4 (2, 3, 5 e 7)
    else:

        # ver se cada número, de 2 a "inteiro", é primo
        # usar loop (while) indo de "contador" até "inteiro"

        # inicializando quantidade_primos como 1, pois sempre haverá o 2
        quantidade_primos = 1 

        contador = 3

        while contador <= inteiro:

            # verificar se contador é primo

            divisor = 2
            resto = 1

            while resto != 0 and divisor != contador:

                resto = contador % divisor
                divisor = divisor + 1

                if resto == 0:

                    #print("Contador NÃO É primo")
                    quantidade_primos = quantidade_primos + 1

                #elif divisor == contador:
    
                    #print("Contador É primo")

            contador = contador + 1

        return quantidade_primos

        
################################################################

n = int(input("Digite um número inteiro maior ou igual a 2: "))

if n < 2:

    print("Número inválido! Deve ser >= a 2!!")

else:

    quantidade = n_primos(n)
    print(quantidade)