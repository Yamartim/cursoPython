#curso de OOP em python

class ContaBanco:

    #construtor da classe, self é a referencia a propria classe, igual ao this no c++
    def __init__(self, numero, titular, saldo, limite = 69000): #é possivel atribuir valores default como eu fiz pro limite 
        print("rodando o construtor... {}".format(self))
        #atribuindo parametros, os "__" antes dos nomes dos atributos representam que eles sao privados e nao devem ser acessados diretamente
        self.__numero = numero      #123
        self.__titular = titular    #.title()    #'el marto marteem'
        self.__saldo = saldo        
        self.__limite = limite 
        # self.__codigo_banco = '001'
        #todos os atributos de classe em python precisam referenciar o objeto onde estao, por isso sao declarados com self


    #metodos get e set funcionam mas em python tem outra alternativa, as propriedades
    # def get_tilular(self):
    #     return self.__titular

    # def get_saldo():
    #     return self.__saldo
    # 
    # def get_limite():
    #     return self.__limite

    # def set_limite(self, limite):
    #     if(limite > 100):
    #         self.__limite = limite

    @property   #dessa forma da pra fazer um get so acessando chamanado o atributo normalmente conta.titular
    def titular(self):
        return self.titular.title()

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @staticmethod   #assim se chama metodos estaticos, nao é necessario instanciar um objeto da classe pra acessar
    def codigo_banco(self):
        return '001'

    def extrato(self):  #todos os metodos tem como parametro self para referenciarem o objeto onde estao, na chamada do metodo é implicito
        print("saldo PEY", self.__saldo)
        print("do titular POW {}".format(self.__titular))

    def __pode_sacar(self, valor_a_sacar):  #metodos privados funcionam igual aos atributos
        money_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= money_disponivel

    def take_munny(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("estas pobre irmao")
            return 0

    def depositar(self, valor):
        self.__saldo +- valor

    def transferencia(self, valor, cb_destino):
        self.take_munny(valor)
        cb_destino.depositar(valor)


# print("oi")
# print("oi de novo")

# conta_martim = ContaBanco(30, "marto", 10)
# conta_martim.extrato()

# conta_martim = ContaBanco(2, "merto", 599999) #atribuindo um novo objeto a conta martim faz com que o ultimo va para o garbage collector
# conta_deco = conta_martim #fazer isso resulta na referencia ao objeto se passada para o conta_deci
# conta_deco = none #fazer isso significa nulificar a referencia, como o null do C