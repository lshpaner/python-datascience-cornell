
# DataFrame indexing

DataFrames are two-dimensional tables, labeled by row and column names, containing of a set of column-oriented data such that each column has a particular datatype (dtype).  Indexing and slicing are the processes of accessing subsets of data in a container by specifying which element(s) one is interested in.  Python lists and numpy arrays are indexed by integer position (e.g., ```my_list[3]``` or ```my_array[5,7]```), while Python dictionaries are indexed by keys (e.g., ```my_dict['name']```).  Because pandas DataFrames contain data in a positional order, *and* have row and column labels, they can be indexed both by position and by a label name.

In this exercise we will explore indexing and slicing in DataFrames.  In addition to getting more experience working with Jupyter notebooks, we can also make use of the some of the nice ways that Jupyter facilities working with DataFrames.

Online Pandas documentation describing indexing in great detail can be found [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html).

### Step 1.

Write some code in the first empty cell below to:

* import the pandas module (using the conventional shorthand renaming)
* read the pizza excel spreadsheet ("PizzaSheet.xlsx") into a dataframe named ```dfp```
* read the climate csv file ("IthacaDailyClimate2018.csv") into a dataframe named ```dfc```

Once you've done so, execute the cell and inspect the two dataframes using the ```info``` and ```head``` methods to see that they loaded correctly, and to remind yourself what the dataframes consist of.  Feel free to add additional code cells if you want to be able to more easily inspect the output of each command as it is run.


```python
import pandas as pd

dfp = pd.read_excel('PizzaSheet.xlsx')
dfc = pd.read_csv('IthacaDailyClimate2018.csv')

dfc.info()
dfc.head()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 365 entries, 0 to 364
    Data columns (total 7 columns):
     #   Column               Non-Null Count  Dtype  
    ---  ------               --------------  -----  
     0   Date                 365 non-null    object 
     1   Maximum Temperature  365 non-null    int64  
     2   Minimum Temperature  365 non-null    int64  
     3   Average Temperature  365 non-null    float64
     4   Precipitation        365 non-null    float64
     5   Snowfall             365 non-null    float64
     6   Snow Depth           365 non-null    float64
    dtypes: float64(4), int64(2), object(1)
    memory usage: 20.1+ KB





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
      <th>Maximum Temperature</th>
      <th>Minimum Temperature</th>
      <th>Average Temperature</th>
      <th>Precipitation</th>
      <th>Snowfall</th>
      <th>Snow Depth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-01-01</td>
      <td>5</td>
      <td>0</td>
      <td>2.5</td>
      <td>0.04</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-01-02</td>
      <td>13</td>
      <td>1</td>
      <td>7.0</td>
      <td>0.03</td>
      <td>0.6</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-01-03</td>
      <td>19</td>
      <td>-2</td>
      <td>8.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018-01-04</td>
      <td>22</td>
      <td>1</td>
      <td>11.5</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018-01-05</td>
      <td>18</td>
      <td>-2</td>
      <td>8.0</td>
      <td>0.09</td>
      <td>1.2</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



### Mechanisms for indexing

Indexing with dataframes can be done through various mechanisms: 

* ```[]```
* ```loc[]```
* ```iloc[]```

The first of these, ```[]```, is the square-bracket based indexing that we are familiar with from Python lists, Python dictionaries, and numpy arrays.  Because pandas dataframes are generally column-oriented, however, indexing with square brackets results in selecting a particular column based on its label.  We can loosely think of a dataframe as something like a dictionary of Series objects: each column label is like a key, and the value associated with that key is the data in that particular column, which is a pandas Series.  For example, ```dfc['Precipitation']``` will extract the column labeled 'Precipitation' and will return a Series (like a 1D numpy array).

It's easiest to see this with some examples.

### Step 2.

Write and execute some code in the cell below to:

* extract the 'Size' column from the dfp dataframe using square brackets, and assign it to the variable ```sizes```

Print the new Series variable you have created.  This Series has the same index as the dfp dataframe (the integers 0 through 6 inclusive, which pandas encodes as a ```RangeIndex(start=0, stop=7, step=1)```, similar to the ```range``` objects found in Python).  Print the type of and the index of ```sizes``` to convince yourself that it is a Series object with that RangeIndex.


```python
sizes = dfp['Size']
print(sizes)
```

    0    L
    1    M
    2    S
    3    M
    4    L
    5    M
    6    L
    Name: Size, dtype: object


### Step 3.

We're not interested just in extracting data, but in computing with the extracted data.  As we've seen, Both Series and DataFrames have methods to compute summary mathematical operations such as ```sum```, ```min```, ```max```, and ```mean```.

In the code cell below, write an expression to compute the mean price of pizzas sold by our pizzeria, and assign that value to the variable ```mean_price```.  (Hint: you can do this in one line by chaining method calls; you don't need to create a separate variable to store the price data first.)

## Graded Cell

This cell is worth 20% of the grade for this assignment.


```python
mean_price = dfp.mean()
print(mean_price)
```

    Price    13.571429
    dtype: float64


## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.


```python
# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testMeanPrice

try:  
    print(testMeanPrice(mean_price))
except Exception as e:
    print("Error!\n" + str(e))
    
