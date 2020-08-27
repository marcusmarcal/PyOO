## Testando POO em Python - Curso Alura
## Marcus Marçal - marcus.marcal@gmail.com
## Branch DEV

class Conta:
    def __init__(self, cpf, nome, saldo, limite = 1000.00):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod
    def banco():
        return "001"

    def extrato(self):
        print("Nome do Cliente: {}".format(self.__nome))
        print("CPF: {}".format(self.__cpf))
        print("Saldo: {}".format(self.__saldo))
        print("Limite : {}".format(self.__limite))
        print("Saldo disponível: {}".format(self.__saldo + self.__limite))

    def __pode_sacar(self, valor):
        disponivel = self.__saldo + self.__limite
        return valor <= disponivel
    
    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Não é possível sacar. Saldo: {}. Limite: {}".format(self.__saldo, self.__limite))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):  # Outra forma de usar o getter
        return self.__saldo

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite): # Alterado setter para novo formato
        self.__limite = limite

# Exemplos de uso...
# conta1 = Conta("956.605.500-53","Marcus Marçal", 200)
# conta2 = Conta("973.952.340.49","Marília Diefenthäler", 2000)
