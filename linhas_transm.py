import pandas as pd
import json

with open('input\linhas_de_transmissao.json') as f:
    data = json.load(f)

lt = {}

for feat in data['features']:
    atributos = feat['attributes']
    atributos.update(feat['geometry'])
    lt[feat['attributes']['objectid']] = atributos

df = pd.DataFrame.from_dict(lt, orient='index')

print(df.columns)

df.columns = ['cod_linha_transm', 'tensao_linha_transm', 'cod_ltransm', 'nome_linha_transm', 'circuito_linha_transm',
              'data_linha_transm', 'cod_operacional_linha_transm', 'coord_linha_transm']

print(df.head())

df.to_csv('output/linhas_transmissao.csv', index_label='id')