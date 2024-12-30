

from typing import List
import datetime
import os
import csv
import requests
import json
import pandas as pd
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class StockData:
    def __init__(self):
        self.data = data


def get_stock_price_data():
    """
    Retrieves stock price data from the AlphaVantage API. Note: this retrieves the
    unadjusted prices (because the adjusted prices require a premium account).

    A month ago is 30 days, and a year ago is 365 days.
    Returns:
        pd.DataFrame: A DataFrame containing the stock prices
    """
    url = 'https://www.alphavantage.co/query'

    api_key = os.getenv('ALPHAVANTAGE_API_KEY')
    all_symbols = get_list_of_symbols(url, api_key)



#    all_symbols = all_symbols[:1]
    all_symbols = ['AAPL']


    params =  {'function': 'TIME_SERIES_DAILY',
               'outputsize': 'full',
               'apikey': api_key,
               }

        for symbol in all_symbols:
        logger.info(f'Getting data for {symbol}')
        
        params['symbol'] = symbol
        #response = requests.get(url, params=params)


        response = """{
    "Meta Data": {
        "1. Information": "Daily Prices (open, high, low, close) and Volumes",
        "2. Symbol": "IBM",
        "3. Last Refreshed": "2024-12-27",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2024-12-27": {
            "1. open": "223.1400",
            "2. high": "224.4200",
            "3. low": "221.4054",
            "4. close": "222.7800",
            "5. volume": "1810760"
        },
        "2024-12-26": {
            "1. open": "223.3100",
            "2. high": "225.4000",
            "3. low": "222.5500",
            "4. close": "224.8900",
            "5. volume": "3287238"
        },
        "2024-12-24": {
            "1. open": "222.2700",
            "2. high": "224.4446",
            "3. low": "221.5428",
            "4. close": "224.4100",
            "5. volume": "1186216"
        },
        "2024-12-23": {
            "1. open": "222.8100",
            "2. high": "223.7400",
            "3. low": "221.0800",
            "4. close": "221.9300",
            "5. volume": "2988137"
        },
        "2024-12-20": {
            "1. open": "222.7300",
            "2. high": "227.6847",
            "3. low": "221.6800",
            "4. close": "223.3600",
            "5. volume": "12423200"
        },
        "2024-12-19": {
            "1. open": "224.4200",
            "2. high": "226.2000",
            "3. low": "222.9800",
            "4. close": "223.9200",
            "5. volume": "4430120"
        },
        "2024-12-18": {
            "1. open": "229.0350",
            "2. high": "229.0350",
            "3. low": "220.0300",
            "4. close": "220.1700",
            "5. volume": "4152517"
        },
        "2024-12-17": {
            "1. open": "229.2300",
            "2. high": "230.2000",
            "3. low": "227.6200",
            "4. close": "228.9700",
            "5. volume": "3651346"
        },
        "2024-12-16": {
            "1. open": "230.7300",
            "2. high": "231.0300",
            "3. low": "226.8800",
            "4. close": "229.3300",
            "5. volume": "3610257"
        },
        "2024-12-13": {
            "1. open": "232.2500",
            "2. high": "233.7750",
            "3. low": "230.2600",
            "4. close": "230.8200",
            "5. volume": "2757683"
        },
        "2024-12-12": {
            "1. open": "230.6600",
            "2. high": "233.8900",
            "3. low": "230.3800",
            "4. close": "232.2600",
            "5. volume": "4515741"
        },
        "2024-12-11": {
            "1. open": "232.6900",
            "2. high": "233.0000",
            "3. low": "229.1300",
            "4. close": "230.1200",
            "5. volume": "3872680"
        },
        "2024-12-10": {
            "1. open": "228.4000",
            "2. high": "234.3900",
            "3. low": "227.8000",
            "4. close": "231.7200",
            "5. volume": "4769531"
        },
        "2024-12-09": {
            "1. open": "238.0000",
            "2. high": "239.3500",
            "3. low": "228.9100",
            "4. close": "230.0000",
            "5. volume": "4970449"
        },
        "2024-12-06": {
            "1. open": "234.4300",
            "2. high": "238.3800",
            "3. low": "234.2200",
            "4. close": "238.0400",
            "5. volume": "4028430"
        },
        "2024-12-05": {
            "1. open": "233.5500",
            "2. high": "236.5200",
            "3. low": "233.4600",
            "4. close": "234.7500",
            "5. volume": "4791116"
        },
        "2024-12-04": {
            "1. open": "230.0000",
            "2. high": "233.7400",
            "3. low": "229.3500",
            "4. close": "233.4900",
            "5. volume": "4104195"
        },
        "2024-12-03": {
            "1. open": "227.2400",
            "2. high": "229.1100",
            "3. low": "226.6700",
            "4. close": "229.0000",
            "5. volume": "3163815"
        },
        "2024-12-02": {
            "1. open": "227.5000",
            "2. high": "228.3800",
            "3. low": "225.5100",
            "4. close": "227.3900",
            "5. volume": "2656181"
        },
        "2024-11-29": {
            "1. open": "227.7500",
            "2. high": "230.3600",
            "3. low": "227.1900",
            "4. close": "227.4100",
            "5. volume": "2640253"
        },
        "2024-11-27": {
            "1. open": "228.8300",
            "2. high": "229.1900",
            "3. low": "224.2700",
            "4. close": "226.9200",
            "5. volume": "2995121"
        },
        "2024-11-26": {
            "1. open": "226.7300",
            "2. high": "228.9800",
            "3. low": "225.5115",
            "4. close": "228.8300",
            "5. volume": "4449543"
        },
        "2024-11-25": {
            "1. open": "223.3500",
            "2. high": "226.4200",
            "3. low": "222.6500",
            "4. close": "226.1300",
            "5. volume": "7189260"
        },
        "2024-11-22": {
            "1. open": "223.3500",
            "2. high": "227.2000",
            "3. low": "220.8900",
            "4. close": "222.9700",
            "5. volume": "5320740"
        },
        "2024-11-21": {
            "1. open": "215.8100",
            "2. high": "222.6300",
            "3. low": "215.2701",
            "4. close": "222.4000",
            "5. volume": "5236434"
        },
        "2024-11-20": {
            "1. open": "211.0000",
            "2. high": "214.9600",
            "3. low": "209.7725",
            "4. close": "214.6000",
            "5. volume": "4562901"
        },
        "2024-11-19": {
            "1. open": "206.5000",
            "2. high": "210.3300",
            "3. low": "206.1900",
            "4. close": "210.2500",
            "5. volume": "2860746"
        },
        "2024-11-18": {
            "1. open": "207.0000",
            "2. high": "208.4150",
            "3. low": "205.3701",
            "4. close": "208.0900",
            "5. volume": "3406045"
        },
        "2024-11-15": {
            "1. open": "207.4600",
            "2. high": "208.4900",
            "3. low": "204.0700",
            "4. close": "204.9900",
            "5. volume": "3986460"
        },
        "2024-11-14": {
            "1. open": "210.0000",
            "2. high": "210.4999",
            "3. low": "206.3500",
            "4. close": "208.9900",
            "5. volume": "6372853"
        },
        "2024-11-13": {
            "1. open": "209.5000",
            "2. high": "211.4100",
            "3. low": "209.0701",
            "4. close": "210.9200",
            "5. volume": "3247830"
        },
        "2024-11-12": {
            "1. open": "211.9000",
            "2. high": "213.0300",
            "3. low": "209.0600",
            "4. close": "210.8600",
            "5. volume": "2818216"
        },
        "2024-11-11": {
            "1. open": "214.4000",
            "2. high": "215.4100",
            "3. low": "213.4800",
            "4. close": "213.5700",
            "5. volume": "3012987"
        },
        "2024-11-08": {
            "1. open": "214.1600",
            "2. high": "216.7000",
            "3. low": "212.7809",
            "4. close": "213.7200",
            "5. volume": "3201038"
        },
        "2024-11-07": {
            "1. open": "213.6400",
            "2. high": "214.5199",
            "3. low": "211.9300",
            "4. close": "213.6900",
            "5. volume": "3675812"
        },
        "2024-11-06": {
            "1. open": "213.4800",
            "2. high": "214.3300",
            "3. low": "210.3700",
            "4. close": "213.6000",
            "5. volume": "3934386"
        },
        "2024-11-05": {
            "1. open": "206.1700",
            "2. high": "208.1150",
            "3. low": "205.5700",
            "4. close": "207.5700",
            "5. volume": "2441535"
        },
        "2024-11-04": {
            "1. open": "207.6500",
            "2. high": "207.7000",
            "3. low": "205.8000",
            "4. close": "206.3200",
            "5. volume": "2594119"
        },
        "2024-11-01": {
            "1. open": "207.7700",
            "2. high": "209.8400",
            "3. low": "207.4100",
            "4. close": "208.2500",
            "5. volume": "3334308"
        },
        "2024-10-31": {
            "1. open": "204.1300",
            "2. high": "208.1300",
            "3. low": "203.5100",
            "4. close": "206.7200",
            "5. volume": "5925250"
        },
        "2024-10-30": {
            "1. open": "209.4800",
            "2. high": "211.1200",
            "3. low": "204.2600",
            "4. close": "204.9000",
            "5. volume": "6956624"
        },
        "2024-10-29": {
            "1. open": "211.9900",
            "2. high": "213.3400",
            "3. low": "209.8500",
            "4. close": "210.4300",
            "5. volume": "5258366"
        },
        "2024-10-28": {
            "1. open": "215.5000",
            "2. high": "216.2500",
            "3. low": "212.7000",
            "4. close": "212.9100",
            "5. volume": "4993343"
        },
        "2024-10-25": {
            "1. open": "216.8000",
            "2. high": "218.6500",
            "3. low": "214.3850",
            "4. close": "214.6700",
            "5. volume": "8482235"
        },
        "2024-10-24": {
            "1. open": "220.8000",
            "2. high": "221.3200",
            "3. low": "216.1600",
            "4. close": "218.3900",
            "5. volume": "11193440"
        },
        "2024-10-23": {
            "1. open": "230.4100",
            "2. high": "233.3400",
            "3. low": "230.2600",
            "4. close": "232.7500",
            "5. volume": "5791002"
        },
        "2024-10-22": {
            "1. open": "231.9900",
            "2. high": "232.9700",
            "3. low": "230.6700",
            "4. close": "232.2500",
            "5. volume": "3180807"
        },
        "2024-10-21": {
            "1. open": "231.2100",
            "2. high": "232.4200",
            "3. low": "230.2600",
            "4. close": "231.7500",
            "5. volume": "2733336"
        },
        "2024-10-18": {
            "1. open": "231.9200",
            "2. high": "232.6499",
            "3. low": "230.1700",
            "4. close": "232.2000",
            "5. volume": "4715688"
        },
        "2024-10-17": {
            "1. open": "232.0000",
            "2. high": "233.1450",
            "3. low": "230.6550",
            "4. close": "232.8800",
            "5. volume": "5040092"
        },
        "2024-10-16": {
            "1. open": "232.1100",
            "2. high": "233.8800",
            "3. low": "231.1200",
            "4. close": "233.6700",
            "5. volume": "2846669"
        },
        "2024-10-15": {
            "1. open": "236.4000",
            "2. high": "237.3700",
            "3. low": "232.7100",
            "4. close": "232.9600",
            "5. volume": "3350556"
        },
        "2024-10-14": {
            "1. open": "233.5700",
            "2. high": "236.1200",
            "3. low": "233.1700",
            "4. close": "235.2600",
            "5. volume": "2524389"
        },
        "2024-10-11": {
            "1. open": "233.2500",
            "2. high": "233.4400",
            "3. low": "230.4600",
            "4. close": "233.2600",
            "5. volume": "3469322"
        },
        "2024-10-10": {
            "1. open": "235.1000",
            "2. high": "235.8300",
            "3. low": "231.8100",
            "4. close": "233.0200",
            "5. volume": "3142031"
        },
        "2024-10-09": {
            "1. open": "229.2000",
            "2. high": "234.9500",
            "3. low": "228.5000",
            "4. close": "234.3000",
            "5. volume": "5083566"
        },
        "2024-10-08": {
            "1. open": "228.1100",
            "2. high": "229.3450",
            "3. low": "227.0401",
            "4. close": "228.6200",
            "5. volume": "3245342"
        },
        "2024-10-07": {
            "1. open": "225.3800",
            "2. high": "227.6700",
            "3. low": "225.0200",
            "4. close": "227.1200",
            "5. volume": "3457952"
        },
        "2024-10-04": {
            "1. open": "223.7500",
            "2. high": "226.0800",
            "3. low": "223.2700",
            "4. close": "226.0000",
            "5. volume": "3554328"
        },
        "2024-10-03": {
            "1. open": "219.5000",
            "2. high": "222.8300",
            "3. low": "219.2700",
            "4. close": "222.7200",
            "5. volume": "3788265"
        },
        "2024-10-02": {
            "1. open": "218.3100",
            "2. high": "220.2000",
            "3. low": "215.7980",
            "4. close": "219.7300",
            "5. volume": "3343399"
        },
        "2024-10-01": {
            "1. open": "220.6300",
            "2. high": "221.1000",
            "3. low": "215.9000",
            "4. close": "219.3500",
            "5. volume": "3548374"
        },
        "2024-09-30": {
            "1. open": "220.6500",
            "2. high": "221.3200",
            "3. low": "219.0200",
            "4. close": "221.0800",
            "5. volume": "3544264"
        },
        "2024-09-27": {
            "1. open": "223.0000",
            "2. high": "224.1500",
            "3. low": "220.7700",
            "4. close": "220.8400",
            "5. volume": "3830335"
        },
        "2024-09-26": {
            "1. open": "222.1100",
            "2. high": "224.0000",
            "3. low": "221.3550",
            "4. close": "223.4300",
            "5. volume": "2673210"
        },
        "2024-09-25": {
            "1. open": "221.1700",
            "2. high": "221.8500",
            "3. low": "220.1600",
            "4. close": "221.2300",
            "5. volume": "2537751"
        },
        "2024-09-24": {
            "1. open": "219.7800",
            "2. high": "221.1900",
            "3. low": "218.1600",
            "4. close": "220.9700",
            "5. volume": "3184114"
        },
        "2024-09-23": {
            "1. open": "218.0000",
            "2. high": "220.6200",
            "3. low": "217.2700",
            "4. close": "220.5000",
            "5. volume": "4074755"
        },
        "2024-09-20": {
            "1. open": "214.3300",
            "2. high": "217.8500",
            "3. low": "213.7400",
            "4. close": "217.7000",
            "5. volume": "9958980"
        },
        "2024-09-19": {
            "1. open": "218.0100",
            "2. high": "218.4800",
            "3. low": "210.3700",
            "4. close": "213.8900",
            "5. volume": "5279559"
        },
        "2024-09-18": {
            "1. open": "214.1300",
            "2. high": "216.8600",
            "3. low": "213.5900",
            "4. close": "214.9400",
            "5. volume": "3482764"
        },
        "2024-09-17": {
            "1. open": "217.2500",
            "2. high": "218.8400",
            "3. low": "213.0000",
            "4. close": "214.1300",
            "5. volume": "5635210"
        },
        "2024-09-16": {
            "1. open": "215.8800",
            "2. high": "217.9000",
            "3. low": "215.5200",
            "4. close": "217.1600",
            "5. volume": "4176257"
        },
        "2024-09-13": {
            "1. open": "212.4800",
            "2. high": "216.0900",
            "3. low": "212.1300",
            "4. close": "214.7900",
            "5. volume": "4572344"
        },
        "2024-09-12": {
            "1. open": "210.0000",
            "2. high": "212.6500",
            "3. low": "208.2650",
            "4. close": "211.6100",
            "5. volume": "4616446"
        },
        "2024-09-11": {
            "1. open": "207.7600",
            "2. high": "210.1200",
            "3. low": "203.0400",
            "4. close": "209.8900",
            "5. volume": "5554309"
        },
        "2024-09-10": {
            "1. open": "204.2000",
            "2. high": "205.8300",
            "3. low": "202.8700",
            "4. close": "205.3200",
            "5. volume": "3070644"
        },
        "2024-09-09": {
            "1. open": "201.9400",
            "2. high": "205.0500",
            "3. low": "201.4300",
            "4. close": "203.5300",
            "5. volume": "3705004"
        },
        "2024-09-06": {
            "1. open": "202.3800",
            "2. high": "204.1000",
            "3. low": "199.3350",
            "4. close": "200.7400",
            "5. volume": "3304491"
        },
        "2024-09-05": {
            "1. open": "204.0800",
            "2. high": "205.9500",
            "3. low": "200.9600",
            "4. close": "202.5900",
            "5. volume": "3229345"
        },
        "2024-09-04": {
            "1. open": "200.7600",
            "2. high": "204.3600",
            "3. low": "200.5000",
            "4. close": "204.1100",
            "5. volume": "3111332"
        },
        "2024-09-03": {
            "1. open": "201.9100",
            "2. high": "204.7200",
            "3. low": "200.2100",
            "4. close": "201.2800",
            "5. volume": "3874697"
        },
        "2024-08-30": {
            "1. open": "199.1100",
            "2. high": "202.1700",
            "3. low": "198.7300",
            "4. close": "202.1300",
            "5. volume": "4750999"
        },
        "2024-08-29": {
            "1. open": "199.3000",
            "2. high": "201.1200",
            "3. low": "198.2700",
            "4. close": "198.9000",
            "5. volume": "2989594"
        },
        "2024-08-28": {
            "1. open": "199.0000",
            "2. high": "200.0000",
            "3. low": "197.4900",
            "4. close": "198.4600",
            "5. volume": "2645244"
        },
        "2024-08-27": {
            "1. open": "197.4400",
            "2. high": "199.4000",
            "3. low": "196.9700",
            "4. close": "198.7300",
            "5. volume": "2617229"
        },
        "2024-08-26": {
            "1. open": "196.0000",
            "2. high": "198.3450",
            "3. low": "195.9000",
            "4. close": "197.9800",
            "5. volume": "2567217"
        },
        "2024-08-23": {
            "1. open": "196.7900",
            "2. high": "197.3800",
            "3. low": "194.3900",
            "4. close": "196.1000",
            "5. volume": "2321961"
        },
        "2024-08-22": {
            "1. open": "197.2500",
            "2. high": "197.9200",
            "3. low": "195.5700",
            "4. close": "195.9600",
            "5. volume": "1969496"
        },
        "2024-08-21": {
            "1. open": "195.9700",
            "2. high": "197.3300",
            "3. low": "194.1150",
            "4. close": "197.2100",
            "5. volume": "2579343"
        },
        "2024-08-20": {
            "1. open": "194.5900",
            "2. high": "196.2100",
            "3. low": "193.7500",
            "4. close": "196.0300",
            "5. volume": "1790371"
        },
        "2024-08-19": {
            "1. open": "193.8400",
            "2. high": "195.5250",
            "3. low": "193.7150",
            "4. close": "194.7300",
            "5. volume": "2361378"
        },
        "2024-08-16": {
            "1. open": "193.5800",
            "2. high": "194.3500",
            "3. low": "192.8600",
            "4. close": "193.7800",
            "5. volume": "2494472"
        },
        "2024-08-15": {
            "1. open": "193.5100",
            "2. high": "194.2500",
            "3. low": "193.2800",
            "4. close": "193.9500",
            "5. volume": "2471985"
        },
        "2024-08-14": {
            "1. open": "191.1500",
            "2. high": "193.0900",
            "3. low": "190.7300",
            "4. close": "192.3200",
            "5. volume": "1895114"
        },
        "2024-08-13": {
            "1. open": "190.2900",
            "2. high": "191.3100",
            "3. low": "189.2100",
            "4. close": "190.9900",
            "5. volume": "2178862"
        },
        "2024-08-12": {
            "1. open": "191.2500",
            "2. high": "191.5761",
            "3. low": "189.0001",
            "4. close": "189.4800",
            "5. volume": "2290421"
        },
        "2024-08-09": {
            "1. open": "191.1800",
            "2. high": "192.6300",
            "3. low": "189.0400",
            "4. close": "191.4500",
            "5. volume": "2773706"
        },
        "2024-08-08": {
            "1. open": "187.5000",
            "2. high": "192.8800",
            "3. low": "187.0000",
            "4. close": "192.6100",
            "5. volume": "3712698"
        },
        "2024-08-07": {
            "1. open": "188.0800",
            "2. high": "189.8700",
            "3. low": "186.7000",
            "4. close": "186.8000",
            "5. volume": "3801942"
        }
    }
}"""
        data = json.loads(response)
        #data = response.json()        



        today = datetime.date.fromisoformat(data['Meta Data']['3. Last Refreshed'])
                
        if 'Time Series (Daily)' in data:
            logger.info(f'Price data received')
            prices = data['Time Series (Daily)']



