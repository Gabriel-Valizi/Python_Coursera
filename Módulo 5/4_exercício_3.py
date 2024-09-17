# Função Verificar Vogal

def vogal (x):
    
    if x == "a" or x == "A" or x == "e" or x == "E" or x == "i" or x == "I" or x == "o" or x == "O" or x == "u" or x == "U":

        x = True
        return x
    
    else:

        x = False
        return x
  
# Função Main

letra = input("Digite uma letra: ")

é_ou_não_é_vogal = vogal(letra)

print(é_ou_não_é_vogal)