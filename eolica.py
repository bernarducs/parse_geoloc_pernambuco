import pandas as pd
import json

with open('input\eolica.json') as f:
    data = json.load(f)

eolica = {}

for feat in data['features']:
    atributos = feat['attributes']
    atributos.update(feat['geometry'])
    eolica[feat['attributes']['objectid']] = atributos

df = pd.DataFrame.from_dict(eolica, orient='index')

print(df.columns)

df.columns = ['cod_eolica', 'nome_eolica', 'codmun_eolica', 'munic_eolica', 'uf_eolica', 'proc_aneel_eolica', 'ato_legal_eolica',
       'p_out_kw_eolica', 'proprietar_eolica', 'atualizaca_eolica', 'eol_versao_eolica', 'logitude_eolica',
       'latitude_eolica', 'dro_dt_vig_eolica', 'ceg_eolica', 'estagio_eolica', 'versao_eolica', 'mod_explor_eolica', 'lng_eolica',
       'lat_eolica']

print(df.head())

df.to_csv('output/eolica_existente.csv', index_label='id')