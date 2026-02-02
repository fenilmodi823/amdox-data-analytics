from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "stock_data.csv"
PROCESSED_DATA_PATH = DATA_DIR / "processed" / "processed_stock_data.csv"
MODEL_PATH = PROJECT_DIR / "models" / "arima_model.pkl"
FIGURES_DIR = PROJECT_DIR / "reports" / "figures"
