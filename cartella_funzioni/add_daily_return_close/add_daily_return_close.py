import pandas as pd

def add_daily_return_close(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a column with daily returns calculated from the 'Close' prices.

    Args:
        df (pd.DataFrame): Input DataFrame containing a 'Close' column.

    Returns:
        pd.DataFrame: The input DataFrame with an additional 'daily_return_close' column containing daily percentage returns.
            Returns None if the 'Close' column is missing.
    """
    
    if 'Close' in df.columns:
        df['daily_return_close'] = df['Close'].pct_change()
    else:
        print("ERROR! The DataFrame does not have the 'Close' column.")
        return None

    return df