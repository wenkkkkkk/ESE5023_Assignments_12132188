# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:42:58 2021

@author: Administrator
"""

import pandas as pd

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
