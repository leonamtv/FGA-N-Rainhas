# Resolvendo N-Rainhas com Algoritmo Genético

Trabalho da disciplina de Inteligência artificial (2020) da turma de Engenharia de computação CEFET-MG. Feito em **Python3**

## Como executar

Para executar o software, você precisa primeiro instalar as dependências. A única dependência para esse programa é o `numpy`. Então, basta instalá-lo com o `pip` assim:

```
pip install numpy
```

Para executar, basta chamar o programa assim:

```
python3 main.py
```

### Interface de linha de comandos

O programa foi feito para que os parâmetros sejam passados via argumento de linha de comando. Os argumentos são passados nesse formato:

```
usage: main.py [-h] [-np NUM_POP] [-ne NUM_ELITE] [-ng NUM_GER]
               [-nr NUM_RAINHAS] [-v] [-im]

FGA para resolver o problema das N-Rainhas

optional arguments:
  -h, --help            Mostra essa mensagem e sai.
  -np NUM_POP, --num-pop NUM_POP
                        Números de indivíduos na população.
  -ne NUM_ELITE, --num-elite NUM_ELITE
                        Número de indivíduos selecionados por elitismo.
  -ng NUM_GER, --num-ger NUM_GER
                        Número de gerações máximas que o FGA irá executar.
  -nr NUM_RAINHAS, --num-rainhas NUM_RAINHAS
                        Número de rainhas que irão ser posicionadas.
  -v, --verbose         Se passado, omite o número e o melhor indivíduo de
                        cada geração assim como sua avaliação
  -im, --gerar-imagem   Se passado, gera um html com a imagem do tabuleiro e
                        abre no navegador.

```

### Exemplo:

-  `python main.py -np 40 -ne 8 -ng 2000 -nr 12 -im`. O código vai executar com uma população de 40 indivíduos, 8 elitizados, 2000 gerações e 12 rainhas, gerando no final a imagem do tabuleiro resolvido caso o FGA convirja.

-  `python main.py -np 20 -ne 2 -ng 100 -nr 8`. O código vai executar com uma população de 20 indivíduos, 2 elitizados, 100 gerações e 8 rainhas.

-  `python main.py`. O código vai executar com uma população de 20 indivíduos, 2 elitizados, 1000 gerações e 8 rainhas.

### Tabuleiro gerado:

<img width=500 src='./assets/tabuleiro.png'>

-----

Autor: [Leonam Teixeira de Vasconcelos](https://leonamtv.github.io/leonamtv/)