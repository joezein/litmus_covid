#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np

file_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
df = pd.read_csv(file_url)

cols = df.columns
for i in range(len(df.columns)-5):
    
    # do processing
    df_ = df
    df_ = df[[cols[0], cols[1], cols[2], cols[3], cols[i+4]]]
    df_[cols[i+5] + ' New Cases'] = df[cols[i+5]] - df[cols[i+4]]
    df_[cols[i+5] + ' Direction'] = np.where(df_[cols[i+5] + ' New Cases']>0,1,0) 
    df_['Date'] = cols[i+5]
    date = cols[i+5]
    
    # path name
    data_date = cols[i+5]
    pull_date = cols[-1]
    path_name = "data_for_day_" + str(i) + "pulled_on_day_" + str(len(df.columns)-5) + ".csv" # handles new countries
    
    #
    df_.to_csv("output_data/" + path_name)


# In[ ]:




