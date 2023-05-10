import os
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import  alpaca_trade_api as tradeapi
import fire
import questionary
import json
from MCForecastTools import MCSimulation


path = "env"
load_dotenv(path, verbose = True)
alpaca_api_key = os.getenv("key")
alpaca_secret_key = os.getenv("secret")

alpaca = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version = "v2")

stocks = {
    "Apple Inc" : "AAPL",
    "Amazon.com Inc" : "AMZN",
    "Tesla Inc" : "TSLA",
    "Johnson & Johnson" : "JNJ",
    "Pfizer Inc" : "PFE",
    "Morgan Stanley" : "MS",
    "Coinbase Gllobal Inc" : "COIN",
    "Visa Inc" : "V",
    "American Express Company" : "AXP",
    "Paypal Holding Inc" : "PYPL",
    "General Electric Company" : "GE",
    "Delta Air Lines Inc" : "DAL",
    "Exxon Mobil Corp" : "XOM"
}

# Global Variables
user_name = ""
favorited_stocks = []

# User intro functionality
def user_intro():
    print("\nWelcome to your portfolio planner.\n")
    print("Here our goal is to help you search, learn, and choose stock that will diversify your future.\n")
    print("Please follow the prompts and answer our very important questions. Your answers will help us get all the important portfolio data you will need to for making promising financial investment choices.\n")

    name = questionary.text("What name should we call you by?").ask()
    user_name = name

    print(f"\nHello {user_name}! Welcome to your portfolio planner!\n")
    

