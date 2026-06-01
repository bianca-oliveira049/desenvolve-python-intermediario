"""Módulo responsável pela criação, manipulação e renderização do labirinto."""

import os
import sys
from rich.console import Console
from rich.table import Table

def criar_labirinto(dificuldade: str) -> list[list[str]]:
    """Lê o arquivo de texto correspondente à dificuldade e gera a matriz do labirinto.

    Args:
        dificuldade (str): Nível de dificuldade ('facil' ou 'dificil').

    Returns:
        list[list[str]]: Matriz bidimensional carregada a partir do arquivo TXT.
    """
    nome_arquivo = f"mapa_{dificuldade}.txt"
    
    if not os.path.exists(nome_arquivo):
        console = Console()
        console.print(f"[bold red]Erro:[/] O arquivo de mapa '{nome_arquivo}' não foi encontrado na raiz do projeto!")
        sys.exit(1)
        
    labirinto = []
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            # Remove o '\n' do final de cada linha e converte a string em uma lista de caracteres
            linha_limpa = linha.strip("\n")
            if linha_limpa:  # Ignora linhas vazias acidentais
                labirinto.append(list(linha_limpa))
                
    return labirinto

def imprimir_labirinto(labirinto: list[list[str]], cor_principal: str) -> None:
    """Renderiza o labirinto no terminal de forma estilizada usando a biblioteca Rich.

    Args:
        labirinto (list[list[str]]): A matriz do labirinto atual.
        cor_principal (str): A cor escolhida pelo jogador.
    """
    console = Console()
    table = Table(show_header=False, padding=0, box=None)

    for linha in labirinto:
        elementos_linha = []
        for celula in linha:
            match celula:
                case "#":
                    elementos_linha.append(f"[{cor_principal}]█[/]")
                case "P":
                    elementos_linha.append("[bold cyan]P[/]")
                case "E":
                    elementos_linha.append("[bold green]E[/]")
                case "*":
                    elementos_linha.append("[bold yellow]*[/]")
                case _:
                    elementos_linha.append(" ")
        table.add_row(*elementos_linha)
    
    console.print(table)