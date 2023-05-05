import os
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import  alpaca_trade_api as tradeapi
import fire
import questionary


load_dotenv("api.env")

alpaca_api_key = os.getenv("key")
alpaca_secret_key = os.getenv("secret")

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

#AAPL
ticker_aapl = ["AAPL"]
timeframe = "1Day"
start_date = pd.Timestamp("2010-01-01", tz="America/New_York").isoformat()
end_date = pd.Timestamp("2023-05-03", tz="America/New_York").isoformat()

aapl = alpaca.get_bars(
    ticker_aapl,
    timeframe,
    start=start_date,
    end=end_date
).df

daily_returns_aapl = aapl['close'].pct_change().dropna()
aar_aapl = daily_returns_aapl.mean() * 1260
asd_aapl = daily_returns_aapl.std() * np.sqrt(1260)
sr_aapl = aar_aapl / asd_aapl

#AMZN
ticker_amzn = ["AMZN"]

amzn = alpaca.get_bars(
    ticker_amzn,
    timeframe,
    start=start_date,
    end=end_date
).df

daily_returns_amzn = amzn['close'].pct_change().dropna()
aar_amzn = daily_returns_amzn.mean() * 1260
asd_amzn = daily_returns_amzn.std() * np.sqrt(1260)
sr_amzn = aar_amzn / asd_amzn

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
                print(f"Sharpe Ratio AAPL = {sr_aapl:.02f}")
                
            elif choice == "AMZN - Amazon.com Inc":
                print(f"Sharpe Ratio AMZN = {sr_amzn:.02f}")
            
            elif choice == "TSLA - Tesla Inc":
                print("TSLA")
            
            elif choice == "JNJ - Johnson & Johnson":
                print("JNJ")
            
            elif choice == "PFE - Pfizer Inc":
                print("PFE")
            
            elif choice == "MS - Morgan Stanley":
                print("MS")
            
            elif choice == "COIN - Coinbase Gllobal Inc":
                print("COIN")
            
            elif choice == "V - Visa Inc":
                print("V")
            
            elif choice == "AXP - American Express Company":
                print("AXP")
            
            elif choice == "PYPL - Paypal Holding Inc":
                print("PYPL")
            
            elif choice == "GE - General Electric Company":
                print("GE")
            
            elif choice == "DAL - Delta Air Lines Inc":
                print("DAL")
            
            elif choice == "XOM - Exxon Mobil Corp":
                print("XOM")
                                        
            elif choice == "Quit - not stock:)":
                cruddy_cli_running = False
                print("Thank you for using the CRUDdy CLI! Goodbye!")

                
        
         # else choice == "Quit":
        #     cruddy_cli_running = False
        #     print("Thank you for using the CRUDdy CLI! Goodbye!")

if __name__ == "__main__":
    fire.Fire(run)