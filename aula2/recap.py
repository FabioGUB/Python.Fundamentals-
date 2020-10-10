#!/usr/bin/python3

# tipos de dados e variaveis

string = 'Isso é uma string'
inteiro =  10
flutuante = 10.6


#entrada e saida

nome = input('Digite seu nome: ') #entrada de dados
print (nome) #saida
import keyword

print (f'palavras que não podem ser usadas para atribuir variáveis  {keyword.kwlist}')

#estrutura de dados

##listas

itens = [1, 2.0, 'string', [1,6,9], 'uva']
itens.append('novo item')
itens.remove(2.0)
itens.pop(2)
itens.insert(4, 'Outra coisa')
itens[1] = 'Novo valor'


print(itens[3])


##tuplas - são imutaveis

dado = (10, 2.0, 'Teste', True)

##dicionário

dados = {'nome': 'Renato',
    'Idade': 27,
    'Linguagem preferida': 'Python e GO'
}

dados.keys()
dados.values()


#estrutura de repeticão

## while

users = ['Barbara', 'Carlos', 'Ramon']
while True:
    login = input('Digite ser login: ')
    if login in users:
        print('Acesso permitido')
        break
    else:
        print('Acesso Negado')
        continue

for index,nome in enumerate(users):
    print(index, nome)




