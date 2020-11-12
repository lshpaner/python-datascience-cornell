
## Cleaning up Data

Sometimes data comes to us in a form that requires some cleaning before we can begin with further analyses.  In this exercise we will explore some tools and strategies for that.

We'll begin by reading in a modified version of the Ithaca climate dataset that we worked with previously.  You should notice that there is a new column in the dataframe, indicating the prevailing Sky conditions for each day (sunny, cloudy, etc.).

Execute the code cell below.


```python
import pandas as pd

df = pd.read_csv('IthacaDailyClimateJan2018expanded.csv')
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 31 entries, 0 to 30
    Data columns (total 8 columns):
     #   Column               Non-Null Count  Dtype  
    ---  ------               --------------  -----  
     0   Date                 31 non-null     object 
     1   Max T                30 non-null     float64
     2   Minimum Temp         28 non-null     float64
     3   Average Temperature  29 non-null     float64
     4   Precipitation        31 non-null     float64
     5   Snowfall             27 non-null     float64
     6   Snow Depth           29 non-null     float64
     7   Sky                  29 non-null     object 
    dtypes: float64(6), object(2)
    memory usage: 2.1+ KB


Let's look at the dataframe in its entirety.  Execute the code cell below.


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Max T</th>
      <th>Minimum Temp</th>
      <th>Average Temperature</th>
      <th>Precipitation</th>
      <th>Snowfall</th>
      <th>Snow Depth</th>
      <th>Sky</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-01-01</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>2.5</td>
      <td>0.04</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>cloudy</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-01-02</td>
      <td>13.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.03</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>partly cloudy</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-01-03</td>
      <td>19.0</td>
      <td>-2.0</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018-01-04</td>
      <td>22.0</td>
      <td>1.0</td>
      <td>11.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>partly sunny</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018-01-05</td>
      <td>18.0</td>
      <td>-2.0</td>
      <td>8.0</td>
      <td>0.09</td>
      <td>1.2</td>
      <td>4.0</td>
      <td>cloudy</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2018-01-06</td>
      <td>2.0</td>
      <td>-3.0</td>
      <td>-0.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>party sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018-01-07</td>
      <td>2.0</td>
      <td>-3.0</td>
      <td>-0.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>partly sunny</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2018-01-08</td>
      <td>24.0</td>
      <td>-3.0</td>
      <td>10.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2018-01-09</td>
      <td>37.0</td>
      <td>23.0</td>
      <td>30.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2018-01-10</td>
      <td>33.0</td>
      <td>15.0</td>
      <td>24.0</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2018-01-11</td>
      <td>41.0</td>
      <td>18.0</td>
      <td>29.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2018-01-12</td>
      <td>57.0</td>
      <td>40.0</td>
      <td>48.5</td>
      <td>0.76</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2018-01-13</td>
      <td>62.0</td>
      <td>12.0</td>
      <td>37.0</td>
      <td>0.94</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>couldy</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2018-01-14</td>
      <td>12.0</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>0.06</td>
      <td>0.9</td>
      <td>6.0</td>
      <td>partly cloudy</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2018-01-15</td>
      <td>12.0</td>
      <td>-9.0</td>
      <td>1.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>partly sunny</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2018-01-16</td>
      <td>22.0</td>
      <td>NaN</td>
      <td>6.5</td>
      <td>0.05</td>
      <td>0.5</td>
      <td>6.0</td>
      <td>cloudy</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2018-01-17</td>
      <td>26.0</td>
      <td>15.0</td>
      <td>20.5</td>
      <td>0.13</td>
      <td>1.6</td>
      <td>8.0</td>
      <td>cloudy</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2018-01-18</td>
      <td>20.0</td>
      <td>-1.0</td>
      <td>9.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2018-01-19</td>
      <td>22.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2018-01-20</td>
      <td>37.0</td>
      <td>8.0</td>
      <td>22.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2018-01-21</td>
      <td>45.0</td>
      <td>16.0</td>
      <td>30.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>partly sunny</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2018-01-22</td>
      <td>NaN</td>
      <td>19.0</td>
      <td>30.5</td>
      <td>0.02</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>partly cloudy</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2018-01-23</td>
      <td>46.0</td>
      <td>35.0</td>
      <td>40.5</td>
      <td>0.01</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>partly cloudy</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2018-01-24</td>
      <td>50.0</td>
      <td>24.0</td>
      <td>37.0</td>
      <td>0.10</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>cloudy</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2018-01-25</td>
      <td>25.0</td>
      <td>16.0</td>
      <td>20.5</td>
      <td>0.02</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>cloudy</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2018-01-26</td>
      <td>24.0</td>
      <td>13.0</td>
      <td>18.5</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2018-01-27</td>
      <td>38.0</td>
      <td>13.0</td>
      <td>25.5</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2018-01-28</td>
      <td>51.0</td>
      <td>NaN</td>
      <td>40.5</td>
      <td>0.02</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>party sunny</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2018-01-29</td>
      <td>46.0</td>
      <td>21.0</td>
      <td>33.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>sunny</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2018-01-30</td>
      <td>37.0</td>
      <td>19.0</td>
      <td>28.0</td>
      <td>0.05</td>
      <td>0.5</td>
      <td>1.0</td>
      <td>cloudy</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2018-01-31</td>
      <td>19.0</td>
      <td>-2.0</td>
      <td>8.5</td>
      <td>0.06</td>
      <td>0.8</td>
      <td>1.0</td>
      <td>cloudy</td>
    </tr>
  </tbody>
</table>
</div>



### Step 1.

Let's examine the column names in a bit more detail.  Execute the code cell below.


```python
df.columns
```




    Index(['Date', 'Max T', 'Minimum Temp', 'Average Temperature', 'Precipitation',
           'Snowfall', 'Snow Depth', 'Sky'],
          dtype='object')



Notice that there are three different temperature columns, but the naming conventions differ for all three: "Max T", "Minimum Temp", and "Average Temperature".  This can lead to confusion because you need to keep track in your mind how temperature is labeled in each column name (T, Temp, Temperature).  Furthermore, the largest temperature is labeled with the shorthand "Max", while the smallest temperature is labeled with the full word "Minimum".  While we are free to choose whatever names we want for our data (within any syntactic rules), it is useful &mdash; for both you the developer and for anyone else who might be using the code &mdash; to establish some uniformity and consistency in naming.  Fortunately, we don't need to go back and modify the original csv file; we can just modify the column names in our code.

In the code cell below, use the ```rename``` method on a dataframe to rename the columns as follows:

* rename 'Max T' to be 'Maximum Temperature'
* rename 'Minimum Temp' to be 'Minimum Temperature'

Consult the [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html) for ```df.rename``` and find an example to "Rename columns using a mapping", which will demonstrate how to pass a dictionary to the method in order to change the column names. Hint: each element in the dictionary is a key/value pair in which the key is the original name and the value is the new name. For example: {original_name: new_name}.

Note that the ```rename``` method will, by default, return a new dataframe with the modified names.  You can either assign that new dataframe to a variable (you can even just reassign it to the name ```df```) or you can use the ```inplace=True``` option to modify ```df``` directly. 

For this exercise, you will use the ```inplace=True``` option in the `rename` method to modify ```df``` directly. After you've done the renaming, inspect the column names of the dataframe to verify that you've changed the names as intended (and if necessary, modify your renaming code until the column names are as desired.)

## Graded Cell

This cell is worth 50% of the grade for this assignment.


```python
df.rename(columns={'Max T':'Maximum Temperature','Minimum Temp': 'Minimum Temperature'},inplace=True )
print(df)

