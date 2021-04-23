#PARA EXECUTAR O PROGRAMA NO TERMINAL BASTA DIGITAR: python3 main.py
'''
Para o entendimento da lógica do programa é necessário que entenda-se o que está atribuido a algumas variáveis:

"dicionario_pontuacao": associa as letras a seus valores;

"banco_palavras": inicialmente é uma lista que representa o banco de palavras que foi fornecido na especificação, apenas está tratado 
                  para as palavras estarem em letras minúsculas e sem acentos (o código utilizado para o tratamento do banco também 
                  está disponível, contudo esse tratamento não é realizado aqui, pois, considerando que o banco de palavras é imutável, 
                  ganha-se performance ao executar esse tratamento em um código externo e apenas colar o resultado aqui. O código está 
                  no arquivo "converter_texto.py"). Esse banco, no entanto, é modificado através da função "modifica_banco_palavras" 
                  do módulo "modificacao_banco_palavras" e passa a ser um dicionário que tem como chave as palavras do banco_palavras
                  original e, como valor, instâncias da classe "ValorBancoPalavras", também definida no módulo "modificacao_banco_palavras".
                  Informações sobre essa função e essa classe estão disponíveis no módulo "modificacao_banco_palavras";

"letras_validas": dicionário que tem, como chave, as letras digitadas pelo usuário na rodada que são chaves válidas no 
                  "dicionario_pontuacao" e, como valor, o número de vezes que essas letras ocorrem.

A lógica do programa se baseia em percorrer as palavras do banco de palavras e verificar se é possível formá-las com os caracteres
inseridos pelo usuário. Essa verificação é feita utilizando-se dos caracteres únicos de cada palavra, assim como, quantos de cada um deles
são necessários em uma palavra. Compare-se esses valores com as chaves da variável "letras_validas" e o valor associado a essas chaves, sendo
uma palavra possível quando todos os seus caracteres únicos são chaves válidas para a variável "letras_validas" e o número de ocorrências
desses caracteres é menor ou igual ao valor associado a "letras_validas" quando usa-se como chave para ela os respectivos caracteres.
É IMPORTANTE RESSALTAR QUE NEM TODAS AS PALAVRAS DO BANCO TEM SEUS CARACTERES COMPARADOS E, TAMBÉM, QUE NÃO OBRIGATORIAMENTE TODOS OS
CARACTERES DE UMA PALAVRA SERÃO COMPARADOS. Ignoram-se palavras com mais caracteres que o número máximo de caracteres validos na rodada 
e, ignoram-se também, palavras que tem pontuação de valor inferior ao da pontuação da(s) palavra(s) que no momento da iteração
ocupam o lugar de melhor palavra. Além disso, as comparações entre os caracteres de uma palavra e dos caracteres disponiveis na rodada 
são interrompidas no caso de  um caracter da palavra  não estar presente na lista de letras da rodada, ou, quando esse caracter está 
presente, porém não em quantidade suficiente. A função responsável por percorrer o banco de palavras e identificar qual a melhor palavra
é a função "calcula_melhor_palavra" do módulo "logica_melhor_palavra", para mais detalhes sobre essas exceções, por favor, 
acesse o módulo citado.

A contagem dos pontos é feita, inicialmente, quando chama-se a função "modifica_banco_palavras". Para não ser necessário calcular a 
pontuação de uma palavra toda vez que ela for usada para uma comparação, a classe "ValorBancoPalavras" possui um campo responsável por
armazenar a pontuação de cada palavra. Contudo, como foi implementado o artigo extra da especificação, "bônus de posição", a pontuação das
palavras são recalculadas sempre que uma nova posição de pontuação bônus for definida pelo usuário e esse novo valor será armazenado pela
variável "pontuacao" da classe "ValorBancoPalavras".
'''


import string
import tratamento_entrada
import logica_melhor_palavra
import modificacao_banco_palavras
import printa_resultado


