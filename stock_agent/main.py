
"""

This is a proof of concept for a agentic LLM system that can query and plot stock data.

Example usage:
python main.py

"""
import logging
import json
from huggingface_hub import login, InferenceClient
from transformers import ReactCodeAgent, HfApiEngine
import os


import price_change
import stock_data
import stock_price_over_time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)




def main():
    login(os.environ['HF_WRITE_TOKEN'])

    llm_engine = HfApiEngine(model="Qwen/Qwen2.5-Coder-32B-Instruct")
    agent = ReactCodeAgent(tools=[
        stock_price_over_time.StockPriceOverTime.plot_stock_prices_over_time,
                                  price_change.PriceChange.get_column_name_from_time_period,
                                  price_change.PriceChange.get_top_increases_in_column_name_time_period,
                                  price_change.PriceChange.plot_already_computed_price_changes,
                                  price_change.PriceChange.plot_price_change_of_stock
                              ], 
                            llm_engine=llm_engine, 
                            additional_authorized_imports=['matplotlib', 'json'])

    data = stock_data.StockData()
    price_change.PriceChange.set_price_df(data.get_stock_price_data())
    stock_price_over_time.StockPriceOverTime.set_data(data.get_stock_price_data())

    prompts = ["Plot the changes of the 5 stocks that increased the most in the last week",
               "Plot the price over time for the stock that increased the most in the last week",
               "Plot the changes of the 5 stocks that increased the most in the last month",
               "Plot the changes of the 5 stocks that increased the most in the last year",]

    for prompt in prompts:
        agent.run(prompt)






if __name__ == '__main__':
    main()