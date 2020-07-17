#!/usr/bin/env python
# coding: utf-8

# # Capstone Project Notebook

# I will be working here on a neighborhoods project

# In[1]:


print("Hello Capstone Project Course!")


# In[2]:


import pandas as np


# In[3]:


import numpy as np


# # week 3 
# ## Segmenting and Clustering Neighborhoods in Toronto

# In[10]:


import pandas as pd

url= 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

dfs= pd.read_html(url)

print(len(dfs))


# In[12]:


print(dfs[0])


# In[24]:


#get the first table
df= dfs[0]
df


# In[28]:


df.drop(df[df['Borough']=='Not assigned'].index, inplace=True)
df


# In[31]:


df= df.groupby(['Postal Code','Borough'], as_index=False).agg(lambda x: ','.join(x))
df


# In[33]:


mask = df['Neighborhood'] == "Not assigned"
df.loc[mask, 'Neighborhood'] = df.loc[mask, 'Borough']
df


# Above table was imported from a website url. It is clean now after removing non assigne cells and combining rows by repeated posstal code. 

# The table is ready now to be used in further explorations 

# In[34]:


df.shape

