#######################
###FED FUNDS FUTURES###
#######################

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
from plotly.offline import plot
import yfinance as yf
from datetime import datetime
from fredapi import Fred
from plotly.subplots import make_subplots
import random


fred = Fred(api_key='369d1c7da6774fdc9c576d8f41178f8f')

def now_utc():
    now = datetime.utcnow()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    return now + str(" UTC")

def date():
    now = datetime.utcnow()
    now = now.strftime("%Y-%m-%d")
    return now

def rand_hex():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())


# oct22 = yf.download('ZQV22.CBT',progress=False)['Adj Close'];
nov22 = yf.download('ZQX22.CBT',progress=False)['Adj Close'];
dec22 = yf.download('ZQZ22.CBT',progress=False)['Adj Close'];

####
jan23 = yf.download('ZQF23.CBT',progress=False)['Adj Close'];
feb23 = yf.download('ZQG23.CBT',progress=False)['Adj Close'];
mar23 = yf.download('ZQH23.CBT',progress=False)['Adj Close'];

apr23 = yf.download('ZQJ23.CBT',progress=False)['Adj Close'];
may23 = yf.download('ZQK23.CBT',progress=False)['Adj Close'];
jun23 = yf.download('ZQM23.CBT',progress=False)['Adj Close'];

jul23 = yf.download('ZQN23.CBT',progress=False)['Adj Close'];
aug23 = yf.download('ZQQ23.CBT',progress=False)['Adj Close'];
sep23 = yf.download('ZQU23.CBT',progress=False)['Adj Close'];

oct23 = yf.download('ZQV23.CBT',progress=False)['Adj Close'];
nov23 = yf.download('ZQX23.CBT',progress=False)['Adj Close'];
dec23 = yf.download('ZQZ23.CBT',progress=False)['Adj Close'];

###
jan24 = yf.download('ZQF24.CBT',progress=False)['Adj Close'];
feb24 = yf.download('ZQG24.CBT',progress=False)['Adj Close'];
mar24 = yf.download('ZQH24.CBT',progress=False)['Adj Close'];

apr24 = yf.download('ZQJ24.CBT',progress=False)['Adj Close'];
may24 = yf.download('ZQK24.CBT',progress=False)['Adj Close'];
# jun24 = yf.download('ZQM24.CBT',progress=False)['Adj Close'];
#
# jul24 = yf.download('ZQN24.CBT',progress=False)['Adj Close'];
# aug24 = yf.download('ZQQ24.CBT',progress=False)['Adj Close'];
# sep24 = yf.download('ZQU24.CBT',progress=False)['Adj Close'];
#
# oct24 = yf.download('ZQV24.CBT',progress=False)['Adj Close'];
# nov24 = yf.download('ZQX24.CBT',progress=False)['Adj Close'];
dec24 = yf.download('ZQZ24.CBT',progress=False)['Adj Close'];


# #23
# jan23 = yf.download('ZQF23.CBT')['Adj Close'];
# feb23 = yf.download('ZQG23.CBT')['Adj Close'];
# mar23 = yf.download('ZQH23.CBT')['Adj Close'];
# apr23 = yf.download('ZQJ23.CBT')['Adj Close'];
# may23 = yf.download('ZQK23.CBT')['Adj Close'];
# june23 = yf.download('ZQM23.CBT')['Adj Close'];
# july23 = yf.download('ZQN23.CBT')['Adj Close'];
# aug23 = yf.download('ZQQ23.CBT')['Adj Close'];
# sep23 = yf.download('ZQU23.CBT')['Adj Close'];
# oct23 = yf.download('ZQV23.CBT')['Adj Close'];
# nov23 = yf.download('ZQX23.CBT')['Adj Close'];
# dec23 = yf.download('ZQZ23.CBT')['Adj Close'];
# #24
# jan24 = yf.download('ZQF24.CBT')['Adj Close'];
# #25
# jan25 = yf.download('ZQF25.CBT')['Adj Close'];

