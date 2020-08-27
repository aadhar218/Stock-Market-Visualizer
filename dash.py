import requests
import json
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd 
from datetime  import datetime
fig = go.Figure()
date =[]
openv =[]
close =[]
high =[]
low =[]
vol=[]
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey=demo")
json_response = response.json()
time = json_response["Weekly Adjusted Time Series"]
print(time["2020-08-07"])
for x in time:
    date.append(x)
    openv.append(time[x]["1. open"])
    high.append(time[x]["2. high"])
    low.append(time[x]["3. low"])
    close.append(time[x]["4. close"])
    vol.append(time[x]["6. volume"])
fig.add_trace(go.Candlestick(x=date,open=openv,high=high,low=low,close=close))
fig.add_trace(go.Bar(x=date,y=vol))
fig.show()