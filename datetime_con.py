import datetime
import time
import math
def datetime_conversion(time_value):
	datetime_format = "%Y-%m-%d %H:%M:%S.%f"
	strptime = datetime.datetime.strptime(time_value, datetime_format)
	return int(time.mktime(strptime.timetuple()))
