import pandas as pd
import requests
import warnings
import random
import time
warnings.filterwarnings(action='ignore')

coin_name = 'KRW-XRP' # Trading Pair
start_time = '2022-02-03T00:00:00' # Today
base_url = 'https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.{}&count=400&to={}.000Z'

cols = ['timestamp', 'openingPrice', 'highPrice', 'lowPrice', 'tradePrice', 'candleAccTradeVolume']
df_out = pd.DataFrame() # Empty DataFrame

for i in range(0,10):
    url = base_url.format(coin_name, start_time)
    webpage = requests.get(url)
    # print(type(webpage))
    # print(webpage.content)

    df_temp = pd.read_json(webpage.content)
    # print(df_temp)
    # print(df_temp.shape)

    df_temp_data = df_temp[cols]
    # print(df_temp_data.head(5))

    df_out = df_out.append(df_temp_data) # Add Data To DataFrame

    # To collect data recursively, get last data of count (400) 
    temp_date = df_temp_data.tail(1)['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')
    start_time = temp_date.values[0]
    
    # Add waiting to avoid server blocking
    wait_time = random.choice([1.2, 1.4, 1.6, 1.8])
    time.sleep(wait_time)
    print(i, end=', ')

df_out.reset_index() #reset index after collect all data
df_out.to_csv("./data/{}.csv".format(coin_name), index=False)