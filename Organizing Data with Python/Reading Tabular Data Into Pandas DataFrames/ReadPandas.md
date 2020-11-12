
## Reading tabular data into pandas dataframes

Pandas provides a variety of functions for reading data tables into DataFrame objects, and for writing those DataFrames out to files in different formats.

Let's start by doing a few imports.  Execute the code cell below.


```python
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```

Let's look at the contents of the current directory with the ```%ls``` magic function.  Execute the code cell below.


```python
%ls
```

    gradebook.db                      jn.py            ReadPandas.ipynb
    IthacaDailyClimate2018.csv        [0m[01;34m__pycache__[0m/
    IthacaDailyClimateMultiyear.xlsx  readPandas1.png


Data tables are often stored in csv (comma-separated values) files.  This is a useful file format, since it is human-readable and is portable across different programs and platforms.

In our current working directory, there is a data file named "IthacaDailyClimate2018.csv", which contains climate data for Ithaca, NY, USA for each day throughout 2018.

In the code cell below, write an expression to use the ```read_csv``` function in pandas to create a dataframe from this csv file, and assign the resulting dataframe to the variable ```df```.  Then write an expression to show the first five rows of the dataframe, using its ```head``` method.  Evaluate the resulting code cell.

Consult the <a href='https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html'>online documentation</a> for more information about the ``read_csv`` function.


```python
df = pd.read_csv("IthacaDailyClimate2018.csv")
```

It's also useful to get an overview of a dataframe by calling the ```info``` method of the dataframe.  Write an expression to print out this summary information, and evaluate the code cell.


```python
df.info()
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


The information printed above reveals that some of the data fields are integers (int64), some are floats (float64), and the ```Date``` field is represented as an "object".  That essentially means that it is being treated as a string, and not recognized to be a date (or datetime) object.

We can refine our call above to ```pd.read_csv``` to provide additional information that the ```Date``` field should be interpreted as a date.  ```pd.read_csv``` has an option called ```parse_dates```.  Use the ```parse_dates``` option and assign it a list containing column names (as strings); pandas will try to parse those columns as datetime objects.

In the code cell below, write a revised expression to read the climate csv file and assign the result to ```df```, except this time provide additional information that the ```Date``` column should be parsed as dates.  Then write an expression to print out the summary information using the ```info``` method.  Evaluate the code cell.

## Graded Cell

This cell is worth 30% of the grade for this assignment.


```python
df = pd.read_csv("IthacaDailyClimate2018.csv", parse_dates=['Date'])
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 365 entries, 0 to 364
    Data columns (total 7 columns):
     #   Column               Non-Null Count  Dtype         
    ---  ------               --------------  -----         
     0   Date                 365 non-null    datetime64[ns]
     1   Maximum Temperature  365 non-null    int64         
     2   Minimum Temperature  365 non-null    int64         
     3   Average Temperature  365 non-null    float64       
     4   Precipitation        365 non-null    float64       
     5   Snowfall             365 non-null    float64       
     6   Snow Depth           365 non-null    float64       
    dtypes: datetime64[ns](1), float64(4), int64(2)
    memory usage: 20.1 KB


## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.


```python
# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testdDfDate

try:
    print(testdDfDate(df))    
except Exception as e:
    print("Error!\n" + str(e))
```

    Correct!


Now that the ```Date``` field has been converted to a datetime64 object, pandas is able to do some useful things with that.  Recall that a dataframe object has a ```plot``` method that allows you to plot different columns against each other, by passing the names of those columns as ```x``` and ```y``` inputs to the method.

In the code cell below, make a call to ```df.plot``` that plots the ```Snow Depth``` throughout the year (i.e., with ```Snow Depth``` on the y-axis and ```Date``` on the x-axis).  Evaluate your plot.  You should notice in the plot that the ticks on the x axis are represented as abbreviations of the months, even though those month abbreviations were not included in the original csv file that we read in.  Because we converted the dates in the previous step, pandas was able to make use of that information to make a usefully formatted plot.

## Graded Cell

This cell is worth 30% of the grade for this assignment. <i>Note: a self-check will not accompany this assignment.</i><br>
Your plot should look like this:


```python
df.plot(x='Date', y= 'Snow Depth')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f1c03c501d0>




![png](output_15_1.png)


Similar to the ```read_csv``` function, pandas also provides a ```read_excel``` function to read tabular data from an Excel spreadsheet into a dataframe.

One feature that distinguishes a csv file from an Excel file is that the latter can contain multiple worksheets. You might be interested in reading in only one worksheet, or you might want to read in several or even all of them.  This is controlled by the ```sheet_name``` option that can be passed to ```read_excel```.

* if ```sheet_name``` is not specified, the first worksheet is read into a dataframe
* if ```sheet_name``` is specified along with the name of a worksheet (e.g., ```sheet_name="2016"```), then the worksheet with that name is read into a dataframe
* if ```sheet_name=None``` is specified, then all worksheets are read into dataframes, and the group is stored in a dictionary keyed on the names of each of the worksheets (technically, stored in an OrderedDict)

The file in your current working directory named "IthacaDailyClimateMultiyear.xlsx" is an Excel workbook containing two worksheets with daily climate data, one for the year 2016 and one for the year 2018.

In the code cell below, use the ```pd.read_excel``` along with the ```sheet_name``` option, to read the worksheet named "2016" into a dataframe named ```df16``` and the worksheet named "2018" into a dataframe named ```df18```.

Consult the <a href='https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html'>online documentation</a> for more information about the ``read_excel`` function.


```python
df16=pd.read_excel('IthacaDailyClimateMultiyear.xlsx', sheet_name='2016')
df18=pd.read_excel('IthacaDailyClimateMultiyear.xlsx', sheet_name='2018')
```

Using the ```sum``` method defined both for DataFrames and Series objects, compute the total amount of Snowfall in Ithaca during 2016, and store the result in the variable ```snow16```.  (Hint: you can either extract Snowfall first and compute the sum on the Series, or do the sum on the DataFrames and then extract the value for Snowfall.)  Do the same for 2018, storing the total amount of snowfall during that year in the variable ```snow18```.

## Graded Cell

This cell is worth 30% of the grade for this assignment.


```python
snow16 = df16[['Snowfall']].sum().tolist()[0]
snow18 = df18[['Snowfall']].sum().tolist()[0]
```

## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.


```python
# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testSnow16, testSnow18

try:
    print(testSnow16(snow16, df16))
except Exception as e:
    print("Error!\n" + str(e))

try:
    print(testSnow18(snow18, df18))
except Exception as e:
    print("Error!\n" + str(e))
```

    Correct!
    snow16 contains the total amount of Snowfall in Ithaca during 2016.
    Correct!
    snow18 contains the total amount of Snowfall in Ithaca during 2018.


Inspect the values of <code>snow16</code> and <code>snow18</code>. Which year had more total snowfall?

In the code cell below, create the variable <code>MORE_SNOW</code> and assign it the value of "2016" or "2018" depending on which year had more total snowfall.  You might even want to write a little code in the cell below to set the value of that variable based on which snow total is greater.

## Graded Cell

This cell is worth 10% of the grade for this assignment.



```python
MORE_SNOW = "2016" if snow16 >= snow18 

```

## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.


```python
# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testMoreSnow
try:
    print(testMoreSnow(MORE_SNOW))
except Exception as e:
    print("Error!\n" + str(e))

```
