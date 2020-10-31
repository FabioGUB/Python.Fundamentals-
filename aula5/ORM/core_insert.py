from core import user_table, engine




def insere_cliente():
    cliente_name = input('Novo cliente: ')
    cliente_endereco = input('Endereco do cliente: ')
    conn= engine.connect()
    insercao= user_table.insert()
    novo_cliente= insercao.values(nome=cliente_name, endereco=cliente_endereco)
    conn.execute(novo_cliente)

if __name__ == '__main__':
    insere_cliente()

