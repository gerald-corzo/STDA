import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from essmi_indicator import *
import xarray as xr


ds = xr.open_dataset('spain_era5_monthly_averaged_sm.nc')
data = ds['svw1_mean']
x = data[:, 25, 36].values # randomly select a point
cdf_x, essmi_fit, kde_cdf, essmi = essmi_count(x)

# Plot the essmi results
date = pd.period_range('2010-01', periods=132, freq='M') # datetime made in attached example
PlotESSMI(x, essmi, date)
