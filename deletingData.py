#deleting unused data 

import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

fig = plt.figure()
ax1 =plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('fiddy_states3.pickle')

HPI_data['Tx1yr'] = HPI_data['TX'].resample('A').mean()

print (HPI_data[['TX','Tx1yr']].head())
#HPI_data.dropna(how='all',inplace =True) # used to drop the data which is not available 
#HPI_data.fillna(method = 'ffill',inplace =True)# used to fill the data it takes the previous value and add it forward  
HPI_data.fillna(method = 'bfill',inplace =True)# used to fill the data it takes the next value and add it forward 
#print (HPI_data[['TX','Tx1yr']].head())

HPI_data[['TX','Tx1yr']].plot(ax= ax1)
plt.legend(loc = 4)
plt.show()

