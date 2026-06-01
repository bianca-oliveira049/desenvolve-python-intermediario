"""Módulo de utilitários para interface, menus e animações visuais."""

import sys
import time
from rich.console import Console
from rich.panel import Panel

console = Console()

def imprime_instrucoes() -> None:
    """Exibe as instruções do jogo formatadas com Rich."""
    texto_instrucoes = (
        "[bold yellow]Controles:[/]\n"
        " Use as teclas [bold cyan]W, A, S, D[/] ou as [bold cyan]Setas direcionais[/] para mover.\n"
        " Pressione [bold red]Q[/] a qualquer momento para desistir e voltar ao menu.\n\n"
        "[bold yellow]Objetivo:[/]\n"
        " Colete todos os cristais ([bold yellow]*[/]) que puder e encontre a saída ([bold green]E[/])!"
    )
    console.print(Panel(texto_instrucoes, title="📜 INSTRUÇÕES DE JOGO", expand=False))
    input("\nPressione Enter para voltar ao menu...")

def imprime_menu(nome_jogador: str, cor: str) -> None:
    """Renderiza o menu principal do jogo de forma limpa e colorida.

    Args:
        nome_jogador (str): Nome fornecido via CLI.
        cor (str): Cor escolhida para os detalhes da interface.
    """
    menu_texto = (
        f"Olá, [bold cyan]{nome_jogador}[/]! Prepare-se para o desafio.\n\n"
        "[1] -> Iniciar Aventura (Jogar)\n"
        "[2] -> Modo Autônomo (Assistir Solução Recursiva)\n"
        "[3] -> Ver Instruções\n"
        "[4] -> Sair do Jogo"
    )
    console.print(Panel(menu_texto, title=f"[{cor}]⚔️ AVENTURA NO LABIRINTO ⚔️[/]", expand=False))

def animacao_vitoria_recursiva(passo: int = 5) -> None:
    """Gera um efeito cascata visual e recursivo para celebrar a vitória.

    Args:
        passo (int): Contador de passos recursivos restantes para a animação.
    """
    if passo == 0:
        return
    
    cores = ["bold red", "bold yellow", "bold green", "bold cyan", "bold magenta"]
    cor = cores[passo % len(cores)]
    
    console.print(f"[{cor}]" + "🎉 " * (6 - passo) + "VOCÊ VENCEU! O LABIRINTO FOI SUPERADO! " + "🎉 " * (6 - passo) + "[/]")
    time.sleep(0.2)
    
    # Chamada recursiva
    animacao_vitoria_recursiva(passo - 1)