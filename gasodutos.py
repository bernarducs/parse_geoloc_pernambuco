import pandas as pd
import os
import json

diretorio = os.getcwd() + '\\input\\gasoduto\\bases'
lista_arquivos = os.listdir(diretorio)

lista_ramais = []
lista_coord = []

for arquivo in lista_arquivos:
    with open(diretorio + '\\'+ arquivo) as file:
        data = json.load(file)
        for d in data['features']:
            lista_ramais.append(d['attributes']['ramal'])
            lista_coord.append(d['geometry']['paths'])

lista_id = [id for id in range(1, 3598)]

dict_dutos = {}
for id, ramal, coord in zip(lista_id, lista_ramais, lista_coord):
    dict_dutos[id] = {'ramal': ramal, 'coord': coord}

df = pd.DataFrame.from_dict(dict_dutos, orient='index')
df.to_csv('output/dutos.csv', index_label='id')