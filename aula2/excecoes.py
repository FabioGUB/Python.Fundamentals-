#!/usr/bin/python3


# Bloco de código passível de erro

# try:
#     print(nome)
# except:
#     print('Um erro aconteceu')



# try:
#     x = float(input('Digite o primeiro número: '))
#     y = float(input('Digite o segundo número: '))
#     print(x + y)

# except Exception as err:
#     print(err, 'Digite apenas números!!')

# finally:
#     print('Saindo do script!')





# Raise Exception

linguagem = 'php'

try:
    if linguagem == 'python':
        print('Eu topo!')
    else:
        raise ValueError('PHP to fora!!!')

except ValueError as err:
    print(err)