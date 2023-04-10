#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.pyplot as pl
import scipy.stats as st
import seaborn as sns
import pandas as pd
from sklearn import datasets
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Path of the file to read
iris_filepath = r"C:\Users\slmnp\Downloads\iris.csv"

# Read the file into a variable iris_data
iris_data = pd.read_csv(iris_filepath, index_col="Id")

# Print the first 5 rows of the data
iris_data.head()


# In[4]:


# Histogram 
sns.histplot(iris_data['Petal Length (cm)'])


# In[11]:


# KDE plot 
sns.kdeplot(data=iris_data['Petal Length (cm)'], shade=True)


# In[12]:


# 2D KDE plot
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")


# In[13]:


# Histograms for each species
sns.histplot(data=iris_data, x='Petal Length (cm)', hue='Species')

# Add title
plt.title("Histogram of Petal Lengths, by Species")


# In[14]:


# KDE plots for each species
sns.kdeplot(data=iris_data, x='Petal Length (cm)', hue='Species', shade=True)

# Add title
plt.title("Distribution of Petal Lengths, by Species")


# In[ ]:




