import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn import linear_model
import sklearn.cross_validation as cv
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib

# pwd
model=pd.read_csv('full_data.csv')
print(model.columns)
# add Hours
Time = pd.to_datetime(model['lpep_pickup_datetime'])
Hour = Time.dt.hour
Date = Time.dt.day
Hours =pd.DataFrame({'Hours':Hour})
Dates =pd.DataFrame({'Dates':Date})
model = pd.concat([model, Hours,Dates], axis=1)
print('added Hours')
# drop nan in zipcodes 
model = model[np.isfinite(model['zipcode'])]
model['zipcode'] = model['zipcode'].apply(int)
model['zipcode'] = model['zipcode'].apply(str)
#print(model['zipcode'][0])

zipcode_dummies = pd.get_dummies(model['zipcode'])
#zipcode_dummies=zipcode_dummies.applymap(np.int)
#Weekday_dummies = pd.get_dummies(model['Weekday'])
# concat together
model = pd.concat([model, zipcode_dummies], axis=1)

model.drop(['Unnamed: 0','Unnamed: 0.1','Ehail_fee','VendorID','Lpep_dropoff_datetime','lpep_pickup_datetime','Store_and_fwd_flag','RateCodeID',
'Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude','Tolls_amount','Payment_type'
,'Trip_type ','address','Coor'], inplace=True, axis=1)
print("Data ready!")

target=model[['Taxi_Demand']]
data = model[[col for col in model.columns if col not in ['Taxi_Demand']]]
print(data.head())

#split into training and testing 
print('training starts!')
x_train, x_test, y_train, y_test = cv.train_test_split(data, target, test_size=2.0/10, random_state=43)
ols = linear_model.LinearRegression()
ols.fit(x_train, y_train)

print('training R^2: %.2f',ols.score(x_train, y_train))
print('testing R^2: %.2f',ols.score(x_test, y_test))

print('training RMSE:', mean_squared_error(y_train, ols.predict(x_train)))
print('testing RMSE:', mean_squared_error(y_test, ols.predict(x_test)))
'''
Training Results: 

training R^2: %.2f 1.0
testing R^2: %.2f 0.999998650117
training RMSE: 5.17259234222e-08
testing RMSE: 1343.06024583

'''
joblib.dump(ols, 'regression_model.pkl', compress=9)
# model_clone = joblib.load('regression_model.pkl')
# data after 12th Feb 10am


#predict_data = data[data['Hours']>9]
#predict_data = predict_data[predict_data['Dates']>12]
#predict_data.to_csv('predict_data.csv')
print('Done!')