```

              Date  Maximum Temperature  Minimum Temperature  Average Temperature  \
    0   2018-01-01                  5.0                  0.0                  2.5   
    1   2018-01-02                 13.0                  1.0                  7.0   
    2   2018-01-03                 19.0                 -2.0                  NaN   
    3   2018-01-04                 22.0                  1.0                 11.5   
    4   2018-01-05                 18.0                 -2.0                  8.0   
    5   2018-01-06                  2.0                 -3.0                 -0.5   
    6   2018-01-07                  2.0                 -3.0                 -0.5   
    7   2018-01-08                 24.0                 -3.0                 10.5   
    8   2018-01-09                 37.0                 23.0                 30.0   
    9   2018-01-10                 33.0                 15.0                 24.0   
    10  2018-01-11                 41.0                 18.0                 29.5   
    11  2018-01-12                 57.0                 40.0                 48.5   
    12  2018-01-13                 62.0                 12.0                 37.0   
    13  2018-01-14                 12.0                  4.0                  8.0   
    14  2018-01-15                 12.0                 -9.0                  1.5   
    15  2018-01-16                 22.0                  NaN                  6.5   
    16  2018-01-17                 26.0                 15.0                 20.5   
    17  2018-01-18                 20.0                 -1.0                  9.5   
    18  2018-01-19                 22.0                  NaN                  NaN   
    19  2018-01-20                 37.0                  8.0                 22.5   
    20  2018-01-21                 45.0                 16.0                 30.5   
    21  2018-01-22                  NaN                 19.0                 30.5   
    22  2018-01-23                 46.0                 35.0                 40.5   
    23  2018-01-24                 50.0                 24.0                 37.0   
    24  2018-01-25                 25.0                 16.0                 20.5   
    25  2018-01-26                 24.0                 13.0                 18.5   
    26  2018-01-27                 38.0                 13.0                 25.5   
    27  2018-01-28                 51.0                  NaN                 40.5   
    28  2018-01-29                 46.0                 21.0                 33.5   
    29  2018-01-30                 37.0                 19.0                 28.0   
    30  2018-01-31                 19.0                 -2.0                  8.5   
    
        Precipitation  Snowfall  Snow Depth             Sky  
    0            0.04       1.0         3.0          cloudy  
    1            0.03       NaN         4.0   partly cloudy  
    2            0.00       0.0         NaN           sunny  
    3            0.00       0.0         3.0    partly sunny  
    4            0.09       1.2         4.0          cloudy  
    5            0.00       0.0         4.0     party sunny  
    6            0.00       0.0         4.0    partly sunny  
    7            0.00       0.0         4.0           sunny  
    8            0.00       0.0         4.0           sunny  
    9            0.00       0.0         4.0           sunny  
    10           0.00       0.0         3.0           sunny  
    11           0.76       0.0         0.0             NaN  
    12           0.94       6.0         6.0          couldy  
    13           0.06       0.9         6.0   partly cloudy  
    14           0.00       0.0         6.0    partly sunny  
    15           0.05       0.5         6.0          cloudy  
    16           0.13       1.6         8.0          cloudy  
    17           0.00       0.0         NaN           sunny  
    18           0.00       0.0         7.0           sunny  
    19           0.00       0.0         6.0             NaN  
    20           0.00       0.0         4.0    partly sunny  
    21           0.02       0.0         3.0   partly cloudy  
    22           0.01       0.0         0.0   partly cloudy  
    23           0.10       0.0         0.0          cloudy  
    24           0.02       NaN         1.0          cloudy  
    25           0.00       NaN         0.0           sunny  
    26           0.00       NaN         0.0           sunny  
    27           0.02       0.0         0.0     party sunny  
    28           0.00       0.0         0.0           sunny  
    29           0.05       0.5         1.0          cloudy  
    30           0.06       0.8         1.0          cloudy  


## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.


```python
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
```

    Correct!
    Dataframe df contains column 'Maximum Temperature'.
    Correct!
    Dataframe df contains column 'Minimum Temperature'.


Execute the cell below and inspect the column names of the dataframe. 


```python
df.columns
```




    Index(['Date', 'Maximum Temperature', 'Minimum Temperature',
           'Average Temperature', 'Precipitation', 'Snowfall', 'Snow Depth',
           'Sky'],
          dtype='object')



### Step 2.

Let's examine the new data in the 'Sky' column.  The entries here are strings representing categorical data, such as "sunny", "partly sunny", "cloudy" and "partly cloudy".  Because they are text-based, it is often useful to verify that there are no mispellings or spelling variants.  A useful method on a Series, or on a column extracted from a DataFrame, is ```unique```, which returns an array of unique entries in that Series or column.

In the code cell below, write and evaluate an expression to extract the unique entries of the 'Sky' column of the dataframe.


```python
df['Sky'].unique()
```




    array(['cloudy', 'partly cloudy', 'sunny', 'partly sunny', 'party sunny',
           nan, 'couldy', ' partly cloudy'], dtype=object)



While it might not have been obvious when looking at the entire dataframe, extracting the group of unique entries in the 'Sky' column makes it obvious that there are some misspellings and other textual problems, such as an extra space at the beginning of ' partly cloudy'.

Pandas dataframes have a ```replace``` method that allows you to change values in a dataframe according to a specified rule, as described [here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html).  If you want to replace text entries (strings), you either need to provide the full string to replace, or use the ```regex=True``` option to specify a regular expression (regex) for replacing part of a string.  In this exercise, let's just specify fully the strings we want to replace.  Note that the ```replace``` method is for changing values in the body of the dataframe, whereas the ```rename``` method used above is for changing the names of the index or column labels.  When called on an entire dataframe, the ```replace``` method will replace all instances of the specified text, regardless of what column it is in.  (If you wanted to replace values only in a particular column, you would first extract that column before doing the replacement.)

In the code cell below, write and evaluate code to replace all the misspelled entries in the dataframe with their corrected versions.  The easiest way to do this is to provide all the corrections in a dictionary which is passed as an argument to the method.  Note that by default, the ```replace``` method will return a new dataframe, so you can either assign it to a variable, or modify the original dataframe in place by using the `inplace=True` option.

For this exercise, you will modify `df` in place by using the `inplace=True` option.


## Graded Cell

This cell is worth 50% of the grade for this assignment.


```python
df.replace({'party sunny':'partly sunny', 'couldy': 'cloudy', ' partly cloudy':'partly cloudy'},inplace=True)
```

## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.


```python
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
    
```

    Correct!
    'party sunny' was corrected.
    Correct!
    'couldy' was corrected.
    Correct!
    ' partly cloudly' was corrected.


After doing the text replacement, re-examine the unique entries of the 'Sky' column to verify that you have corrected the problems with the original data.  (There should be 5 unique entries.)  If you have not fixed all the problems, modify your replacement code above and continue until the data are corrected.


```python
df['Sky'].unique()
```




    array(['cloudy', 'partly cloudy', 'sunny', 'partly sunny', nan],
          dtype=object)


