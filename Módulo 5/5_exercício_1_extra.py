############ Função FizzBuzz ############

def fizzbuzz (x):

    resto = x % 3
    resto2 = x % 5

    if resto == 0 and resto2 != 0:

        x = "Fizz"
        return x

    elif resto != 0 and resto2 == 0:

        x = "Buzz"
        return x
    
    elif resto == 0 and resto2 == 0:

        x = "FizzBuzz"
        return x
    
    elif resto != 0 and resto2 != 0:

        return x

############ Função Main ############

numero = int(input("Digite um número inteiro: "))

resultado = fizzbuzz (numero)

print(resultado)

