#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from STDA import *
from Indicators import *

#%%
Df=pd.read_excel('Bagmati.xlsx',index_col=0,parse_dates=True)
Df.head()

# %%
#Make Monthly
PlotTsScales(Df['P'])

# %%
PlotRollingWindos(Df['P'])


#%%
#Create Monthly time series 
Ts=Df['P'].resample('M').sum()
Ts.plot()
plt.grid()
plt.title('Monthly time series')

# %%
#SPI defined by the Span 
Span=1
x=spi(Ts,Span)

# %%
S=x[9]
PlotSPI(S,Ts) 


# %%

Tss=np.ones(len(Ts))*-1
#Ts['Th']=Tss

EstimateDrought(S,Tss,PoolValue=1,MinDrought=1)


#plt.pcolor()
# %%
