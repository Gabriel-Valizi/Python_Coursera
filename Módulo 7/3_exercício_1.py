largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

l = a = 1
while a <= altura:

    while l <= largura:

        print("#", end='')
        l = l + 1

    print()    
    a = a + 1
    l = 1