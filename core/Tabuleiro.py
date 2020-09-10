from core.NRainhasInd import NRainhasInd

import os
import calendar
import time

class Tabuleiro () :

    def __init__ ( self, ind : NRainhasInd ) :
        self.__individuo = ind
        self.__startHtml ( )

    def __getStyle ( self ) :
        return """
        * {
            padding : 0;
            margin : 0;
        }
        body {
            background-image : linear-gradient(to right, #34c3eb, #6899ed);
        }
        .tabuleiro {
            position: absolute;
            width : 500px;
            height : 500px;
            border : 10px solid #468759; 
            top: 50%;
            left: 50%;
            -ms-transform: translate(-50%, -50%);
            transform: translate(-50%, -50%);
            -webkit-box-shadow: 33px 14px 111px -8px rgba(122,122,122,1);
            -moz-box-shadow: 33px 14px 111px -8px rgba(122,122,122,1);
            box-shadow: 33px 14px 111px -8px rgba(122,122,122,1);
        }
        table tr td img {
            width : 80px;
            border : 0;
        }
        table tr td {
            width : 80px;
            height : 80px;
            border : none;
        }     
        .claro {
            background-color : #cef0d8;
        }   
        .escuro {
            background-color : #468759;
        }
        """

    def __startHtml ( self ) :
        self.__baseHtml =  '<html><head><title>{}-rainhas</title>'.format(str(self.__individuo.nRainhas))
        self.__baseHtml += '<style>{}</style></head><body>'.format(self.__getStyle())

    def __closeHtml ( self ) :
        self.__baseHtml += '</body></html>'

    def gerarImagem ( self, pathToSave : str = './output' ) :
        url_queen = '../assets/queen.png'
        self.__baseHtml += "<table class='tabuleiro'>"
        cont = 0
        for i in range( self.__individuo.nRainhas ) :
            self.__baseHtml += "<tr>"
            for ind in  self.__individuo.genes :
                self.__baseHtml += "<td class='{}'>".format( 'claro' if cont % 2 == 0 else 'escuro' )                
                self.__baseHtml += "<img src='{}'>".format(url_queen) if ind == i else '&nbsp;'
                self.__baseHtml += "</td>"
                cont += 1
            if self.__individuo.nRainhas % 2 == 0 :
                cont += 1
            self.__baseHtml += "</tr>"
        self.__baseHtml += "</table>"
        self.__closeHtml()
        if not os.path.isdir ( pathToSave ) :
            os.makedirs ( pathToSave )
        name = 'tabuleiro-{}-rainhas-{}.html'.format( str(self.__individuo.nRainhas), str(calendar.timegm(time.gmtime())))
        _file = open(os.path.join( pathToSave, name ), 'w')
        print('Tabuleiro salvo em {}'.format(os.path.abspath(os.path.join(pathToSave, name))))
        _file.write(self.__baseHtml)
        _file.close()
        return os.path.abspath(os.path.join(pathToSave, name))