
import requests
import pandas as pd
from pandas.io.json import json_normalize
import json
import matplotlib.pyplot as plt
import pandas as pd
stock_symbols = [
    'PCRFY',
    'AMZN',
    'YUM',
    'PEP',
    'BGS',
    'DELL',
    'ELED',
    'SOUND',
    'SPOT',
    'WMT',
    'HUBS',
    'INTC'
]

url = "https://alpha-vantage.p.rapidapi.com/query"

querystring = {"interval":"5min","function":"TIME_SERIES_INTRADAY","symbol":"MSFT","datatype":"json","output_size":"compact"}

headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())
