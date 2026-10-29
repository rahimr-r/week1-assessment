#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Week 1 Assessment - City Analysis")


# 
# # Week 1 Assessment: City Analysis
# 
# ## 1. Introduction
# 
# This notebook analyzes employee data from `data/cities.csv`.
# 
# ## 2. Objectives
# 
# - Load employee data using Pandas.
# - Find employees by city.
# - Calculate salary statistics.
# - Measure execution time using `%timeit`.
# - Summarize the findings.
# 

# In[4]:


import pandas as pd
from pathlib import Path

data_path = Path("data/cities.csv")
print("File exists:", data_path.exists())

df = pd.read_csv(data_path)
df


# In[5]:


print("Total rows:", len(df))
print("Total columns:", len(df.columns))

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())


# In[6]:


chennai_employees = df[df["city"] == "Chennai"]

print("Employees in Chennai:", len(chennai_employees))
chennai_employees


# In[7]:


print("Average salary:", df["salary"].mean())
print("Highest salary:", df["salary"].max())
print("Lowest salary:", df["salary"].min())

print("\nAverage salary by city:")
print(
    df.groupby("city")["salary"]
    .mean()
    .sort_values(ascending=False)
)


# In[8]:


get_ipython().run_line_magic('timeit', 'df.groupby("city")["salary"].mean()')


# 
# # Week 1 Assessment: City Analysis
# 
# ## 1. Introduction
# 
# This notebook analyzes employee data from `data/cities.csv`.
# 
# ## 2. Objectives
# 
# - Load employee data using Pandas.
# - Find employees by city.
# - Calculate salary statistics.
# - Measure execution time using `%timeit`.
# - Summarize the findings.
# 
# ## 3. Conclusion
# 
# The dataset contains 8 employees and 4 columns.
# Bangalore has the highest average salary.
# Mumbai has the lowest average salary.
# Three employees are from Chennai.
# The overall average salary is 39000.
# 

# In[ ]:




