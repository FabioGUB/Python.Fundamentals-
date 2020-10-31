import modules.banco as banco
import threading

if __name__ == "__main__":
    user = input('Username: ')
    try:
        tr = threading.Thread(target=banco.selecionar)
        tr.start()
    except Exception as e:
        print('Falha ao criar thread: {e}')
    while tr.isAlive:
        mensagem = input('')
        banco.cadastrar(user, mensagem)

