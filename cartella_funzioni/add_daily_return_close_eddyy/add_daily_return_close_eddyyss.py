

import pandas as pd 

def add_daily_return_close_eddyy (df : pd.DataFrame) :
    """
    Adds the daily return of the column 'Close' to the given DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing a 'Close' column.

    Returns
    -------
    pandas.DataFrame or None
        DataFrame with a new column 'daily_return_open' representing the percentage change of 'Close'.
        Returns None if the 'Close' column does not exist.
    """


    if 'Close' in df.columns : 
        df['daily_return_open'] = df['Close'].pct_change()
    else : 
        print("The DataFrame does not contain the column 'close' ") 
        return None 
    return df 


