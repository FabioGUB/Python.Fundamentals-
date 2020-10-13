import random
import datetime



class Banco:


    def __init__(self):
        self.nbanco = '999'
        self.conta = '06759-235'
        self.agencia = '08'
        self.cliente = 'Maria da Conceição'
        self.sald = random.randint(0, 5000) + random.random()

    def depositar(self):
        x = float(input('\033[1mValor a ser depositado: R$\033[m'))
        print(f'\033[1mNovo saldo: {self.sald + x:.2f}\033[m')
    def sacar(self):
        y = float(input('\033[1mValor a ser sacado: R$\033[m'))
        if y <= self.sald:
            print(f'\033[1mSeu novo saldo é de: {self.sald - y:.2f}\033[m')
        else:
            print('\033[1mSaldo insuficiente\033[m')
    def extrato(self):
        print(f'\033[1mNúmero do banco: {self.nbanco}')
        print(f'Número da Agência: {self.agencia}')
        print(f'Cliente: {self.cliente}')
        print(f'Seu saldo atual: {self.sald:.2f}')
        print(f'Data {datetime.date.today()}\033[m')

cliente1 = Banco()

print(f'{"OldBank":^25}')
print('='*25)
print(f'{"Bem vindo(a)!":^25}')
print('O que deseja fazer hoje?')

while True:
    print('''Para extrato digite 1
Para saque digite 2
Para deposito digite 3
Para sair digite 000''')
    print('='*25)
    x = int(input('Opção desejada: '))
    print('='*25)
    if x == 1:
        cliente1.extrato()
        print('=' * 25)
    elif x == 2:
        cliente1.sacar()
        print('=' * 25)
    elif x == 3:
        cliente1.depositar()
        print('=' * 25)
    elif x == 000:
        print('Tenha um ótimo dia, até mais.')
        break
    else:
        print('Opção inválida, tente novamente.')

#necessita atualizar o saldo conforme deposita ou saca




