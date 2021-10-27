# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 11:44:33 2021

@author: Administrator
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Sig_eqs = pd.read_csv(r"E:\zwk\earthquakes-2021-10-27_10-51-53_+0800.tsv", sep = '\t')

Sig_eqs['Deaths'].sum()

death_country = Sig_eqs.groupby('Country').sum().sort_values('Deaths', ascending = False)['Deaths']

death_country.head(10)

Sig_eqs[(Sig_eqs['Mag'] > 6.0)]['Mag'].count()

eqs_year = Sig_eqs[(Sig_eqs['Mag'] > 6.0)].groupby('Year').count()['Mag']

fig = plt.figure()

eqs_year['Mag'].plot()

eqs_year.index()

eqs_year = Sig_eqs[(Sig_eqs['Mag'] > 6.0)].groupby('Year','Mag')

a = eqs_year.groupby('Year')['Mag'].count()

a.plot('Year','Mag')

b = a.to_frame()
fig = b['Mag'].plot()

countryeqs = Sig_eqs['Country','Mag','Year',]

c = Sig_eqs.groupby('Country').count()['Mag']
c.index == 'CHINA'
c.values
dict_c = {'country':c.index, 'num_eqs':c.values}
df_c = pd.DataFrame(dict_c)

f = df_c[(df_c['country'] == 'CHINA')]['num_eqs']
print(f)

df_c.loc[0]
df_c

print(c['CHINA'])

g = input('a')
print(c[g])

df_c.iloc[0]
#d = Sig_eqs.groupby('Country').sum()['Mag']

def CountEq_LargestEq(country):
    c = Sig_eqs.groupby('Country').count()['Mag']
    print('the total number of earthquake is:')
    print(c[country])























