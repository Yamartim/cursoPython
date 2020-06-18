#curso de OOP em python

class ContaBanco:

    #construtor da classe, self é a referencia a propria classe, igual ao this no c++
    def __init__(self, numero, titular, saldo, limite = 69000): #é possivel atribuir valores default como eu fiz pro limite 
        print("rodando o construtor... {}".format(self))
        #atribuindo parametros
        self.numero = numero    #123
        self.titular = titular  #'el marto marteem'
        self.saldo = saldo
        self.limite = limite