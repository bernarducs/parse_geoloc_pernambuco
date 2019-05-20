import pandas as pd
import json

with open('input\subestacoes.json') as f:
    data = json.load(f)

subestacoes = {}

for feat in data['features']:
    subestacoes[feat['attributes']['objectid']] = feat['attributes']

df = pd.DataFrame.from_dict(subestacoes, orient='index')

df.to_csv('output/subestacoes.csv', index_label='id')
