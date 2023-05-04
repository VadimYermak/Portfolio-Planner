import questionary
import fire

def run_crud(message="Hello, we can suggest you next stocks: AAPL, TSLA"):
	print(message)
if __name__ == '__main__':
	fire.Fire(run_crud)
    
table_name = questionary.text("What stock do you want to choose to see Sharpe Ratio?").ask()
                              
print(table_name)