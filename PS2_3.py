# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:50:14 2021

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


wind = pd.read_csv(r"E:\zwk\2281305.csv")

wsp = wind[['STATION','DATE','WND']]
wsp_wnd = wsp[['WND']]
wsp_wnd1 = wsp_wnd.astype(str)
wsp_wnd1 = wsp_wnd1.WND.str.split(pat = ',', expand = True)
wsp_wnd1.columns = ['wd','wq','wt','ws','wsq']


wsp1 = wsp.join(wsp_wnd1)

#filter

wsp1['wd'] = wsp1['wd'].astype(int)

wsp1 = wsp1[(wsp1['wd'] < 999)]

wsp1['wq'] = wsp1['wq'].astype(int)

wsp1 = wsp1[(wsp1['wq'] < 2)]

wsp1['ws'] = wsp1['ws'].astype(int)

wsp1 = wsp1[(wsp1['wq'] < 9999)]

#trend
wsp_date = wsp[['DATE']]
wsp_date1 = wsp_date.astype(str)
wsp_date1 = wsp_date1.DATE.str.split(pat = '-|T|:', expand = True)
wsp_date1.columns = ['year','month','day','hour','min','sec']

wsp1 = wsp1.join(wsp_date1)
wsp1['month'] = wsp1['month'].astype(int)
wsp1['year'] = wsp1['year'].astype(int)

wsp2 = wsp1.groupby(['year','month']).mean()

wsp1['month']

wsp3 = wsp1.groupby(['year','month'])['ws'].mean().unstack()
wsp3.plot.bar()

# I still use data of Q2

# year series of wd, wq, ws, wsq
wsp1['wsq'] = wsp1['wsq'].astype(int)

wsp1.groupby('year').mean()['wd'].plot()
wsp1.groupby('year').mean()['wq'].plot()
#no change

wsp1.groupby('year').mean()['ws'].plot()

wsp1.groupby('year').mean()['wsq'].plot()
#no change

wsp1['day'] = wsp1['day'].astype(int)

# year series of wd, ws

wsp1.groupby('month').mean()['wd'].plot()
wsp1.groupby('month').mean()['ws'].plot()


wsp1.month
# scatter plot & relaionship
plt.figure(figsize = (6,6)) 
plt.scatter(wsp1.month, wsp1.wd,color="blue")
plt.scatter(wsp1.month, wsp1.ws,color="blue")

wsp_wnd1['wq'] = wsp_wnd1['wq'].astype(int)
wsp_wnd1['wd'] = wsp_wnd1['wd'].astype(int)
wsp_wnd1['ws'] = wsp_wnd1['ws'].astype(int)
wsp_wnd1['wsq'] = wsp_wnd1['wsq'].astype(int)

plt.scatter(wsp_wnd1.wq, wsp_wnd1.wd,color="blue")

wsp_wnd2 = wsp_wnd1[(wsp_wnd1['ws'] < 9999)]

plt.scatter(wsp_wnd2.wsq, wsp_wnd2.ws,color="blue")

plt.scatter(wsp_wnd1.wd, wsp_wnd1.ws,color="blue")

plt.scatter(wsp_wnd2.wd, wsp_wnd2.ws,color="blue")
