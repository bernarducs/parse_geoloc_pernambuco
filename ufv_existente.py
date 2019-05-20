import pandas as pd
import json

with open('input/ufv_existente.json') as f:
    data = json.load(f)

ufv_exis = {}

for feat in data['features']:
    atributos = feat['attributes']
    atributos.update(feat['geometry'])
    ufv_exis[feat['attributes']['OBJECTID']] = atributos

df = pd.DataFrame.from_dict(ufv_exis, orient='index')
print(df.shape)

df.columns = ['cod_ufv_exis', 'Nome_ufv_exis', 'ESTAGIO_ufv_exis', 'TIPO_ufv_exis', 'INIC_OPER_ufv_exis',
              'P_OUT_KW_ufv_exis', 'COMBUST_ufv_exis', 'UF1_ufv_exis', 'lng_ufv_exis', 'lat_ufv_exis']

print(df.head())

df.to_csv('output/ufv_existente.csv', index_label='id')