dicionario_pontuacao = {"a" : 1, "b" : 3, "c" : 3, "d" : 2, "e" : 1, "f" : 5, "g" : 2, "h" : 5, "i" : 1, "j" : 8, "l" : 1,
"m" : 3, "n" : 1, "o" : 1, "p" : 3, "q" : 13, "r" : 1, "s" : 1, "t" : 1, "u" : 1, "v" : 5, "x" : 8, "z" : 13} 
banco_palavras = ['abacaxi', 'manada', 'mandar', 'porta', 'mesa', 'dado', 'mangas', 'ja', 'coisas', 'radiografia', 
'matematica', 'drogas', 'predios', 'implementacao', 'computador', 'balao', 'xicara', 'tedio', 'faixa', 'livro', 
'deixar', 'superior', 'profissao', 'reuniao', 'predios', 'montanha', 'botanica', 'banheiro', 'caixas', 'xingamento', 
'infestacao', 'cupim', 'premiada', 'empanada', 'ratos', 'ruido', 'antecedente', 'empresa', 'emissario', 'folga', 'fratura', 
'goiaba', 'gratuito', 'hidrico', 'homem', 'jantar', 'jogos', 'montagem', 'manual', 'nuvem', 'neve', 'operacao', 'ontem', 
'pato', 'pe', 'viagem', 'queijo', 'quarto', 'quintal', 'solto', 'rota', 'selva', 'tatuagem', 'tigre', 'uva', 'ultimo', 
'vituperio', 'voltagem', 'zangado', 'zombaria', 'dor']
banco_palavras = modificacao_banco_palavras.modifica_banco_palavras(banco_palavras, dicionario_pontuacao)
# O banco passa a associar as palavra com suas pontuações e a quantidade de cada letra única que as formam.
# Mais informações sobre essa modificação podem ser obtidas acessando o módulo "modificacao_banco_palavras".

print("---------------------------------------------------------------------------------")
print("\nPara finalizar o programa digite 'SAIR' como as letras disponíveis na jogada.\n")
print("---------------------------------------------------------------------------------\n")
letras_rodada = input("Digite as letras disponíveis nesta jogada: ")
posicao_bonus_antiga = 0
while (letras_rodada != "SAIR"):

    posicao_bonus = int(input("Digite a posição bônus: "))
    if posicao_bonus_antiga != posicao_bonus:
        if posicao_bonus >= 0:
            posicao_bonus_antiga = posicao_bonus
            for palavra in banco_palavras:
                banco_palavras[palavra].set_pontuacao_bonus(palavra, dicionario_pontuacao, posicao_bonus)
                # Modifica a pontuação de cada palavra do banco de acordo com a posição bônus fornecida.
        elif posicao_bonus < 0:
            print("Posição inválida!")
            continue

    letras_validas, letras_nao_usadas, num_letras_validas = tratamento_entrada.trata_entrada(letras_rodada, dicionario_pontuacao)
    # Separa e formata a entrada da maneira necessária para ser usada no cálculo da melhor palavra.
    # Mais informações sobre esse tratamento estão disponíveis no módulo "tratamento_entrada"

    melhor_palavra = logica_melhor_palavra.calcula_melhor_palavra(banco_palavras, letras_validas, num_letras_validas)
    # Cálculo da melhor palavra possível é realizado aqui. Informações sobre o funcionamento desse função são encontradas 
    # no módulo "logica_melhor_palavra".

    if melhor_palavra != '':
        printa_resultado.imprime_resultado(melhor_palavra, banco_palavras[melhor_palavra].pontuacao, letras_validas, letras_nao_usadas)
    else:
        print("\nNenhuma palavra encontrada.")
        print("Sobraram:", str.upper(letras_rodada))
        print("\n---------------------------------------------------------------------------------\n")
    letras_rodada = input("Digite as letras disponíveis nesta jogada: ")
    if letras_rodada == "SAIR":
        print("Programa finalizado!")