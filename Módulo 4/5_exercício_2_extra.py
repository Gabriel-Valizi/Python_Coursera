n = int(input("Digite um número inteiro: "))

ultimo_digito = n % 10
n = n // 10
adjacente_igual = False

while n > 0:

    proximo_digito = n % 10

    if proximo_digito == ultimo_digito:

        adjacente_igual = True
        break

    ultimo_digito = proximo_digito
    n = n // 10

if adjacente_igual:

    print("sim")

else:
    
    print("não")