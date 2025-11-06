'''Imprime uma string ou texto de um arquivo aplicando estilos como mudança de cor.'''

from rich.console import Console

def imprimeColorido(texto, isArquivo) :
    '''Imprime texto colorido.
    Recebe como parâmetro uma string 'texto' e uma variável booleana 'isArquivo' que indica se 'texto' é uma string
    comum ou caminho para um arquivo.
    Se 'isArquivo' for falso, a função a imprimirá em vermelho.
    Se 'isArquivo' for verdadeiro, o conteúdo do arquivo será impresso em azul.'''

    console = Console()
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as arq:
            leitor = arq.readlines()
            for linha in leitor:
                console.print(linha, style="blue")
    else:
        console.print(texto, style="red")

def imprimePiscando(texto, isArquivo):
    '''Imprime texto piscando, colorido e com fundo colorido.
    
    Recebe como parâmetro uma string 'texto' e uma variável booleana 'isArquivo' que indica se 'texto' é uma string
    comum ou caminho para um arquivo.
    Se 'isArquivo' for falso, a função a imprimirá piscando com o texto em vermelho e o fundo branco.
    Se 'isArquivo' for verdadeiro, 
    o conteúdo do arquivo será impresso piscando com o texto em branco e o fundo azul.'''

    console = Console()
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as arq:
            leitor = arq.readlines()
            for linha in leitor:
                console.print(linha, style='blink bold white on blue')
    else:
        console.print(texto, style='blink bold red on white')
