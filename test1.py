import pandas as pd
import datetime 
# import pandas.io.data as web
from pandas_datareader import data as web
import matplotlib.pyplot as pyplot
from matplotlib import style 
style.use('ggplot')

start = datetime.datetime(2005,1,1)
end = datetime.datetime(2016,1,1)

df = web.DataReader("XOM","yahoo",start,end)

print(df.head())

df['Adj Close'].plot()

pyplot.show()