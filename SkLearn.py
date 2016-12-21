#SkLearn 
import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
from sklearn import svm ,preprocessing, cross_validation

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
y = np.array(housing_data['lable'])
x = np.array(housing_data.drop(['lable','US_HPI_Future'],1))
x = preprocessing.scale(x)

x_train ,x_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size =0.2)

clf  = svm.SVC(kernel='linear')
clf.fit(x_train,y_train)
print (clf.score(x_test,y_test))