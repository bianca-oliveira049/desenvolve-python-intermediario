"""Script principal para execução do jogo 'Aventura no Labirinto'."""

import argparse
import sys
import time
from rich.console import Console
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover, obter_comando_teclado, resolver_labirinto_recursivo
from aventura_pkg.utils import imprime_menu, imprime_instrucoes, animacao_vitoria_recursiva

def jogar_modo_manual(labirinto: list[list[str]], cor: str) -> None:
    """Gerencia o loop principal do jogo para o modo em que o usuário joga."""
    console = Console()
    pos_atual, pontuacao = iniciar_jogador(labirinto)
    
    # Armazena os itens originais do mapa para pontuar
    linhas, colunas = len(labirinto), len(labirinto[0])
    
    while True:
        console.clear()
        console.print(f"[bold]Pontuação Atual: [yellow]{pontuacao}[/][/]\n")
        imprimir_labirinto(labirinto, cor)
        console.print("\n[italic gray]Mova com W/A/S/D ou Q para sair...[/]")
        
        comando = obter_comando_teclado()
        if comando == 'q':
            break
            
        nova_pos = mover(labirinto, pos_atual, comando)
        
        if nova_pos != pos_atual:
            # Apaga a marca antiga do jogador
            labirinto[pos_atual[0]][pos_atual[1]] = " "
            
            # Checa se coletou item
            if labirinto[nova_pos[0]][nova_pos[1]] == "*":
                pontuacao += 10
            
            # Checa se chegou na saída
            if labirinto[nova_pos[0]][nova_pos[1]] == "E":
                console.clear()
                animacao_vitoria_recursiva()
                console.print(f"\n[bold green]Parabéns! Pontuação final: {pontuacao} pontos.[/]")
                input("\nPressione Enter para continuar...")
                break
                
            pos_atual = nova_pos
            labirinto[pos_atual[0]][pos_atual[1]] = "P"

def jogar_modo_autonomo(labirinto: list[list[str]], cor: str) -> None:
    """Usa a função recursiva de pathfinding para resolver o labirinto sozinho."""
    console = Console()
    pos_inicial, _ = iniciar_jogador(labirinto)
    
    # Descobre o caminho usando a busca por retrocesso recursiva
    caminho = resolver_labirinto_recursivo(labirinto, pos_inicial, set())
    
    if not caminho:
        console.print("[bold red]Não foi possível encontrar uma solução para este labirinto.[/]")
        input()
        return

    # Remove o 'P' inicial da matriz para a animação limpa
    labirinto[pos_inicial[0]][pos_inicial[1]] = " "

    for coordenada in caminho:
        console.clear()
        l, c = coordenada
        caractere_original = labirinto[l][c]
        
        # Coloca o jogador temporariamente na posição do caminho
        labirinto[l][c] = "P"
        imprimir_labirinto(labirinto, cor)
        console.print("\n[bold magenta]🤖 Modo IA: Assistindo solução recursiva...[/]")
        time.sleep(0.4)
        
        if caractere_original == "E":
            console.clear()
            animacao_vitoria_recursiva()
            input("\nAlgoritmo concluiu a execução. Pressione Enter...")
            break
            
        # Restaura o espaço vazio
        labirinto[l][c] = " "

def main():
    """Configura os argumentos e gerencia o fluxo do menu."""
    parser = argparse.ArgumentParser(description="Jogo Aventura no Labirinto - Terminal Interativo.")
    
    # Configuração dos 5 argumentos/opções
    parser.add_argument('--name', type=str, required=True, help="Nome do(a) jogador(a) [OBRIGATÓRIO]")
    parser.add_argument('--color', type=str, default="blue", choices=["red", "green", "blue", "yellow", "magenta"], help="Cor principal das paredes")
    parser.add_argument('--dificuldade', type=str, default="facil", choices=["facil", "dificil"], help="Nível de dificuldade do Labirinto")
    parser.add_argument('--disable-sound', action='store_true', help="Desativa efeitos sonoros simulados")
    parser.add_argument('--max-tentativas', type=int, default=3, help="Número de vidas extra")

    args = parser.parse_args()
    console = Console()

    while True:
        console.clear()
        imprime_menu(args.name, args.color)
        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1":
                mapa = criar_labirinto(args.dificuldade)
                jogar_modo_manual(mapa, args.color)
            case "2":
                mapa = criar_labirinto(args.dificuldade)
                jogar_modo_autonomo(mapa, args.color)
            case "3":
                console.clear()
                imprime_instrucoes()
            case "4":
                console.print(f"\n[bold yellow]Obrigado por jogar, {args.name}! Até a próxima.[/]")
                sys.exit(0)
            case _:
                console.print("[bold red]Opção Inválida! Tente novamente.[/]")
                time.sleep(1)

if __name__ == "__main__":
    main()