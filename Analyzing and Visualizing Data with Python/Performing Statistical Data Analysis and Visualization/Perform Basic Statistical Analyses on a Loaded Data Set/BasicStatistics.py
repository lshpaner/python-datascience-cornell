#!/usr/bin/env python
# coding: utf-8

# ## Analyzing the World Happiness Data
# 
# ### Computing summary statistics
# 

# In this exercise, we will use pandas to compute some summary statistics of the WHR data.
# 
# We'll repeat here some of the code developed in a previous exercise so that we can continue to work with data in this exercise.  Execute the following code cells to load and reconfigure the data.

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.display.float_format = '{:.2f}'.format


# In[2]:


dfraw = pd.read_excel('WHR2018Chapter2OnlineData.xls', sheet_name='Table2.1')


# In[3]:


cols_to_include = ['country', 'year', 'Life Ladder', 
                   'Positive affect','Negative affect',
                   'Log GDP per capita', 'Social support',
                   'Healthy life expectancy at birth', 
                   'Freedom to make life choices', 
                   'Generosity', 'Perceptions of corruption']

df = dfraw[cols_to_include]


# ### Step 1
# 
# In the code cell below, call the ```info``` method on the dataframe ```df``` to remind yourself what the dataframe consists of.

# In[4]:


df.info()


# ### Step 2
# 
# The ```describe``` method on a dataframe provides a useful statistical summary of the data.  In the code cell below, enter an expression to call this method and examine the output.

# In[5]:


df.describe()


# Let's look at the output above and compare it with data presented in Table 4 of [Appendix 1 of the 2018 World Happiness Report](https://s3.amazonaws.com/happiness-report/2018/Appendix1ofChapter2.pdf).  Here is Table 4 reproduced from that report:
# 
# <img src='appendix4.png' width=650 height=650 align="left"/>

# Imagine that you were asked to produce a table of this form from the underlying data.  Let's see what is required to get our summary data to resemble Table 4.

# ### Step 3.
# 
# The first thing you'll notice is that the orientation of the table is different from that produced by ```df.describe```, with data categories listed in rows and summary statistics in the columns.  One easy way to reorient the data produced by ```describe``` is to look at the <i>transpose</i> of the data, that is, what one gets when rows and columns are swapped.
# 
# The transpose of a dataframe can be accessed simply by accessing the attribute named ```.T``` on the dataframe.  Note that ```T``` is not a method that is called, so it is not followed by parentheses.  Instead, it is a static attribute of the dataframe that can be accessed through that name.
# 
# In the code cell below, write and evaluate an expression to return the transpose of the summary description provided by ```describe```.

# In[6]:


df.T


# ### Step 4.
# 
# This is looking a bit more like Table 4, although there is some extraneous information that we can remove using the ```drop``` method on a dataframe.  We can also rename the quantities produced by ```df.describe``` to make them appear as in Table 4.
# 
# Examine the documentation for ```df.drop``` and note that one can specify one or more labels to drop, as well as an axis along which to drop.  For our summary data, we'd like to drop the row labeled 'year' and the columns labeled by '25%', '50%', and '75%', since they are not included in Table 4.
# 
# In the code cell below, we define a dictionary for the column renaming, and a list defining the column order for the finished table.  In the empty code cell below that, write and evaluate code to do the following:
# 
# * From the transposed summary data, drop the row labeled 'year'.
# * From the resulting dataframe, drop the columns labeled '25%', '50%', and '75%'.
# * Using the `rename` method on the resulting dataframe, rename the columns according to the mapping defined in ```column_renaming```. 
# * Select out the columns in the list defined by ```column_order``` and assign the resulting dataframe to the variable ```dfsummary```.
# 
# Note that you can either do each step above sequentially, storing the result in a variable, or you can string each call one right after the other in one line (by chaining a series of method calls).
# 
# Once you've assigned the result to ```dfsummary```, examine that new dataframe and compare it to Table 4.

# In[7]:


column_renaming = {'count': 'N', 'mean': 'Mean', 'std': 'Std. Dev.', 'min': 'Min.', 'max': 'Max.'}
column_order = ['Mean', 'Std. Dev.', 'Min.', 'Max.', 'N']


# In[8]:


dfsummary = df.drop(columns = ['year'])
dfsummary = dfsummary.describe().T.drop(columns = ['25%','50%', '75%']).rename(columns = column_renaming)
dfsummary = dfsummary[column_order]
dfsummary


