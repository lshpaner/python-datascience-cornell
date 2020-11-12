#!/usr/bin/env python
# coding: utf-8

# ## Dealing with Missing Data
# 
# Missing data is a common fact of life in data science.  We will explore here some tools for identifying and dealing with missing data.
# 
# In the code cell below, we'll import pandas and then read a csv file with daily climate data in Ithaca, NY during the month of January 2018.  Execute the next code cell, which will display the dataframe after reading it in.

# In[1]:


import pandas as pd
df = pd.read_csv('IthacaDailyClimateJan2018.csv', parse_dates=['Date'])
df


# ### Step 1.
# 
# To examine the summary information of the dataframe using the <code>info</code> method, execute the code cell below. You should note that different columns have different numbers of missing entries.  Pandas uses the word "null" to refer to missing data, such that a "non-null" entry is one that is not missing.

# In[2]:


df.info()


# ### Step 2.
# 
# Even though data are missing, pandas is able to compute a variety of useful things from the data that are present.  In the code cell below, enter and execute an expression to compute the mean of each column of the dataframe, storing the result in a variable named ```meanvals```, and then print those mean values.

# ## Graded Cell
# 
# This cell is worth 35% of the grade for this assignment.

# In[3]:


meanvals = df.mean()


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[4]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testMean

try:
    print(testMean(meanvals))    
except Exception as e:
    print("Error!\n" + str(e))
    


# ### Step 3.
# 
# A pandas dataframe has a method ```isnull``` that returns a new dataframe that is the shape of the original dataframe, but contains only boolean values, such that an entry is ```True``` if the corresponding entry in the original is missing (is null) and ```False``` if the corresponding entry is present (is not null).  Pandas dataframes also have a method ```notnull``` that reverses the logic of the ```isnull``` test.
# 
# In the code cell below, execute a call to ```df.isnull()``` and examine the output.  You should observe that the resulting dataframe mostly contains ```False```, but is ```True``` wherever ```df``` has a missing entry.

# In[5]:


df.isnull()


# ### Step 4.
# 
# From the summary information we printed above, we could try to estimate how many missing entries each column has, by subtracting the number of non-null entries from the total.  But even easier is just to compute that, using the output from ```df.isnull()```.  Even though that dataframe is composed of entries that are either ```True``` or ```False```, it is useful to recall that in Python, ```True``` has value equal to 1, and ```False``` has value equal to 0.  Therefore, to count the number of missing entries in each column, all we need to do is sum up each column of the dataframe returned by the command ```df.isnull()```; each instance of missing data (```True```) will add one count to the sum.  You have previously been instructed how to sum up a dataframe over all rows for each column by calling the ```sum``` method with the appropriate axis parameter.
# 
# In the code cell below, write an expression that computes the number of missing entries in each column, and assign the result to the variable ```num_missing```.  Print out ```num_missing``` to see the counts in each column.

# ## Graded Cell
# 
# This cell is worth 35% of the grade for this assignment.

# In[6]:


num_missing = df.isnull().sum()
print(num_missing)


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[7]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testNumMissing

try:
    print(testNumMissing(num_missing))    
except Exception as e:
    print("Error!\n" + str(e))
    


# ### Step 5.
# 
# Having computed above how many entries are missing in each column, maybe you want to know how many entries are missing in all (i.e., over columns).  Write an expression to compute the total number of missing entries in the entire dataframe ```df```, and store the result in the variable ```total_missing```.  (Hint: you can append one more function call to the code that you wrote in the previous step to sum up the counts over all columns.)  Print the value of ```total_missing```.

# In[8]:


total_missing = df.isnull().sum().sum()
print(total_missing)


# ### Step 6.
# 
# While we can compute some things even with missing data, we might be interested in trying to estimate values for those missing entries, or in filling out the dataframe for an analysis that requires that all data be available. If you do intend to fill in missing data, you'll want to think carefully about the best approach to that, based on your particular dataset and the questions you are interested in.  Different methods can produce substantially different estimates, as demonstrated below.
# 
# One approach would be to use the ```fillna``` method on a dataframe to fill in missing data in each column.  We might decide that where we have missing data, we can replace it by the mean value of all the present data in that column.  
# 
# In the code cell below, fill each missing entry according to the column mean, and assign the result to the variable ```df1```.  In other words, all missing entries in a given column should be assigned to the mean value of the data that are present in that column.  (Hint, you can use ```df.mean()``` to compute the mean value of each column, and use that result as input to fill in the missing data.)

# In[9]:


df1 = df.fillna(df.mean())


# ### Step 7.
# 
# The ```fillna``` method used above assigns each missing entry to the same value per column.  Since our climate data occur as a time series (from the beginning to the end of the month), it might be more reasonable to try to fill in data based upon nearby dates, rather than assigning it to the mean over the entire month.  Since temperatures and snowfalls are more likely to be correlated over nearby days, this might be a better approach to filling in the data.
# 
# Fortunately, pandas provides a method for *interpolating* data based on nearby values: a linear interpolation, for example, assigns to a missing entry the average value of the entries before and after it.  Additional information about interpolation is provided [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html).
# 
# In the code cell below, use the ```interpolate``` method on the climate dataframe, and the ```'linear'``` method for interpolation, assigning the result to the variable ```df2```.

# In[10]:


df2 = df.interpolate(method = 'linear')


# ### Step 8.
# 
# Compute the difference between ```df1``` and ```df2```, and assign the result to the variable ```diff12``` (Hint: Use an arithmetic operator to find the difference).  Examine the contents of ```diff12```.  You should note that ```diff12``` has value 0 everywhere that ```df``` had data present, since no estimates were required to fill in those entries.  For those entries with missing data, the two methods of estimation can vary considerably.

# ## Graded Cell
# 
# This cell is worth 30% of the grade for this assignment.

# In[11]:


diff12 = df1 - df2


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[12]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testDifference

try:
    print(testDifference(diff12))    
except Exception as e:
    print("Error!\n" + str(e))
    

