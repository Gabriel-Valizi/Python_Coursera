import re

######################################################################################################################################################################################
def le_assinatura():
    
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

######################################################################################################################################################################################
def le_textos():

    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''

    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    while texto:

        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

######################################################################################################################################################################################
def separa_sentencas(texto):

    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''

    sentencas = re.split(r'[.!?]+', texto)

    if sentencas[-1] == '':

        del sentencas[-1]

    return sentencas

######################################################################################################################################################################################
def separa_frases(sentenca):

    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''

    return re.split(r'[,:;]+', sentenca)

######################################################################################################################################################################################
def separa_palavras(frase):

    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''

    return frase.split()

######################################################################################################################################################################################
def n_palavras_unicas(lista_palavras):

    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''

    freq = dict()
    unicas = 0

    for palavra in lista_palavras:

        p = palavra.lower()

        if p in freq:

            if freq[p] == 1:

                unicas -= 1

            freq[p] += 1

        else:

            freq[p] = 1
            unicas += 1

    return unicas

######################################################################################################################################################################################
def n_palavras_diferentes(lista_palavras):

    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''

    freq = dict()

    for palavra in lista_palavras:

        p = palavra.lower()

        if p in freq:

            freq[p] += 1

        else:

            freq[p] = 1

    return len(freq)

######################################################################################################################################################################################
###### 1ª ASSINATURA: TAMANHO MÉDIO DE PALAVRA ######

def calcula_tamanho_medio_palavra (texto):

    sentencas = separa_sentencas (texto)  # separa o texto em sentenças
    total_palavras = 0
    total_caracteres = 0

    for sentenca in sentencas: # percorrendo o vetor sentencas, com várias sentencas

        frases = separa_frases (sentenca)  # separa a sentença em frases

        for frase in frases: # percorrendo o vetor frases, com várias frases

            palavras = separa_palavras (frase)  # separa a frase em palavras
            total_palavras += len (palavras)  # conta o número de palavras
            total_caracteres += sum (len(palavra) for palavra in palavras)  # soma o número de caracteres em todas as palavras

    if total_palavras == 0:  # evita divisão por zero
        
        return 0

    return total_caracteres / total_palavras  # tamanho médio de palavra

######################################################################################################################################################################################
###### 2ª ASSINATURA: RELAÇÃO TYPE-TOKEN ######

def calcula_relacao_type_token (texto):
    
    palavras_total = []  # Armazena todas as palavras do texto
    sentencas = separa_sentencas (texto)  # separa o texto em sentenças

    for sentenca in sentencas: # percorrendo o vetor sentencas, com várias sentencas

        frases = separa_frases (sentenca)  # separa a sentença em frases

        for frase in frases: # percorrendo o vetor frases, com várias frases

            palavras = separa_palavras (frase)  # separa a frase em palavras
            palavras_total.extend(palavras)  # Adiciona todas as palavras à lista

    total_palavras = len(palavras_total)
    total_palavras_diferentes = n_palavras_diferentes(palavras_total)

    if total_palavras == 0:  # evita divisão por zero
        
        return 0

    return total_palavras_diferentes / total_palavras

######################################################################################################################################################################################
###### 3ª ASSINATURA: RAZÃO HAPAX LEGOMANA ######

def calcula_razao_hapax_legomana (texto):

    palavras_total = []  # Armazena todas as palavras do texto
    sentencas = separa_sentencas (texto)  # separa o texto em sentenças

    for sentenca in sentencas: # percorrendo o vetor sentencas, com várias sentencas

        frases = separa_frases (sentenca)  # separa a sentença em frases

        for frase in frases: # percorrendo o vetor frases, com várias frases

            palavras = separa_palavras(frase)
            palavras_total.extend(palavras)  # Adiciona todas as palavras à lista

    total_palavras = len(palavras_total)
    total_palavras_unicas = n_palavras_unicas(palavras_total)

    if total_palavras == 0:  # evita divisão por zero
        
        return 0

    return total_palavras_unicas / total_palavras

######################################################################################################################################################################################
###### 4ª ASSINATURA: TAMANHO MÉDIO DE SENTENÇA ######

def calcula_tamanho_medio_sentenca (texto):

    sentencas = separa_sentencas (texto)  # separa o texto em sentenças
    total_sentencas = len (sentencas)
    total_caracteres = 0

    for sentenca in sentencas:

        # Removendo pontuações que separam as sentenças
        sentenca_sem_pontuacao = re.sub(r'[.!?]+', '', sentenca)
        total_caracteres += len(sentenca_sem_pontuacao)  # soma o número de caracteres em todas as sentenças

    total_sentencas = len(sentencas)

    if total_sentencas == 0:  # evita divisão por zero
        
        return 0

    return total_caracteres / total_sentencas  # tamanho médio de sentença

######################################################################################################################################################################################
###### 5ª ASSINATURA: COMPLEXIDADE DE SENTENÇA ######

