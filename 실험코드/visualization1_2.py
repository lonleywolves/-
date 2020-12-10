from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

file_path_2020_micro = 'month2020_micro.csv'
file_path_2019_micro = 'month2019_micro.csv'
micro2020 = pd.read_csv(file_path_2020_micro)
micro2019 = pd.read_csv(file_path_2019_micro)

plt.rc('font', family='Malgun Gothic')


micro2019_avg = micro2019.loc[0:0,'1월':'10월']
micro2019_trans = micro2019_avg.transpose()

micro2020_avg = micro2020.loc[0:0,'1월':'10월']
micro2020_trans = micro2020_avg.transpose()

plt.plot(micro2019_trans)
plt.plot(micro2020_trans)
plt.xlabel('month')
plt.ylabel('pm2.5')
plt.title("초미세먼지")
plt.legend(['2019', '2020'])
