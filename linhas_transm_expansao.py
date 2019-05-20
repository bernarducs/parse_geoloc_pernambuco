import pandas as pd
import json

with open('input/linha_transm_expansao.json') as f:
    data = json.load(f)

transm_exp = {}

for feat in data['features']:
    atributos = feat['attributes']
    atributos.update(feat['geometry'])
    transm_exp[feat['attributes']['OBJECTID']] = atributos

df = pd.DataFrame.from_dict(transm_exp, orient='index')

print(df.columns)

df.columns = ['cod_ltransm_exp', 'Nome_ltransm_exp', 'Tensao_ltransm_exp', 'Ano_ltransm_exp',
              'Situacao_ltransm_exp', 'Comp_ltransm_exp', 'paths_ltransm_exp']

print(df.head())

df.to_csv('output/linha_transm_expansao.csv', index_label='id')