def calcula_complexidade_sentenca (texto):

    sentencas = separa_sentencas (texto)  # separa o texto em sentenças
    total_sentencas = len (sentencas)
    total_frases = 0

    for sentenca in sentencas: # percorrendo o vetor sentencas, com várias sentencas

        frases = separa_frases (sentenca)  # separa a sentença em frases
        total_frases += len (frases)

    if total_sentencas == 0:  # evita divisão por zero
        
        return 0

    return total_frases / total_sentencas  # complexidade de sentença

######################################################################################################################################################################################
###### 6ª ASSINATURA: TAMANHO MÉDIO DE FRASE ######
import re

def calcula_tamanho_medio_frase(texto):
    sentencas = separa_sentencas(texto)  # separa o texto em sentenças
    total_caracteres = 0
    total_frases = 0

    for sentenca in sentencas:
        frases = separa_frases(sentenca)  # separa a sentença em frases
        total_frases += len(frases)  # conta o número de frases

        for frase in frases:
            # Removendo pontuações que separam as frases
            frase_sem_pontuacao = re.sub(r'[,:;]+', '', frase)
            total_caracteres += len(frase_sem_pontuacao)  # soma o número de caracteres em todas as frases

    if total_frases == 0:  # evita divisão por zero
        return 0

    return total_caracteres / total_frases  # tamanho médio de frase

######################################################################################################################################################################################
def calcula_assinatura(texto):
    
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    # recebe vetor com texto e devolve vetor com 6 elementos --> 6 assinaturas

    # 1) Tamanho médio de palavra --> soma dos tamanhos das palavras dividida pelo número total de palavras
    tamanho_médio_da_palavra = calcula_tamanho_medio_palavra (texto)

    # 2) Relação Type-Token
    relacao_type_token = calcula_relacao_type_token (texto)

    # 3) Razão Hapax Legomana
    razao_hapax_legomana = calcula_razao_hapax_legomana (texto)

    # 4) Tamanho médio de sentença
    tamanho_médio_da_sentenca = calcula_tamanho_medio_sentenca (texto)

    # 5) Complexidade de sentença
    complexidade_da_sentenca = calcula_complexidade_sentenca (texto)

    # 6) Tamanho médio de frase
    tamanho_médio_da_frase = calcula_tamanho_medio_frase (texto)

    return [tamanho_médio_da_palavra, relacao_type_token, razao_hapax_legomana, tamanho_médio_da_sentenca, complexidade_da_sentenca, tamanho_médio_da_frase]

######################################################################################################################################################################################

def compara_assinatura(as_a, as_b):

    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    Somatorio = 0
    numero_traço = 0

    while numero_traço < 6:

        Diferenca = abs (as_a [numero_traço] - as_b [numero_traço])
        Somatorio += Diferenca
        numero_traço += 1

    S_grau_similaridade = Somatorio / 6    
    
    return S_grau_similaridade

######################################################################################################################################################################################

def avalia_textos(textos, ass_cp):

    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    
    maiores_diferencas = float('inf')   # inicializa com infinito, para que qualquer grau de similaridade calculado será menor que esse valor, 
                                        # permitindo que o primeiro texto processado seja considerado.
    texto_com_maior_probabilidade = -1  # inicializa com -1 para indicar que nenhum texto foi encontrado
                                        # servirá para armazenar o índice do texto que tiver a maior probabilidade de estar infectado.

    for i, texto in enumerate(textos):

        assinatura_texto = calcula_assinatura (texto)  # calcula a assinatura para o texto atual

        grau_similaridade = compara_assinatura (ass_cp, assinatura_texto)  # compara a assinatura do texto com a assinatura típica
        
        # Verifica se a diferença é a menor encontrada
        if grau_similaridade < maiores_diferencas:

            maiores_diferencas = grau_similaridade
            texto_com_maior_probabilidade = i + 1  # adiciona 1 para retornar o índice correto

    return texto_com_maior_probabilidade

######################################################################################################################################################################################

# Função Main

# ASSINATURA B!!!!!!!!!!!!!!!!!! 
# É o modelo que temos como entrada, do aluno infectado com COH-PIAH

# Chama a função le_assinatura (), que não recebe nada de parâmetro
# Ela retorna um vetor de 6 elementos, que são os 6 tipos de assinaturas
assinaturas_texto_b = le_assinatura()

# ASSINATURAS A!!!!!!!!!!!!!!!!!
# Para cada texto que o usuário der como entrada, será calculado sua assinatura

# Chama a função le_textos ()

textos_do_programa = le_textos()

# Avalia os textos com a assinatura típica
texto_com_maior_probabilidade = avalia_textos (textos_do_programa, assinaturas_texto_b)

print (f"O texto {texto_com_maior_probabilidade} tem maior probabilidade de ter sido infectado por COH-PIAH.")