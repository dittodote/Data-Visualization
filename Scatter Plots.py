#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import seaborn as sns
import pandas as pd
from bmi import calculate_bmi


# In[25]:


# Path of the file to read
insurance_filepath = r"C:\Users\slmnp\Downloads\insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)


# In[26]:


insurance_data.head()


# In[27]:


sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])


# In[28]:


sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])


# In[29]:


sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])


# In[30]:


sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)


# In[32]:


sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])


# In[ ]:




