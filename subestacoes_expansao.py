import pandas as pd
import json

with open('input/subestacoes_expansao.json') as f:
    data = json.load(f)

subestacao_exp = {}

for feat in data['features']:
    atributos = feat['attributes']
    atributos.update(feat['geometry'])
    subestacao_exp[feat['attributes']['OBJECTID']] = atributos

df = pd.DataFrame.from_dict(subestacao_exp, orient='index')

print(df.columns)

df.columns = ['cod_subest_exp', 'Nome_subest_exp', 'Tensao_subest_exp', 'Situacao_subest_exp',
              'Ano_Opera_subest_exp', 'lng_subest_exp', 'lat_subest_exp']

print(df.head())

df.to_csv('output/subest_expansao.csv', index_label='id')