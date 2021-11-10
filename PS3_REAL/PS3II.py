# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 17:15:35 2021

@author: Administrator
"""

import netCDF4 as nc
import xarray as xr
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn
#import file (please read together rather than line by line)
import os
wdir = os.path.realpath(os.curdir)
b = os.path.split(os.path.realpath(__file__))[0]
b = os.path.join(b, 'CERES_EBAF-TOA_200003-201701.nc')
ds2 = xr.open_dataset(b, engine = 'netcdf4')

#2.1
ds2.toa_lw_all_mon.mean(dim = 'time').plot(size = 7, robust = True)
ds2.toa_sw_all_mon.mean(dim = 'time').plot(size = 7, robust = True)
ds2.toa_net_all_mon.mean(dim = 'time').plot(size = 7, robust = True)

dsadd = ds2.toa_lw_all_mon+ds2.toa_sw_all_mon+ds2.toa_net_all_mon
dsadd.mean(dim = 'time').plot(size = 7, robust = True,cbar_kwargs={'label' : 'radiation_add_up'})
ds2.solar_mon.mean(dim = 'time').plot(size = 7, robust = True)

#2.2
weights = np.cos(np.deg2rad(ds2.lat))
ds2.toa_lw_all_mon.mean(dim = 'time').weighted(weights).mean(dim = ('lon','lat'))
#240.26666558
ds2.toa_sw_all_mon.mean(dim = 'time').weighted(weights).mean(dim = ('lon','lat'))
#99.13858336
ds2.solar_mon.mean(dim = 'time').weighted(weights).mean(dim = ('lon','lat'))
#340.28355233
#ds2.toa_cre_lw_mon.mean(dim = 'time').weighted(weights).mean(dim = ('lon','lat'))

#2.3 total amount of net radiation (of solar?)
ds2.solar_mon.mean(dim = 'lat').plot(size = 7, robust = True, cbar_kwargs={'label' : 'solar_mon(W m-1)'})
ds2.toa_net_all_mon.mean(dim = 'lat').plot(size = 7, robust = True, cbar_kwargs={'label' : 'net_radiation_mon(W m-1)'})

#2.4
#low cloud (<=25%)
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(6, 9))
ds2.toa_sw_all_mon.where(ds2.cldarea_total_daynight_mon <= 25).mean(dim = 'time').plot(ax = ax1, robust = True)
ds2.toa_lw_all_mon.where(ds2.cldarea_total_daynight_mon <= 25).mean(dim = 'time').plot(ax = ax2, robust = True)
ax1.set_title('low cloud short wave radiation')
ax2.set_title('low cloud long wave radiation')
fig.tight_layout()

#high cloud(>=75%)
fig1, (ax3, ax4) = plt.subplots(2, 1, sharex=True, figsize=(6, 9))
ds2.toa_sw_all_mon.where(ds2.cldarea_total_daynight_mon >= 75).mean(dim = 'time').plot(ax = ax3, robust = True)
ds2.toa_lw_all_mon.where(ds2.cldarea_total_daynight_mon >= 75).mean(dim = 'time').plot(ax = ax4, robust = True)
ax3.set_title('high cloud short wave radiation')
ax4.set_title('high cloud long wave radiation')
fig1.tight_layout()

#2.5
ds2.toa_lw_all_mon.where(ds2.cldarea_total_daynight_mon <= 25).mean(dim = 'time').weighted(weights).mean(dim = ('lon','lat'))
#270.8530266 v.s. #240.26666558
ds2.toa_sw_all_mon.where(ds2.cldarea_total_daynight_mon <= 25).mean(dim = 'time').weighted(weights).mean(dim = ('lon','lat'))
#75.49432387 v.s. #99.13858336

ds2.toa_lw_all_mon.where(ds2.cldarea_total_daynight_mon >= 75).mean(dim = 'time').weighted(weights).mean(dim = ('lon','lat'))
#225.7084414 v.s. #240.26666558
ds2.toa_sw_all_mon.where(ds2.cldarea_total_daynight_mon >= 75).mean(dim = 'time').weighted(weights).mean(dim = ('lon','lat'))
#113.15712212 v.s. #99.13858336


