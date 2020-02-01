import random
 
# inicio da definicao da classe
class TiaVelha:
    def __init__(self, nome, idade):
        """
        inicializador da classe.
        cada tia velha criada
        serah criada por este metodo init
        """
 
        #definindo os atributos
        self.nome=nome
        self.idade=idade
        self.frases=[]
 
        #criando o repertorio de frases
        self.frases.append( "Como voce cresceu!" )
        self.frases.append( "Voce precisa arrumar uma namoraaaada!" )
        self.frases.append( "Voce ainda nao arrumou emprego?!!" )
        self.frases.append( "Respeita sua mae, menino!" )
        self.frases.append( "Gracinha!" )
 
    def falar(self):
        """
        metodo principal da tia velha
        """
        x=len(self.frases)
        n=int(random.random()*x-1)
        print (self.frases[n])
 
    def apresentar_se(self):
        print   ("""
                Ola.
                Meu nome eh """ + self.nome + """
                e tenho """ + str(self.idade)  + """ anos.
                Sou uma tia velha e o que mais faco eh falar
                """
                )
 
# o codigo abaixo somente
# sera executado se este
# arquivo for executado
# diretamente.
#
# nao o serah se a classe
# TiaVelha for importada
# para dentro de outro
# programa python
if __name__=='__main__':
 
    # criando uma 'nova' tia velha
    # com nome 'Odila' e idade 67
    # eh neste momento que __init__()
    # serah chamado
    odila=TiaVelha('Odila',67)
 
    # executando um metodo
    odila.apresentar_se()
 
    print
    print
    print
 
    # fazendo a tia odila falar 15 vezes
    for x in range(15):
        odila.falar()
