

from transformers import tool
import json
import matplotlib.pyplot as plt


class PriceChange:
    price_df = None

    def set_price_df(price_df: pd.DataFrame):
        """
        Sets the price_df attribute to the given DataFrame

        Args:
            price_df: (pd.DataFrame) The DataFrame to set the price_df attribute to
        """
        PriceChange.price_df = price_df

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
            return 'day_chaane'
        elif 'week' == frequency.to_lower():
            return 'week_change'
        elif 'month' == frequency.to_lower():
            return 'month_change'
        elif 'year' == frequency.to_lower():
            return 'year_change'

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

        plt.show()

        return "Done"
