from sqlalchemy import update
from core import user_table, engine


def atualiza_cliente():
    username = input('Digite o nome atual do cliente: ')
    conn = engine.connect()
    atualizar = update(user_table).where(user_table.c.nome == username)
    novo_nome = input('Insira o novo nome: ')
    atualizar = atualizar.values (nome= novo_nome)
    resultado = conn.execute(atualizar)
    print(resultado.rowcount)


if __name__ == "__main__":
    atualiza_cliente()