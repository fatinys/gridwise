
import pandas as pd

def add_features(df):
    """
    Preprocesses a time series DataFrame by adding temporal features and lagged demand columns.
    
    Args:
        df (pd.DataFrame): Input DataFrame with a datetime index and 'demand-mwh' column
    
    Returns:
        pd.DataFrame: Processed DataFrame with additional features
    """
    processed_df = df.copy()
    
    processed_df['hour'] = processed_df.index.hour
    processed_df['day'] = processed_df.index.weekday + 1  # 1-7 (Monday-Sunday)
    processed_df['month'] = processed_df.index.month
    
    processed_df['is_weekend'] = processed_df['day'].isin([5, 6])  # 5=Saturday, 6=Sunday
    
    processed_df['demand_lag1'] = processed_df['demand-mwh'].shift(1)
    processed_df['demand_lag2'] = processed_df['demand-mwh'].shift(2)
    processed_df['demand_lag24'] = processed_df['demand-mwh'].shift(24)
    
    return processed_df

