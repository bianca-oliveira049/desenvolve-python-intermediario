'''Imprime texto parte por parte acompanhado de indicador de progresso'''

from rich.progress import Progress, SpinnerColumn
import time

def imprimeBarraComum(texto, isArquivo):
    '''Imprime texto parte por parte acompanhado de barra comum de progresso
    
    Recebe como parâmetro uma string 'texto' e uma variável booleana 'isArquivo' que indica se 'texto' é uma string
    comum ou caminho para um arquivo.
    Se 'isArquivo' for falso, será impressa uma palavra da string por vez.
    Se 'isArquivo' for verdadeiro, será impressa cada linha do arquivo por vez.'''
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as arq:
            leitor = arq.readlines()
            with Progress() as progresso:
                task = progresso.add_task("Imprimindo conteúdo do arquivo...", total=len(leitor))

                for i in range(len(leitor)):
                    print(leitor[i])
                    progresso.update(task, advance=len(leitor[i]) / 10)
                    time.sleep(0.2)
    else:
        string = texto.split(" ")
        with Progress() as progresso:
            task = progresso.add_task("Imprimindo string...", total=len(string))
            
            for i in range(len(string)):
                    print(string[i])
                    progresso.update(task, advance=len(string[i]) / 10)
                    time.sleep(0.2)

def imprimeSpinner(texto, isArquivo):
    '''Imprime o texto parte por parte acompanhado do spinner de 'bouncing ball'.
    
    Recebe como parâmetro uma string 'texto' e uma variável booleana 'isArquivo' que indica se 'texto' é uma string
    comum ou caminho para um arquivo.
    Se 'isArquivo' for falso, será impressa uma palavra por vez.
    Se 'isArquivo' for verdadeiro, será impressa uma linha do arquivo por vez.'''
    if isArquivo:
        with open(texto, 'r', encoding='utf-8') as arq:
            leitor = arq.readlines()
            with Progress(SpinnerColumn(spinner_name="bouncingBall"),) as progresso:
                task = progresso.add_task("Imprimindo conteúdo do arquivo...", total=None)
                
                for i in range(len(leitor)):
                    print(leitor[i])
                    progresso.update(task, advance=len(leitor[i]) / 10)
                    time.sleep(0.2)
    else:
        string = texto.split(" ")
        with Progress(SpinnerColumn(spinner_name="bouncingBall"),) as progresso:
            task = progresso.add_task("Imprimindo string...", total=None)
            
            for i in range(len(string)):
                    print(string[i])
                    progresso.update(task, advance=len(string[i]) / 10)
                    time.sleep(0.2)

