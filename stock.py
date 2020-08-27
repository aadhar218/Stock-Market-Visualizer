#!/usr/bin/env python
import pandas as pd 
import numpy as np
import datetime
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests


api_key = 'PYR50CGFSRXWXQ6J'
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo")
response1 = requests.get("https://www.alphavantage.co/query?function=SMA&symbol=MSFT&interval=weekly&time_period=10&series_type=open&apikey=demo")
json_response1 = response1.json()
json_response = response.json()
time = json_response["Time Series (5min)"]
sma = json_response1["Technical Analysis: SMA"]
date=[]
openv=[]
high=[]
low=[]
close=[]
vol=[]
ma=[]
for x in time:
    date.append(x)
    openv.append(time[x]["1. open"])
    high.append((time[x]["2. high"]))
    low.append(time[x]["3. low"])
    close.append(time[x]["4. close"])
    vol.append(time[x]["5. volume"])
for x in sma:
    ma.append(sma[x]["SMA"])


fig = make_subplots(rows=2, cols=1, 
                    shared_xaxes=True, 
                    vertical_spacing=0.02)
fig.add_trace(go.Candlestick(x=date,
                open=openv, high=high,
                low=low, close=close),row=1,col=1)
fig.add_trace(go.Bar(x=date,y=vol),row=2,col=1)

fig.add_trace(go.Scatter(x=date,y=ma),row=1,col=1)

fig.update_layout(template='plotly_dark',xaxis_rangeslider_visible=True)
fig.show()
