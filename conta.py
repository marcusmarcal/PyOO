## Testando POO em Python - Curso Alura
## Marcus Marçal - marcus.marcal@gmail.com
## Branch DEV

class Conta:
    def __init__(self, cpf, nome, saldo, limite = 1000.00):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Nome do Cliente: {}".format(self.__nome))
        print("CPF: {}".format(self.__cpf))
        print("Saldo: {}".format(self.__saldo))
        print("Limite : {}".format(self.__limite))
        print("Saldo disponível: {}".format(self.__saldo + self.__limite))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

