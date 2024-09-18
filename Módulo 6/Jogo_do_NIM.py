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

# Função principal
def main ():

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")

    tipo_de_jogo = int(input("Escolha:"))

    if tipo_de_jogo == 1:

        print("\nVocê escolheu uma partida isolada!\n")
        partida ()

    elif tipo_de_jogo == 2:

        print("\nVocê escolheu um campeonato!\n")
        campeonato()

################################################################################

# Execução do programa
main ()


################################################################################
################################################################################
################################################################################
################################################################################
################################################################################




    # Função que representa a jogada do computador
def computador_escolhe_jogada(n, m):
    # O computador tenta deixar múltiplos de (m+1)
    jogada = 1
    while jogada <= m:
        if (n - jogada) % (m + 1) == 0:
            return jogada
        jogada += 1
    # Se não conseguir, tira o máximo possível
    return m

# Função que representa a jogada do usuário
def usuario_escolhe_jogada(n, m):
    jogada_valida = False
    while not jogada_valida:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada >= 1 and jogada <= m and jogada <= n:
            jogada_valida = True
        else:
            print("Oops! Jogada inválida! Tente de novo.")
    return jogada

# Função que executa uma partida
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    # Decidindo quem começa
    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_computador = False
    else:
        print("Computador começa!")
        vez_do_computador = True

    # Laço principal da partida
    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peça(s).")
            vez_do_computador = False
        else:
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peça(s).")
            vez_do_computador = True
        n -= jogada
        print(f"Agora restam {n} peça(s) no tabuleiro.\n")

    # Mensagem final
    if vez_do_computador:
        print("Você ganhou!")
    else:
        print("O computador ganhou!")

# Função que executa um campeonato de 3 partidas
def campeonato():
    placar_computador = 0
    placar_usuario = 0

    for _ in range(3):
        print("\n**** Nova partida ****\n")
        partida()
        if vez_do_computador:
            placar_usuario += 1
        else:
            placar_computador += 1

    # Placar final
    print(f"\nPlacar: Você {placar_usuario} X {placar_computador} Computador")

# Função principal
def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")

    escolha = int(input())

    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
    elif escolha == 2:
        print("\nVocê escolheu um campeonato!\n")
        campeonato()

# Executa o programa
main()
