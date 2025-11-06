'''Imprime texto em painel.'''

from rich.panel import Panel
from rich.console import Console

def imprimePainel(texto, isArquivo):
    '''Cria um painel e imprime o texto dentro dele.
    
    Recebe como parâmetro uma string 'texto' e uma variável booleana 'isArquivo' que indica se 'texto' é uma string
    comum ou caminho para um arquivo.
    Se 'isArquivo' é falso, imprime o conteúdo da string em um painel.
    Se 'isArquivo' é verdadeiro, junta as linhas do arquivo em uma string e imprime dentro de um painel.'''

    console = Console()
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as arq:
            painel = Panel("".join(arq.readlines()))
    else:
        painel = Panel(texto)
    
    console.print(painel)

def imprimeComTitulo(texto, isArquivo):
    '''Imprime texto dentro do painel com um título indicando se é de um arquivo ou uma string
    
    Recebe como parâmetro uma string 'texto' e uma variável booleana 'isArquivo' que indica se 'texto' é uma string
    comum ou caminho para um arquivo.
    Se 'isArquivo' for falso, imprime o conteúdo da string em um painel com o título 'String exemplo'.
    Se 'isArquivo' for verdadeiro, junta as linhas do arquivo em uma string e imprime dentro de um painel 
    com o título 'Texto do arquivo'.'''

    console = Console()

    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as arq:
            painel = Panel("".join(arq.readlines()), title="Texto do arquivo")
    else:
        painel = Panel(texto, title="String exemplo")

    console.print(painel)
