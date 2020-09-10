from core.Individuo import Individuo

import numpy as np
import random as rnd

class NRainhasInd ( Individuo ) :

    def __init__ ( self, nRainhas : int = 0, initRandom : bool = True ) :
        Individuo.__init__( self, -1 )
        self.nRainhas = nRainhas
        if initRandom:
            base = np.array([ i for i in range(self.nRainhas) ])
            self.genes = np.random.permutation ( base )
        else:
            self.genes = np.zeros ( self.nRainhas, dtype = int )

    def __getitem__ ( self, index ):
        return self.genes[index]

    def __setitem__ ( self, index, value ) :
        self.genes[index] = value

    def __str__ ( self ) :
        res = '['
        for gene in self.genes:
            res += ' ' + str(gene) 
        return res + ' ]'

    def recombinar ( self, ind : Individuo, verbose : bool = False ) :
        individuos_recombindos = []

        corte = rnd.randint( 1, self.nRainhas - 1 )

        if verbose :
            print('Corte: ', str(corte))
            print('Pai a  : ', str(self))
            print('Pai b  : ', str(ind))

        filho_a = NRainhasInd( self.nRainhas, initRandom=False )
        filho_b = NRainhasInd( self.nRainhas, initRandom=False )

        filho_a[ :corte ] = self[ :corte ]
        filho_a[ corte: ] = ind[ corte: ]

        posicoes_repetidas = []

        for i in range ( corte, self.nRainhas ) :
            for j in range ( 0, corte ) :
                if filho_a[i] == filho_a[j] :
                    posicoes_repetidas.append(i)

        while len ( posicoes_repetidas ) > 0 :
            for i in range ( self.nRainhas ) :
                if i not in filho_a.genes :
                    index = posicoes_repetidas.pop()
                    filho_a[index] = i

        filho_b[ :corte ] = ind[ :corte ]
        filho_b[ corte: ] = self[ corte: ]

        if verbose :
            print('Filho a bef.: ', str(filho_a))
            print('Filho b bef.: ', str(filho_b))
        
        posicoes_repetidas = []

        for i in range ( corte, self.nRainhas ) :
            for j in range ( 0, corte ) :
                if filho_b[i] == filho_b[j] :
                    posicoes_repetidas.append(i)

        while len ( posicoes_repetidas ) > 0 :
            for i in range ( self.nRainhas ) :
                if i not in filho_b.genes :
                    index = posicoes_repetidas.pop()
                    filho_b[index] = i

        if verbose :
            print('Filho a aft.: ', str(filho_a))
            print('Filho b aft.: ', str(filho_b))

        individuos_recombindos.append(filho_a)
        individuos_recombindos.append(filho_b)

        return np.array(individuos_recombindos)

    def mutar ( self ) :
        mutante = NRainhasInd ( self.nRainhas, initRandom=False )
        mutante.genes = self.genes
        index_a, index_b = rnd.randint( 0, self.nRainhas - 1 ), rnd.randint( 0, self.nRainhas - 1 )
        while index_a == index_b :
            index_a, index_b = rnd.randint( 0, self.nRainhas - 1 ), rnd.randint( 0, self.nRainhas - 1)
        mutante[ index_a ], mutante[ index_b ] = mutante[ index_b ], mutante[ index_a ]
        return mutante

    def getAvaliacao ( self )  :
        if self._avaliacao == -1 :
            colisoes = 0

            for i in range ( self.nRainhas ) :
                for j in range ( i + 1, self.nRainhas ) :
                    if self[i] == self[j] :
                        colisoes += 1
                    if self[i] == ( self[j] - abs( j - i ) ) :
                        colisoes += 1
                    if self[i] == ( self[j] + abs( j - i ) ) :
                        colisoes += 1
            
            self._avaliacao = colisoes
            
        return self._avaliacao