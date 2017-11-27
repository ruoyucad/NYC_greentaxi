import pandas as pd 
import numpy as np 
import statsmodels as sm
# for ploting
import matplotlib.pyplot as plt
import seaborn as sns
#for treemap
import squarify

# loading dataset 1.5 millions rows 
data = pd.read_csv('full_data.csv')
print('There are %s sets of data in total'%(data.shape[0]))
#first 5 sets
data.head()
data.describe()
# check for missing values for each columns
data.isnull().sum()
# need to drop uncessary columns
data.drop(['Unnamed: 0','Unnamed: 0.1','Ehail_fee'], inplace=True, axis=1)
#remove missing values in certain columns
data = data[pd.notnull(data['address'])]
data = data[pd.notnull(data['zipcode'])]
data = data[pd.notnull(data['Trip_type '])]
# now whole set is clean
# time conversion 
data['Lpep_dropoff_datetime']=pd.to_datetime(data['Lpep_dropoff_datetime'])
print(data['Lpep_dropoff_datetime'][0])
# add hours
hour = data.Lpep_dropoff_datetime.dt.hour
data['hour'] = hour
# shows hourly distribution
sns.countplot(x = 'hour', data = data)

# showing payment method distribution
# add label to payment methods
# bin edge need to be 1 more that type numbers
types = [0, 1, 2, 3, 4, 5]
group_payment = ['CRD', 'CSH', 'DIS', 'NOC', 'UNK']
data['group_payment'] = pd.cut(data['Payment_type'], types, labels=group_payment)

# trip distance distribution
print(data.Trip_distance.min() , data.Trip_distance.max())
# avg trip distance
print(round(data.Trip_distance.sum()/data['Trip_distance'].count(),2))
# plot the distribution 
distances = [0, 5, 10, 50, 100, 200, 250]
group_distances = ['0-5 miles', '5-10 miles', '10-50 miles', '50-100 miles', '100-200 miles', '200 miles above']
data['group_distances'] = pd.cut(data['Trip_distance'], distances, labels=group_distances)
# bar chart
sns.countplot(y = 'group_distances', data = data, orient='h')
# see the density
sns.kdeplot(data['Trip_distance'], shade=True)

#Taxi Service request distribution
data['Trip_type_volume'] = data.groupby('Trip_type ')['Trip_type '].transform('count')
# 1= Street-hail，2= Dispatch
print(set(data['Trip_type '].tolist()))
sns.countplot(x = 'Trip_type_volume', data = data, orient='v')
# plt.plot()
