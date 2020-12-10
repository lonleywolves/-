from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

file_path_2020= 'month2020.csv'
file_path_2019= 'month2019.csv'
month2020 = pd.read_csv(file_path_2020)
month2019 = pd.read_csv(file_path_2019)

plt.rc('font', family='Malgun Gothic')


avg2019 = month2019.loc[0:0,'1월':'10월']
avg2019_trans = avg2019.transpose()

avg2020 = month2020.loc[0:0,'1월':'10월']
avg2020_trans = avg2020.transpose()

plt.plot(avg2019_trans)
plt.plot(avg2020_trans)
plt.xlabel('month')
plt.ylabel('pm10')
plt.title("미세먼지")
plt.legend(['2019', '2020'])
