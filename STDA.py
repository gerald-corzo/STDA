import numpy as np

def MonthlyPercentiles(ts,Percentile=5):
    """
    MonthlyPercentiles _summary_

    _extended_summary_

    Parameters
    ----------
    ts : Pandas (time series)
        Value to estimate the percentile
    Percentile : int, optional
        _description_, by default 5

    Returns
    -------
    _type_
        Array of 12 months percentile (assuming daily values were in the time series)
    """
    Tst=np.zeros(len(ts))
    Nts=ts.groupby(by=[ts.index.month])
    P=np.zeros(len(Nts.groups))
    for i in range(12):
        P[i]=np.percentile(Nts.get_group(i+1),Percentile)
    return P

def ExtendThresholds(ts,Pm):
    """
    ExtendThresholds Projects and array from 12 values into an array of the size
    of the time series provided. In general, copying the values in the Pm array and
    copying it into the corresponding days of each month of each year. Is to not
    that the Pm stands for Percentile each months and this routing is made
    to analyse the concept of drought 
    Parameters
    ----------
    ts : Numpy
        time series of one variable
    Pm : numpy array
        array contaning float values that correspondong to each month

    Returns
    -------
    Tst
    Numpy Array with the time series data of the daily percentiles
        
    """    
    Tst=np.zeros(len(ts))
    for i,v in enumerate(ts):
        M=ts.index.month[i]
        Tst[i]=Pm[M-1]
        #print(i)
    #print(len(Tst))    
    
    return Tst

def SmoothMonth(Tst,Span):
    """
    SmoothMonth Moving Average smooth of a time series

    Parameters
    ----------
    Tst : Numpy array (1d)
        _description_
    Span : Int
        Number of time steps in the centered moving average

    Returns
    -------
    Numpy time series
        moving average of the time series used as input
    """    
    #For pandas time series
    #Roll=Tst.rolling(window=Span,center=Center)
    #MA=Roll.mean()    
    MA=np.convolve(Tst, np.ones(Span), 'full') / Span

    return MA[:-(Span-1)]


def EstimateDrought(ts,Tss,PoolValue=5,MinDrought=3):
    
    Dts=np.zeros(len(ts))
    Dts[ts<Tss]=1
    nd=0
    Start=[]
    End=[]
    Dur=[]
    for i,v in enumerate(Dts):
        #Change to drought
        if v == 1 and i!=0:
            #Check pooling
            if End[-1]-i>PoolValue:
                if Dts[i-1]==0:
                    Start.append(i)
                    nd=nd+1
            else:
                End.pop()
                print(r'Pooled together in ts={i} date={ts.index[i]}')
        #Change to no drought
        if v == 0 and i!=0:
            if Dts[i-1]==1:
                End.append(i)
                if End[-1]>Start[-1]: 
                    if Dur[-1]<MinDrought:
                        Dur.append(End[-1]-Start[-1])
                else:
                    print('Time series started with a Drought state')
                    nd=nd+1



    print(nd)
    print(Start)
    print(End)
    return nd, Start,End