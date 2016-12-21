# getting to know about quandl

import quandl
import pandas as pd
import pickle

api_key = '6GRG9BiEz-maqagk9H5z'

df = quandl.get('FMAC/HPI_AK',authtoken=api_key)

# print(df.head())
def state_list():
	fiddy_states = pd.read_csv('state_table.csv')
	return fiddy_states.abbreviation

# print (fiddy_states.abbreviation)

def grab_inital_state_data():
	states = state_list()
	main_df =pd.DataFrame()
	for abbv in states:
		query = "FMAC/HPI_" +str(abbv)
		df = quandl.get(query ,authtoken = api_key)
		df = df.pct_change()
		df.rename(columns = {'Value':str(abbv)}, inplace = True)
		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df)
			#PICKLE VERSION
	pickle_out = open ('fiddy_states.pickle','wb')
	pickle.dump(main_df,pickle_out)
	pickle_out.close()

# grab_inital_state_data()

#PICKLE VERSION
# pickle_in = open ('fiddy_states.pickle','rb')

# hpi_data = pickle.load(pickle_in)
# #PICKLE VERSION


# # print(hpi_data)

# # pandas version 
# hpi_data.to_pickle('pickle.pickle')
# HPI_data = pd.read_pickle('pickle.pickle')
# HPI_data['TX2'] =HPI_data['TX'] *2
# print(HPI_data[['TX','TX2']])	






