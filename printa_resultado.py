''' Módulo responsável pela exibição do resultado obtido.'''

import collections

def imprime_resultado(melhor_palavra, pontuacao, letras_validas, letras_nao_usadas):
    '''Essa função apenas realiza algumas operações sobre as letras da rodada para exibir a saída no formato pedido.'''

    print(f"\n{str.upper(melhor_palavra)}, palavra de {pontuacao} pontos.")
    count_letras_best_word = dict(collections.Counter(melhor_palavra))
    for char in letras_validas: 
        # Irá comparar todas as letras inseridas pelo usuário com as que foram necessárias para formar a palavra
        # para poder exibir quais letras não foram utilizadas.
        if char in count_letras_best_word:
            letras_validas[char] = letras_validas[char] - count_letras_best_word[char]
            if letras_validas[char] > 0:
                for i in range(letras_validas[char]):
                    letras_nao_usadas.append(char)
        else:
            for i in range(letras_validas[char]):
                letras_nao_usadas.append(char)
    if letras_nao_usadas:
        print("Sobraram:", ", ".join([x.upper() for x in letras_nao_usadas]) + ".")
    print("\n---------------------------------------------------------------------------------\n")