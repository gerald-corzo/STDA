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

# %% Obtaining the threshold time series
Tts=ExtendThresholds(ts,Pm)


# %%
Tss=SmoothMonth(Tts,10)


# %%
ND,St,En=EstimateDrought(ts,Tss,PoolValue=5,MinDrought=3)



#%%



<<<<<<< HEAD
=======


# %%
>>>>>>> 477f0ecbfb325a5a4a2e398bf0b20e387a613339
