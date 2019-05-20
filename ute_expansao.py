import pandas as pd
import json

with open('input/ute_expansao.json') as f:
    data = json.load(f)

ute_expans = {}

for feat in data['features']:
    atributos = feat['attributes']
    atributos.update(feat['geometry'])
    ute_expans[feat['attributes']['OBJECTID']] = atributos

df = pd.DataFrame.from_dict(ute_expans, orient='index')
print(df.columns)

df.columns = ['cod_ute_exp', 'Nome_ute_exp', 'Situacao_ute_exp', 'Potencia_ute_exp', 'Comb_ute_exp', 'UF_ute_exp',
       'Subsistema_ute_exp', 'Ano_ute_exp', 'lng_ute_exp', 'lat_ute_exp']

print(df.head())

df.to_csv('output/ute_expansao.csv', index_label='id')
