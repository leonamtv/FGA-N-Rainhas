from abc import ABC, abstractmethod

class Individuo ( ABC ):

    def __init__ ( self, avaliacao : float = -1 ) :
        self._avaliacao = avaliacao

    @abstractmethod
    def recombinar ( self, ind ) -> list : 
        pass

    @abstractmethod
    def mutar ( self ) :
        pass

    @abstractmethod
    def getAvaliacao ( self ) -> float :
        pass