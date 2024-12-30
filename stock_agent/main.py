

import logging
import price_change
import stock_data


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    data = stock_data.StockData()
    price_change.PriceChange.set_price_df(data.get_stock_price_data())
    
    results = price_change.PriceChange.get_top_changes('day_increase', 5)
    price_change.PriceChange.plot_already_computed_price_changes(results)


if __name__ == '__main__':
    main()