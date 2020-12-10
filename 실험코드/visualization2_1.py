#2019년 data. 데이터에는 2020과의 비교를 위해 최솟값, 최댓값이 들어있습니다.!



import pandas as pd
import folium
import json

file_path = 'pm10.csv'
pm10 = pd.read_csv(file_path)


geo_path = 'seoul_municipalities_geo_simple.json'
geo_json = json.load(open(geo_path,encoding="utf-8"))

latitude = 37.715133
longtitude = 126.734086


m = folium.Map([latitude, longtitude])

folium.Choropleth(
    geo_data=geo_json,
    name='mymap',
    data=pm10,
    columns=['name', 'avg'],
    key_on='feature.properties.name',
    fill_color='YlOrBr',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='pm10'
).add_to(m)

m




#####2020년 data
file_path2 = 'month2020.csv'
pm10_2020 = pd.read_csv(file_path2)

data2 = pm10_2020[1:28]

data2020 = data2[['name', 'avg']]

m = folium.Map([latitude, longtitude])

folium.Choropleth(
    geo_data=geo_json,
    name='choropleth',
    data=data2020,
    columns=['name', 'avg'],
    key_on='feature.properties.name',
    fill_color='YlOrBr',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='pm10'
).add_to(m)

m
