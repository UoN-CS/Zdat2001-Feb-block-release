import pandas as pd

def load_data(filepath):
    """Load CSV data into a Pandas DataFrame."""
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """Perform basic cleaning by dropping missing values and standardising column names on the DataFrame."""
    df = df.dropna()  # Drop missing values
    df.columns = df.columns.str.lower()
    return df
