#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Path of the file to read
flight_filepath = r"C:\Users\slmnp\Downloads\flight_delays.csv"

# Read the file into a variable flight_data
flight_data = pd.read_csv(flight_filepath, index_col="Month")


# In[7]:


import pandas as pd


# In[9]:


# Print the data
flight_data


# In[14]:


# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")

# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])

# Add label for vertical axis
plt.ylabel("Arrival delay (in minutes)")


# In[13]:


# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import seaborn as sns


# In[15]:


# Bar chart showing average arrival delay for Spirit Airlines flights by month
sns.barplot(x=flight_data.index, y=flight_data['NK'])


# In[16]:


# Set the width and height of the figure
plt.figure(figsize=(14,7))

# Add title
plt.title("Average Arrival Delay for Each Airline, by Month")

# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)

# Add label for horizontal axis
plt.xlabel("Airline")


# In[17]:


# Heatmap showing average arrival delay for each airline by month
sns.heatmap(data=flight_data, annot=True)


# In[ ]:




