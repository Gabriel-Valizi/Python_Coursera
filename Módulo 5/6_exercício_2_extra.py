# Função max

def maximo (x, y, z):
    
    if x >= y and x >= z:

        return x
    
    elif y >= x and y >= z:

        return y
    
    elif z >= x and z >= y:

        return z

# Função main

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

maior = maximo(x, y, z)

print(maior)