import pandas as pd
import json

with open('input/ufv_expansao.json') as f:
    data = json.load(f)

ufv_exp = {}

for feat in data['features']:
    atributos = feat['attributes']
    atributos.update(feat['geometry'])
    ufv_exp[feat['attributes']['OBJECTID']] = atributos

df = pd.DataFrame.from_dict(ufv_exp, orient='index')

df.columns = ['cod_ufv_exp', 'Nome_ufv_exp', 'Subsistema_ufv_exp', 'Potencia_ufv_exp',
              'Situacao_ufv_exp', 'Ano_ufv_exp', 'lng_ufv_exp', 'lat_ufv_exp']


print(df.columns)

df.to_csv('output/ufv_expansao.csv', index_label='id')