# Sharpe ratio functionality
def get_sharpe_ratio(ticker):
    
    # Api dat information inputs
    timeframe = "1Day"
    start_date = pd.Timestamp("2010-01-01", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2023-05-03", tz="America/New_York").isoformat()
    
    # Api data to dataframe
    df = alpaca.get_bars(
    ticker,
    timeframe,
    start=start_date,
    end=end_date
    ).df
    
    # Data return computations
    daily_returns = df['close'].pct_change().dropna()
    annual_average_return = daily_returns.mean() * 1260
    annual_standard_deviation = daily_returns.std() * np.sqrt(1260)
    sharpe_ratio = annual_average_return / annual_standard_deviation
    
    print(f"Sharpe ratio for {ticker} is {sharpe_ratio : .02f}")
    print(f"Annualized Average Return is {annual_average_return : .02f}")
    print(f"Annualized Standard Deviation is {annual_standard_deviation : .02f}.")
    
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
def mc_sim(df_portfolio, weight1, weight2, investment_years, initial_investment):

    MC_simulation = MCSimulation(
        portfolio_data = df_portfolio,
        weights = [weight1, weight2],
        num_simulation = 100,
        num_trading_days = 252 * investment_years
    )

    MC_summary_statistics = MC_simulation.summarize_cumulative_return()
    
    ci_95_lower_cumulative_return = MC_summary_statistics[8] * initial_investment
    ci_95_upper_cumulative_return = MC_summary_statistics[9] * initial_investment
    
    return print(MC_summary_statistics, 
                 f"The lowest value of your portfolio is {ci_95_lower_cumulative_return: .02f}.", 
                 f"The highest value of your portfolio is {ci_95_upper_cumulative_return: .02f}.", 
                 )
    
    
# Application run functionality    
def run():
    if user_name == "":
        user_intro()
    
    cruddy_cli_running = True
    
    # Dictionary with provided stock names and ticker symbols
    stocks = {
        "Apple Inc" : "AAPL",
        "Amazon.com Inc" : "AMZN",
        "Tesla Inc" : "TSLA",
        "Johnson & Johnson" : "JNJ",
        "Pfizer Inc" : "PFE",
        "Morgan Stanley" : "MS",
        "Coinbase Gllobal Inc" : "COIN",
        "Visa Inc" : "V",
        "American Express Company" : "AXP",
        "Paypal Holding Inc" : "PYPL",
        "General Electric Company" : "GE",
        "Delta Air Lines Inc" : "DAL",
        "Exxon Mobil Corp" : "XOM"
    }

    while cruddy_cli_running:
        choice = questionary.select(
            "Where would you like to continue?",
            choices=["Research Stocks", "Run Monte Carlo Simulation", "Favorites List", "Quit"]
        ).ask()
        
        if choice == "Research Stocks":
            print("\nHere you can choose a stock to research\n")
            print("If you are satisfied with the data you can add it to your favorites or move on to the next module\n")
            
            continue_answer = questionary.select("Shall we continue?\n", choices = ["Yes", "No"]).ask()
            if continue_answer == "No":
                cruddy_cli_running = False
                print("\nThank you for using the CRUDdy CLI! Goodbye!")
                                                 
            choice = questionary.select(
                f"{user_name} what stocks would you like to review?", 
                choices = [ 
                    "Apple Inc",
                    "Amazon.com Inc",
                    "Tesla Inc",
                    "Johnson & Johnson",
                    "Pfizer Inc",
                    "Morgan Stanley",
                    "Coinbase Gllobal Inc",
                    "Visa Inc",
                    "American Express Company",
                    "Paypal Holding Inc",
                    "General Electric Company",
                    "Delta Air Lines Inc",
                    "Exxon Mobil Corp",
                    "QUIT - not stock :("
                ]).ask()
        
            if choice != "QUIT - not stock :(":
                get_sharpe_ratio(stocks[choice])
                favorite_stock = questionary.select("\nWould you like to add to favorites?\n", choices = ["Yes", "No"]).ask()
                
                # Add stock to favorites list
                if favorite_stock == "Yes":
                    if stocks[choice] not in favorited_stocks:
                        favorited_stocks.append(stocks[choice])
                    else:
                        print("stock is already in favorites\n")
                
            else:
                cruddy_cli_running = False
                print("\nThank you for using the CRUDdy CLI! Goodbye!")
                
        elif choice == "Run Monte Carlo Simulation":
            print("This module will perform a simulation of your portfolio performance. Please answer the following questions.")
    
        
            initial_investment = questionary.text("How much money (USD) are you investing in this portfolio?").ask()
            investment_years = questionary.text("How many years will you be investing?").ask()
            stock1 = stocks[questionary.select("Select a stock for your portfolio", choices = stocks).ask()]
            stock2 = stocks[questionary.select("Select a second stock for your portfolio", choices = stocks).ask()]
            
            portfolio_weights = questionary.select(
                f"Would you like to this to be an equally-weighted portfolio? (ie: .50 {stock1} and .50 {stock2})?",
                choices=["Yes", "No",]).ask()

            if portfolio_weights == "Yes":
                weight1 = .50
                weight2 = .50
            
            else:
                weight1 = float(questionary.text(
                    f"What percentage of the portfolio will be made up of {stock1}? Please enter the percentage in decimal format.").ask())
                confirm = questionary.select(f"The remainder of the portfolio will comprise of {1.0 - weight1 : .02}. Is this correct?", choices = ["Yes", "No"]).ask()
        
                if confirm == "Yes":
                    weight2 = 1.0 - weight1
                
                else:
                    cruddy_cli_running = False
                    print("\nThank you for using the CRUDdy CLI! Goodbye!")

            cruddy_cli_running = True

            while cruddy_cli_running:
                choice = questionary.select(
                    "Would you like to start a Monte Carlo Simulation?", 
                    choices=["Yes", "No"]).ask()
        
                if choice == "Yes":
                    mc_sim(df_portfolio(stock1, stock2), 
                           float(weight1), 
                           float(weight2), 
                           int(investment_years), 
                           int(initial_investment))
     
                else:
                    cruddy_cli_running = False
                    print("\nThank you for using the CRUDdy CLI! Goodbye!")
                    
        elif choice == "Favorites List":
            if favorited_stocks == []:
                print("Favorites list is empty\n")
            else:
                for stock in favorited_stocks:
                    print(stock)
            
        else:
            cruddy_cli_running = False
            print("\nThank you for using the CRUDdy CLI! Goodbye!")
        
                                                 
                                                 
if __name__ == "__main__":
    fire.Fire(run)