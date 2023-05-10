# Project 1


## Description
This is the Project 1 submission for Group 3.

## Background
Financial concepts and wealth management can be daunting to understand for people who do not have a background in finance.

Financial Portfolio planner that allows user to research stocks and create  a portfolio
• General user typical has assets that they don’t know what to do. This program helps them predict their potential returns for investment.
• Programs allows for users to preview the expected return for stocks and given their appetite for risk
• Gives users access to tools… and expertise to assist them wealth amplifications

## Images

## Instructions


## Installation Requirements
Import the following packages before running the script. Note that the user will need to create a .env file with their own API keys.
```
import os
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
import fire
import questionary
import json
from MCForecastTools import MCSimulation

%matplotlib inline
```
## Acknowledgements

## License
