#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[5]:


import dataiku
from dataiku import pandasutils as pdu
import pandas as pd


# In[7]:


# Example: load a DSS dataset as a Pandas dataframe
mydataset = dataiku.Dataset("Donnees_Assurance_insurance_data")
df = mydataset.get_dataframe()

df.head(10)


# In[9]:


df.info()


# In[10]:


df.shape


# In[13]:


df.describe(include="all")


# In[ ]:




