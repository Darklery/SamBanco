class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado. Saldo atual: R${self.saldo}')

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Saldo atual: R${self.saldo}')
        else:
            print('Saldo insuficiente.')

    def extrato(self):
        print(f'Titular da conta: {self.titular}')
        print(f'Saldo: R${self.saldo}')


# Exemplo de uso
conta = ContaBancaria("Joaquim")

conta.deposito(100)  # Depósito de R$100 realizado. Saldo atual: R$100

conta.saque(50)  # Saque de R$50 realizado. Saldo atual: R$50

conta.extrato()
# Titular da conta: Joaquim
# Saldo: R$50
