"""
This module contains a class for downloading & savingstock price data from the AlphaVantage API.
"""

from typing import List
import datetime
import random
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
        self.data = self.download_stock_price_data()


    def download_stock_price_data(self) -> dict:
        """
        Retrieves stock price data from the AlphaVantage API. Note: this retrieves the
        unadjusted prices (because the adjusted prices require a premium account). The format
        of the returned data is as follows:
        {
            "symbol1": {<API response for symbol1 as a dictionary>},
            "symbol2": {<API response for symbol2 as a dictionary>},
            ...
        }

        Returns:
            dict: A dictionary containing the stock price API responses
        """
        url = 'https://www.alphavantage.co/query'

        filename = 'stock_data.json'
    
        if os.path.exists(filename):
            logger.info('Loading stock price data from file')
            with open(filename, 'r') as f:
                data = json.load(f)
            return data

        logger.info('Downloading stock price data')

        number_of_symbols = 24 #The free API is limited to 25 calls per day (and 1 was used to 
                               #get the list of symbols)

        api_key = os.getenv('ALPHAVANTAGE_API_KEY')
     
        all_symbols = self.get_list_of_symbols(url, api_key)

        all_symbols = random.sample(all_symbols, number_of_symbols)

        params =  {'function': 'TIME_SERIES_DAILY',
                'outputsize': 'full',
                'apikey': api_key,
                }

        results = {}
        for symbol in all_symbols:
            logger.info(f'Getting data for {symbol}')
            
            params['symbol'] = symbol
            response = requests.get(url, params=params)

            data = response.json()        

            results[symbol] = data

        with open(filename, 'w') as f:
            json.dump(results, f, indent=4)
            
        return results


    def get_list_of_symbols(self, url: str, api_key: str) -> List[str]:
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

    def get_stock_price_data(self) -> dict:
        return self.data

if __name__ == '__main__':
    d = StockData()
    df = d.get_stock_price_changes()
    print(df.head())