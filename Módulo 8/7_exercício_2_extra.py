def ordem_inversa(lista):
    nova_lista_invertida = []
    tamanho = len(lista)

    # Percorre a lista de trás para frente, adicionando elementos à nova lista
    for i in range(tamanho - 1, -1, -1):  # Inicia do último elemento até o primeiro
        nova_lista_invertida.append(lista[i])

    return nova_lista_invertida

#################################

# Inicializa a lista

lista_inteiros = []
elemento = 1

while elemento != 0:

    elemento = int(input("Digite um número inteiro (0 para encerrar): "))

    if elemento != 0:  # Apenas adiciona a lista se não for 0
        lista_inteiros.append(elemento)

# Chama a função para inverter a lista
lista_invertida = ordem_inversa(lista_inteiros)

# Imprime a lista invertida como números em cada linha
for i in lista_invertida:

    print(i)

