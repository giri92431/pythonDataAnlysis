

#Qunadl2
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = '6GRG9BiEz-maqagk9H5z'

df = quandl.get('FMAC/HPI_AK',authtoken=api_key)

def HPI_Benchmark():
	df = quandl.get('FMAC/HPI_USA',authtoken=api_key)
	df.rename(columns = {'Value':str('United States')}, inplace = True)
	df["United States"] = (df["United States"] - df["United States"][0] ) /df["United States"][0]* 100.0
	return df

def mortgage_30():
	df =quandl.get("FMAC/MORTG",trim_start="1975-01-01" ,authtoken =api_key)
	df.rename(columns = {'Value':str('value')}, inplace = True)
	df["value"] = (df["value"] -df["value"][0])/df["value"][0] * 100.0
	df = df.resample('d').mean()
	df = df.resample('M').mean()
	df.columns =['m30']
	return df

def sp500_data():
    df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=api_key)
    df["Adjusted Close"] = (df["Adjusted Close"]-df["Adjusted Close"][0]) / df["Adjusted Close"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Adjusted Close':'sp500'}, inplace=True)
    df = df['sp500']
    return df

def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Value':'GDP'}, inplace=True)
    df = df['GDP']
    return df

def us_unemployment():
    df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=api_key)
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df=df.resample('1D').mean()
    df=df.resample('M').mean()
    return df

m30 = mortgage_30();	
HPI_data = pd.read_pickle('fiddy_states3.pickle')
HPI_bench = HPI_Benchmark()
sp500 = sp500_data()
gdp = gdp_data()
unemployment = us_unemployment()
HPI = HPI_data.join([HPI_bench,m30,sp500,gdp,unemployment])
HPI.dropna(inplace = True)

HPI.to_pickle('HPI.pickle')

# State_HPI_M30 =HPI_data.join(m30)

# print(State_HPI_M30.corr()['m30'].describe())




