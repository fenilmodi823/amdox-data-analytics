import pandas as pd
import numpy as np
import pmdarima as pm
import joblib
import sys
import os
import warnings
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.config import PROCESSED_DATA_PATH, MODEL_PATH

def train():
    print("--- Phase 2: Model Training Execution ---")
    warnings.filterwarnings('ignore')
    
    # 1. Load Processed Data
    print(f"Loading processed data from: {PROCESSED_DATA_PATH}")
    if not os.path.exists(PROCESSED_DATA_PATH):
        print(f"Error: {PROCESSED_DATA_PATH} not found. Run make_dataset.py first.")
        return

    df = pd.read_csv(PROCESSED_DATA_PATH, parse_dates=['Date'], index_col='Date')
    df.sort_index(inplace=True)
    
    # 2. Split Data
    train_size = int(len(df) * 0.9)
    train_data = df['Close'][:train_size]
    test_data = df['Close'][train_size:]
    print(f"Train Samples: {len(train_data)}, Test Samples: {len(test_data)}")
    
    # 3. Auto-ARIMA Training
    print("Starting Auto-ARIMA optimization (m=7, d=1)...")
    model = pm.auto_arima(train_data,
                          m=7,
                          d=1,
                          seasonal=True,
                          stepwise=True,
                          suppress_warnings=True,
                          error_action='ignore')
    
    print(f"Best Model Parameters: {model.order}")
    print(model.summary())
    
    # 4. Save Model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    print(f"Saving model to: {MODEL_PATH}")
    joblib.dump(model, MODEL_PATH)
    
    # 5. Generate Forecast & Save Results
    print("Generating Forecast for Test Period...")
    forecast, conf_int = model.predict(n_periods=len(test_data), return_conf_int=True)
    
    # Metrics
    rmse = np.sqrt(mean_squared_error(test_data, forecast))
    print(f"Validation RMSE: {rmse:.2f}")
    
    # Export Results for Power BI / Visualization
    export_df = pd.DataFrame({
        'Date': test_data.index,
        'Actual_Price': test_data.values,
        'Predicted_Price': forecast.values,
        'Lower_Conf': conf_int[:, 0],
        'Upper_Conf': conf_int[:, 1]
    })
    
    # Save where config points, or default to data/processed
    forecast_path = os.path.join(os.path.dirname(PROCESSED_DATA_PATH), 'forecast_results.csv')
    export_df.to_csv(forecast_path, index=False)
    print(f"Forecast results saved to: {forecast_path}")

if __name__ == "__main__":
    train()
