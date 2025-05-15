import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, GridSearchCV, KFold, cross_val_score
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import os
import seaborn as sns
import matplotlib.ticker as ticker
from sklearn.cluster import KMeans
from sklearn.inspection import permutation_importance

df = pd.read_csv("economy_growth.csv")
df = df.dropna()
X = df.drop(columns=['GDP (current US$)','country'],axis=1)
y = np.log1p(df['GDP (current US$)'])

# cross_val_score method

model = XGBRegressor(random_state=42)
score = cross_val_score(model,X,y,cv=5,scoring='r2')
print(f"R^2 Score with Cross Validation : {np.mean(score):.4f}")

model.fit(X, y)
y_pred_log = model.predict(X)
y_pred = np.expm1(y_pred_log) 
df['Predicted GDP (current US$)'] = y_pred

df.to_csv("gdp_predictions.csv",index=False)
