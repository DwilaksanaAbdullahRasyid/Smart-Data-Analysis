#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json
import pprint
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[2]:


response=requests.get('https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json')
content = response.content
json_tree = json.loads(content)


# In[3]:


df=pd.DataFrame(json_tree)


# In[41]:


df=pd.read_csv('youbike-taipei.csv',sep=';')


# In[44]:


import folium

leftRatio=df['sbi']/df['tot']*100
df['lat']=pd.to_numeric(df['lat'])
df['lng']=pd.to_numeric(df['lng'])

loc=df[['lat','lng']].values.tolist()
mapit = folium.Map( location=loc[6], zoom_start=6 )
for point in range(0, len(loc)):
    folium.Marker(loc[point], popup=[leftRatio[point],df['snaen'][point],df['sarean'][point]]).add_to(mapit)
mapit

