'''
Este módulo é importante, pois define qual será o formato do banco de palavras. 
Possui, além da definição da classe que representa os valores associados a uma palavra no banco de palavras, funções para os cálculos
e modificações desses valores e também a função para transformar o banco de palavras inicial em um dicionário no qual as chaves são
as palavras do banco original e os valores são instâncias da classe definida nesse módulo.
'''

import collections


class ValorBancoPalavras:
    '''
    Classe que define os valores associados a cada chave do banco de palavras na forma de dicionário.
    Variável "pontuacao_base" armazena a pontuação da palavra sem o bônus de posição.
    Variável "pontuacao" armazena a pontuação da palavra com o bônus de posição.
    Variável "contagem_letras" é um dicionário que associa as letra únicas de uma palavra com o número de ocorrências delas.
    '''

    def __init__(self, palavra, dicionario_pontuacao):
        self.pontuacao_base = self.calcula_pontuacao_base(palavra, dicionario_pontuacao)
        self.pontuacao = self.pontuacao_base
        self.contagem_letras = dict(collections.Counter(palavra)) 
    
    def calcula_pontuacao_base(self, palavra, dicionario_pontuacao):
        ''' Retorna qual é a pontuação base da palavra percorrendo os caracteres que a formam e somando seus valores.'''

        pontuacao = 0
        for letra in palavra:
            pontuacao += dicionario_pontuacao[letra]
        return pontuacao

    def set_pontuacao_bonus(self, palavra, dicionario_pontuacao, index):
        ''' Redefine o valor da variável "pontuacao" de acordo com o bônus de posição de cada rodada.'''

        if index == 0:
            self.pontuacao = self.pontuacao_base
        elif index <= len(palavra):
            self.pontuacao = self.pontuacao_base + dicionario_pontuacao[palavra[index - 1]]


def modifica_banco_palavras(banco_palavras, dicionario_pontuacao):
    ''' 
    Função que irá criar um novo banco de palavras, baseado no banco como visto no módulo "main", que será um dicionário que associa
    as palavras do banco com os valores definidos na classe "ValorBancoPalavras". Essa banco modificado é então retornado e atribuído
    a váriavel "banco_palavras" no módulo "main". 
    '''

    banco_palavras_modificado = dict()
    for palavra in banco_palavras:
        banco_palavras_modificado[palavra] = ValorBancoPalavras(palavra, dicionario_pontuacao)
    return banco_palavras_modificado
