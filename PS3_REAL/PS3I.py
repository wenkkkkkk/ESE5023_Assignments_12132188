# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 15:34:01 2021

@author: Administrator
"""

import netCDF4 as nc
import xarray as xr
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn
import os

#1.1
#read file
wdir = os.path.realpath(os.curdir)
a = os.path.split(os.path.realpath(__file__))[0]
a = os.path.join(a, 'NOAA_NCDC_ERSST_v3b_SST.nc')
ds = xr.open_dataset(a, engine = 'netcdf4')

#position
pos = ds.sst.sel(lat = slice(-5,5), lon = slice(190,240))

# Group data by month
group_data = ds.sst.sel(lat = slice(-5,5), lon = slice(190,240)).groupby('time.month')

# Apply mean to grouped data, and then compute the anomaly 
tas_anom = group_data - group_data.mean(dim='time')

#3-month rolling means
me3 = tas_anom.rolling(time = 3, min_periods=2, center= True).mean()

#regional mean
weights = np.cos(np.deg2rad(pos.lat))
reg_mean = me3.weighted(weights).mean(dim=['lat', 'lon'])
me3.weighted(weights).mean(dim=['lat', 'lon']).plot()


#1.2
fig, ax1 = plt.subplots(1, 1, sharex=True, figsize=(6, 6))
ax1.fill_between(reg_mean.time.values, 0, reg_mean.values,where= reg_mean.values>0, facecolor = 'red')
ax1.fill_between(reg_mean.time.values, 0, reg_mean.values,where= reg_mean.values<0, facecolor = 'blue')
ax1.plot(reg_mean.time.values,reg_mean.values, color = "black", alpha = 0.5, label = '3 months running mean')
ax1.axhline(y = 0.5, ls = '--', color = 'red', alpha = 0.5, label = 'El Nino threshold')
ax1.axhline(y = -0.5, ls = '--', color = 'blue', alpha = 0.5, label = 'La Nina threshold')
ax1.set_ylabel('anomaly/°C')
ax1.set_xlabel('year')
ax1.set_title('SST Anomaly in Nino 3.4 Region (5N-5S, 120-170W)')
ax1.legend()
fig.tight_layout()














