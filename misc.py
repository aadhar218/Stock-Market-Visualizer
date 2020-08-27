import time
import matplotlib.pyplot as plt
import numpy as np
import datetime
import requests
import json
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
fig = plt.figure()
ax1 = plt.subplot(1,1,1)
ax1.plot(date[1:50],openv[1:50])
ax1.plot(date[1:50],high[1:50])
ax1.plot(date[1:50],low[1:50])
ax1.plot(date[1:50],close[1:50])
plt.show()