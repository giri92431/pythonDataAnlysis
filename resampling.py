#Qunadl2
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = '6GRG9BiEz-maqagk9H5z'

df = quandl.get('FMAC/HPI_AK',authtoken=api_key)

# print(df.head())
def state_list():
	fiddy_states = pd.read_csv('state_table.csv')
	return fiddy_states.abbreviation

def grab_inital_state_data():
	states = state_list()
	main_df =pd.DataFrame()
	for abbv in states:
		query = "FMAC/HPI_" +str(abbv)
		df = quandl.get(query ,authtoken = api_key)
		df.rename(columns = {'Value':str(abbv)}, inplace = True)
		df[abbv] = (df[abbv] - df[abbv][0] ) /df[abbv][0]* 100.0
		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df)
			#PICKLE VERSION
	pickle_out = open ('fiddy_states3.pickle','wb')
	pickle.dump(main_df,pickle_out)
	pickle_out.close()

#grab_inital_state_data()
def HPI_Benchmark():
	df = quandl.get('FMAC/HPI_USA',authtoken=api_key)
	df.rename(columns = {'Value':str('United States')}, inplace = True)
	print (df['United States'])
	df["United States"] = (df["United States"] - df["United States"][0] ) /df["United States"][0]* 100.0
	return df

fig = plt.figure()
ax1 =plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('fiddy_states3.pickle')

Tx1yr = HPI_data['TX'].resample('A', how ='ohlc')

#Tx1yr = HPI_data['TX'].resample('A', how ='mean')

HPI_data['TX'].plot(ax = ax1 ,label ='Monthly Tx HPI')
Tx1yr.plot(ax = ax1,label ='yearly Tx HPI')

plt.legend(loc=4)
plt.show()

HPI_data['TX'].plot(ax = ax1)
benchmark = HPI_Benchmark()

HPI_data.plot(ax =ax1)
benchmark.plot(ax =ax1 ,color ='k', linewidth =10)

plt.legend().remove()
plt.show()

# HPI_states_correlation =HPI_data.corr() # provides the corellation 
# # print(HPI_states_correlation)
# print (HPI_states_correlation.describe()) # provides the descreption