#RRP RATE
rrp = fred.get_series('RRPONTSYAWARD')

#IOER
ioer = fred.get_series('IORB')

#IOER_Discounted
ioer_disc = fred.get_series('IOER')
ioer_full = ioer_disc.append(ioer)

#Effective Fed Funds
eff = fred.get_series('DFF')
eff_hist = fred.get_series('FEDFUNDS')

#S&P 500
sp = fred.get_series('SP500')

#Discount Window Rate
dwr = fred.get_series('DPCREDIT')

#Total Bank Credit
tbc = fred.get_series('TOTBKCR', units = 'pc1')

#SOFR rate
sofr = fred.get_series('SOFR')
sofr = sofr.fillna(method = 'pad')

#FOMC Summary Median Projection
dot = fred.get_series('FEDTARMD')
dot

rollback = 10 #years

rrp = rrp.tail(365*rollback)
rrp = rrp.fillna(method='ffill');

ioer_full = ioer_full.tail(365*rollback)
ioer_full = ioer_full.fillna(method='ffill');

eff = eff.tail(365*rollback)

sp = sp.tail(365*rollback)

dwr = dwr.tail(365*rollback)

tbc = tbc.tail(365*rollback)

sofr = sofr.tail(365*rollback)

dot = dot.tail(3)


# oct22_adj = 100-oct22
nov22_adj = 100-nov22
dec22_adj = 100-dec22

jan23_adj = 100-jan23
feb23_adj = 100-feb23
mar23_adj = 100-mar23

apr23_adj = 100-apr23
may23_adj = 100-may23
jun23_adj = 100-jun23

jul23_adj = 100-jul23
aug23_adj = 100-aug23
sep23_adj = 100-sep23

oct23_adj = 100-oct23
nov23_adj = 100-nov23
dec23_adj = 100-dec23

jan24_adj = 100-jan24
feb24_adj = 100-feb24
mar24_adj = 100-mar24

apr24_adj = 100-apr24
may24_adj = 100-may24
# jun24_adj = 100-jun24
#
# jul24_adj = 100-jul24
# aug24_adj = 100-aug24
# sep24_adj = 100-sep24
#
# oct24_adj = 100-oct24
# nov24_adj = 100-nov24
dec24_adj = 100-dec24



fedfunds_plot = px.line()
fedfunds_plot.add_trace(go.Scatter(x = rrp.index, y = rrp.values, name = 'O/N RRP', opacity=1, line = dict(color='#075E45', width=2, dash='dash')));
fedfunds_plot.add_trace(go.Scatter(x = ioer_full.index, y = ioer_full.values, name = 'IOER',opacity=1, line = dict(color='#75160C', width=2, dash='dash')));
fedfunds_plot.add_trace(go.Scatter(x = eff.index, y = eff.values, name = 'EFFR', line = dict(color='white', width=3)));
fedfunds_plot.add_trace(go.Scatter(x = sofr.index, y = sofr.values, name = 'SOFR', line = dict(color='darkgreen', width=2),opacity = .5));

# fedfunds_plot.add_trace(go.Scatter(x = dwr.index, y = dwr.values, name = 'DWR', line = dict(color='#23254D', width=1, dash='dash')));

#command out if all auto
# fedfunds_plot.add_trace(go.Scatter(x = mar22_adj.index, y = mar22_adj.values, name = 'MAR 22', line = dict(color='#279C9C', width=2),opacity = .8));

# fedfunds_plot.add_trace(go.Scatter(x = apr22_adj.index, y = apr22_adj.values, name = 'APR 22', line = dict(color='#D9A514', width=2),opacity = .8));
# fedfunds_plot.add_trace(go.Scatter(x = may22_adj.index, y = may22_adj.values, name = 'MAY 22', line = dict(color='#AC71F0', width=2),opacity = .8));
# fedfunds_plot.add_trace(go.Scatter(x = jun22_adj.index, y = jun22_adj.values, name = 'JUN 22', line = dict(color='#23254D', width=2),opacity = .8));

