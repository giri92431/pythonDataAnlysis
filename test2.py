import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style 
import numpy as np
style.use('ggplot')


web_stats = {'Day':[1,2,3,4,5,6,],
			'Visitors':[43,54,65,23,53,32],
			'Bounce_Rate':[65,52,62,64,54,66]}

df = pd.DataFrame(web_stats)

# print(df)
# print(df.head())
# print(df.tail())

# df = df.set_index("Day")

df.set_index('Day' ,inplace= True )
# print(df.Visitors.tolist())

print(np.array(df[['Bounce_Rate','Visitors']]))


df2 = pd.DataFrame(np.array(df[['Bounce_Rate','Visitors']]))
print (df2)
