import pandas as pd
import numpy as np
import datetime
import time
from datetime_con import datetime_conversion
import math

file = 'ggevent.csv'

df = pd.read_csv(file)

df = df.drop(['random','debug'],axis = 1)

users = df['ai5'].unique()
for name,groups in df.groupby(df['ai5']):
	flag = True
	previous = []
	start = []
	end = []
	valid_session = 0
	total_session = 0
	total_time = 0
	df_user = groups
	df_user = df_user.sort_values(by = ['timestamp'],axis = 0)
	for index,row in df_user.iterrows():
		if flag:
			value = row.values
			if (value[4] == 'ggstart'):
				previous = start = row.values
				flag = False
			continue
		current = row.values
		diff = datetime_conversion(current[1]) - datetime_conversion(previous[1])
		if (previous[4] == 'ggstart' and current[4] == 'ggstop'):
			previous = end = current
		elif diff > 30:
			if (previous[4] == current[4] == 'ggstop'):
				flag = True
			elif (previous[4] == 'ggstop' and current[4] == 'ggstart'):
				previous = start = current
			elif (previous[4] == 'ggstart' and current[4] == 'ggstart'):
				previous = start = current
			if np.any(end):	
				time_for_session = datetime_conversion(end[1]) - datetime_conversion(start[1])
			if time_for_session >= 60:
				valid_session += 1
				total_time += time_for_session
			if time_for_session > 1:
				total_session += 1  
	print "Valid Sessions = {} and Total Sessions  = {}  for user = {}".format(valid_session,total_session,name)
