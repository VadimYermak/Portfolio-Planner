import os
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import  alpaca_trade_api as tradeapi
import fire
import questionary

path = "env"
load_dotenv(path, verbose = True)

alpaca_api_key = os.getenv("key")
alpaca_secret_key = os.getenv("secret")

alpaca = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version="v2")

ticker = ["AAPL"]
timeframe = "1Day"
start_date = pd.Timestamp("2010-01-01", tz="America/New_York").isoformat()
end_date = pd.Timestamp("2023-05-03", tz="America/New_York").isoformat()

aapl = alpaca.get_bars(
    ticker,
    timeframe,
    start=start_date,
    end=end_date
).df

daily_returns_aapl = aapl['close'].pct_change().dropna()
aar_aapl = daily_returns_aapl.mean() * 1260
asd_aapl = daily_returns_aapl.std() * np.sqrt(1260)
sr_aapl = aar_aapl / asd_aapl

def run():

    cruddy_cli_running = True

    while cruddy_cli_running:
        choice = questionary.select(
            "What do you want to do?",
            choices=["Option 1", "Option 2", "Quit"]
        ).ask()
        
        if choice == "Option 1":
            choice = questionary.select(
                "What stocks do you want to review?", 
                choices = ["AAPL", "GOOG", "Quit"]
                ).ask()
            
            if choice == "AAPL":
                print(sr_aapl)
                
            elif choice == "GOOG":
                print("GOOG")
                
            elif choice == "Quit":
                cruddy_cli_running = False
                print("Thank you for using the CRUDdy CLI! Goodbye!")

                
        
        # else choice == "Quit":
        #     cruddy_cli_running = False
        #     print("Thank you for using the CRUDdy CLI! Goodbye!")

if __name__ == "__main__":
    fire.Fire(run)