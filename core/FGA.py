from core.IndividuoFactory import IndividuoFactory
from core.Tabuleiro import Tabuleiro

import numpy as np
import random as rnd

class FGA :

    @classmethod
    def executar ( cls, 
                   nPop        : int, 
                   nGeracoes   : int, 
                   nElite      : int, 
                   indFactory  : IndividuoFactory,
                   verbose     : bool = False,
                   printResult : bool = True,
                   gerarHtml   : bool = False ) -> int :
        """
        Método estático que executa o FGA para o problema das N rainhas, onde:

        Parâmetros:
            - nPop       = (obrigatório) Números de indivíduos na população
            - nGerações  = (obrigatório) Número de gerações que o software irá exe-
                            cutar no máximo (caso haja algum indivíduo que já cum-
                            pra o objetivo -- 0 colisões, o FGA para de executar)
            - nElite     = (obrigatório) Número de indivíduos que irão passar pa-
                            ra a próxima geração por mero elitismo.
            - indFactory = (obrigatório) Objeto do tipo IndividuoFactory, utiliza-
                            do para gerar a população base de cada geração.
            - verbose    = (opcional, padrão false) Caso seja verdadeiro, imprime
                            o número e o melhor indivíduo de cada geração assim como 
                            sua avaliação.
            - printResult = (opcional, padrão true) Caso seja verdadeiro, imprime o 
                            resultado obtido caso o agoritmo convirja para a condição 
                            de parada.
            - gerarHtml   = (opcional, padrão false) Caso seja verdadeiro, gera um html
                            com o tabuleiro do melhor indivíduo, caso e quando o algori-
                            tmo convergir.

        Retorna:

            Um inteiro com o número da geração na qual o algoritmo convergiu. Caso o 
            retorno seja igual a -1, o FGA não convergiu.
        """
        
        if verbose :
            print('executando...')

        # Cria a população inicial
        pop = np.array([ indFactory.getIndividuo() for _ in range(nPop) ])

        for g in range ( nGeracoes ) :
            filhos = []

            # Adicionando população inicial à lista de população total
            filhos.extend(pop)

            # Gerando nPop indivíduos recombinados
            for i in range ( 1, nPop, 2 ):
                filhos_recombinados = pop[i - 1].recombinar(pop[i])
                filhos.extend(filhos_recombinados)

            # Gerando nPop indivíduos mutantes            
            for i in range ( 0, nPop ):
                filhos.append(pop[i].mutar())

            def getAvaliacoes ( individuos ) :
                """
                Retorna uma lista de avaliações dos indivíduos
                """
                return [ individuo.getAvaliacao() for individuo in individuos ]

            # Ordena os filhos por ordem de avaliação
            filhos.sort ( key=lambda ind:ind.getAvaliacao())

            newPop = []

            if nElite > nPop :
                raise Exception('Número de elite deve ser menor que a população')

            avaliacoes = getAvaliacoes ( filhos )

            def roleta_viciada ( ) :
                """
                Retorna o índice da roleta viciada realizada sob a lista de avaliações.
                """
                somatorio = sum ( 1. / i if i != 0 else 0 for i in avaliacoes )
                roleta = rnd.uniform( 0, somatorio )
                soma = 0.0
                i = 0
                while soma < roleta and i < len ( avaliacoes ) :
                    soma += avaliacoes[i]
                    i += 1
                return i if i < len ( avaliacoes ) else ( len( avaliacoes ) - 1 )
            
            if verbose :
                print(f'{bcolors.FAIL}Geração {bcolors.BOLD}' 
                        + str(g + 1) + f'{bcolors.OKGREEN} | Melhor ind: {bcolors.OKBLUE}' 
                        + str(filhos[0]) + f'{bcolors.OKGREEN} | aval: {bcolors.OKBLUE}' 
                        + str(filhos[0].getAvaliacao()) + f'{bcolors.ENDC}' )

            # Adiciona a elite, removendo a da lista de filhos
            elitistas = filhos[:nElite]
            del filhos[:nElite]
            del avaliacoes[:nElite]
            newPop.extend(elitistas)

            # Adiciona individuos da lista de filhos utilizando a roleta
            # viciada até que o número de indivíduos seja atingido.
            while len(newPop) < nPop :
                i = roleta_viciada ()
                newPop.append(filhos[i])
                del filhos[i]
                del avaliacoes[i]

            pop = newPop
            
            # Checa se algum indivíduo possui avaliação 0 e para caso haja
            for aval, ind in zip ([ ind.getAvaliacao() for ind in pop ], pop ) :
                if aval == 0 :
                    if printResult :
                        print('------- Convergiu -----------')
                        print('Geração ' + str(g + 1) + f' | Melhor ind: {bcolors.OKGREEN}{bcolors.BOLD}' 
                              + str(ind) + f'{bcolors.ENDC} | aval: ' + str(aval))
                        print('-----------------------------')
                    if gerarHtml :
                        tab = Tabuleiro(ind)
                        pathToFile = tab.gerarImagem()
                        import webbrowser
                        webbrowser.open(pathToFile, new=2)
                    if verbose :
                        print('...execução finalizada')
                    return g + 1
        if verbose :
            print('...execução finalizada')
        
        return -1

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'