import pandas as pd
import numpy as np
import  alpaca_trade_api as tradeapi
from colorama import Fore, Back, Style

# Sharpe ratio functionality
def get_sharpe_ratio(ticker, alpaca):
    
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
    annual_average_return = daily_returns.mean() * 252
    annual_standard_deviation = daily_returns.std() * np.sqrt(252)
    sharpe_ratio = annual_average_return / annual_standard_deviation
    
    print(f"\nSharpe ratio for {ticker} is " + Fore.RED + f"{sharpe_ratio : .02f}" + Style.RESET_ALL +".")
    print(f"Annualized Average Return is " + Fore.RED + f"{annual_average_return : .02f}" + Style.RESET_ALL +".")
    print(f"Annualized Standard Deviation is " + Fore.RED + f"{annual_standard_deviation : .02f}" + Style.RESET_ALL +".\n")