'''Neste módulo é realizado o tratamento dos caracteres inseridos como letras disponíveis na jogada'''

import collections


def trata_entrada(letras_rodada, dicionario_pontuacao):
    '''
    Recebe como entrada todas as letras inseridas pelo usuário e o dicionário de letras que pontuam. Transforma
    todos as letras inseridas pelo usuário em letras minúsculas e realiza as operações necessárias para retornar três valores:
    letras_validas: dicionário que tem como chaves os caracteres que podem compor uma palavra do banco de palavras e como 
                   valor o número de vezes que esses caracteres foram inseridos pelo usuário;
    letras_nao_usadas: lista de caracteres inseridos pelo usuário que não podem compor uma palavra do banco;
    num_letras_validas: número total de caracteres inseridos pelo usuário que podem compor uma palavra do banco de palavras.
    '''

    letras_validas = str.lower(letras_rodada) 
    letras_nao_usadas = list()
    for char in letras_validas:      
        if char not in dicionario_pontuacao.keys():
            letras_validas = letras_validas.replace(char, "")
            letras_nao_usadas.append(char)      #Caracteres inválidos são salvos para serem exibidos no final.
    num_letras_validas = len(letras_validas)     #Esse valor será utilizado posteriormente para o calculo da palavra possível de maior pontuação
    letras_validas = dict(collections.Counter(letras_validas))
    return letras_validas, letras_nao_usadas, num_letras_validas 