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


PoolValue=5
Dts=np.zeros(len(ts))
Dts[ts<Tss]=1
nd=0
Start=[]
End=[]
for i,v in enumerate(Dts):
    #Change to drought
    if v == 1 and i!=0:
        if Dts[i-1]==0:
            Start.append(i)
            nd=nd+1
    #Change to no drought
    if v == 0 and i!=0:
        if Dts[i-1]==1:
            End.append(i)
            if End[-1] >Start[-1]: 
                Dur=End[-1]-Start[-1]
                
            else:
                print('Time series started with a Drought state')
                nd=nd+1



print(nd)
print(Start)
print(End)
# %%
