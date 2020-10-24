import random
import datetime



class Banco:


    def __init__(self, conta, cliente):
        self.nbanco = '999'
        self.conta = conta
        self.agencia = '08'
        self.cliente = cliente
        self.sald = random.randint(0, 5000) + random.random()

    def depositar(self):
        x = float(input('\033[1mValor a ser depositado: R$\033[m'))
        self.sald += x
        print(f'\033[1mNovo saldo: {self.sald:.2f}\033[m')
    def sacar(self):
        y = float(input('\033[1mValor a ser sacado: R$\033[m'))
        if y <= self.sald:
            self.sald -= y
            print(f'\033[1mSeu novo saldo é de: {self.sald:.2f}\033[m')
        else:
            print('\033[1mSaldo insuficiente\033[m')
    def extrato(self):
        print(f'\033[1mNúmero do Banco: {self.nbanco}')
        print(f'Número da Agência: {self.agencia}')
        print(f'Cliente: {self.cliente}')
        print(f'Seu saldo atual: {self.sald:.2f}')
        print(f'Data {datetime.date.today()}\033[m')







