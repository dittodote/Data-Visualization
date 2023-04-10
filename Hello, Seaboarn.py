#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
print("Setup Complete")


# In[41]:


# Path of the file to read
cancer_filepath = r"C:\Users\slmnp\Downloads\cancer.csv"


# In[42]:


# read the CSV file into a pandas DataFrame
cancer_data = pd.read_csv(cancer_filepath, index_col="Concavity (worst)", parse_dates=True)


# In[43]:


# Print the first 5 rows of the data
cancer_data.head()


# In[47]:


# Set the width and height of the figure
plt.figure(figsize=(16,6))

# Line chart showing how cancer rise over time 
sns.lineplot(data=fifa_data)


# In[ ]:




