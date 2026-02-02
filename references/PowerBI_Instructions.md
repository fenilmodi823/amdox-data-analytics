# 📈 Power BI Dashboard Setup Guide

## Step 1: Import Data
1. Open Power BI Desktop.
2. Click **Get Data** -> **Text/CSV**.
3. Select `data/processed/powerbi_master_data.csv`.
4. Click **Load**.

## Step 2: Visual 1 - Price Trend & Forecast
* **Visual Type:** Line Chart.
* **X-Axis:** `Date`
* **Y-Axis:** `Close_Price`
* **Legend:** `Type` (This splits the line into Historical vs. Forecast colors).
* **Analytics Pane:** Add a "Trend Line" to see the overall direction.

## Step 3: Visual 2 - Confidence Intervals (The "Risk" Zone)
* **Visual Type:** Line & Clustered Column Chart (or custom Area chart).
* **X-Axis:** `Date` (Filter to show only the last 6 months).
* **Y-Axis:** `Close_Price`, `Lower_Bound`, `Upper_Bound`.
* **Note:** This highlights the range where the price is expected to fluctuate.

## Step 4: Visual 3 - Volatility Gauge
* **Visual Type:** Card or Gauge.
* **Field:** Average of `Volatility`.
* **Purpose:** Shows how risky the asset is right now.
