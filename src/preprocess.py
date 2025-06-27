import pandas as pd

def load_data(filepath):
    """Load raw dataset from CSV"""
    return pd.read_csv(filepath)

def clean_data(df):
    """Basic cleaning: remove duplicates, handle missing"""
    df = df.drop_duplicates()
    df = df.dropna()  # or fillna(...) depending on your target
    return df

def save_processed_data(df, output_path):
    """Save cleaned data"""
    df.to_csv(output_path, index=False)

