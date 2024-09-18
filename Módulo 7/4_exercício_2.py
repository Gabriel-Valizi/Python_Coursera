largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

# Laço para a altura do retângulo
a = 1
while a <= altura:

    # Para as bordas superior e inferior
    if a == 1 or a == altura:

        l = 1

        while l <= largura:

            print("#", end='')
            l = l + 1

        print()

    # Para as bordas laterais e o preenchimento interno
    else:
        
        l = 1
        while l <= largura:

            if l == 1 or l == largura:

                print("#", end='')

            else:

                print(" ", end='')

            l = l + 1

        print()

    a = a + 1
