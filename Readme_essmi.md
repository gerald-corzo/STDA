**Drought Index** - Empirical Standardized Soil Moisture (ESSMI)

**Desription**
ESSMI is a good indicator for evaluating drought degree and probability while only using soil moisture record. We roughly realized the codes through the framework proposed by the ESSMI authors since that the essmi calculation seems not be publical released. (we do not strictly follow the original recommended method for optimizing bandwidth selection of KDE)

Reference: 
Carrão, Hugo, et al. "An empirical standardized soil moisture index for agricultural drought assessment from remotely sensed data." International journal of applied earth observation and geoinformation 48 (2016): 74-84.

**Features:**
  1.Estimates (agricultural) drought index from monthly timse series
  2.Estiimates drought index corresponding to the values per month and generates a time series of thresholds

**Codes:**
The related repository is attached in the STDA path, including:
essmi_indicator.py (functions: essmi calculation and visualizaiton),
essmi_main.py(main program), and 
era5_monthly_averaged_sm.nc(sample data for input)
