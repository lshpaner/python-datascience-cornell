#!/usr/bin/env python
# coding: utf-8

# # DataFrame indexing

# DataFrames are two-dimensional tables, labeled by row and column names, containing of a set of column-oriented data such that each column has a particular datatype (dtype).  Indexing and slicing are the processes of accessing subsets of data in a container by specifying which element(s) one is interested in.  Python lists and numpy arrays are indexed by integer position (e.g., ```my_list[3]``` or ```my_array[5,7]```), while Python dictionaries are indexed by keys (e.g., ```my_dict['name']```).  Because pandas DataFrames contain data in a positional order, *and* have row and column labels, they can be indexed both by position and by a label name.
# 
# In this exercise we will explore indexing and slicing in DataFrames.  In addition to getting more experience working with Jupyter notebooks, we can also make use of the some of the nice ways that Jupyter facilities working with DataFrames.
# 
# Online Pandas documentation describing indexing in great detail can be found [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html).

# ### Step 1.
# 
# Write some code in the first empty cell below to:
# 
# * import the pandas module (using the conventional shorthand renaming)
# * read the pizza excel spreadsheet ("PizzaSheet.xlsx") into a dataframe named ```dfp```
# * read the climate csv file ("IthacaDailyClimate2018.csv") into a dataframe named ```dfc```
# 
# Once you've done so, execute the cell and inspect the two dataframes using the ```info``` and ```head``` methods to see that they loaded correctly, and to remind yourself what the dataframes consist of.  Feel free to add additional code cells if you want to be able to more easily inspect the output of each command as it is run.

# In[1]:


import pandas as pd

dfp = pd.read_excel('PizzaSheet.xlsx')
dfc = pd.read_csv('IthacaDailyClimate2018.csv')

dfc.info()
dfc.head()


# ### Mechanisms for indexing
# 
# Indexing with dataframes can be done through various mechanisms: 
# 
# * ```[]```
# * ```loc[]```
# * ```iloc[]```
# 
# The first of these, ```[]```, is the square-bracket based indexing that we are familiar with from Python lists, Python dictionaries, and numpy arrays.  Because pandas dataframes are generally column-oriented, however, indexing with square brackets results in selecting a particular column based on its label.  We can loosely think of a dataframe as something like a dictionary of Series objects: each column label is like a key, and the value associated with that key is the data in that particular column, which is a pandas Series.  For example, ```dfc['Precipitation']``` will extract the column labeled 'Precipitation' and will return a Series (like a 1D numpy array).
# 
# It's easiest to see this with some examples.

# ### Step 2.
# 
# Write and execute some code in the cell below to:
# 
# * extract the 'Size' column from the dfp dataframe using square brackets, and assign it to the variable ```sizes```
# 
# Print the new Series variable you have created.  This Series has the same index as the dfp dataframe (the integers 0 through 6 inclusive, which pandas encodes as a ```RangeIndex(start=0, stop=7, step=1)```, similar to the ```range``` objects found in Python).  Print the type of and the index of ```sizes``` to convince yourself that it is a Series object with that RangeIndex.

# In[2]:


sizes = dfp['Size']
print(sizes)


# ### Step 3.
# 
# We're not interested just in extracting data, but in computing with the extracted data.  As we've seen, Both Series and DataFrames have methods to compute summary mathematical operations such as ```sum```, ```min```, ```max```, and ```mean```.
# 
# In the code cell below, write an expression to compute the mean price of pizzas sold by our pizzeria, and assign that value to the variable ```mean_price```.  (Hint: you can do this in one line by chaining method calls; you don't need to create a separate variable to store the price data first.)

# ## Graded Cell
# 
# This cell is worth 20% of the grade for this assignment.

# In[3]:


mean_price = dfp.mean()
print(mean_price)


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[4]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testMeanPrice

try:  
    print(testMeanPrice(mean_price))
except Exception as e:
    print("Error!\n" + str(e))
    


# ### Step 4.
# 
# We can use the same square-bracket based indexing to extract multiple columns from a dataframe.  In this case, we need to group the column labels of interest in a Python list.  If a dataframe df has columns named 'A', 'B', 'C', 'D', 'E', and we want to extract just columns 'B' and 'E', that could be accomplished with the expression ```df[['B','E']]```, i.e., we can index based on the list of columns ```['B','E']```.  In the cell below, write some code to extract both the columns 'Topping #1' and 'Topping #2' from dfp, and store the result in the variable ```top2```.

