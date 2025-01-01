"""
This module contains a class for plotting stock prices over time.
"""

import matplotlib.pyplot as plt
import datetime
import json
import pandas as pd
from transformers import tool

class StockPriceOverTime:
    data = None
    average_df = None

    def set_data(data: dict) -> None:
        StockPriceOverTime.data = data

        StockPriceOverTime.calculate_average_price_over_time()

    def calculate_average_price_over_time() -> None:
        """
        Returns the average price over time for each symbol in StockPriceOverTime.data

        Returns:
            str: A JSON-formatted string containing the average price over time for each symbol
        """
        average_prices = {'date': [], 'price': []}
        prices = {}

        for symbol in StockPriceOverTime.data:
            data = StockPriceOverTime.data[symbol]
            data = data['Time Series (Daily)']

            for date, v in data.items():
                price = float(v['4. close']) 

                if date not in prices:
                    prices[date] = {'price': price, 'count': 1}
                else:
                    prices[date]['price'] = (prices[date]['price'] * prices[date]['count'] + price) / (prices[date]['count'] + 1)
                    prices[date]['count'] += 1

        for date, v in prices.items():
            average_prices['date'].append(datetime.date.fromisoformat(date))
            average_prices['price'].append(v['price'])

        StockPriceOverTime.average_df = pd.DataFrame(average_prices)

    @tool
    def plot_stock_prices_over_time(symbols: str) -> str:
        """
        Plots the stock prices over time for each symbol in symbols. Symbols is a JSON-formatted string
        containing a list of symbols.

        Args:
            symbols: (str) A JSON-formatted string containing a list of symbols
        
        Returns:
            str: "Done"
        """
        symbols = json.loads(symbols)

        for symbol in symbols:
            plot_data = StockPriceOverTime.data[symbol]['Time Series (Daily)']
            x = []
            y = []

            for k, v in plot_data.items():
                x.append(datetime.date.fromisoformat(k))
                y.append(float(v['4. close']))

            plt.plot(x, y, label=symbol)

        plt.plot(StockPriceOverTime.average_df['date'], StockPriceOverTime.average_df['price'], label='Average')
        plt.legend()
        
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(f'Stock price over time for {symbol}')


        plt.show()

        return "Done"