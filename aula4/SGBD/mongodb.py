#!/home/developer/PythonFundamentals/venv/bin/python
from pymongo import MongoClient
import urllib.parse

password = '4linux'
dbname= 'dexterops'
client = MongoClient(f"mongodb+srv://Admin:{password}@pythonfund4mentals.w3rqf.mongodb.net/<{dbname}>?retryWrites=true&w=majority")
collection = client.fila
def inserir_dados():
    try:
        collection.fila.insert_one({"empresa": "4linux",
                        "curso" : [{"nome": "Python Fundamentals",
                         "carga horaria": 40},
                         {"nome": "Linux Fundamentals",
                         "carga horaria": 40}]})

    except Exception as e:
        print(f'erro:{e}')

def buscar_dados():
    for r in collection.fila.find():
        print(f"Empresa: {r['empresa']}")
        for c in r['curso']:
            print('='* 20)
            print(f"Nome: {c['nome']}\n Carga Horaria: {c['carga horaria']}\n")
