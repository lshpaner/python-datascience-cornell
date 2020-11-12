#!/usr/bin/env python
# coding: utf-8

# ## Reading Tables from a Relational Database

# Relational databases can hold multiple data tables, and are often used when those tables are related to each other through the use of shared keys.  Many relational databases support queries in SQL, the "Structured Query Language", to extract data based on criteria of interest.  The SQLAlchemy package in Python enables one to connect to a SQL database and extract data based on SQL queries into Pandas DataFrames.
# 
# Let's start with a couple imports &mdash; execute the code cell below.

# In[1]:


from sqlalchemy import create_engine
import pandas as pd


# ### Step 1.
# 
# You will be working with a sqlite database named "product_data.sqlite". sqlite is a relational database management system that support SQL databases in files, as opposed to residing on a separate database server somewhere.
# 
# Execute the code cell below. It contains an expression that creates a sqlalchemy engine object by connecting to the "product_data.sqlite" database, and assigns that object to variable `engine`.

# In[2]:


engine = create_engine('sqlite:///product_data.sqlite')


# ### Step 2.
# 
# Since a relational database can hold multiple tables, it's useful to be able to determine what tables are contained in a database.  The engine object you created has a method called ```table_names``` that returns a list of table names.  Use this method to assign the list of table names to the variable ```tables```, and print the value of ```tables```.

# ## Graded Cell
# 
# This cell is worth 30% of the grade for this assignment.

# In[3]:


tables = engine.table_names()


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[4]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testTables

try:
    print(testTables(tables))    
except Exception as e:
    print("Error!\n" + str(e))


# ### Step 3.
# 
# Following the examples shown in the video, in the code cell below, write and evaluate three statements to extract the sales, orders, and inventory tables from the databases, and assign each of those dataframes to an associated variable (named ```sales```, ```orders```, and ```inventory```, respectively).  Inspect each of the three dataframes, either by printing them out in the cell below, or adding additional code cells to inspect the contents of each dataframe individually.

# In[5]:


sales = pd.read_sql_query('SELECT * FROM sales',engine)
orders = pd.read_sql_query('SELECT * FROM orders',engine)
inventory = pd.read_sql_query('SELECT * FROM inventory',engine)


# ### Step 4.
# 
# Inspect the `inventory table`. You will see a column named `paper`. Imagine you want to know when your inventory of paper is too large, say, more than 700 reams.  In the code cell below, write and evaluate an expression to extract the rows in which the paper inventory is more than 700. Assign the database output to the variable ```too_much_paper```, and examine the extracted dataframe.
# 
# Hint: 
# If you are uncertain about how to write this query, take a moment to reflect on the example Professor Myers provided in the "Reading Tables From a Relational Database" video. In that video, Professor Myers used the following SQL query to illustrate one way you can refine a query to return very precise information from a database.
# 
# `low_inventory = pd.read_sql_query('SELECT * from inventory where (Pencils < 200) or (Pens < 200) or (Erasers < 50) or (Paper < 300)', engine)`
# 
# This query asks the `inventory` table to return all of its records where either the value in the `Pencils` column is less than 200 or the value in the `Pens` column is less than 200 or the value in the `Erasers` column is less than 50 or the value in the `Paper` column is less than 300.
# 
# In fact, the sample query above gives you more than you need to achieve the goal of this assignement. Because you are asked to return rows where `Paper` is greater than 700, you won't need all of the additional `or` statements that check the values in other columns.

# ## Graded Cell
# 
# This cell is worth 35% of the grade for this assignment.

# In[6]:


too_much_paper = pd.read_sql_query('SELECT * FROM inventory where Paper > 700',engine)


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[7]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testPaper

try:
    print(testPaper(too_much_paper))    
except Exception as e:
    print("Error!\n" + str(e))


# ### Step 5.
# 
# SQL queries provide a wide range of functionalities.  For example, you can numerically sort the rows in the output with the keywords ```order by```.  Imagine you have a SQL query like 'select [MAIN QUERY]' where MAIN_QUERY reflects whatever you're extracting from the database; you can tack on to the end of a SQL query string additional query details of the form:
# 
# * 'select [MAIN QUERY] order by COLUMN_NAME' : to sort the output based on the specified COLUMN_NAME in ascending order (default)
# 
# * 'select [MAIN QUERY] order by COLUMN_NAME desc' : to sort the output based on the specified COLUMN_NAME in descending order
# 
# In the code cell below, write and evaluate an expression to extract all the sales data (using the 'select * from sales' query you've used previously), sorted in descending order by the Paper sales in each month.  Assign the result to the variable ```top_paper_sales``` and inspect the dataframe.

# ## Graded Cell
# 
# This cell is worth 35% of the grade for this assignment.

# In[8]:


top_paper_sales = pd.read_sql_query('SELECT * FROM sales order by Paper desc',engine)


# ## Self-Check
# 
# Run the cell below to test the correctness of your code above before submitting for grading.

# In[9]:


# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testPaperSales

try:
    print(testPaperSales(top_paper_sales))    
except Exception as e:
    print("Error!\n" + str(e))


# ### Step 6.
# 
# An overview of SQL queries is outside the scope of this course, but if you are familiar with SQL, feel free to experiment some more to extract data from our product database.
