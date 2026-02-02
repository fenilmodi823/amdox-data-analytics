import pandas as pd
import numpy as np
import warnings
import os
import sys
from statsmodels.tsa.stattools import adfuller

# Add project root to sys.path to allow imports from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def check_stationarity(series):
    """Checks stationarity using ADF test."""
    print(f"Performing ADF Test on {series.name}...")
    result = adfuller(series.dropna())
    print(f'ADF Statistic: {result[0]}')
    print(f'p-value: {result[1]}')
    if result[1] <= 0.05:
        print("Result: Stationary (Reject H0)")
    else:
        print("Result: Non-Stationary (Fail to Reject H0)")
    return result[1]

def main():
    print("--- Phase 1: Data Engineering Execution ---")
    warnings.filterwarnings('ignore')
    
    # 1. Load Data
    print(f"Loading raw data from: {RAW_DATA_PATH}")
    if not os.path.exists(RAW_DATA_PATH):
        print(f"Error: {RAW_DATA_PATH} does not exist.")
        return
        
    df = pd.read_csv(RAW_DATA_PATH, parse_dates=['Date'], index_col='Date')
    df.sort_index(inplace=True)
    print(f"Initial Shape: {df.shape}")

    # 2. Preprocessing
    # Resample to Daily to ensure full timeline (optional but good practice)
    # df = df.resample('D').last() 
    
    # Forward Fill (Strict Protocol)
    print("Applying Forward Fill...")
    df.ffill(inplace=True)
    
    # Check for remaining NaNs (e.g., at the start)
    if df.isnull().sum().any():
        print("Warning: NaNs remain after ffill (likely at start). Filling with bfill.")
        df.bfill(inplace=True)
        
    # 3. Stationarity (Information only, we don't save differenced data for modeling usually, 
    # as Auto-ARIMA handles d parameter, but we test it for EDA)
    check_stationarity(df['Close'])
    
    # 4. Save
    # Ensure directory exists
    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    
    print(f"Saving processed data to: {PROCESSED_DATA_PATH}")
    df.to_csv(PROCESSED_DATA_PATH)
    print("Data Engineering Complete.")

if __name__ == "__main__":
    main()
