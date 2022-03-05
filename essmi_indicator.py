import numpy as np
#import pylab as plt
import datetime
import pandas as pd
import xarray as xr
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
#------------------------------#
# Ref: Carrão, Hugo, et al. "An empirical standardized soil moisture index for agricultural drought assessment from remotely sensed data."
#      International journal of applied earth observation and geoinformation 48 (2016): 74-84.
# Code by: Xiaoyi Wang
# Date: 03-04-2022
#------------------------------#
# Empirical standard soil moisture index
def essmi_count(ts):
    # Ref: Carrão, Hugo, et al. "An empirical standardized soil moisture index for agricultural drought assessment from remotely sensed data."
    # International journal of applied earth observation and geoinformation 48 (2016): 74-84.
    
    # ts represents a time-series data at a location(grid)
    
    # STEP1: log transform for ds, for matching the requirement of KDE
    ts_in = np.log(ts) - np.log(1 - ts)
    
    # STEP2: KDE is empolyed to estimate PDF
    kde = sm.nonparametric.KDEUnivariate(ts_in)
    kde.fit(kernel='gau', bw='normal_reference', fft=True, weights=None, gridsize=None)  # Estimate the densities
    
    # STEP3: retrieve essmi (Inverse of CDF)
    kde_cdf = kde.cdf
    essmi_fit = stats.norm.ppf(kde_cdf, loc=0, scale=1)
    cdf_x = np.exp(kde.support) / (1 + np.exp(kde.support)) # Convert the xticklabel(log transformed data) to original data in CDF plot  
    
    # STEP4: Obatain essmi time series at different data ticks
    essmi = stats.norm.ppf(np.interp(ts, cdf_x, kde.cdf), loc=0, scale=1)

    return cdf_x, essmi_fit, kde_cdf, essmi
    
def PlotESSMI(ts, essmi, date):
    # date = pd.period_range('2010-01', periods=132, freq='M') # datetime made in attached example
    fig, ax = plt.subplots(figsize=(10, 4))
    ax2 = ax.twinx()
    #plt.subplots_adjust(hspace=0.15)
    col_scheme=np.where((essmi>-1) & (essmi<1), 'b','r') # blue means noral while red means dry or wet
    ax2.scatter(date.to_timestamp(),x,alpha=1, s=4.5, marker='^',edgecolors='k')
    Mylim=ax2.get_ylim()
    plt.ylim(Mylim[0],Mylim[1]*1.4)
    ax.bar(date.to_timestamp(), S, width=25, align='center', color=col_scheme, label='ESSMI ',alpha=0.5)
    ax.axhline(y=-1, color='g',linestyle='--')
    ax.axhline(y=1, color='g',linestyle='--')
    ax.set_ylabel('ESSMI', fontsize=12)
    ax.set_xlim([datetime.date(2010,1,1), datetime.date(2020,12,31)])
    ax2.set_ylabel('Soil moisture (${m^3}$/${m^3}$)',fontdict={'weight': 'normal', 'size': 12})
    plt.grid(color='grey', linestyle='--', linewidth=0.5)
    #plt.savefig(r'C:\ESSMI_single_pixel_11years.png',dpi=300)
    plt.show() 
    