# fedfunds_plot.add_trace(go.Scatter(x = jul22_adj.index, y = jul22_adj.values, name = 'JUL 22', line = dict(color='#52A31D', width=2),opacity = .8));
# fedfunds_plot.add_trace(go.Scatter(x = aug22_adj.index, y = aug22_adj.values, name = 'AUG 22', line = dict(color='#CC1D92', width=2),opacity = .8));
# fedfunds_plot.add_trace(go.Scatter(x = sep22_adj.index, y = sep22_adj.values, name = 'SEP 22', line = dict(color='#48B8F0', width=2),opacity = .8));

# fedfunds_plot.add_trace(go.Scatter(x = oct22_adj.index, y = oct22_adj.values, name = 'OCT 22', line = dict(color='#077D55', width=2),opacity = .8));
fedfunds_plot.add_trace(go.Scatter(x = nov22_adj.index, y = nov22_adj.values, name = 'NOV 22', line = dict(color='#75160C', width=2),opacity = .8));
fedfunds_plot.add_trace(go.Scatter(x = dec22_adj.index, y = dec22_adj.values, name = 'DEC 22', line = dict(color='#279C9C', width=2),opacity = .8));

fedfunds_plot.add_trace(go.Scatter(x = dec23_adj.index, y = dec23_adj.values, name = 'DEC 23', line = dict(color='white', width=2),opacity = .3));
fedfunds_plot.add_trace(go.Scatter(x = dec24_adj.index, y = dec24_adj.values, name = 'DEC 24', line = dict(color='white', width=2),opacity = .2));


fedfunds_plot.update_layout(template='plotly_dark');
fedfunds_plot.update_layout(font_color="white")

fedfunds_plot.update_layout(height=600,width=1000,font=dict(family="Roboto Mono",size=11));
fedfunds_plot.update_layout(title =f"Fed Funds Futures Implied Hikes   (Updated: {now_utc()})",title_y=0.95,title_x=0.08);

fedfunds_plot.update_xaxes(showline=True, linewidth=1, linecolor='white', mirror=True,ticks='outside');
fedfunds_plot.update_yaxes(showline=True, linewidth=1, linecolor='white', mirror=True,ticks='outside');

fedfunds_plot.update_layout(scene = dict(
                    xaxis_title='Year',
                    yaxis_title='Rate'));

fedfunds_plot.show()


curve_december_22 = {'2023-1-3': dec22_adj.values[-1]}
curve_december_22 = pd.Series(data=curve_december_22)

curve_december_23 = {'2024-1-2': dec23_adj.values[-1]}
curve_december_23 = pd.Series(data=curve_december_23)

curve_december_24 = {'2025-1-2': dec24_adj.values[-1]}
curve_december_24 = pd.Series(data=curve_december_24)

# {'2024-02-01': jan24_adj.values[-1], '2024-03-01': feb24_adj.values[-1], '2024-04-01': mar24_adj.values[-1], '2024-05-01': apr24_adj.values[-1], '2024-06-01': may24_adj.values[-1], '2024-07-01': jun24_adj.values[-1], '2024-08-01': jul24_adj.values[-1], '2024-09-01': aug24_adj.values[-1], '2024-10-01': sep24_adj.values[-1], '2024-11-01': oct24_adj.values[-1], '2024-12-01': nov24_adj.values[-1],

forward = {
date():nov22_adj.values[-1],'2022-12-13':nov22_adj.values[-1],
'2022-12-14':dec22_adj.values[-1],'2023-1-26': dec22_adj.values[-1],
'2023-01-27': jan23_adj.values[-1], '2023-03-16': jan23_adj.values[-1],
'2023-03-17': mar23_adj.values[-1], '2023-04-27': mar23_adj.values[-1],
'2023-04-28': apr23_adj.values[-1],'2023-06-15': apr23_adj.values[-1],
'2023-06-16': jun23_adj.values[-1],'2023-07-27': jun23_adj.values[-1],
'2023-07-28': jul23_adj.values[-1],'2023-09-21': jul23_adj.values[-1],
'2023-09-22': sep23_adj.values[-1], '2023-11-02': sep23_adj.values[-1],
'2023-11-03': nov23_adj.values[-1],'2024-1-15': nov23_adj.values[-1],
'2024-1-16': dec23_adj.values[-1]}

