
## Analyzing the World Happiness Data


### Preparing the data for analysis

In this exercise, we will do some initial data imports and preprocessing to get the data ready for further analysis.  We will repeat these same basic steps in subsequent exercises.  Begin by executing the code cell below to import some necessary packages.  Note that the last line in the code cell below is intended to instruct pandas to display floating point numbers to 2 decimal places (`.2f`).  This is just one of many pandas display options that can be configured, as described [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html).


```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
pd.options.display.float_format = '{:.2f}'.format
```

### Step 1

Create a Pandas dataframe named ```dfraw``` by reading in the data in the worksheet named "Table2.1" from the spreadsheet "WHR2018Chapter2OnlineData.xls".


```python
dfraw = pd.read_excel('WHR2018Chapter2OnlineData.xls', sheet_name='Table2.1')
```

To facilitate working with the data, it will be useful to select a subset of the data from the full dataset and to rename the columns to make them less verbose.  In the code cell below, the variable ```cols_to_include``` contains a list of column names to extract.
Execute the cell. 


```python
cols_to_include = ['country', 'year', 'Life Ladder', 
                   'Positive affect','Negative affect',
                   'Log GDP per capita', 'Social support',
                   'Healthy life expectancy at birth', 
                   'Freedom to make life choices', 
                   'Generosity', 'Perceptions of corruption']
```

### Step 2

Using the variables defined above, in the code cell below, write and evaluate an expression to create a new dataframe named `df` that includes the subset of data in `cols_to_include`.

## Graded Cell

This cell is worth 100% of the grade for this assignment.


```python
df = dfraw[cols_to_include]
```

## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.


```python
# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testDf

try:
    print(testDf(df, dfraw))    
except Exception as e:
    print("Error!\n" + str(e))
```

    Correct!


### Step 3.

Take a peek at the head of the new dataframe.


```python
df.head()
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
      <th>country</th>
      <th>year</th>
      <th>Life Ladder</th>
      <th>Positive affect</th>
      <th>Negative affect</th>
      <th>Log GDP per capita</th>
      <th>Social support</th>
      <th>Healthy life expectancy at birth</th>
      <th>Freedom to make life choices</th>
      <th>Generosity</th>
      <th>Perceptions of corruption</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Afghanistan</td>
      <td>2008</td>
      <td>3.72</td>
      <td>0.52</td>
      <td>0.26</td>
      <td>7.17</td>
      <td>0.45</td>
      <td>49.21</td>
      <td>0.72</td>
      <td>0.18</td>
      <td>0.88</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Afghanistan</td>
      <td>2009</td>
      <td>4.40</td>
      <td>0.58</td>
      <td>0.24</td>
      <td>7.33</td>
      <td>0.55</td>
      <td>49.62</td>
      <td>0.68</td>
      <td>0.20</td>
      <td>0.85</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Afghanistan</td>
      <td>2010</td>
      <td>4.76</td>
      <td>0.62</td>
      <td>0.28</td>
      <td>7.39</td>
      <td>0.54</td>
      <td>50.01</td>
      <td>0.60</td>
      <td>0.14</td>
      <td>0.71</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Afghanistan</td>
      <td>2011</td>
      <td>3.83</td>
      <td>0.61</td>
      <td>0.27</td>
      <td>7.42</td>
      <td>0.52</td>
      <td>50.37</td>
      <td>0.50</td>
      <td>0.18</td>
      <td>0.73</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Afghanistan</td>
      <td>2012</td>
      <td>3.78</td>
      <td>0.71</td>
      <td>0.27</td>
      <td>7.52</td>
      <td>0.52</td>
      <td>50.71</td>
      <td>0.53</td>
      <td>0.25</td>
      <td>0.78</td>
    </tr>
  </tbody>
</table>
</div>


