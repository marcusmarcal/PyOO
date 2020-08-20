
class Conta:
    def __init__(self, cpf, nome, saldo, limite = 1000.00):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Nome do Cliente: {}".format(self.nome))
        print("CPF: {}".format(self.cpf))
        print("Saldo: {}".format(self.saldo))
        print("Limite : {}".format(self.limite))
        print("Saldo disponível: {}".format(self.saldo + self.limite))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

