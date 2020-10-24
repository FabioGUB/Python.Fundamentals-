#!/usr/bin/python3

import psycopg2 


# try:
#     con  = psycopg2.connect("host=localhost dbname=projeto user=admin password=4linux")
    
# except Exception as e:
#     print(f'Erro: {e}')
#     print('Fazendo Roll Back')
#     con.rollback()
# # finally:
# #     print('Finalizando conexao com o banco de dados')
# #     cur.close()
# #     con.close()





# # cur = con.cursor()
# #     cur.execute("insert into scripts(nome, conteudo) values ('devops', 'projeto de python')")
# #     con.commit()
# #     print('registro criado')



# def insert_new(nome = str, conteudo= str):
#     try: 
#         cur = con.cursor()
#         cur.execute(f"insert into scripts(nome, conteudo) values ('(nome)', '(conteudo)')")
#         con.commit()
#         print('Registro executado com sucesso')
#     except Exception as e:
#         print(f'Erro: {e}')
#         con.rollback()
#     finally:
#         cur.close()
#         con.close()
#         print('fim')
# def get_all():
#     try:
#         cur = con.cursor
#         cur.execute('select * from scripts')
#         print(f'Todos: {cur.fetchall()}')
#     except Exception as e:
#         print(f'Erro: {e}')
#         print('Fazendo Roll Back')
#         con.rollback()

# def del_by_name(nome):
#     try: 
#         cur = con.cursor()
#         cur.execute(f"delete from scripts where nome ='{nome}'")
#         print(f'{nome} deletado')
#     except Exception as e:
#         print('Erro:', e)
#         print('Fazendo Roll Back')
#     finally:
#             cur.close()
#             con.close()
#             print('fim')


            
# def update_by_name():
#     pass

# del_by_name('teste')








class sgbd:

    def __init__(self):    
        self.con = psycopg2.connect("host=localhost \
                                dbname=projeto \
                                user=admin     \
                                password=4linux")
    
    def __del__(self):
        print('Conexão Fechada')
        self.con.close()
        del self


    def insert_new(self, nome, conteudo):
        try:
            self.cur = self.con.cursor()
            self.cur.execute(f"insert into scripts(nome,conteudo) values ('{nome}','{conteudo}')")
            self.con.commit()
            print('Regitro executado com sucesso!')
        except Exception as e:
            print(f'Erro: {e}')
            self.con.rollback()


    def get_all(self):
        try:
            self.con
            self.cur = self.con.cursor()
            self.cur.execute("select * from scripts")
            resultado = self.cur.fetchone()
            print(resultado)
            # print(f'Todos os registros: {}')
        except Exception as e:
            print(f'Erro: {e}')
    def search(self):
        try:
            self.con
            self.cur = self.con.cursor()
            resultado = self.cur.fetchone()
            print(resultado)
        except Exception as e:
            print(f'Erro: {e}')

    def delete_by_name(self,nome):
        try:
            self.cur = self.con.cursor()
            self.cur.execute(f"delete from scripts where nome = '{nome}'")
            print('Registro deletado com sucesso!')
            self.con.commit()
        except Exception as e:
            print('Erro:', e)
            self.con.rollback()

    def delete_by_id(self,sid):
        try:
            self.cur = self.con.cursor()
            self.cur.execute(f"delete from scripts where id = '{sid}'")
            print('Registro deletado com sucesso!')
            self.con.commit()
        except Exception as e:
            print('Erro:', e)
            self.con.rollback()

    def update_name(self, nome, sid):
        try:
            self.cur = self.con.cursor()
            self.cur.execute(f"update scripts set nome='{nome}' where id = '{sid}'")
            self.cur.execute('select * from scripts')
            print(f"resultado: {self.cur.fetchall()}")
            self.con.commit()
        except Exception as e:
            print('Erro:', e)
            self.con.rollback()
teste.sgbd()
teste.search