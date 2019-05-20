import pandas as pd
import json

with open('input\hidroeletricas.json') as f:
    data = json.load(f)

# lista_campos = [x for x in data['features'][0]['attributes'].keys()]

# hidroele_coord = [x['geometry']['paths'] for x in data['features']]

hidroele = {}

for feat in data['features']:
    hidroele[feat['attributes']['objectid']] = feat['attributes']

df = pd.DataFrame.from_dict(hidroele, orient='index')

df.to_csv('output/hidroeletricas.csv', index_label='id')