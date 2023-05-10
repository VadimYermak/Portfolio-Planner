# Project 1

## Description
This is the Project 1 submission for Group 3.
• Executive summary: Briefly explain your project and how it relates to fintech and financial programming.
• Financial Portfolio planner that allows user to research stocks and create  a portfolio
• General user typical has assets that they don’t know what to do. This program helps them predict their potential returns for investment.
• Programs allows for users to preview the expected return for stocks and given their appetite for risk
Gives users access to tools… and expertise to assist them wealth amplifications

## Background
Financial concepts and wealth management can be daunting to understand for people who do not have a background in finance.

## Installation Requirements / Technologies
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
## Images
The script allows user prompts to select from a list with very few manual entries.

| Select stocks from a list| Monte Carlo Simulation |
| :-----------------:| :-----------------:|
| <img src = "https://github.com/VadimYermak/Project-1/blob/main/Images/Stocks%20List.png" width="300">| <img src = "https://github.com/VadimYermak/Project-1/blob/main/Images/Monte%20Carlo%20Simulation.png" width="420"> |

User can also generate a Favorites List for their stocks for future reference.

<img src = "https://github.com/VadimYermak/Project-1/blob/main/Images/Favorites%20List.png" width="300">

## Collaborators

## Acknowledgements

## License
Copyright. This application has no owner. 