def get_stock_price_changes():
    """
    Retrieves stock price increases from the AlphaVantage API. Note: this retrieves the
    unadjusted prices (because the adjusted prices require a premium account).

    A month ago is 30 days, and a year ago is 365 days.
    Returns:
        pd.DataFrame: A DataFrame containing the stock prices
    """
    url = 'https://www.alphavantage.co/query'

    api_key = os.getenv('ALPHAVANTAGE_API_KEY')




    price_data = {
        'symbol': [],
        'date': [],
        'last_price': [],
        'day_increase': [],
        'week_increase': [],
        'month_increase': [],
        'year_increase': [],
    }
    
    today = None
    yesterday = None
    week_ago = None
    month_ago = None
    year_ago = None


            if today is None:
                today = datetime.date.fromisoformat(data['Meta Data']['3. Last Refreshed'])
                yesterday = today - datetime.timedelta(days=1)
                week_ago = today - datetime.timedelta(days=7)
                month_ago = today - datetime.timedelta(days=30)
                year_ago = today - datetime.timedelta(days=365)


            last_price = float(prices[today.isoformat()]['4. close'])
            price_data['symbol'].append(symbol)
            price_data['date'].append(today.isoformat())
            price_data['last_price'].append(last_price)
            
            for element in [
                            ('day_increase', yesterday),
                            ('week_increase', week_ago), 
                            ('month_increase', month_ago), 
                            ('year_increase', year_ago)]:
                field_name, start_date = element

                while start_date.isoformat() not in prices and start_date.year > 2020:
                    start_date -= datetime.timedelta(days=1)


                if start_date.isoformat() not in prices:
                    logger.info(f'No data for {field_name} for {symbol}')
                    price_data[field_name].append(None)
                    continue

                then_price = float(prices[start_date.isoformat()]['4. close'])

                logger.info(f'Date for {field_name} is {start_date.isoformat()} and price is {then_price}')
                price_data[field_name].append((last_price - then_price) / then_price * 100)
    
            
    return pd.DataFrame(price_data)


def get_list_of_symbols(url: str, api_key: str) -> List[str]:
    """
    Retrieves a list of currently listed US stock symbols

    Args:
        url: (str) The url of the API from which to get the list of symbols
        api_key: (str) The API key to use for authentication

    Returns:
        List[str]: The list of stock symbols

    """
    symbol_index = 0

    params =  {'function': 'LISTING_STATUS',
               'apikey': api_key}

    all_symbols = []

    with requests.Session() as s:
        download = s.get(url, params=params)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        for row in my_list:
            all_symbols.append(row[symbol_index])

    return all_symbols[1:]

if __name__ == '__main__':
    d = get_stock_price_changes()
    print(d.head())