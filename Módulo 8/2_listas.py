def clone (lista):

    clone = []

    for objeto in lista:

        clone.append(objeto)
    
    return clone

##########################################

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista [0:4])
print(lista[2:7])

inicio = lista [:4]
print(inicio)
final = lista [5:]
print(final)

lista_extra = clone (lista)

# para clonar, usar isso --> lista[:]

nova_lista = lista[:]
print(nova_lista)

print(lista_extra)
lista_extra[0] = 1000

print(lista)
print(lista_extra)

