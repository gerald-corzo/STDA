#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from STDA import *

#%%
Df=pd.read_excel('BagmatiDischarge.xlsx',index_col=0,parse_dates=True)
Df.head()
Df.plot(y='Calibrated')
ts=Df['Calibrated']
ts.plot()

# %%
Pm=MonthlyPercentiles(ts,Percentile=5)
plt.plot(Pm)
plt.title('Percentile of monthly values')

# %%
