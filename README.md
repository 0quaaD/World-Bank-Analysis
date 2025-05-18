# 🌍 GDP Prediction and Visualization Project

This repository contains a machine learning pipeline to predict GDP (Gross Domestic Product) using various economic indicators, as well as a Power BI dashboard for interactive data visualization.

## 📈 Project Highlights

- **Dataset:** Preprocessed economic data (`economy_growth.csv`)
- **Model Used (for economy_growth.csv dataset) :** XGBoost Regressor (R² ≈ 0.93+ with cross-validation)
- **Output:** Predicted GDP values with error metrics saved to `gdp_predictions.csv`
- **Visualization:** Power BI dashboard showcasing country-level GDP trends and prediction accuracy

### The Dataset
This dataset provides a comprehensive collection of time series data sourced from the World Bank Open Data Platform, covering a wide range of global indicators from 1960 to the most recently published year. It includes economic, social, environmental, and demographic metrics, making it an ideal resource for researchers, data scientists, and policymakers interested in global development trends, economic forecasting, or socio-economic analysis.
The original source of the entire datasets: https://www.kaggle.com/datasets/georgejdinicola/world-bank-indicators

## 🧠 Model Overview

The model pipeline includes:
- Feature selection and data scaling
- Cross-validation using `cross_val_score` (5-fold)
- GDP prediction in logarithmic scale to handle skewness
- Evaluation using R², MAE, and RMSE

### Performance

- ✅ R² Score: ~0.93+ (validated)
- ✅ Model Error Rate computed per country
- ✅ Log-transformed targets for more stable regression

## 📊 Power BI Dashboard

A Power BI report (not uploaded here) provides:
- Interactive GDP maps
- Year-over-year GDP growth comparison
- Model prediction vs actual GDP plots
- Error rate heatmaps


## 🚀 How to Run the Model

1. Install dependencies (recommended: Python 3.8+)

```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost
```

2. Visualization
- You need to install PowerBI from Microsoft to use interactive dashboard based on the dataset

## 📌 Future Improvements
- Add a web app interface (Streamlit or Flask)
- Incorporate time-series forecasting
