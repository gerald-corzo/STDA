# Drought Analysis 


## Desription
This repository contains a simple library (file) called STDA (Spatial Temoral Drought Analysis)


## Features
* Estimates hydrological drought from timse series 
* Makes monthly analysis of daily data 
* Estiimates percentiles per month and generates a time series of thresholds
* Makes the analysis of drought events.

## Examples

Read file

    $ Df=pd.read_excel('BagmatiDischarge.xlsx',index_col=0,parse_dates=True)

Estimate the monthly Percentiles
    $ Pm=MonthlyPercentiles(ts,Percentile=5)

Obtain a time series of this percentiles

    $ Tts=ExtendThresholds(ts,Pm)

## Making the drought analysis

Using the time series read above and the threshold

    $ EstimateDrought(ts,Tss,PoolValue=5,MinDrought=3)


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