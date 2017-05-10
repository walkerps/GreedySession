import pandas as pd
import numpy as np

file = 'ggevent.log'

df = pd.read_json(file,lines = True)

with open('ggevent.json','w') as f:
	f.write(df.to_json(orient = 'records', lines = True))

