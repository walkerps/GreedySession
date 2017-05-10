import pandas as pd
import numpy as np

file = 'ggevent.json'

df = pd.read_json(file,lines = True)

bottles = pd.read_json(df['bottle'].to_json(),orient = 'index')

headers = pd.read_json(df['headers'].to_json(),orient = 'index')

post = pd.read_json(df['post'].to_json(),orient = 'index')

result_data = pd.concat([bottles,headers,post],axis  = 1)

result_data.to_csv('ggevent.csv',index = False)
