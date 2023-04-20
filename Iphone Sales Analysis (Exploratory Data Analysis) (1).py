#!/usr/bin/env python
# coding: utf-8

# # Import Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# # Import Dataset

# In[20]:


df = pd.read_csv("apple_products.csv")
df


# # Exploratory Data Analysis

# In[21]:


df.head()


# # Data Shape

# In[22]:


df.shape


# Rows are 62 and columns are 11

# # Describe Data Statistics

# In[23]:


df.describe()


# # Check Data Types

# In[24]:


# df.dtypes
df.info()


# # Check For Null Values

# In[25]:


df.isna().sum()


# - There is no any null value in dataset

# # Check for unique values

# In[26]:


# unique values in each column
df.nunique()


# In[27]:


df['Brand'].unique()


# In[28]:


df['Star Rating'].unique()


# In[29]:


df['Ram'].unique()


# In[30]:


b= sns.PairGrid(df)
b.map(plt.scatter)


# In[31]:


df.corr()


# In[32]:


sns.heatmap(df.corr())


# In[33]:


sns.pairplot(df)


# # Iphone sales analysis in India

# Creating a dataframe by storing all the data about the top 10 hightest-rated iPhones in india on Flipcart. It will help in 
# understanding what kind of iPhones are liked the most in India.
# 

# In[34]:


high_rated = df.sort_values(by=["Star Rating"],ascending= False)
high_rated = high_rated.head(10)
print(high_rated["Product Name"])


# Top 5 most liked iPhones in India
# 1. APPLE iPhone 11 Pro Max (Midnight Green, 64 GB)
# 2. APPLE iPhone 11 Pro Max (Space Grey, 64 GB)
# 3. APPLE iPhone 11 Pro Max (Midnight Green, 256 GB)
# 4. APPLE iPhone 11 Pro Max (Gold, 64 GB)
# 5. APPLE iPhone 11 Pro Max (Gold, 256 GB)

# # Number of rating of the hightest-rated iPhones on Flipcart:

# In[35]:


iphones = high_rated["Product Name"].value_counts()
label= iphones.index
counts = high_rated["Number Of Ratings"]
fig = px.bar(high_rated,x= label,y=counts,title="Number of rating of Hightest Rated iPhones")
fig.show()


# APPLE iPhone 8 plus (Gold,64 GB) has the most rating on Flipcart.

# In[36]:


iphones = high_rated["Product Name"].value_counts()
label= iphones.index
counts = high_rated["Number Of Reviews"]
fig = px.bar(high_rated,y= 'Product Name', x='Number Of Reviews',title="Number of Reviews of Highest Rated iPhones")
fig.show()

#plt.xlabel('iphone.index')
#plt.ylabel('Number of Reviews')
#plt.title('Number of Reviews of Highest Rated iPhones')
#plt.hist(high_rated,rwidth=2.5,orientation='vertical')


# APPLE iPhone 8 Plus(Gold,64 GB) is also leading in the highest number of reviews on Flipcart among the highest-rated iPhones in 
# India

# # Relationship betweeen the sale price of iPhones and their rating on Flipcart

# In[37]:


fig = px.scatter(data_frame=df, x= 'Number Of Ratings', y ='Sale Price',size='Discount Percentage',title='Relationship between Sale Price and Number of Rating')
fig.show()


# There is a negative relationship between the sale price of iPhones and the number of ratings.It means iPhones with lower sale price are sold more in India.

# # Relationship between the discount percentage on iPhones on Flipcart and the number of ratings

# In[38]:


sns.relplot( x ='Number Of Reviews', y = 'Discount Percentage', data = df,hue='Sale Price')


# There is a linear relationship between the discount percentage on iPhones on Flipcart and the number of ratings. It means iPhones with high discounts are sold more in India.

# # Conclusion

# 1. APPLE iPhone 8 plus (Gold, 64 GB) was the most appreciated iphone in India.
# 2. iPhones with lower sale prices are sold more in India.
# 3. iPhones with high discounts are sold more in India.

# In[ ]:




