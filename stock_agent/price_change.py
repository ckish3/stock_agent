

from transformers import tool
import json
import matplotlib.pyplot as plt
import pandas as pd
import logging
import datetime


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class PriceChange:
    price_df = None

    def set_price_df(data: dict):
        """
        Sets the price_df attribute to the given DataFrame

        Args:
            price_df: (pd.DataFrame) The DataFrame to set the price_df attribute to
        """

        price_df = PriceChange.get_stock_price_changes(data)
        PriceChange.price_df = price_df

    def get_stock_price_changes(all_data: dict) -> pd.DataFrame:
        """
        Computes stock price increases from the price data in self.data.

        A month ago is 30 days, and a year ago is 365 days.
        Returns:
            pd.DataFrame: A DataFrame containing the stock prices
        """



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

        for symbol in all_data:

            data = all_data[symbol]
            
            if 'Time Series (Daily)' in data:
                logger.info(f'Price data received for {symbol}')
                prices = data['Time Series (Daily)']

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

        logger.info(price_data)       
        return pd.DataFrame(price_data)


    @tool
    def get_column_name(frequency: str) -> str:
        """
        Returns the column name for a given frequency ("day", "week", "month", or "year")

        Args:
            frequency: (str) The frequency to get the column name for ("day", "week", "month", or "year")

        Returns:
            str: The column name for the given frequency: "day_change", "week_change", "month_change", or "year_change"
        """
        if 'day' == frequency.to_lower():
            return 'day_increase'
        elif 'week' == frequency.to_lower():
            return 'week_increase'
        elif 'month' == frequency.to_lower():
            return 'month_increase'
        elif 'year' == frequency.to_lower():
            return 'year_increase'

    @tool
    def get_top_changes(column_name: str, number_of_results: int) -> str:
        """
        Returns a list of the top stock price changes as a JSON string with the following format:
        {
            "symbol1": change1,
            "symbol2": change2,
            "Average": average_change
        }

        Args:
            column_name: (str) The column name to sort by ("day_change", "week_change", "month_change", or "year_change")
            number_of_results: (int) The number of stocks to include in the returned JSON string

        Returns:
            str: A JSON string containing the top stock price changes
        """
        df = PriceChange.price_df.sort_values(by=column_name, ascending=False)
        top_changes = df.head(number_of_results)[['symbol', column_name]]

        result = {}

        for index, row in top_changes.iterrows():
            result[row['symbol']] = row[column_name]

        result['Average'] = PriceChange.price_df[column_name].mean()

        return json.dumps(result)

    @tool
    def plot_already_computed_price_changes(names_and_values: str) -> str:
        """
        Plots the already computed stock price changes. Note: this function assumes that the JSON string contains the
        following format:
        {
            "symbol1": change1,
            "symbol2": change2,
            "Average": average_change
        }

        Args:
            names_and_values: (str) A JSON string containing the stock symbols and price changes to plot

        Returns:
            str: "Done"
        """
        names_and_values = json.loads(names_and_values)
        names = list(names_and_values.keys())
        values = list(names_and_values.values())

        plt.bar(names, values)
        plt.ylabel('Percent Increase')
        plt.title(f'Stock price changes')

        plt.show()

        return "Done"

    
    @tool
    def plot_price_change_of_stock(symbol: str, column_name: str) -> str:
        """
        Plots the stock price change of a single stock. Given a symbol, it gets the price change of that stock and plots
        it.

        Args:
            symbol: (str) The stock symbol to plot
            column_name: (str) The column name to plot ("day_change", "week_change", "month_change", or "year_change")

        Returns:
            str: "Done"
        """
        values = {}
        symbol = symbol.upper()
    
        values[symbol] = PriceChange.price_df[PriceChange.price_df['symbol'] == symbol][column_name].values[0]
        values["Average"] = PriceChange.price_df[column_name].mean()

        plt.bar(values.keys(), values.values())
        plt.ylabel('Percent Increase')
        plt.title(f'Stock price {column_name.replace("_", " ")} of {symbol}')
        plt.show()

        return "Done"
