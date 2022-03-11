# Drought Analysis 


## Desription
This repository contains a library called STDA (Spatial Temoral Drought Analysis) that estimates various types of drought indicators and analysis time series of drought events. 

## Features

Meteorological drought from time series
- Calaculates the SPI (inside file called indicators)
- Calculates drough events assuming you define a SPI threshold (-1,-1.5...)
- Provides tools to tak into account the concept of pooling(consecutive drought event) and remove short droughts

Hydrological drought
- Time series in format of Data frame with datetime column can be used to estimate monthly aggregates. 
- Estimates a threshold based on the monthly averages (and uses a moving average to soften the threshold monthly boundaries)
- Estimate the number of event comparing the hydrological discharge with the threshold estimated from historical values

Soil Moisture Index *Empirical Standardized Soil Moisture, ESSMI)

Evaluates drought degree and probability while only using soil moisture record. We roughly realized the codes through the framework proposed by the ESSMI authors since the essmi calculation seems not be publical released. (we do not strictly follow the original recommended method for optimizing bandwidth selection of KDE)

Reference: Carrão, Hugo, et al. "An empirical standardized soil moisture index for agricultural drought assessment from remotely sensed data." International journal of applied earth observation and geoinformation 48 (2016): 74-84.

Features: 
1.Estimates (agricultural) drought index from monthly timse series 
2.Estiimates drought index corresponding to the values per month and generates a time series of thresholds

Codes: The related repository is attached in the STDA path, including: essmi_indicator.py (functions: essmi calculation and visualizaiton), essmi_main.py(main program), and era5_monthly_averaged_sm.nc(sample data for input, ERA5 monthly soil moisture averaged from hourly data in Spain)- 



* Estimates hydrological drought from timse series 
* Makes monthly analysis of daily data 
* Estiimates percentiles per month and generates a time series of thresholds
* Makes the analysis of drought events.

## Examples

Read file

    $ Df=pd.read_excel('BagmatiDischarge.xlsx',index_col=0,parse_dates=True)
> Here we assume you are looking for a threshold analysis based on hydrological daily time series data (River discharge)

Estimate the monthly Percentiles
    $ Pm=MonthlyPercentiles(ts,Percentile=5)

> To find an anomaly here we look at monthly values of daily dischage and find the percentile (95%) of lowest values in the history of daily values in a month). For this the data needs to have been provided with date column. 

Obtain a time series of this percentiles


    $ Tts=ExtendThresholds(ts,Pm)

> Since the monthly percentile is only one per month, here we extend the time series to have one value of percentile per each value of the time serie (assuming daily streamflows)

    $ SmoothMonth(Tst,Span)
> Since the percentiles refer to an anomaly event, and a step-wise percentile is not realisitic, it is suggested to make it smooth, by applyting a moving average. The value of the span here referes to the number of daily time steps which you want to consider on the smoothing (Moving Aaverage)

## Making the drought analysis

Using the time series read above and the threshold
Tss is a numpy array of Threshold (time series)
ts is the time series of the Drought indicator, can be SPI or can be a variable is the threshold is a moving average of a percentile (used to deinfe drought as an anomaly) 

    $ EstimateDrought(ts,Tss,PoolValue=5,MinDrought=3)
> Definition of drought will be an anomaly on daily discharges and will be defined 


##  STDA.py

Contains:
1. MonthlyPercentiles 
2. ExtendThresholds
3. SmoothMonth 

---

> In the example you will see that the main function reads a time series data from Excel file
> Then provides uses MonthlyPercentiles to obtain a time series of thresholds (per month)
> Then Smooth performs a moving average to have a smooth threshold for your time series
> Then Drought Analysis is used to define values 1 as drough (below the threshold) and 0 as normal. Then number of events, start and end of events are calculated




[STAND](https://research.tudelft.nl/en/publications/an-approach-to-characterise-spatio-temporal-drought-dynamics)


### 1.0.0.0
* Initial release.

## License
copyright Copyright (C) 2022 Gerald corzo

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under the conditions of the GPLv3 license.
