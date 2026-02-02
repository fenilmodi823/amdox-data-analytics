# Time Series Analysis with Cryptocurrency

## Description
This project implements an end-to-end Data Analytics pipeline for cryptocurrency price forecasting. 
It utilizes **Auto-ARIMA** for statistical modeling to predict future trends based on historical data. 
The pipeline includes rigorous Data Engineering (cleaning, stationarity testing), advanced Modeling (seasonal adjustments), and Visualization (Forecast vs Actuals, Power BI Dashboarding).

## Key Features
- **Data Engineering**: Automated stationarity checks (ADF Test) and handling of missing values.
- **Modeling**: Auto-ARIMA optimization with weekly seasonality (`m=7`).
- **Validation**: Strict Time Series Cross-Validation (RMSE Analysis).
- **Dashboarding**: Prepared Master Dataset for interactive Power BI reporting.

## Installation
Ensure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```

## Usage

### 1. Data Cleaning
Run the ETL pipeline to process raw data:
```bash
python src/data/make_dataset.py
```
*Output: `data/processed/processed_stock_data.csv`*

### 2. Model Training
Train the ARIMA model and generate forecasts:
```bash
python src/models/train_model.py
```
*Output: `models/arima_model.pkl` and `data/processed/forecast_results.csv`*

### 3. Visualization & Dashboarding
- Run `notebooks/3.0-visualization.ipynb` for detailed plots.
- Run `notebooks/3.0-dashboard-prep.ipynb` to generate `powerbi_master_data.csv`.
- Follow `references/PowerBI_Instructions.md` to setup the dashboard.

## Results
The current model achieved an **RMSE** (Root Mean Squared Error) of approx **11.85** on the test set.

| Metric | Score | Note |
|--------|-------|------|
| RMSE | 11.85 | Lower is better |
| MAE | 11.01 | Average absolute deviation |

The model successfully captures the general trend but highlights the high volatility inherent in cryptocurrency markets.
