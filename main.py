from core.FGA import FGA
from core.NRainhasIndFactory import NRainhaIndFactory
from core.Tabuleiro import Tabuleiro

import argparse

parser = argparse.ArgumentParser(description='FGA para resolver o problema das N-Rainhas', add_help=False)

num_pop = 20
num_elite = 2
num_rainhas = 8
num_ger = 1000
verbose = True
print_result = True
gerar_imagem = False

# Criando interface de argumentos
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Mostra essa mensagem e sai.')
parser.add_argument('-np', '--num-pop', action='store', nargs=1, help='Números de indivíduos na população.')
parser.add_argument('-ne', '--num-elite', action='store', nargs=1, help='Número de indivíduos selecionados por elitismo.')
parser.add_argument('-ng', '--num-ger', action='store', nargs=1, help='Número de gerações máximas que o FGA irá executar.')
parser.add_argument('-nr', '--num-rainhas', action='store', nargs=1, help='Número de rainhas que irão ser posicionadas.')
parser.add_argument('-v', '--verbose', action='store_false', help='Se passado, omite o número e o melhor indivíduo de cada geração assim como sua avaliação')
parser.add_argument('-im', '--gerar-imagem', action='store_true', help='Se passado, gera um html com a imagem do tabuleiro e abre no navegador.')

args = parser.parse_args()

if args.num_pop :
    num_pop = int(args.num_pop[0])
if args.num_elite :
    num_elite = int(args.num_elite[0])
if args.num_rainhas :
    num_rainhas = int(args.num_rainhas[0])
if args.num_ger :
    num_ger = int(args.num_ger[0])
if args.gerar_imagem :
    gerar_imagem = args.gerar_imagem
if args.verbose :
    verbose = args.verbose

FGA.executar ( nPop=num_pop,
               nGeracoes=num_ger,
               nElite=num_elite,
               indFactory=NRainhaIndFactory(num_rainhas),
               verbose=verbose,
               printResult=print_result,
               gerarHtml=gerar_imagem )

