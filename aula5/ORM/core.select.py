from sqlalchemy import select
from core import user_table

def seleciona_todos():
    sel = select([user_table])
    for cliente in sel.execute():
        print(cliente['nome'])
        print('='* 25) 




def seleciona_um():
    nome_cliente = input('Nome do cliente: ')
    sel = select([user_table]).where(user_table.c.nome == nome_cliente)
    print([cliente for cliente in sel.execute()])


if __name__ == '__main__':
    seleciona_todos()
