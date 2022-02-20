from cProfile import label
from scipy.stats import gamma
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as st

#Standardized Precipitation Index Function
def spi(Ts, Span):
    #% spi(ts, Span)  Stadard precipitation index
    #%  Span in months
    #% ts dataframe 
    #% [Z]=SPI(tsz);
    #%  Applies a  gama fit, then calculates the probability of zeros
    #%  and then makes a cumulative probability function with the gama fit plus
    #%  the probability of non-zeros, after this it makes a zscore calculation
    #%  which is a conventional statistical normalization of the data
    #%  Convert into a normal distribution and based on the prob. of the gama
    #%  calculates the Z value of the normal distribution
    #% Developed by: Gerald Corzo
    #% Updated from Matlab version Novembre 2009, Wageningen University, The Netherlands
    #% Copyright Gerald A. Corzo

    '''Scale Parameter (β)
    The scale parameter for the gamma distribution represents the mean time between events. Statisticians denote this parameter using beta (β).

    For example, if you measure the time between accidents in days and the scale parameter equals 4, there are four days between accidents on average.
    
    Shape Parameter (α)
    
    The shape parameter for the gamma distribution specifies the number of events you are modeling. For example, if you want to evaluate probabilities for the elapsed time of three accidents, the shape parameter equals 3. Shape must be positive, but it does not have to be an integer. Statisticians denote the shape parameter using alpha (α).

    The plot below shows how changing the shape parameter affects the distribution while holding the other parameters constant.
    
    fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data)
    https://statisticsbyjim.com/probability/gamma-distribution/
    https://github.com/jeffjay88/Climate_Indices/blob/main/1D_spi_pandas.ipynb 
    '''

    #ds - data ; thresh - time interval / scale
    #Rs=ts.resample('M').sum()
    #Rs=ts.rolling('30D').sum()
    #Rs.plot()
    #print(len(Rs))
    
    #Rolling Mean / Moving Averages
    ds_ma = Ts.rolling(Span, center=False).mean()
    

    #Natural log of moving averages
    ds_In = np.log(ds_ma)
    ds_In[ np.isinf(ds_In) == True] = np.nan  #Change infinity to NaN
    
    #Overall Mean of Moving Averages
    ds_mu = np.nanmean(ds_ma)
    
    #Summation of Natural log of moving averages
    ds_sum = np.nansum(ds_In)
        
    #Computing essentials for gamma distribution
    n = len(ds_In[Span-1:])                  #size of data
    A = np.log(ds_mu) - (ds_sum/n)             #Computing A
    alpha = (1/(4*A))*(1+(1+((4*A)/3))**0.5)   #Computing alpha  (a)
    beta = ds_mu/alpha                         #Computing beta (scale)
    
    #gamma, exponential, Weibull, and lognormal
    #Gamma Distribution (CDF)

    Gamma = gamma.cdf(ds_ma, a=alpha, scale=beta)  
    
    #Standardized Precipitation Index   (Inverse of CDF)
    norm_spi = st.norm.ppf(Gamma, loc=0, scale=1)  #loc is mean and scale is standard dev.
    
    return ds_ma, ds_In, ds_mu, ds_sum, n, A, alpha, beta, Gamma, norm_spi



def PlotSPI(S,Ts):
    fig, ax = plt.subplots()

    ax2 = ax.twinx()
    #plt.subplots_adjust(hspace=0.15)
    col_scheme=np.where(S>-1, 'b','r')
    #ax2.invert_yaxis()

    ax2.plot(Ts,alpha=0.5)
    Mylim=ax2.get_ylim()
    plt.ylim(Mylim[0],Mylim[1]*1.4)
    #print()

    #ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.bar(Ts.index, S, width=25, align='center', color=col_scheme, label='SPI ',alpha=0.5)

    ax.axhline(y=0, color='k')
    #ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.legend(loc='upper right')
    ax.set_yticks(range(-3,4), range(-3,4))
    ax.set_ylabel('SPI', fontsize=12)

    ax2.set_ylabel('Ranfall (mm)', color='b')
    plt.grid()
    plt.show()   


def PlotTsScales(Df):
    
    fig, ax = plt.subplots()
    ax2=ax.twinx()
    Rs=Df.resample('D').sum()
    ax2.plot(Rs,alpha=0.3, label='Daily')
    ax2.legend(['Daily'],loc='upper left')
    #ax2.legend(handles=[line1], loc='upper right')
    print(len(Rs))


    Rs=Df.resample('M').sum()
    ax.plot(Rs,color='g', label='Montly',linestyle='-.')
    print(len(Rs))
    #ax.legend('Montly')

    Rs=Df.resample('Y').sum()
    ax.plot(Rs,color='c', label='Yealy',linestyle='--')
    print(len(Rs))
    #ax.legend('Yearly')
    
    #plt.legend(['Daily','Monthly','Yearly'],loc='lower right')
    handles, labels = ax.get_legend_handles_labels()

    # reverse the order
    ax.legend(handles[::-1], labels[::-1])
    plt.title('Graph of time series at different time steps (sum)')


def PlotRollingWindos(Df):
    fig, ax = plt.subplots()
    ax2=ax.twinx()
    
    Rs=Df.rolling('30D').mean()
    ax2.plot(Rs, label='30 D Mean')
    print(len(Rs))
    ax2.plot(Rs,alpha=0.3, label='Daily')
    ax2.legend(['30 Days'],loc='upper left')

    Rs=Df.rolling('60D').mean()
    ax.plot(Rs,label='60 Days Mean')
    print(len(Rs))

    Rs=Df.rolling('90D').mean()
    ax.plot(Rs,label='90 Days Mean')
    print(len(Rs))
    handles, labels = ax.get_legend_handles_labels()

    # reverse the order
    ax.legend(handles[::-1], labels[::-1])
    plt.title('Moving window analysis')