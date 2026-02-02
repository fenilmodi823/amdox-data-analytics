import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
from src.config import FIGURES_DIR

def plot_forecast(y_train, y_test, y_pred, conf_int=None, title='Forecast vs Actual'):
    """
    Plots the training data, actual test data, and forecasted values.
    
    Args:
        y_train (pd.Series): Historical training data.
        y_test (pd.Series): Actual test data.
        y_pred (pd.Series): Forecasted values (same index as y_test).
        conf_int (np.array, optional): Confidence intervals (lower, upper).
        title (str): Plot title.
    """
    plt.figure(figsize=(14, 7))
    
    # Plot Training Data (Zoom in on last year for clarity if needed, or full)
    # Showing last 200 points of training for context
    plt.plot(y_train.index[-200:], y_train[-200:], label='Training History')
    
    # Plot Actual Test Data
    plt.plot(y_test.index, y_test, label='Actual Price', color='green')
    
    # Plot Forecast
    plt.plot(y_test.index, y_pred, label='Forecast', color='red', linestyle='--')
    
    # Shade Confidence Interval
    if conf_int is not None:
        plt.fill_between(y_test.index, 
                         conf_int[:, 0], 
                         conf_int[:, 1], 
                         color='pink', alpha=0.3, label='95% Confidence Interval')
    
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    
    # Save
    os.makedirs(FIGURES_DIR, exist_ok=True)
    save_path = os.path.join(FIGURES_DIR, 'forecast_plot.png')
    plt.savefig(save_path)
    print(f"Forecast plot saved to {save_path}")
    plt.show()

def plot_residuals(residuals, title='Residual Analysis'):
    """
    Plots residual distribution and diagnostics.
    """
    fig, ax = plt.subplots(1, 2, figsize=(16, 5))
    
    # 1. Residuals over time
    sns.lineplot(data=residuals, ax=ax[0])
    ax[0].set_title('Residuals over Time')
    ax[0].axhline(0, color='r', linestyle='--')
    
    # 2. Distribution
    sns.histplot(residuals, kde=True, ax=ax[1])
    ax[1].set_title('Residual Distribution')
    
    # Save
    os.makedirs(FIGURES_DIR, exist_ok=True)
    save_path = os.path.join(FIGURES_DIR, 'residual_analysis.png')
    plt.savefig(save_path)
    print(f"Residual plot saved to {save_path}")
    plt.show()
