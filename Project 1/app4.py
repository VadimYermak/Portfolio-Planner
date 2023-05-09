import os
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import  alpaca_trade_api as tradeapi
import fire
import questionary
from MCForecastTools import MCSimulation

load_dotenv("api.env")

alpaca_api_key = os.getenv("key")
alpaca_secret_key = os.getenv("secret")

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

def research(ticker):
    
    timeframe = "1Day"
    start_date = pd.Timestamp("2010-01-01", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2023-05-03", tz="America/New_York").isoformat()
    
    df = alpaca.get_bars(
    ticker,
    timeframe,
    start=start_date,
    end=end_date
    ).df
    
    daily_returns = df['close'].pct_change().dropna()
    aar = daily_returns.mean() * 1260
    asd = daily_returns.std() * np.sqrt(1260)
    sr = aar / asd
    
    print(f"Sharpe ratio for {ticker} is {sr : .02f}, Annualized Average Return is {aar : .02f}, Annualized Standard Deviation is {asd : .02f}.")

def run():
       
    cruddy_cli_running = True
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
            "Welcome to our application! What do you want to do?",
            choices=["Count Sharpe Ratio", "Run Monte Carlo Simulation", "Quit"]
        ).ask()
        
        if choice == "Count Sharpe Ratio":
            choice = questionary.select(
                "What stocks do you want to review?", 
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
                research(stocks[choice])
            else:
                cruddy_cli_running = False
                print("Thank you for using the CRUDdy CLI! Goodbye!")

if __name__ == "__main__":
    fire.Fire(run)
                
        
         # else choice == "Quit":
        #     cruddy_cli_running = False
        #     print("Thank you for using the CRUDdy CLI! Goodbye!")

if __name__ == "__main__":
    fire.Fire(run)