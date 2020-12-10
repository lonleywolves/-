#2019년 data. 데이터에는 2020과의 비교를 위해 최솟값, 최댓값이 들어있습니다.!

import pandas as pd
import numpy as np
import matplotlib as plt
import folium
import json


geo_path = 'seoul_municipalities_geo_simple.json'
geo_json = json.load(open(geo_path,encoding="utf-8"))

#file_path = 'month2019_2.csv'
#pm10_2019 = pd.read_csv(file_path)

file_path = 'pm10_csv'
pm10 = pd.read_csv(file_path)

data1= pm10_2019[1:28]
data2019 = data1[['name', 'avg']]


#lat = 37.542921398212634
#long = 126.9887885123524

latitude = 37.715133
longtitude = 126.734086


m = folium.Map([latitude, longtitude])

folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=data2019,
    columns=['name', 'avg'],
    key_on='feature.properties.name',
    fill_color='YlOrBr',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='pm10'
).add_to(m)

m
