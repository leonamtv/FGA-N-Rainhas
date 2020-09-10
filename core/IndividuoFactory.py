from abc import ABC, abstractmethod

class IndividuoFactory ( ABC ) :

    @abstractmethod
    def getIndividuo ( self ):
        pass