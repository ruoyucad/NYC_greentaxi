import numpy as np
import pandas as pd
from sklearn import linear_model
import sklearn.cross_validation as cv
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib

df =pd.read_csv('predict_data.csv')
df.drop(['Unnamed: 0'],inplace=True, axis=1)
model = joblib.load('regression_model.pkl')
results = model.predict(df)
print(results)