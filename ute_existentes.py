import pandas as pd
import json

with open('input/ute_existente.json') as f:
    data = json.load(f)

ute_exis = {}

for feat in data['features']:
    atributos = feat['attributes']
    atributos.update(feat['geometry'])
    ute_exis[feat['attributes']['OBJECTID']] = atributos

df = pd.DataFrame.from_dict(ute_exis, orient='index')

print(df.columns)
df.columns = ['cod_ute_exis', 'Nome_ute_exis', 'UF1_ut_exis', 'COMBUST_ute_exis', 'P_OUT_KW_ute_exis', 'INIC_OPER_ute_exis',
       'ESTAGIO_ute_exis', 'lng_ute_exis', 'lat_ute_exis']

print(df.head())

df.to_csv('output/ute_existente.csv', index_label='id')