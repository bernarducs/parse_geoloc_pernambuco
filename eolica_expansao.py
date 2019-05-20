import pandas as pd
import json

with open('input\eolica_expansao.json') as f:
    data = json.load(f)

eolica_expansao = {}

for feat in data['features']:
    atributos = feat['attributes']
    atributos.update(feat['geometry'])
    eolica_expansao[feat['attributes']['OBJECTID']] = atributos

df = pd.DataFrame.from_dict(eolica_expansao, orient='index')

print(df.columns)

df.columns = ['cod_eolica_exp', 'Nome_eolica_exp', 'Situacao_eolica_exp', 'Potencia_eolica_exp', 'UF_eolica_exp',
              'Subsitema_eolica_exp', 'Ano_eolica_exp', 'lng_eolica_exp', 'lat_eolica_exp']

print(df.head())

df.to_csv('output/eolica_expansao.csv', index_label='id')