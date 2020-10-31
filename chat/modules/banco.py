from pymongo import MongoClient, DESCENDING
import time

try:
    dbname = 'chat'
    password = '4linux'

    client = MongoClient(f"mongodb+srv://admin:{password}@pythonfundamentals.qexci.mongodb.net/{dbname}?retryWrites=true&w=majority")
    db = client['chat']

except Exception as e:
    print(f'Erro:{e}')
    exit()
    

def cadastrar(nome, mensagem):
    data = {
        'nome': nome,
        'mensagem': mensagem,
        #'hora': time.strftime('%d-%m -%Y %H:%M:%S')
    }
    db.chat.insert(data)

def selecionar():
    ultima = [x for x in db.chat.find().sort('_id', DESCENDING)]
    while True:
        data = [x for x in db.chat.find().sort('_id', DESCENDING)]
        if data != ultima:
            ultima = data
            print(f'{data[0]["nome"]} : {data[0] ["mensagem"]} \n') 
        time.sleep(2)
