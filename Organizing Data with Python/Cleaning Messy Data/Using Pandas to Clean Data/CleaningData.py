#!/usr/bin/env python
# coding: utf-8

# ## Cleaning up Data
# 
# Sometimes data comes to us in a form that requires some cleaning before we can begin with further analyses.  In this exercise we will explore some tools and strategies for that.
# 
# We'll begin by reading in a modified version of the Ithaca climate dataset that we worked with previously.  You should notice that there is a new column in the dataframe, indicating the prevailing Sky conditions for each day (sunny, cloudy, etc.).
# 
# Execute the code cell below.

# In[1]:


import pandas as pd

df = pd.read_csv('IthacaDailyClimateJan2018expanded.csv')
df.info()


# Let's look at the dataframe in its entirety.  Execute the code cell below.

# In[2]:


df


# ### Step 1.
# 
# Let's examine the column names in a bit more detail.  Execute the code cell below.

# In[3]:


df.columns


# Notice that there are three different temperature columns, but the naming conventions differ for all three: "Max T", "Minimum Temp", and "Average Temperature".  This can lead to confusion because you need to keep track in your mind how temperature is labeled in each column name (T, Temp, Temperature).  Furthermore, the largest temperature is labeled with the shorthand "Max", while the smallest temperature is labeled with the full word "Minimum".  While we are free to choose whatever names we want for our data (within any syntactic rules), it is useful &mdash; for both you the developer and for anyone else who might be using the code &mdash; to establish some uniformity and consistency in naming.  Fortunately, we don't need to go back and modify the original csv file; we can just modify the column names in our code.
# 
# In the code cell below, use the ```rename``` method on a dataframe to rename the columns as follows:
# 
# * rename 'Max T' to be 'Maximum Temperature'
# * rename 'Minimum Temp' to be 'Minimum Temperature'
# 
# Consult the [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) for ```df.rename``` and find an example to "Rename columns using a mapping", which will demonstrate how to pass a dictionary to the method in order to change the column names. Hint: each element in the dictionary is a key/value pair in which the key is the original name and the value is the new name. For example: {original_name: new_name}.
# 
# Note that the ```rename``` method will, by default, return a new dataframe with the modified names.  You can either assign that new dataframe to a variable (you can even just reassign it to the name ```df```) or you can use the ```inplace=True``` option to modify ```df``` directly. 
# 
# For this exercise, you will use the ```inplace=True``` option in the `rename` method to modify ```df``` directly. After you've done the renaming, inspect the column names of the dataframe to verify that you've changed the names as intended (and if necessary, modify your renaming code until the column names are as desired.)

# ## Graded Cell
# 
# This cell is worth 50% of the grade for this assignment.

# In[4]:


df.rename(columns={'Max T':'Maximum Temperature','Minimum Temp': 'Minimum Temperature'},inplace=True )
print(df)


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[5]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testChangeNameMax, testChangeNameMin

try:
    print(testChangeNameMax(df))    
except Exception as e:
    print("Error!\n" + str(e))
    
try:
    print(testChangeNameMin(df))    
except Exception as e:
    print("Error!\n" + str(e))


# Execute the cell below and inspect the column names of the dataframe. 

# In[6]:


df.columns


# ### Step 2.
# 
# Let's examine the new data in the 'Sky' column.  The entries here are strings representing categorical data, such as "sunny", "partly sunny", "cloudy" and "partly cloudy".  Because they are text-based, it is often useful to verify that there are no mispellings or spelling variants.  A useful method on a Series, or on a column extracted from a DataFrame, is ```unique```, which returns an array of unique entries in that Series or column.
# 
# In the code cell below, write and evaluate an expression to extract the unique entries of the 'Sky' column of the dataframe.

# In[7]:


df['Sky'].unique()


# While it might not have been obvious when looking at the entire dataframe, extracting the group of unique entries in the 'Sky' column makes it obvious that there are some misspellings and other textual problems, such as an extra space at the beginning of ' partly cloudy'.
# 
# Pandas dataframes have a ```replace``` method that allows you to change values in a dataframe according to a specified rule, as described [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html).  If you want to replace text entries (strings), you either need to provide the full string to replace, or use the ```regex=True``` option to specify a regular expression (regex) for replacing part of a string.  In this exercise, let's just specify fully the strings we want to replace.  Note that the ```replace``` method is for changing values in the body of the dataframe, whereas the ```rename``` method used above is for changing the names of the index or column labels.  When called on an entire dataframe, the ```replace``` method will replace all instances of the specified text, regardless of what column it is in.  (If you wanted to replace values only in a particular column, you would first extract that column before doing the replacement.)
# 
# In the code cell below, write and evaluate code to replace all the misspelled entries in the dataframe with their corrected versions.  The easiest way to do this is to provide all the corrections in a dictionary which is passed as an argument to the method.  Note that by default, the ```replace``` method will return a new dataframe, so you can either assign it to a variable, or modify the original dataframe in place by using the `inplace=True` option.
# 
# For this exercise, you will modify `df` in place by using the `inplace=True` option.
# 

# ## Graded Cell
# 
# This cell is worth 50% of the grade for this assignment.

# In[8]:


df.replace({'party sunny':'partly sunny', 'couldy': 'cloudy', ' partly cloudy':'partly cloudy'},inplace=True)


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[9]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testChangePartlySunny, testChangeCloudy, testChangePartlyCloudy

try:
    print(testChangePartlySunny(df))    
except Exception as e:
    print("Error!\n" + str(e))
    
try:
    print(testChangeCloudy(df))    
except Exception as e:
    print("Error!\n" + str(e))
    
try:
    print(testChangePartlyCloudy(df))    
except Exception as e:
    print("Error!\n" + str(e))
    


# After doing the text replacement, re-examine the unique entries of the 'Sky' column to verify that you have corrected the problems with the original data.  (There should be 5 unique entries.)  If you have not fixed all the problems, modify your replacement code above and continue until the data are corrected.

# In[10]:


df['Sky'].unique()

