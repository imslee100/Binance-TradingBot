from gettext import npgettext
import pandas as pd
import requests
import warnings
warnings.filterwarnings(action='ignore')

coin_name = 'KRW-XRP' # Trading Pair
start_time = '2022-02-03T00:00:00' # Today
base_url = 'https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.{}&count=400&to={}.000Z'

cols = ['timestamp', 'openingPrice', 'highPrice', 'lowPrice', 'tradePrice', 'candleAccTradeVolume']
df_out = pd.DataFrame() # Empty DataFrame

for i in range(0,1):
    url = base_url.format(coin_name, start_time)
    webpage = requests.get(url)
    print(type(webpage))
    print(webpage.content)
