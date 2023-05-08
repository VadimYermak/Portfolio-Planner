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
    
    print(f"Sharpe ratio for {ticker} is {sr : .02f}.")

def run():
    
       
    cruddy_cli_running = True

    while cruddy_cli_running:
        choice = questionary.select(
            "Welcome to our application! What do you want to do?",
            choices=["Count Sharpe Ratio", "Run Monte Carlo Simulation", "Quit"]
        ).ask()
        
        if choice == "Count Sharpe Ratio":
            choice = questionary.select(
                "What stocks do you want to review?", 
                choices = ["AAPL - Apple Inc", "AMZN - Amazon.com Inc", "TSLA - Tesla Inc", "JNJ - Johnson & Johnson", "PFE - Pfizer Inc", "MS - Morgan Stanley", "COIN - Coinbase Gllobal Inc", "V - Visa Inc", "AXP - American Express Company", "PYPL - Paypal Holding Inc", "GE - General Electric Company", "DAL - Delta Air Lines Inc", "XOM - Exxon Mobil Corp", "QUIT - not stock:)"]
                ).ask()
            
            if choice == "AAPL - Apple Inc":
                research("AAPL")
                
            elif choice == "AMZN - Amazon.com Inc":
                research("AMZN")
            
            elif choice == "TSLA - Tesla Inc":
                research("TSLA")
            
            elif choice == "JNJ - Johnson & Johnson":
                research("JNJ")
            
            elif choice == "PFE - Pfizer Inc":
                research("PFE")
            
            elif choice == "MS - Morgan Stanley":
                research("MS")
            
            elif choice == "COIN - Coinbase Gllobal Inc":
                research("COIN")
            
            elif choice == "V - Visa Inc":
                research("V")
            
            elif choice == "AXP - American Express Company":
                research("AXP")
            
            elif choice == "PYPL - Paypal Holding Inc":
                research("PYPL")
            
            elif choice == "GE - General Electric Company":
                research("GE")
            
            elif choice == "DAL - Delta Air Lines Inc":
                research("DAL")
            
            elif choice == "XOM - Exxon Mobil Corp":
                research("XOM")
                                        
            elif choice == "Quit - not stock:)":
                cruddy_cli_running = False
                print("Thank you for using the CRUDdy CLI! Goodbye!")

                
        
         # else choice == "Quit":
        #     cruddy_cli_running = False
        #     print("Thank you for using the CRUDdy CLI! Goodbye!")

if __name__ == "__main__":
    fire.Fire(run)