# Função max

def maximo (x, y):
    
    if x > y:

        return x
    
    else:

        return y

# Função main

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

maior = maximo(x, y)
print(maior)