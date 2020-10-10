


# linguagem = 'Python'
 
from functools import reduce

# def retorna_linguegem():
#     global linguagem    
#     linguagem = 'PHP'
#     print(linguagem)

# print(linguagem)

# if __name__ == '__main__':
#     retorna_linguegem()



# loja de roupas


# produto1 = {'nome' : 'Tenis', 'valor' : 210.7}
# produto2 = {'nome' : 'Meia', 'valor' : 10.70}
# produto3 = {'nome' : 'Camisa', 'valor' : 49.90}
# produto4 = {'nome' : 'Calca', 'valor' : 120.00}

# carrinho = []

# carrinho.append(produto1)
# carrinho.append(produto2)
# carrinho.append(produto3)
# carrinho.append(produto4)


# black_friday = lambda x: x/2

# for c in carrinho:
#     print(f'Nome do Produto: {c["nome"]}')
#     print(f'Valor original: {c["valor"]}')
#     print(f'Valor com desconto: {black_friday(c["valor"])}')

# def adicionaProduto(Produto):
#     global carrinho
#     carrinho.append(Produto)


# def totalCarrinho(carrinho):
#     return sum(produto['valor'] for produto in carrinho)


# def cupomDesconto(cupom=''):
#     if cupom == 'xyzgratis':
#         return 0.5
#     else: 
#         return 1

# adicionaProduto(produto1)
# adicionaProduto(produto2)
# adicionaProduto(produto4)


# print(f'O total de sua compra é: {totalCarrinho(carrinho)*cupomDesconto()}')
# print(f'Com o cupom xyzgratis o valor total será de: {totalCarrinho(carrinho)*cupomDesconto("xyzgratis")}')

# *args = tupla
# **kwarg = dicionario


# def alterarServidor(*servidores):
#     print('O IP atual é:', servidores[0])
#     print('O novo IP é: ', servidores[1])



# def descobreDicionario(**dicionario):
#     print(dicionario)
#     for k in dicionario.keys():
#         print(f'chave: {k}')
#         print(f'Tem o valor: {dicionario[k]}')

# descobreDicionario(servidor='frodo', ip='192.168.15.100', demonio='4linux.com.br')


# var = lambda x, y: x + y

# print(var(1,2))




numeros = [2,3,4,5,6,7,8,9]

# dobro =list(map(lambda x: x*2, numeros)) # aplica a var para cada item da lista # lambda com map

# print(dobro)


# soma = reduce((lambda x,y: x + y), numeros) #soma tudo # lambda com reduce

# print(soma)

# numeros_pares = list(filter(lambda x: x % 2 == 0, numeros)) # lambda com filter 

# print(numeros_pares)



