<h1 align="center">Porfolio Planner</h1>

## Table of contents

- [Description](#description)
- [Background](#background)
- [Installation Requirements / Technologies](#installation-requirements-technologies)
- [Images](#images)
- [License](#license)

## Description
<div align="center">
<img src="Images/Portfolio Planner.gif" style="width: 100px; height: 100px; object-fit: none; object-position: 25% 25%;></img>
</div>
<br/>
                                               
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

    MIT License

    Copyright (c) 2023 Columbia University - CU-VIRT-FIN-PT-03-2023-U-B-TTH - Team 3

    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
