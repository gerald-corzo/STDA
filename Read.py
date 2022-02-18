#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
Df=pd.read_excel('BagmatiDischarge.xlsx',index_col=0,parse_dates=True)
#Df.set_index(pd.DatetimeIndex(Df['Date'])
Df.head()
#Df=Df.iloc[:3]
#Df.plot(x='Date',y='Calibrated')


#%%
ts=Df['Calibrated']
ts.plot()
#ts=ts.to_numpy()



#%%
#group by
Nts=ts.groupby(by=[ts.index.month])
Nts.head()

#Percentiles
P=Nts.describe(percentiles=[0.05,0.1,0.15,0.2])
#Threshold Array
Ths=P['5%'].array
Ths=Ths.to_numpy()

#Tsd time series of thresholds Tst and moving average Tsm
Tst=np.zeros(len(ts))
Tsm=np.zeros(len(ts))

Span=10




#%%
for i,v in enumerate(ts):
    M=ts.index.month[i]
    #Time series Threshold    
    Tst[i]=Ths[M-1]
    if i>Span:
        Tsm[i]=np.sum(Tst[(i-Span+1):(i+1)])/Span
    else:
        Tsm[i]=Tst[i]
    

#%%
plt.plot(Tst)
plt.plot(Tsm,'-g')
plt.xlim(Span,Span+150)
plt.ylim(0,20)


#%%
#read data
Th=np.percentile(ts,5)



#%%
x=np.linspace(1,len(ts),len(ts))
y=Th*np.ones(len(x))
plt.plot(x,y,'r.')
plt.plot(ts)


# %%
#My time series

Dts=np.zeros(len(ts))
Dts[ts<Th]=1
plt.plot(Dts)

#%%
#How many drought
nd=np.sum(Dts)


# %%
def CalcNDroughts(ts,Perc=20):
    #Receives the ts
    #Receive the Perc
    Th=np.percentile(ts,Perc)
    Dts=np.zeros(len(ts))
    Dts[ts<Th]=1
    nd=0
    for i,v in enumerate(Dts):
        if v == 0 and i!=0:
            if Dts[i-1]==1:
                nd=nd+1 
    print(nd)
    return nd,Dts

#%%

for i in [5,10,15,20,25,30,35]:
    Nd,Ts2=CalcNDroughts(ts,Perc=i)



# %%
def PlotDts(ts,Perc=5):
    Th=np.percentile(ts,Perc)
    x=np.linspace(1,len(ts),len(ts))
    y=Th*np.ones(len(x))
    plt.plot(x,y,'r.')
    plt.plot(ts)
    plt.figure(figsize=(10,5))
    #plt.xlim(500,800)
    #plt.xlim(1210,1240)
    return Th

# %%
