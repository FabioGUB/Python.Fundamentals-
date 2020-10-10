#!/usr/bin/python3


#abrindo arquivo com python

# arquivo = open('arquivo.txt', 'w')
# arquivo.write('novo arquivo')
# arquivo.close()
 


#pandas 


import pandas as pd 


df = pd.read_csv('dados.csv', sep=';')
print(df.head())

