# NYC_greentaxi
This project is aimd to analyse NYC green taxi data and find possible insights within
The goal is to find the relationship of the taxi demand with attributes like lengh of the trip, pickup location etc. 
![Alt text](https://github.com/ruoyucad/NYC_greentaxi/blob/master/weekends.PNG?raw=true "popular location on Weekend")
# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
```
  git clone https://github.com/ruoyucad/NYC_greentaxi.git 
```
# Prerequisites
```
  python 3.4, sklearn, pandas, numpy, geopy, seaborn
```
#Installing
```
sudo pip install numpy pandas geopy seaborn sklearn
```
if you have both ptyhon2 and python3 on your machine remember to use designated pip.

For python2 
```
pip install package_name
```
For python3
```
pip3 install package_name
```

# Data Cleaning & with Feature Engineering
The raw data contains about 1.5 million rows and 25 columns, each columns represents a feature of the trip information
such as 'Lpep_dropoff_datetime','lpep_pickup_datetime','Pickup_longitude','Pickup_latitude','Dropoff_longitude','Dropoff_latitude','Tolls_amount','Payment_type' etc. 

data_clearning.py and feature_engineering_taxi_demaind.py are used for data preprocessing. 
Notice:  feature_engineering_taxi_demaind.py will use Geopy for fetch address info, but it needs to set a timeout 
because Geopy will block the ip if too many requests occur.(Generating addresses might take a long time, go get some coffee.)
```
 python3 data_clearning.py
 python3 feature_engineering_taxi_demaind.py
```
zipcodes_coords.csv will be generated for modeling and prediction
![Alt text](https://github.com/ruoyucad/NYC_greentaxi/blob/master/weekdays.PNG?raw=true "popular location on Weekdays")
# Modeling & predict 
After feature engineering, three more features will be generated 'zipcode', 'address', 'Demand'
'Demand' varibale will be used as dependent variable 

# Authors
Ruoyu Qian -Initial work
