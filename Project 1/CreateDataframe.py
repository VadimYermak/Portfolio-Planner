import pandas as pd
import  alpaca_trade_api as tradeapi

# Create a dataframe from two stock inputs:
def df_portfolio(stock1, stock2, api_key, secret_key):
    alpaca = tradeapi.REST(api_key, secret_key, api_version = "v2")

    tickers = [stock1, stock2]
    timeframe = "1Day"
    start_date = pd.Timestamp("2010-01-01", tz="America/New_York").isoformat()
    end_date = pd.Timestamp("2023-05-03", tz="America/New_York").isoformat()

    df_portfolio = alpaca.get_bars(tickers, timeframe, start = start_date, end = end_date).df

    stock1_df = df_portfolio[df_portfolio["symbol"]== stock1].drop("symbol", axis=1)
    stock2_df = df_portfolio[df_portfolio["symbol"]== stock2].drop("symbol", axis=1)
     
    df_portfolio = pd.concat([stock1_df, stock2_df], axis=1, keys=[stock1, stock2])
    
    return df_portfolio
