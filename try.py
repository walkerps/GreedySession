import pandas as pd
import numpy as np
import datetime
import time
from datetime_con import datetime_conversion

file = 'ggevent.csv'

df = pd.read_csv(file)

df = df.drop(['random','debug'],axis = 1)

users = df['ai5'].unique()
previous = 0
flag = True
previous = []
start = []
end = []
valid_session = 0
total_session = 0
for name,groups in df.groupby(df['ai5']):
	df_user = groups
	df_user = df_user.sort_values(by = ['timestamp'],axis = 0)
	print df_user.size
	for index,row in df.iterrows():
		print row.values