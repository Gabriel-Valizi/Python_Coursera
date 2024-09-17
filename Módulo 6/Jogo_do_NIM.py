#def campeonato ():

    #chamar partida 3 vezes

##############################################################################

def computador_escolhe_jogada (n, m):

    # COMPUTADOR COMEÇANDO............
    
    tiradas = 0
    deixadas = n - tiradas
    resto = deixadas % (m+1)

    return tiradas

    # USUARIO COMEÇANDO............

    tiradas = 0
    deixadas = n - tiradas
    resto = deixadas % (m+1)

    return tiradas
    
##############################################################################

def usuario_escolhe_jogada (n, m):

    tiradas = int(input("Quantas peças você vai tirar?"))

    if tiradas > m:

        print("Oops! Jogada inválida! Tente de novo.")

    else: 

        print("Você tirou", tiradas, "peças.")
        deixadas = n - tiradas
        print("Agora restam apenas", deixadas, "peças no tabuleiro")

    return tiradas
    
################################################################################

def partida ():

    i = 1
    fim_de_jogo = False

    while not fim_de_jogo:

        print("**** Rodada", i, "****")

        n = int(input("Quantas peças?"))
        m = int(input("Limite de peças?"))

        resto = n % (m+1)

        # são múltiplos
        if resto == 0:

            print("Você começa!")
            computador_escolhe_jogada (n, m)

        else:

            print("Computador começa!")
            usuario_escolhe_jogada (n, m)

################################################################################

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada\n2 - para jogar um campeonato 2")

tipo_de_jogo = int(input("Escolha:"))

if tipo_de_jogo == 1:

    print("Você escolheu uma partida isolada!")
    partida ()

elif tipo_de_jogo == 2:

    print("Você escolheu um campeonato!")
    #campeonato()