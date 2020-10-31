from sqlalchemy import delete
from core import user_table, engine

def delete_cliente():
    nome_cliente = input('usuario a ser excluido: ')
    conn=engine.connect()
    dell= delete(user_table).where(user_table.c.nome==nome_cliente)
    resultado = conn.execute(dell)
    print(resultado.rowcount)

if __name__ == "__main__":
    delete_cliente()