```

    Correct!


### Step 4.

We can use the same square-bracket based indexing to extract multiple columns from a dataframe.  In this case, we need to group the column labels of interest in a Python list.  If a dataframe df has columns named 'A', 'B', 'C', 'D', 'E', and we want to extract just columns 'B' and 'E', that could be accomplished with the expression ```df[['B','E']]```, i.e., we can index based on the list of columns ```['B','E']```.  In the cell below, write some code to extract both the columns 'Topping #1' and 'Topping #2' from dfp, and store the result in the variable ```top2```.


```python
top2 = dfp[['Topping #1', 'Topping #2']]
print(top2)
```

      Topping #1 Topping #2
    0  Pepperoni     Garlic
    1    Peppers     Onions
    2        NaN        NaN
    3        NaN        NaN
    4    Spinach        NaN
    5     Capers  Anchovies
    6    Sausage  Pepperoni


### Indexing using loc

Indexing of a dataframe using ```loc``` is more general, in that it enables to access both rows and columns based on label names.  It uses the same sort of multi-dimensional indexing that is used for numpy arrays, although with row and/or column labels rather than integer positional indexes.  By this we mean that the first entry in an index refers to row labels, and the second index refers to column labels.  If only one entry is specified, it is used to identify a row in a dataframe.

Slicing is also supported using the colon ```:```, just as with Python lists and numpy arrays.  Unlike those other slicing operations, however, slicing a pandas dataframes includes data at the stop location.

### Step 5.

Using the ```loc``` method, write code in the cell below to:

* extract the "Base" column from ```dfp``` for all pizzas sold, and assign that to the variable ```bases```
* print ```bases```


```python
bases = dfp.loc[:,'Base']
print(bases)
```

    0        Cheese
    1        Cheese
    2    Margherita
    3    Margherita
    4        Bianco
    5      Marinara
    6        Cheese
    Name: Base, dtype: object


### Step 6.

Using the ```loc``` method, write code in the cell below to:

* extract the data from all of the Toppings columns in ```dfp``` for all pizzas sold, by slicing from "Topping #1" through "Topping #5", and assign that to the variable ```toppings```
* print ```toppings```


```python
toppings = dfp.loc[:,'Topping #1':'Topping #5']
print(toppings)
```

      Topping #1 Topping #2 Topping #3 Topping #4 Topping #5
    0  Pepperoni     Garlic        NaN        NaN        NaN
    1    Peppers     Onions     Olives        NaN        NaN
    2        NaN        NaN        NaN        NaN        NaN
    3        NaN        NaN        NaN        NaN        NaN
    4    Spinach        NaN        NaN        NaN        NaN
    5     Capers  Anchovies   Pecorino        NaN        NaN
    6    Sausage  Pepperoni     Onions    Peppers  Mushrooms


Instead of *printing* toppings, simply evaluate it instead in the empty code cell below (by executing the statement ```toppings```).  You should notice that the rendering of the dataframe in the notebook is fancier than what printing provides, and that there is an ```Out[]``` statement that represents the dataframe ```toppings```.


```python
toppings
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
      <th>Topping #1</th>
      <th>Topping #2</th>
      <th>Topping #3</th>
      <th>Topping #4</th>
      <th>Topping #5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Pepperoni</td>
      <td>Garlic</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Peppers</td>
      <td>Onions</td>
      <td>Olives</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Spinach</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Capers</td>
      <td>Anchovies</td>
      <td>Pecorino</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Sausage</td>
      <td>Pepperoni</td>
      <td>Onions</td>
      <td>Peppers</td>
      <td>Mushrooms</td>
    </tr>
  </tbody>
</table>
</div>



### Step 7.

The ```count``` method on a DataFrame or Series counts the number of non-missing (non-empty) entries in each column.

Write a statement using the count method that computes the number of pizzas with 5 toppings (i.e., the number of pizzas for which the entry in "Topping #5" is not empty), and assign it to the variable ```num5```.  (There are a couple ways you can do this: (1) you can first extract the "Topping #5" column from the dataframe as a Series, and then compute the count, or (2) you can compute the counts for the entire dataframe, and then extract the count for "Topping #5".)

## Graded Cell

This cell is worth 60% of the grade for this assignment.


```python
num5 = dfp.loc[:,'Topping #5'].count()
print(num5)
```

    1


## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.


```python
# Run this self-test cell to check your code; do not add code or delete code in this cell

from jn import testNumPizzas

try:  
    print(testNumPizzas(num5, dfp))
except Exception as e:
    print("Error!\n" + str(e))
    

```

    Correct!


### Selecting data subsets based on a condition

Subsets of data can also be extracted from a DataFrame or Series based on some sort of logical condition, similar to how it is supported with numpy arrays.  A logical comparison can be made to produce a DataFrame or Series consisting of boolean values (either True or False, depending on whether the condition being tested is met or not), and indexing on those boolean values extracts only those entries that are True (i.e., that satisfy the comparison).

For example, if we wanted to extract only those rows in the pizza dataframe corresponding to Large pizzas, we could write:

```
larges = dfp.loc[dfp['Size'] == 'L']
```


### Step 8.

In addition to the pizza dataframe, you also loaded the climate dataframe at the top of this exercise.  Let's say you wanted to know how many days during 2018 the temperature in Ithaca, NY reached at least 70 degrees Fahrenheit sometime during the day.

* In the code cell below, write an expression to extract a new dataframe containing those days where the temperature reached at least 70 degrees, and assign that to the variable ```at_least_70```.  (You might need to think some about what the different columns in the full dataframe represent to decide how to extract the subset of interest.)
* After that, write another expression that computes how many days reached at least 70 degrees, and assign that to the variable ```num_at_least_70```.

## Graded Cell

This cell is worth 20% of the grade for this assignment.


```python
at_least_70 = dfc.loc[dfc["Maximum Temperature"] >= 70]
num_at_least_70 = at_least_70.shape[0]
```

## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.


```python
# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import test70DegreeDays
try:  
    print(test70DegreeDays(at_least_70, num_at_least_70, dfc))
except Exception as e:
    print("Error!\n" + str(e))
   
```

    Correct!

