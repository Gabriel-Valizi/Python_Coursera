lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# dá pra usar no if como condição
print(1 in lista)
print(100 in lista)

# append --> altera lista existente
lista.append(100)

lista_2 = [11, 12, 13]

# concatenação de listas -->  só pode concatenar lista com lista, e não lista com qualquer coisa
# cria nova lista
print(lista + lista_2)

# repete os valores como se fosse concatenação
lista_duplicado = lista * 2
print(lista_duplicado)

# remoção em listas
del lista[0]
print(lista)
del lista[0:3]
print(lista)

