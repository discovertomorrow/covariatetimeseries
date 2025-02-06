# Covariate Time Series Collection 🕰️📊

:rocket: This repository provides a collection of time series with covariates and indicators. It’s designed to be ready-to-use for forecasting projects. :chart_with_upwards_trend:

## 🌟 Overview of the Collection

- **383 time series** (173 endogenous, 210 exogenous) sourced from **12 datasets**.  
- Covering four domains:  
  - 📦 *Demand*  
  - ⚡ *Energy*  
  - 🌿 *Nature*  
  - 👫 *Human*  
- Multiple granularities: *minutely, hourly, daily, weekly, monthly, quarterly* (majority are hourly and daily).  
- Time series lengths range from **74 datapoints** to over **2 million datapoints**.  
- Includes **past**, **future**, and **categorical covariates**, with up to **64 covariates** per series.  

## 🛠️ Preprocessing Details
 
- A `date` column is included in the format `YYYY-MM-DD` or `YYYY-MM-DD HH:MM:SS`.  
- Missing values have been imputed based on the characteristics of each time series.  
- Only numerical values are included (categorical features are represented as integers).  
- No normalization has been applied.  

## 📋 Dataset Overview  

The  dataset overview table (src/covariatetimeseries/data_collections/_collection_info.csv) provides details about:  
- Dataset names (similar to file names without extension).  
- Domains, granularities, and time series lengths.  
- Lists of targets and covariates names (separated into past, future, and categorical covariates).  
- Number of time series per dataset and corresponding column name. 

A more detailed description is available in the dataset description notebook (dataset_description.ipynb).

## ⬇️ Installation

In order to use `covariatetimeseries`, you need a Python environment with Python 3.9 or higher.

You can install the package directly from Github using `pip`:

```bash
pip install git+https://github.com/discovertomorrow/covariatetimeseries.git@v1.0
```

## 📂 How to Use

```python
import covariatetimeseries as cots

# Get and overview with
cots.meta

# Get the hole data set with cots.[datasetname]
cots.illness

# Get time series with a single target column.               
cots.load_timeseries(dataset_name='housing',
                     target_name='CSUSHPISA',
                     ts_name=None,                   # optional - Use if there are multiple time series with the same target column, ex. target_name='sales', ts_name="item_1"
                     other_targets_as_covs=True,     # optional - other targets were returned as past covariates
                     exclude_time_covariates=False,  # optional - if true covariates like weekday were excluded
                     verbose=True)                   # optional - prints a summary of the dataset and different covariates

          date   CSUSHPISA  MORTGAGE30US    UMCSENT  INTDSRUSM193N   MSPUS        GDP    MSACSR       PERMIT    TLRESCONS  EVACANTUSQ176N  quarter  year
0   2003-01-01  129.321000      5.840769  79.966667       2.250000  186000  11174.129  4.200000  1806.333333  421328.6667           14908        1  2003
1   2003-04-01  131.756000      5.506923  89.266667       2.166667  191800  11312.766  3.833333  1837.666667  429308.6667           15244        2  2003
2   2003-07-01  135.013000      6.033846  89.300000       2.000000  191900  11566.669  3.633333  1937.333333  458890.0000           15614        3  2003
3   2003-10-01  138.835667      5.919286  91.966667       2.000000  198800  11772.234  3.966667  1972.333333  491437.3333           15654        4  2003
4   2004-01-01  143.298667      5.597500  98.000000       2.000000  212700  11923.447  3.700000  1994.666667  506856.3333           15895        1  2004
..         ...         ...           ...        ...            ...     ...        ...       ...          ...          ...             ...      ...   ...
69  2020-04-01  217.239000      3.239231  74.066667       0.250000  322600  19636.731  5.300000  1210.666667  603744.6667           13876        2  2020
70  2020-07-01  222.641333      2.952308  75.666667       0.250000  337500  21362.428  3.400000  1577.666667  646601.6667           14249        3  2020
71  2020-10-01  233.090000      2.760714  79.800000       0.250000  358700  21704.706  3.866667  1698.333333  707944.3333           15446        4  2020
72  2021-01-01  242.267000      2.875833  80.233333       0.250000  369800  22313.850  4.333333  1765.666667  753515.6667           15602        1  2021
73  2021-04-01  253.814000      3.003846  85.566667       0.250000  382600  23046.934  5.300000  1679.333333  795501.3333           15658        2  2021

[74 rows x 13 columns]

```
