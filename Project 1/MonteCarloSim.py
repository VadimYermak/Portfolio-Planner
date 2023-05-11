from MCForecastTools import MCSimulation
from colorama import Fore, Back, Style

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
                 f"The lowest value of your portfolio is" + Fore.RED + f"{ci_95_lower_cumulative_return: .02f}" + Style.RESET_ALL +".", 
                 f"The highest value of your portfolio is" + Fore.RED + f"{ci_95_upper_cumulative_return: .02f}" + Style.RESET_ALL +".\n", 
                 )