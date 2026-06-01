"""Módulo responsável pelas ações do jogador, pontuação e algoritmo de resolução."""

import time
from pynput import keyboard

def iniciar_jogador(labirinto: list[list[str]]) -> tuple[tuple[int, int], int]:
    """Localiza o jogador 'P' no labirinto e inicia a pontuação.

    Args:
        labirinto (list[list[str]]): A matriz do labirinto.

    Returns:
        tuple[tuple[int, int], int]: Posição inicial (linha, coluna) e pontuação inicial (0).
    """
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == "P":
                return (i, j), 0
    return (1, 1), 0

def obter_comando_teclado() -> str:
    """Captura de forma síncrona uma tecla pressionada pelo usuário usando pynput.

    Returns:
        str: Comando correspondente ('w', 'a', 's', 'd' ou 'q' para sair).
    """
    comando = ["" ]
    
    def on_press(key):
        try:
            if key.char in ['w', 'a', 's', 'd', 'q']:
                comando[0] = key.char
                return False
        except AttributeError:
            if key == keyboard.Key.up: comando[0] = 'w'
            elif key == keyboard.Key.down: comando[0] = 's'
            elif key == keyboard.Key.left: comando[0] = 'a'
            elif key == keyboard.Key.right: comando[0] = 'd'
            return False

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        
    return comando[0]

def mover(labirinto: list[list[str]], pos_atual: tuple[int, int], direcao: str) -> tuple[int, int]:
    """Calcula a nova posição do jogador com base na direção e valida colisões e limites.

    Args:
        labirinto (list[list[str]]): O mapa do jogo.
        pos_atual (tuple[int, int]): Coordenadas (linha, coluna) atuais.
        direcao (str): Tecla de direção ('w', 'a', 's', 'd').

    Returns:
        tuple[int, int]: Nova coordenada do jogador.
    """
    linha, coluna = pos_atual
    nova_linha, nova_coluna = linha, coluna

    match direcao:
        case "w": nova_linha -= 1
        case "s": nova_linha += 1
        case "a": nova_coluna -= 1
        case "d": nova_coluna += 1

    if 0 <= nova_linha < len(labirinto):
        if 0 <= nova_coluna < len(labirinto[nova_linha]):
            # Só checa a parede se a posição for válida
            if labirinto[nova_linha][nova_coluna] != "#":
                return nova_linha, nova_coluna
                
    return pos_atual

def resolver_labirinto_recursivo(
    labirinto: list[list[str]], 
    atual: tuple[int, int], 
    visitados: set[tuple[int, int]]
) -> list[tuple[int, int]] | None:
    """Algoritmo que encontra o caminho até a saída 'E'.

    Args:
        labirinto (list[list[str]]): A matriz do labirinto.
        atual (tuple[int, int]): Posição atual da busca.
        visitados (set): Conjunto de posições já exploradas.

    Returns:
        list[tuple[int, int]] | None: Lista de coordenadas do caminho ou None se sem saída.
    """
    l, c = atual

    # Casos base de parada
    if labirinto[l][c] == "E":
        return [atual]
    if labirinto[l][c] == "#" or atual in visitados:
        return None

    visitados.add(atual)

    # Direções: Cima, Baixo, Esquerda, Direita
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dl, dc in direcoes:
        proximo = (l + dl, c + dc)
        caminho = resolver_labirinto_recursivo(labirinto, proximo, visitados)
        if caminho is not None:
            return [atual] + caminho

    return None