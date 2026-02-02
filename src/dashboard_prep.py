import pandas as pd
import numpy as np
import sys
import os
from pathlib import Path

# Fix Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.config import PROCESSED_DATA_PATH

# Define Paths
FORECAST_PATH = PROJECT_ROOT / "data/processed/forecast_results.csv"
MASTER_OUTPUT_PATH = PROJECT_ROOT / "data/processed/powerbi_master_data.csv"

def main():
    # --- LOAD DATA ---
    # 1. Historical Data
    print(f"Loading History from: {PROCESSED_DATA_PATH}")
    df_history = pd.read_csv(PROCESSED_DATA_PATH, parse_dates=['Date'])
    df_history['Type'] = 'Historical'

    # 2. Forecast Data
    print(f"Loading Forecast from: {FORECAST_PATH}")
    df_forecast = pd.read_csv(FORECAST_PATH, parse_dates=['Date'])
    df_forecast['Type'] = 'Forecast'

    # --- DATA TRANSFORMATION & MERGE ---
    # Prepare History for Merge
    df_hist_clean = pd.DataFrame({
        'Date': df_history['Date'],
        'Close_Price': df_history['Close'],
        'Type': 'Historical',
        'Lower_Bound': np.nan,
        'Upper_Bound': np.nan
    })

    # Prepare Forecast for Merge
    df_fcast_clean = pd.DataFrame({
        'Date': df_forecast['Date'],
        'Close_Price': df_forecast['Predicted_Price'], # We plot prediction as the main line here
        'Type': 'Forecast',
        'Lower_Bound': df_forecast['Lower_Conf'],
        'Upper_Bound': df_forecast['Upper_Conf']
    })

    # Concatenate
    df_master = pd.concat([df_hist_clean, df_fcast_clean], axis=0)
    df_master.sort_values('Date', inplace=True)

    # --- FEATURE ENGINEERING ---
    # 1. Calculate 7-Day Moving Average (Trend)
    df_master['MA_7'] = df_master['Close_Price'].rolling(window=7).mean()

    # 2. Calculate Daily Volatility (Absolute % Change)
    df_master['Volatility'] = df_master['Close_Price'].pct_change().abs() * 100

    # --- EXPORT ---
    df_master.to_csv(MASTER_OUTPUT_PATH, index=False)
    print(f"SUCCESS: Master dataset saved to {MASTER_OUTPUT_PATH}")
    print(f"Rows: {len(df_master)}")
    print(df_master.tail())

if __name__ == "__main__":
    main()