def frwrd(time):
    forward = {
    '2022-11-2':nov22_adj.values[time],'2022-12-13':nov22_adj.values[time],
    '2022-12-14':dec22_adj.values[time],'2023-1-26': dec22_adj.values[time],
    '2023-01-27': jan23_adj.values[time], '2023-03-16': jan23_adj.values[time],
    '2023-03-17': mar23_adj.values[time], '2023-04-27': mar23_adj.values[time],
    '2023-04-28': apr23_adj.values[time],'2023-06-15': apr23_adj.values[time],
    '2023-06-16': jun23_adj.values[time],'2023-07-27': jun23_adj.values[time],
    '2023-07-28': jul23_adj.values[time],'2023-09-21': jul23_adj.values[time],
    '2023-09-22': sep23_adj.values[time], '2023-11-02': sep23_adj.values[time],
    '2023-11-03': nov23_adj.values[time],'2024-1-15': nov23_adj.values[time],
    '2024-1-16': dec23_adj.values[time]
    }
    return forward

# pd.Series(data=frwrd(-2))
# datetime.strptime(date(),'%Y-%m-%d').date() - datetime.strptime(pd.Series(data=frwrd(-2)).index[1],'%Y-%m-%d').date()
#
# date()

# fedfunds_plot.add_trace(go.Scatter(x = curve_december_22.index, y = curve_december_22.values, name = 'DEC 22',marker=dict(color='#279C9C',size=5,line=dict(width=1))));
# fedfunds_plot.add_trace(go.Scatter(x = curve_december_23.index, y = curve_december_23.values, name = 'DEC 23',marker=dict(color='white',size=5,line=dict(width=1))));
# fedfunds_plot.add_trace(go.Scatter(x = curve_december_24.index, y = curve_december_24.values, name = 'DEC 24',marker=dict(color='white',size=5,line=dict(width=1))));

fedfunds_plot.add_trace(go.Scatter(x =  pd.Series(data=forward).index, y =  pd.Series(data=forward).values, name = 'Implied HK t-0', line = dict(color='red', width=2.5),opacity = .7, mode='lines'));
# fedfunds_plot.add_trace(go.Scatter(x = pd.Series(data=frwrd(-2)).index, y = pd.Series(data=frwrd(-2)).values, name = '" HK t-1', line = dict(color='white', width=2),opacity = .5, mode = 'lines'));
# fedfunds_plot.add_trace(go.Scatter(x = pd.Series(data=frwrd(-6)).index, y = pd.Series(data=frwrd(-6)).values, name = f" HK t{-6}", line = dict(color='white', width=2),opacity = .3, mode = 'lines'));
# fedfunds_plot.add_trace(go.Scatter(x = pd.Series(data=frwrd(-30)).index, y = pd.Series(data=frwrd(-30)).values, name = f" HK t{-30}", line = dict(color='white', width=2),opacity = .1, mode = 'lines'));
fedfunds_plot.add_trace(go.Scatter(x = dot.index, y = dot.values, name = 'FOMC Dots Median', line = dict(color='#ffcc00', width=2, dash = 'dash'),opacity = .7, mode = 'lines+markers',marker_symbol='cross',marker=dict(size=6, color = '#ffcc00')));


for i in range(-30,-2,5):
    plot = fedfunds_plot.add_trace(go.Scatter(x = pd.Series(data=frwrd(i)).index, y = pd.Series(data=frwrd(i)).values, name = f" HK t{i}", line = dict(color='white', width=2),opacity = (1-(-1*i/100))/3, mode = 'lines'));

plot.show()


fedfunds_plot.show()
