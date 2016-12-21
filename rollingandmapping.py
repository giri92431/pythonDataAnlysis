#Structure data Set using rolling and mapping 

import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean

style.use('fivethirtyeight')

api_key = '6GRG9BiEz-maqagk9H5z'

df = quandl.get('FMAC/HPI_AK',authtoken=api_key)


def create_labels(cur_hpi ,fut_hpi):
	if fut_hpi > cur_hpi:
		return 1
	else:
		return 0

def moving_average(values):
# create your own rolling funtion
	return mean(values)

housing_data =pd.read_pickle('HPI.pickle')

housing_data = housing_data.pct_change()
# print (housing_data.head())
housing_data.replace([np.inf ,-np.inf] , np.nan ,inplace =True)

housing_data.dropna(inplace = True)

housing_data['US_HPI_Future'] = housing_data['United States'].shift(-1)

housing_data.dropna(inplace =True)

housing_data['lable'] =list(map(create_labels,housing_data['United States'], housing_data['US_HPI_Future']))
# mapping a function is very important

#print(housing_data.head())
# print (housing_data[['US_HPI_Future','United States']])


#housing_data['ma_appaly_example'] = pd.rolling_apply(housing_data['m30'],10,moving_average)

#print(housing_data.tail())