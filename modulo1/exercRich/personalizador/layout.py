'''Imprime texto modificando a sua distribuição no espaço do terminal'''

from rich.layout import Layout
from rich.console import Console

def imprimeEsquerdaDireita(texto, isArquivo):
    '''Distribui o texto à esquerda e à direita do terminal.
    
    Recebe como parâmetro uma string 'texto' e uma variável booleana 'isArquivo' que indica se 'texto' é uma string
    comum ou caminho para um arquivo.
    Divide o terminal em dois lados: esquerda e direita. 
    Depois divide o texto ao meio e imprime a primeira parte à esquerda e a segunda parte à direita.'''

    layout = Layout()
    console = Console()
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as arq:
            leitor = arq.readlines()
            meio = len(leitor) // 2
            esquerda = "".join(leitor[0:meio])
            direita = "".join(leitor[meio:len(leitor)])
            
            
    else:
        meio = len(texto) // 2
        esquerda = texto[0:meio]
        direita = texto[meio:len(texto)]
    
    layout.split_row(Layout(name='left'), Layout(name='right'),)         
    layout['left'].update(esquerda)
    layout['right'].update(direita)
    console.print(layout, '\n')

def imprimeDiagonal(texto, isArquivo):
    '''Imprime o texto em uma parte superior, esquerda ou direita, e outra parte na divisão inferior oposta
    
    Recebe como parâmetro uma string 'texto' e uma variável booleana 'isArquivo' que indica se 'texto' é uma string
    comum ou caminho para um arquivo.
    Se 'isArquivo' é falso, imprime metade da string na parte superior direita e metade na parte inferior esquerda.
    Se 'isArquivo' for verdadeiro, imprime metade do conteúdo do arquivo na parte superior esquerda 
    e a outra metade na parte inferior direita.'''
    layout = Layout()
    console = Console()

    layout.split_row(Layout(name='left'), Layout(name='right'),)
    layout['left'].split_column(Layout(name='up-left'), Layout(name='down-left'),)
    layout['right'].split_column(Layout(name='up-right'), Layout(name='down-right'),)

    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as arq:
            leitor = arq.readlines()
            meio = len(leitor) // 2
            cima = "".join(leitor[0:meio])
            baixo = "".join(leitor[meio:len(leitor)])
            
            layout['up-left'].update(cima)
            layout['down-right'].update(baixo)
            
    else:
        meio = len(texto) // 2
        cima = texto[0:meio]
        baixo = texto[meio:len(texto)]

        layout['up-right'].update(cima)
        layout['down-left'].update(baixo)

    console.print(layout, '\n')