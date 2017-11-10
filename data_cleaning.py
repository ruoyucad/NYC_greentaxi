
# coding: utf-8

# In[1]:


# Gale take home with NYC green taxi data (Feb 2016, 237MB)
'''
tasks:
1. Download the data, load it into your favorite statistical programing software or database.
Report the number of rows and columns that you've loaded.

2. Visualize trip distance by time in any way you see fit, any observations?

4. What are the most popular pickup locations on weekdays vs weekend?

5. Build a model to forecast the number of trips by hour for the next 12 hours after Feb 12th 10:00 am. How well did you do?
 
'''

# In[2]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

print('Started!')
raw_data = pd.read_csv("green_tripdata_2016-02.csv")
print(raw_data.shape)

raw_data.columns
raw_data.head()
raw_data.Trip_distance.describe()
raw_data.lpep_pickup_datetime.describe()
raw_data.Lpep_dropoff_datetime.describe()
length_of_trip = []
print(type(raw_data.lpep_pickup_datetime[0]))

# convert str to timestamps
raw_data['lpep_pickup_datetime'] = pd.to_datetime(raw_data.lpep_pickup_datetime)
raw_data['Lpep_dropoff_datetime'] = pd.to_datetime(raw_data.Lpep_dropoff_datetime)
#make new column named lenght_of_trip by substracting pickup time from dropoff time
raw_data['lenght_of_trip'] = raw_data['Lpep_dropoff_datetime'] - raw_data['lpep_pickup_datetime'] 

# describtion of the trip lenght column
raw_data.lenght_of_trip.describe()
# convert Timedelta to seconds for easier calculation
raw_data['lenght_of_trip'] = raw_data['lenght_of_trip'] / np.timedelta64(1, 's')
print(raw_data.head())

'''
# in general the distance and time have a positive correalation
plt.scatter(raw_data['lenght_of_trip'].sample(30), raw_data['Trip_distance'].sample(30))
plt.xlabel("length of trips in Seconds")
plt.ylabel("Trip Distance In Miles")
plt.show()
'''

# add Weekday columns , 0 being Monday, 6 being Sunday
raw_data['Weekday'] = raw_data['lpep_pickup_datetime'].dt.dayofweek

raw_data.to_csv('data_with_weekdays.csv')

print('Done !')
