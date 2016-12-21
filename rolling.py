#Rolling 
# u can add the data get the mean of it min and max etc with the data between a given time frame for ex between a certain data frame
#

import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
from pandas import Series
style.use('fivethirtyeight')

fig = plt.figure()
ax1 =plt.subplot2grid((2,1),(0,0))
ax2 =plt.subplot2grid((2,1),(1,0) ,sharex= ax1)
HPI_data = pd.read_pickle('fiddy_states3.pickle')

# HPI_data['Tx12MA'] = HPI_data['TX'].rolling(center=False,window = 12).mean() # mean
# HPI_data['Tx12STD'] = HPI_data['TX'].rolling(center=False,window = 12).std() # average

# HPI_data[['TX','Tx12MA']].plot(ax= ax1)
# HPI_data['Tx12STD'].plot(ax= ax2)
# plt.legend(loc = 4)
# plt.show()
TX_AK_12corr = HPI_data['TX'].rolling(center =True ,window =12).corr() # corelation
HPI_data['TX'].plot(ax =ax1 ,label = 'TX HPI')
HPI_data['AK'].plot(ax =ax1 ,label = 'Ak HPI')
ax1.legend(loc =4)

TX_AK_12corr.plot(ax =ax2, label ='TX_AK_12corr')
plt.legend(loc=4)
plt.show()