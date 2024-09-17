############ Função Verificar Primo ############

def verificar_primo (x):

    divisor = 2
    resto = 1

    # Verifica se x = 2 (já é primo)
    if x == 2:

        return "É primo"

    # x != 2
    else:

        while resto != 0 and divisor != x:

            resto = x % divisor
            divisor = divisor + 1

            # Verifica se é primo
            if divisor == x:

                return "É primo"

            # Verifica se não é primo
            elif resto == 0:

                return "Não é primo"

############ Função Maior Primo ############

def maior_primo (x):

    # Verifica se o número é menor que 2
    if x < 2:
        
        return "Tem que ser um número inteiro maior ou igual a 2!!"
    
    aux = verificar_primo(x)

    # x >= 2
    if aux == "É primo":

        return x
    
    else:
        
        y = x
        primo = 1
        while primo:

            y = y - 1
            aux2 = y
            aux2 = verificar_primo(y)

            if aux2 == "É primo":

                primo = 0
                return y

############ Função Main ############

a = int(input("Digite um número inteiro maior ou igual a 2: "))

# retorno = número inteiro
maior_num_primo = maior_primo (a)

print(maior_num_primo)