# ### Step 5
# 
# You may notice that one lingering point of discrepancy between the summary dataframe you've produced and the WHR Table 4 is that the number of counts ```N``` in Table 4 is reported as an integer, whereas it is a floating point number in our summary dataframe.  We can alter the type of that column with the code in the following cell.  Execute the code cell below.

# In[9]:


dfsummary['N'] = dfsummary['N'].astype(int)
dfsummary


# ### Step 6
# 
# Appendix 1 of the WHR presents several tables similar to Table 4, for different intervals of years, in order to examine how the summary statistics have changed over time.  In the code cells above, we executed several steps to produce a summary dataframe of the desired form.  Since we will want to produce different summary tables for different intervals of years, we can bundle up all the data processing steps above into a new <b>function</b> that we can call, by passing in different dataframes as input to the function.  If we wanted to get summary statistics for just a subset of years, we could create a new dataframe by filtering the full dataset just for those years, and then pass the new dataframe to our function.
# 
# In the code cell below, write a <b>function</b> named ```produce_summary_table``` that takes a dataframe as an argument (i.e `produce_summary_table(df)`) and returns a <b>summary dataframe</b>. 
# 
# * The input <b>dataframe</b> should be derived from the WHR2018Chapter2OnlineData.xls Table 2.1 data we've been working with.
# 
# * The returned <b>summary dataframe</b> should be in the same form as Table 4 above. 
# 
# * In writing this function, you should include all of the steps we took in Steps 4 and 5 above to achieve the final result; you will also want to pull in the code above that defines the variables ```column_renaming``` and ```column_order```. 
# 
# 

# ## Graded Cell
# 
# This cell is worth 100% of the grade for this assignment.

# In[10]:


def produce_summary_table(df):
    cols_to_include = ['country', 'year', 'Life Ladder', 
                   'Positive affect','Negative affect',
                   'Log GDP per capita', 'Social support',
                   'Healthy life expectancy at birth', 
                   'Freedom to make life choices', 
                   'Generosity', 'Perceptions of corruption']

    df = df[cols_to_include]

    column_renaming = {'count': 'N', 'mean': 'Mean', 'std': 'Std. Dev.', 'min': 'Min.', 'max': 'Max.'}
    column_order = ['Mean', 'Std. Dev.', 'Min.', 'Max.', 'N']
    dfsummary = df.drop(columns = ['year'])
    dfsummary = dfsummary.describe().T.drop(columns = ['25%','50%', '75%']).rename(columns = column_renaming)
    dfsummary = dfsummary[column_order]
    dfsummary['N'] = dfsummary['N'].astype(int)
    return dfsummary
    


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[11]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testFunction

try:
    print(testFunction(produce_summary_table))    
except Exception as e:
    print("Error!\n" + str(e))
    


# Test your new function with the dataframe ```df``` that we were working with above.  It should return the summary table that mirrors Table 4.

# In[12]:


produce_summary_table(df)


# Appendix 1 of the WHR presents similar summary tables for different groups of years:
# 
# * 2005-2007: Table 5
# * 2008-2010: Table 6
# * 2015-2017: Table 7
# 
# To reproduce each of these tables, you will want to create a new dataframe that filters out the subset of the data in the specified years, as was discussed above in Step 6.  There are various ways to do this extraction.  One way is to use the ```isin``` method on a dataframe or series, which can be used to select those entries which are contained within a specified set of values.  For example, the expression ```df[df.year.isin(range(1900,2000))]``` would return a new dataframe containing all rows of ```df``` that had a year between 1900 and 1999.

# ### Step 7
# 
# In the empty code cell below, do the following:<br>
# Create three new dataframes for each of the year ranges associated with Tables 5, 6, and 7, by extracting the appropriate set of years. Using the function you wrote above, create a summary table for each dataframe (your function takes a dataframe as input). Assign the resulting summary tables to the names ```dfsummary0507```, ```dfsummary0810```, and ```dfsummary1517```. 
# <br>
# <br>
# The remaining three code cells below are populated with the table names ```dfsummary0507```, ```dfsummary0810```, and ```dfsummary1517```. Once you have created these summary tables as outlined above, execute these cells to compare your tables with the corresponding tables in WHR Appendix 1. 

# In[13]:


dfsummary0507 = produce_summary_table(df.loc[(df['year'] >= 2005) & (df['year'] <= 2007)])
dfsummary0810 = produce_summary_table(df.loc[(df['year'] >= 2008) & (df['year'] <= 2010)])
dfsummary1517 = produce_summary_table(df.loc[(df['year'] >= 2015) & (df['year'] <= 2017)])


# In[14]:


dfsummary0507


# In[15]:


dfsummary0810


# In[16]:


dfsummary1517

