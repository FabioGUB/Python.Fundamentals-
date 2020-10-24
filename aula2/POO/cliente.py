from banco import Banco




print(f'{"OldBank":^25}')
print('='*25)
x = str(input('Digite o Número da Conta: '))
y = str(input('Nome do Cliente: '))
print(f'{"Bem vindo(a)!":^25}')
print(f'O que deseja fazer hoje {y}?')

cliente1 = Banco(x,y)

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

