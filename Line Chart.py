#!/usr/bin/env python
# coding: utf-8

# In[12]:


# importing the quired libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[7]:


# Path of the file to read
spotify_filepath = r"C:\Users\slmnp\Downloads\spotify.csv"

# Read the file into a variable spotify_data
spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)


# In[8]:


# Print the first 5 rowsw of the data
spotify_data.head()


# In[9]:


# Print the last five rows of the data
spotify_data.tail()


# In[14]:


# Line chart showing daily global stream of each song
sns.lineplot(data=spotify_data)


# In[13]:


import seaborn as sns


# In[15]:


# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)


# In[16]:


list(spotify_data.columns)


# In[17]:


# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")

# Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")

# Add label for horizontal axis
plt.xlabel("Date")


# In[18]:


# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")


# In[20]:


# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")


# In[21]:


# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Something Just Like This'], label="Something Just Like This")


# In[ ]:




