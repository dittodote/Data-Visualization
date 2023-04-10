#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.pyplot as pl
import scipy.stats as st
import seaborn as sns
import pandas as pd
from sklearn import datasets
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


# Path of the file to read
spotify_filepath = r"C:\Users\slmnp\Downloads\spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)

# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)


# In[8]:


# Change the style of the figure to the "dark" theme
sns.set_style("dark")

# Line chart 
plt.figure(figsize=(12,6))
sns.lineplot(data=spotify_data)


# In[ ]:




