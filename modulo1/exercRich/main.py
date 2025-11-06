from personalizador import layout
from personalizador import painel 
from personalizador import progresso 
from personalizador import estilo 
import argparse

modulosFuncoes = {0: {
                    "nome": "estilo",
                    "funcoes": {
                        "f1": estilo.imprimeColorido,
                        "f2": estilo.imprimePiscando},
                    "map_func_nomes": {
                    "f1": "Colorido",
                    "f2": "Piscando"}
                    }, 
                  1: {
                    "nome": "layout",
                    "funcoes": {
                        "f1": layout.imprimeEsquerdaDireita,
                        "f2": layout.imprimeDiagonal},
                    "map_func_nomes": {
                        "f1": "EsquerdaDireita",
                        "f2": "Diagonal"}               
                    }, 
                  2: {
                    "nome": "painel",
                    "funcoes": {
                        "f1": painel.imprimePainel,
                        "f2": painel.imprimeComTitulo},
                    "map_func_nomes": {
                        "f1": "Painel",
                        "f2": "ComTitulo"}          
                    }, 
                  3: {
                    "nome": "progresso",
                    "funcoes": {
                        "f1": progresso.imprimeBarraComum,
                        "f2": progresso.imprimeSpinner},
                    "map_func_nomes": {
                        "f1": "BarraComum",
                        "f2": "Spinner"} 
                    }}

def gerarChoices(estrutura_modulos):
    modulo_choices = list(estrutura_modulos.keys()) + [info["nome"] for info in estrutura_modulos.values()]
    funcao_choices = set()
    for info in estrutura_modulos.values():
        funcao_choices.update(info["funcoes"].keys()) 
        funcao_choices.update(info["map_func_nomes"].values()) 
    return modulo_choices, list(funcao_choices)

modChoices, funChoices = gerarChoices(modulosFuncoes)

def buscarModulo(mod):
    try:
        if int(mod) in modulosFuncoes:
            return modulosFuncoes[int(mod)]
    except ValueError:
        pass 
        
    modLower = str(mod).lower()
    for _, info in modulosFuncoes.items():
        if info["nome"].lower() == modLower:
            return info
    
    return None

def buscarFuncao(func, modulo_info):
    """Procura a função pelo ID Curto (f1, f2) ou Nome Completo."""
    
    # 1. Tenta buscar pelo ID Curto (f1, f2)
    if func in modulo_info["funcoes"]:
        nome_display = modulo_info["map_func_nomes"].get(func, func)
        return modulo_info["funcoes"][func], nome_display

    # 2. Tenta buscar pelo Nome Completo (o objeto da função é o valor)
    input_func_lower = func.lower()
    for func_id, func_nome in modulo_info["map_func_nomes"].items():
        if input_func_lower == func_nome.lower():
            return modulo_info["funcoes"][func_id], func_nome

    return None, None

parser = argparse.ArgumentParser()

parser.add_argument('texto', type=str, 
                    help= "Texto a ser impresso ou caminho para um arquivo.")

parser.add_argument('-a', '--arquivo', action='store_true', 
                    help="Essa opção deve ser ativada se 'texto' for caminho para um arquivo.")

parser.add_argument('-m', '--modulo', 
                    choices=[str(c) for c in modChoices],
                    help="Módulo a ser selecionado: {estilo, layout, painel, progresso} por nome ou {0, 1, 2, 3} por id.")

parser.add_argument('-f', '--funcao', required=True,
                    choices=funChoices, 
                    help="função a ser selecionada: {f1, f2} por id ou por nome")

args = parser.parse_args()

info_modulo = buscarModulo(args.modulo)

funcaoExecutar, nomeFuncao = buscarFuncao(args.funcao, info_modulo)

if not funcaoExecutar: print("Função não encontrada!")
else: funcaoExecutar(args.texto, args.arquivo)