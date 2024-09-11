numero = int(input("Escreva um número inteiro: "))

resto1 = numero % 3
resto2 = numero % 5

if resto1 == 0 and resto2 == 0:

    print("FizzBuzz")

else: 

    print(numero)