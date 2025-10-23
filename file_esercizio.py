import yfinance as yf
import pandas as pd 
import memory_handling as mh


def main(ticker):
    apple_data_df = yf.download(
    tickers=ticker, 
    start='2025-10-01', # Correct YYYY-MM-DD format
    end='2025-10-20',   # Correct YYYY-MM-DD format
    interval="1d" 
    )
    apple_data_df.columns = ['Close' , 'High' , 'Low' , 'Open' , 'Volume']
    data_saver = mh.PickleHelper(apple_data_df)
    filename = 'file_prova'
    data_saver.pickle_dump(filename)


    

    
if __name__ == "__main__":
    main('AAPL')