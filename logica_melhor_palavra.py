'''Módulo responsável por calcular qual é a melhor palavra na rodada.'''



def calcula_melhor_palavra(banco_palavras, letras_validas, num_letras_validas):
    ''' 
    Função que irá realizar as comparações necessárias para definir qual é a melhor palavra e retornar essa informação.
    Para que isso seja feito de forma mais eficiente, reduz-se o número de comparação entre caracteres.
    Essa redução é alcançada ignorando palavras com mais caracteres que o número máximo de caracteres disponiveis na rodada e,
    ignorando também, palavras que tem pontuação de valor inferior ao da pontuação da melhor palavra atual. Além disso, 
    as comparações entre os caracteres de uma palavra e dos caracteres disponiveis na rodada são interrompidas no caso de 
    um caracter da palavra  não estar presente na lista de letras da rodada, ou, quando esse caracter está presente, 
    porém não em quantidade suficiente.
    No caso de múltiplas palavras possíveis com a pontuação mais alta, elas serão salvas em uma lista que será posteriormente
    enviada para a função "Desempate".
    '''

    pontuacao_maxima = 0
    break_flag = False
    palavras_maior_valor = list()
    for palavra in banco_palavras:
        count = 0
        break_flag = False
        if ((len(palavra) <= num_letras_validas) and (banco_palavras[palavra].pontuacao >= pontuacao_maxima)) :     
            # Descarta palavras que tem tamanho maior que o total de letras disponiveis para serem formadas e 
            # palavras de pontuação inferior a pontuação da palavra de maior valor atual.
            for char in banco_palavras[palavra].contagem_letras:
                if ((char not in letras_validas) or (char in letras_validas 
                and letras_validas[char] < banco_palavras[palavra].contagem_letras[char])):    
                    # Descarta palavras que não podem ser formadas pela falta de letras na rodada.  
                    break_flag = True
                    break
            if not break_flag: 
                # Se passou por todos os caracteres e não definiu a break_flag para True, 
                #significa que a palavra deve ser considerada para a posição de melhor palavra.
                if palavras_maior_valor and banco_palavras[palavras_maior_valor[0]].pontuacao < banco_palavras[palavra].pontuacao:
                    # Reinicia a lista de palavras que fazem o maior número de pontos no caso de uma palavra com maior valor.
                    palavras_maior_valor.clear()
                    palavras_maior_valor.append(palavra)
                    pontuacao_maxima = banco_palavras[palavras_maior_valor[0]].pontuacao
                else:
                    # Palavras que podem ser formadas e que tem o mesmo valor da de valor máximo atual são salvas. 
                    palavras_maior_valor.append(palavra)
                    pontuacao_maxima = banco_palavras[palavras_maior_valor[0]].pontuacao
    melhor_palavra = ''
    if len(palavras_maior_valor) > 1:
        melhor_palavra = desempate(palavras_maior_valor)
    elif len(palavras_maior_valor) == 1:
        melhor_palavra = palavras_maior_valor[0]                    
    return melhor_palavra

def desempate(palavras_maior_valor):
    '''
    Função que irá retornar qual palavra será a melhor no caso de múltiplas palavras possíveis com a pontuação mais alta.
    Os critérios de desempate são os definidos no documento fornecidos pela empresa.
    '''

    index = 0
    tam_menor_word = len(palavras_maior_valor[0])
    palavras_menor_len = list()
    melhor_palavra = ''
    for word in palavras_maior_valor:       #desempate por tamanho de palavra
        if len(word) < tam_menor_word:
            tam_menor_word = len(word)
            palavras_menor_len.clear()
            palavras_menor_len.append(word)
        elif len(word) == tam_menor_word:
            palavras_menor_len.append(word)
    if len(palavras_menor_len) > 1:     #desempate por ordem alfabética
        palavras_menor_len.sort()
    return palavras_menor_len[0]