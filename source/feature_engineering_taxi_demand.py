import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm
import numpy as np
import re
import time
import csv

print("Here we go")
geolocator = Nominatim()
data = pd.read_csv("data_with_weekdays.csv")
print('Data read! ')
# check nan value for pick up point
data = data[np.isfinite(data['Pickup_latitude'])]
print(data.shape)
# modify the lat & long in order to get addresses

# for weekdays change coordinates granularities
lat_day = data['Pickup_latitude'].tolist()
lon_day = data['Pickup_longitude'].tolist()
lat_day = [round(i,3) for i in lat_day]
lat_day = [str(i) for i in lat_day]
lon_day = [round(i,3) for i in lon_day]
lon_day =[str(i) for i in lon_day]
lon_day =[' ,'+ i for i in lon_day]
coor_day = [x+y for x,y in zip(lat_day,lon_day)]
set1 = set(coor_day)
unique_coord = list(set1)

print('Done')

data['Coor'] = coor_day

# for count merging later

df1=pd.DataFrame({'Coor':unique_coord})

addresses = []
notfound = 0 
# get all the geo info 
for i in tqdm(unique_coord):
	location = geolocator.reverse(i,timeout=50)
	if location.address == None:
		location ='NaN'
		notfound += 1
		addresses.append(location)
		print(len(addresses))
		print(addresses[-1])
		print("%d" % notfound+ 'hasnt been found')
	else:	
		print(location.address)
		addresses.append(location.address)
		print(len(addresses))
		print(addresses[-1])
	time.sleep(1)


print(len(addresses))
print(df1.shape)
df1['address'] = addresses

# merge address to dataframe
# merge frist then count
# COUNT meaning the amount of taxi in that certain address
zipcodes = []
for i in addresses:    
    num = re.findall(r"\D(\d{5})\D", i)
    num = list(filter(str.isdigit, num))
    zipcode = ''.join(num)
    zipcodes.append(zipcode)
# add zipcode
df1['zipcode'] = zipcodes
df1.to_csv("zipcodes_coords.csv")
#merge
data =pd.merge(data, df1, how='left', on=['Coor'])
#Count taxi amount in certain Zip Code
# add zipcode frequency aka Taxi demand to original dataframe
data['Taxi_Demand'] = data.groupby('zipcode')['zipcode'].transform('count')
data.to_csv('full_data.csv')
print('Done')