# In[5]:


top2 = dfp[['Topping #1', 'Topping #2']]
print(top2)


# ### Indexing using loc
# 
# Indexing of a dataframe using ```loc``` is more general, in that it enables to access both rows and columns based on label names.  It uses the same sort of multi-dimensional indexing that is used for numpy arrays, although with row and/or column labels rather than integer positional indexes.  By this we mean that the first entry in an index refers to row labels, and the second index refers to column labels.  If only one entry is specified, it is used to identify a row in a dataframe.
# 
# Slicing is also supported using the colon ```:```, just as with Python lists and numpy arrays.  Unlike those other slicing operations, however, slicing a pandas dataframes includes data at the stop location.

# ### Step 5.
# 
# Using the ```loc``` method, write code in the cell below to:
# 
# * extract the "Base" column from ```dfp``` for all pizzas sold, and assign that to the variable ```bases```
# * print ```bases```

# In[6]:


bases = dfp.loc[:,'Base']
print(bases)


# ### Step 6.
# 
# Using the ```loc``` method, write code in the cell below to:
# 
# * extract the data from all of the Toppings columns in ```dfp``` for all pizzas sold, by slicing from "Topping #1" through "Topping #5", and assign that to the variable ```toppings```
# * print ```toppings```

# In[7]:


toppings = dfp.loc[:,'Topping #1':'Topping #5']
print(toppings)


# Instead of *printing* toppings, simply evaluate it instead in the empty code cell below (by executing the statement ```toppings```).  You should notice that the rendering of the dataframe in the notebook is fancier than what printing provides, and that there is an ```Out[]``` statement that represents the dataframe ```toppings```.

# In[8]:


toppings


# ### Step 7.
# 
# The ```count``` method on a DataFrame or Series counts the number of non-missing (non-empty) entries in each column.
# 
# Write a statement using the count method that computes the number of pizzas with 5 toppings (i.e., the number of pizzas for which the entry in "Topping #5" is not empty), and assign it to the variable ```num5```.  (There are a couple ways you can do this: (1) you can first extract the "Topping #5" column from the dataframe as a Series, and then compute the count, or (2) you can compute the counts for the entire dataframe, and then extract the count for "Topping #5".)

# ## Graded Cell
# 
# This cell is worth 60% of the grade for this assignment.

# In[9]:


num5 = dfp.loc[:,'Topping #5'].count()
print(num5)


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[10]:


# Run this self-test cell to check your code; do not add code or delete code in this cell

from jn import testNumPizzas

try:  
    print(testNumPizzas(num5, dfp))
except Exception as e:
    print("Error!\n" + str(e))
    


# ### Selecting data subsets based on a condition
# 
# Subsets of data can also be extracted from a DataFrame or Series based on some sort of logical condition, similar to how it is supported with numpy arrays.  A logical comparison can be made to produce a DataFrame or Series consisting of boolean values (either True or False, depending on whether the condition being tested is met or not), and indexing on those boolean values extracts only those entries that are True (i.e., that satisfy the comparison).
# 
# For example, if we wanted to extract only those rows in the pizza dataframe corresponding to Large pizzas, we could write:
# 
# ```
# larges = dfp.loc[dfp['Size'] == 'L']
# ```
# 

# ### Step 8.
# 
# In addition to the pizza dataframe, you also loaded the climate dataframe at the top of this exercise.  Let's say you wanted to know how many days during 2018 the temperature in Ithaca, NY reached at least 70 degrees Fahrenheit sometime during the day.
# 
# * In the code cell below, write an expression to extract a new dataframe containing those days where the temperature reached at least 70 degrees, and assign that to the variable ```at_least_70```.  (You might need to think some about what the different columns in the full dataframe represent to decide how to extract the subset of interest.)
# * After that, write another expression that computes how many days reached at least 70 degrees, and assign that to the variable ```num_at_least_70```.

# ## Graded Cell
# 
# This cell is worth 20% of the grade for this assignment.

# In[11]:


at_least_70 = dfc.loc[dfc["Maximum Temperature"] >= 70]
num_at_least_70 = at_least_70.shape[0]


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[12]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import test70DegreeDays
try:  
    print(test70DegreeDays(at_least_70, num_at_least_70, dfc))
except Exception as e:
    print("Error!\n" + str(e))
   

