import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation

import fire
import questionary

path = "env"
load_dotenv(path, verbose = True)

# Create a dataframe from two stock inputs:
def df_portfolio(stock1, stock2):
    alpaca_api_key = os.getenv("key")
    alpaca_secret_key = os.getenv("secret")

    alpaca = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version = "v2")

    tickers = [stock1, stock2]
    timeframe = "1Day"
    start_date = pd.Timestamp("2010-01-01", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2023-05-03", tz="America/New_York").isoformat()

    df_portfolio = alpaca.get_bars(tickers, timeframe, start = start_date, end = end_date).df

    stock1_df = df_portfolio[df_portfolio["symbol"]== stock1].drop("symbol", axis=1)
    stock2_df = df_portfolio[df_portfolio["symbol"]== stock2].drop("symbol", axis=1)
     
    df_portfolio = pd.concat([stock1_df, stock2_df], axis=1, keys=[stock1, stock2])
    
    return df_portfolio


# Monte Carlo simulation with df_portfolio defined as a parameter
def mc_sim(df_portfolio, weight1, weight2, investment_years):

    MC_simulation = MCSimulation(
        portfolio_data = df_portfolio,
        weights = [weight1, weight2],
        num_simulation = 100,
        num_trading_days = 252 * investment_years
    )

    MC_summary_statistics = MC_simulation.summarize_cumulative_return()
    
    return MC_summary_statistics

def run():
    print("This module will perform a simulation of your portfolio performance. Please answer the following questions.")
    
        
    stock1 = input("Please enter one stock to be included in your portfolio.")
    weight1 = float(input(f"You have selected {stock1}. What is the weight?"))
    stock2 = input("Please enter a second stock to be included in your portfolio.")
    weight2 = float(input(f"You have selected {stock2}. What is the weight?"))

    cruddy_cli_running = True

    while cruddy_cli_running:
        choice = questionary.select(
            "Would you like to start a Monte Carlo Simulation?",
            choices=["Yes", "No"]
        ).ask()
        
        if choice == "Yes":
            investment_years = input("How many years would you like to invest?")
            
            mc_sim(df_portfolio(stock1, stock2), weight1, weight2, investment_years)
        
            
            
            
if __name__ == "__main__":
    fire.Fire(run)

#Parameters
# portfolio_data
# weights
# num_simulation
# num_trading_days
# initial_investment #float which serves as the current value of the portfolio


# For the weights parameter, we must list the weight of each asset in the order that the assets appear in the DataFrame in the portfolio_data parameter. The Alpaca API call that we made earlier returned a DataFrame that lists KO before MSFT. Therefore, we must list the weight of KO before the weight of MSFT.


# """Create a Financial Planner for Retirement """

# calculate the range of the probable cumulative returns for a $10,000 investment
# ci_95_lower_cumulative_return = MC_summary_statistics[8] * 10000 
# ci_95_upper_cumulative_return = MC_summary_statistics[9] * 10000

    
#     # Create a test DataFrame
#     stocks_dataframe = pd.DataFrame({'AAPL': [1, 2], 'GOOG': [3, 4]})
#     # Create the database table called 'stocks'
#     create_table(engine, 'stocks', stocks_dataframe)

#     cruddy_cli_running = True

#     while cruddy_cli_running:
#         choice = questionary.select(
#             "What do you want to do?",
#             choices=["Read", "Update", "Delete", "Quit"]
#         ).ask()

#ideas

# Choices


# 1) Statistics
# 2) 95% CI Percentile, 
# 3a) Target valuation of portfolio after given time, percent chance of meeting goal
# 3b) Portfolio optimization recommendations and percent chance of meeting goal





