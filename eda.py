#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns



df = pd.read_csv(r'C:\Users\cheta\OneDrive\Desktop\mbti_1.csv') 
# To display the top 5 rows
df.head(5)


# In[ ]:


df.isnull().any()


# In[ ]:


df.dtypes


# In[ ]:


df.shape


# In[ ]:


duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows:" , duplicate_rows_df.shape)


# In[ ]:


df.count
df = df.drop_duplicates()
print(df.isnull().sum())
df = df.dropna()


# In[ ]:


df.info()


# In[ ]:


df.describe(include=['object'])


# In[ ]:


types = np.unique(np.array(df['type']))
types


# In[ ]:


total = df.groupby(['type']).count()*50
total


# In[ ]:


plt.figure(figsize = (16,6))
plt.bar(np.array(total.index), height = total['posts'],color=('pink'))
plt.xlabel('Personality type of the post', size = 20)
plt.ylabel('No. of posts ', size = 20)
plt.title('POSTS FOR EACH PERSONALIY TYPE')


# In[ ]:


plt.figure(figsize=(20,10))
c= df.corr()
sns.heatmap(c,cmap='BrBG',annot=True)


# In[ ]:




