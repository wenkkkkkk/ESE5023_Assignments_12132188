# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:21:01 2021

@author: Administrator
"""

#!/usr/bin/env python
import time
import traceback
import glob
import os, random, shutil
import sys
import argparse
import pandas as pd
import xarray as xr
import numpy as np
import netCDF4 as nc
# from scipy import ndimage
# import pyresample
# from osgeo import gdal, osr, gdal_array
# from skimage import morphology

# import multiprocessing as mp
import matplotlib.pyplot as plt

#3.1
wdir = os.path.realpath(os.curdir)
a = os.path.split(os.path.realpath(__file__))[0]
a = os.path.join(a, 'NOAA_NCDC_ERSST_v3b_SST.nc')
ds4 = xr.open_dataset(a, engine = 'netcdf4')

#Plot a time series of a certain variable with monthly seasonal cycle removed.

weights4 = np.cos(np.deg2rad(ds4.lat))


year_group_data = ds4.sst.groupby('time.year').mean()
yearsstglobal = year_group_data.weighted(weights4).mean(dim=['lat', 'lon'])

fig5, ax5 = plt.subplots(1, 1, sharex=True, figsize=(9, 6))
yearsstglobal.plot(ax = ax5)
ax5.set_title('year-averaged SST globally change')
ax5.set_ylabel('sst (°C)')
fig5.tight_layout()


#%% 3.2
wdir = os.path.realpath(os.curdir)
c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201901.001.nc')
d1 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201904.001.nc')
d4 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201907.001.nc')
d7 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201910.001.nc')
d10 = xr.open_dataset(c, engine = 'netcdf4')



# ds3 = xr.concat([d1,d4,d7,d10], dim='time')
# file is  too large to read at the same time...
ds3 = xr.merge([xr.open_dataset(f) for f in glob.glob(c)])

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201902.001.nc')
d2 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201903.001.nc')
d3 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201905.001.nc')
d5 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201906.001.nc')
d6 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201908.001.nc')
d8 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201909.001.nc')
d9 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201911.001.nc')
d11 = xr.open_dataset(c, engine = 'netcdf4')

c = os.path.split(os.path.realpath(__file__))[0]
c = os.path.join(c, 'FLDAS_NOAH01_CP_GL_M.A201912.001.nc')
d12 = xr.open_dataset(c, engine = 'netcdf4')


ds3 = xr.concat([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12], dim='time')


#ET
ds3.Evap_tavg.mean(dim = 'time').plot(size = 7, robust = True, cbar_kwargs={'label' : 'ET(Kg m-2 S-1)'})
#rainfall
ds3.Rainf_f_tavg.mean(dim = 'time').plot(size = 7, robust = True, cbar_kwargs={'label' : 'Rainfall(Kg m-2 S-1)'})
# total soil water
soil = ds3.SoilMoi00_10cm_tavg+ds3.SoilMoi40_100cm_tavg+ds3.SoilMoi10_40cm_tavg+ds3.SoilMoi100_200cm_tavg
soil = soil *1000
soil.mean(dim = 'time').plot(size = 7, robust = True, cbar_kwargs={'label' : 'Soil Moisture(kg/m3)'})



#snow cover percentage
ds3.SnowCover_inst.mean(dim = 'time').plot(size = 7, robust = True, cbar_kwargs={'label' : 'snow_cover_factor(%)'})
weights6 = np.cos(np.deg2rad(ds3.X))
sf = ds3.SnowCover_inst.weighted(weights6).mean(dim=['X','Y'])
sf.plot()

#snow depth
ds3.SnowDepth_inst.mean(dim = 'time').plot(size = 7, robust = True, cbar_kwargs={'label' : 'snow_depth_factor(m)'})

sf1 = ds3.SnowDepth_inst.weighted(weights6).mean(dim=['X', 'Y'])
sf1.plot()

#ds2.toa_sw_all_mon.where(ds2.cldarea_total_daynight_mon <= 25).mean(dim = 'time').plot(ax = ax1, robust = True)

