#!/usr/bin/env python
# coding: utf-8

# ## Analyzing the World Happiness Data
# 
# 
# ### Preparing the data for analysis

# In this exercise, we will do some initial data imports and preprocessing to get the data ready for further analysis.  We will repeat these same basic steps in subsequent exercises.  Begin by executing the code cell below to import some necessary packages.  Note that the last line in the code cell below is intended to instruct pandas to display floating point numbers to 2 decimal places (`.2f`).  This is just one of many pandas display options that can be configured, as described [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html).

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.display.float_format = '{:.2f}'.format


# ### Step 1
# 
# Create a Pandas dataframe named ```dfraw``` by reading in the data in the worksheet named "Table2.1" from the spreadsheet "WHR2018Chapter2OnlineData.xls".

# In[2]:


dfraw = pd.read_excel('WHR2018Chapter2OnlineData.xls', sheet_name='Table2.1')


# To facilitate working with the data, it will be useful to select a subset of the data from the full dataset and to rename the columns to make them less verbose.  In the code cell below, the variable ```cols_to_include``` contains a list of column names to extract.
# Execute the cell. 

# In[3]:


cols_to_include = ['country', 'year', 'Life Ladder', 
                   'Positive affect','Negative affect',
                   'Log GDP per capita', 'Social support',
                   'Healthy life expectancy at birth', 
                   'Freedom to make life choices', 
                   'Generosity', 'Perceptions of corruption']


# ### Step 2
# 
# Using the variables defined above, in the code cell below, write and evaluate an expression to create a new dataframe named `df` that includes the subset of data in `cols_to_include`.

# ## Graded Cell
# 
# This cell is worth 100% of the grade for this assignment.

# In[4]:


df = dfraw[cols_to_include]


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[5]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testDf

try:
    print(testDf(df, dfraw))    
except Exception as e:
    print("Error!\n" + str(e))


# ### Step 3.
# 
# Take a peek at the head of the new dataframe.

# In[6]:


df.head()

