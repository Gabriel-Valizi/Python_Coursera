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

################################################################################

# Função que representa a jogada do usuário
def usuario_escolhe_jogada(n, m):

    jogada_valida = False

    while not jogada_valida:

        jogada = int(input("Quantas peças você vai tirar? "))

        if jogada >= 1 and jogada <= m and jogada <= n:

            jogada_valida = True

        else:
            print("\nOops! Jogada inválida! Tente de novo.\n")

    return jogada
    
################################################################################

# Função que executa uma partida
def partida ():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças? "))

    # Decidindo quem começa
    resto = n % (m + 1)

    if resto == 0: # são múltiplos

        print("\nVocê começa!\n")
        vez_do_computador = False

    else: # resto != 0 (não são múltiplos)

        print("\nComputador começa!\n")
        vez_do_computador = True

    # Laço principal da partida

    while n > 0:

        if vez_do_computador: # é a vez do computador
                
            jogada = computador_escolhe_jogada(n, m)
            print(f"O computador tirou {jogada} peça(s).")
            vez_do_computador = False

        else: # não é a vez do computador
                
            jogada = usuario_escolhe_jogada(n, m)
            print(f"Você tirou {jogada} peça(s).")
            vez_do_computador = True

        n = n - jogada
        print(f"Agora restam {n} peça(s) no tabuleiro.\n")

    # Mensagem final
    if vez_do_computador:

        print("Fim de jogo! Você ganhou!")
        return "usuario"

    else:

        print("Fim de jogo! O computador ganhou!")
        return "computador"

################################################################################

# Função que executa um campeonato de 3 partidas
def campeonato():

    placar_computador = 0
    placar_usuario = 0
    rodada = 1

    while rodada <= 3:

        print(f"\n**** Rodada {rodada} ****\n")
        vencedor = partida()

        if vencedor == "computador":

            placar_computador += 1

        else:

            placar_usuario += 1

        rodada += 1

    print("\n**** Final do campeonato! ****\n")

    # Placar final
    print(f"Placar final: Você {placar_usuario} X {placar_computador} Computador")

################################################################################

# Função principal
def main ():

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")

    tipo_de_jogo = int(input("Escolha: "))

    if tipo_de_jogo == 1:

        print("\nVocê escolheu uma partida isolada!\n")
        partida ()

    elif tipo_de_jogo == 2:

        print("\nVocê escolheu um campeonato!")
        campeonato()

################################################################################

# Execução do programa
main ()