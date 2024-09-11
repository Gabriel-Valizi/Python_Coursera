import math

x1 = int(input("Escreva um número inteiro: "))
y1 = int(input("Escreva um número inteiro: "))
x2 = int(input("Escreva um número inteiro: "))
y2 = int(input("Escreva um número inteiro: "))

d = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

if d >= 10:

    print("longe")

else:

    print("perto")