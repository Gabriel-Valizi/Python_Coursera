n = int(input("Digite o valor de n: "))

quociente = n // 10
resto = n % 10

soma = resto

#print(quociente)
#print(resto)
#print(soma)

#print("-------------------------------------------")

while quociente > 10: 

    resto = quociente % 10
    quociente = quociente // 10

    soma = soma + resto

   # print(resto)
   # print(quociente)
    #print(soma)

    #print("-------------------------------------------")

soma_total = quociente + soma

print(soma_total)
#print("A soma total é", soma_total)
#print(quociente)
#print(soma)
#print(resto)