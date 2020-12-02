
# Clustering Using Scikit-learn

We're going to continue to investigate some of the functionality provided by scikit-learn (sklearn) for doing machine learning, and specifically in this exercise, clustering.  As before, we will use the World Happiness Report (WHR) data for this exercise, in order to see to what extent we can group different countries together (into clusters) based solely on the indicator values contained in the WHR dataset.

### Step 1.

Execute the code cell below to import some modules and read in and preprocess the WHR data as we have done previously in the classification exercise. We've condensed several groups of previous operations into the code cell below, producing both a dataframe containing the raw numerical data (named ```df2```) and a second dataframe containing the scaled numerical data (named ```X_scaled```), in which scaling has been done to normalize each column to have zero mean and unit standard deviation.

The last line in the code cell below returns the head of the ```df2``` dataframe, to remind you what is in that dataset, and the subsequent code cell (which you should also execute) returns the head of the ```X_scaled``` dataframe.


```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
%matplotlib inline

dfraw = pd.read_excel('WHR2018Chapter2OnlineData.xls', sheet_name='Table2.1')
cols_to_include = ['country', 'year', 'Life Ladder', 
                   'Positive affect','Negative affect',
                   'Log GDP per capita', 'Social support',
                   'Healthy life expectancy at birth', 
                   'Freedom to make life choices', 
                   'Generosity', 'Perceptions of corruption']
renaming = {'Life Ladder': 'Happiness', 
            'Log GDP per capita': 'LogGDP', 
            'Social support': 'Support', 
            'Healthy life expectancy at birth': 'Life', 
            'Freedom to make life choices': 'Freedom', 
            'Perceptions of corruption': 'Corruption', 
            'Positive affect': 'Positive', 
            'Negative affect': 'Negative'}
df = dfraw[cols_to_include].rename(renaming, axis=1)
key_vars = ['Happiness', 'LogGDP', 'Support', 'Life', 'Freedom', 'Generosity', 'Corruption', 'Positive', 'Negative']

# read in data from SupportingFactors worksheet into a new dataframe dfsupp
dfsupp = pd.read_excel('WHR2018Chapter2OnlineData.xls', sheet_name='SupportingFactors')

# extract out region information from SupportingFactors dataframe
regions = dfsupp[['country', 'Region indicator']].rename({'Region indicator': 'region'}, axis=1)

# compute the mean values of all the WHR data for each country, averaging over all years in the dataset
dfmean = df.groupby('country').mean().drop('year', axis=1)

# merge the mean WHR data with the region information extracted previously
df2 = pd.merge(dfmean, regions, on='country').dropna()

# set the index of df2 to be the country name
df2.set_index('country', inplace=True)

# import the StandardScaler
from sklearn.preprocessing import StandardScaler

# extract out the numerical data and scale it to zero mean and unit standard deviation
X = df2[key_vars]
scaler = StandardScaler().fit(X)
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns = X.columns, index = X.index)


# examine the df2 dataframe -- mean WHR values for each country, along with associated regions
df2
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
      <th>Happiness</th>
      <th>Positive</th>
      <th>Negative</th>
      <th>LogGDP</th>
      <th>Support</th>
      <th>Life</th>
      <th>Freedom</th>
      <th>Generosity</th>
      <th>Corruption</th>
      <th>region</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>3.806614</td>
      <td>0.580873</td>
      <td>0.301283</td>
      <td>7.419697</td>
      <td>0.517146</td>
      <td>50.838271</td>
      <td>0.544895</td>
      <td>0.118428</td>
      <td>0.826794</td>
      <td>South Asia</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>4.988791</td>
      <td>0.642628</td>
      <td>0.303256</td>
      <td>9.247059</td>
      <td>0.723204</td>
      <td>68.027213</td>
      <td>0.626155</td>
      <td>-0.105019</td>
      <td>0.859691</td>
      <td>Central and Eastern Europe</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>5.555004</td>
      <td>0.616524</td>
      <td>0.265460</td>
      <td>9.501728</td>
      <td>0.804633</td>
      <td>64.984461</td>
      <td>0.536398</td>
      <td>-0.208236</td>
      <td>0.661478</td>
      <td>Middle East and North Africa</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>4.420299</td>
      <td>0.613339</td>
      <td>0.351173</td>
      <td>8.713935</td>
      <td>0.737973</td>
      <td>51.729801</td>
      <td>0.455957</td>
      <td>-0.077940</td>
      <td>0.867018</td>
      <td>Sub-Saharan Africa</td>
    </tr>
    <tr>
      <th>Argentina</th>
      <td>6.406131</td>
      <td>0.840998</td>
      <td>0.273187</td>
      <td>9.826051</td>
      <td>0.906080</td>
      <td>66.764205</td>
      <td>0.753122</td>
      <td>-0.154544</td>
      <td>0.844038</td>
      <td>Latin America and Caribbean</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Venezuela</th>
      <td>6.414997</td>
      <td>0.823428</td>
      <td>0.219652</td>
      <td>9.706075</td>
      <td>0.925062</td>
      <td>64.120754</td>
      <td>0.682923</td>
      <td>-0.192087</td>
      <td>0.782355</td>
      <td>Latin America and Caribbean</td>
    </tr>
    <tr>
      <th>Vietnam</th>
      <td>5.293268</td>
      <td>0.631631</td>
      <td>0.209818</td>
      <td>8.477400</td>
      <td>0.827200</td>
      <td>65.357492</td>
      <td>0.871811</td>
      <td>0.019168</td>
      <td>0.781401</td>
      <td>Southeast Asia</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>3.969106</td>
      <td>0.536306</td>
      <td>0.299466</td>
      <td>8.191046</td>
      <td>0.721817</td>
      <td>54.056593</td>
      <td>0.626482</td>
      <td>-0.132600</td>
      <td>0.833238</td>
      <td>Middle East and North Africa</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>4.685380</td>
      <td>0.722792</td>
      <td>0.275567</td>
      <td>8.095450</td>
      <td>0.745987</td>
      <td>49.643073</td>
      <td>0.749263</td>
      <td>-0.008872</td>
      <td>0.831900</td>
      <td>Sub-Saharan Africa</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>4.064211</td>
      <td>0.719749</td>
      <td>0.214457</td>
      <td>7.415946</td>
      <td>0.811693</td>
      <td>46.415665</td>
      <td>0.564987</td>
      <td>-0.064208</td>
      <td>0.849916</td>
      <td>Sub-Saharan Africa</td>
    </tr>
  </tbody>
</table>
<p>152 rows × 10 columns</p>
</div>



Execute the code cell below to examine ```X_scaled```.


```python
X_scaled
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
      <th>Happiness</th>
      <th>LogGDP</th>
      <th>Support</th>
      <th>Life</th>
      <th>Freedom</th>
      <th>Generosity</th>
      <th>Corruption</th>
      <th>Positive</th>
      <th>Negative</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>-1.443128</td>
      <td>-1.438896</td>
      <td>-2.425953</td>
      <td>-1.333584</td>
      <td>-1.397623</td>
      <td>0.735439</td>
      <td>0.451854</td>
      <td>-1.262731</td>
      <td>0.471370</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>-0.360792</td>
      <td>0.054466</td>
      <td>-0.681799</td>
      <td>0.776161</td>
      <td>-0.776670</td>
      <td>-0.719736</td>
      <td>0.632648</td>
      <td>-0.638194</td>
      <td>0.499009</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>0.157600</td>
      <td>0.262588</td>
      <td>0.007447</td>
      <td>0.402698</td>
      <td>-1.462554</td>
      <td>-1.391919</td>
      <td>-0.456675</td>
      <td>-0.902184</td>
      <td>-0.030449</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>-0.881273</td>
      <td>-0.381215</td>
      <td>-0.556782</td>
      <td>-1.224159</td>
      <td>-2.077245</td>
      <td>-0.543385</td>
      <td>0.672914</td>
      <td>-0.934399</td>
      <td>1.170248</td>
    </tr>
    <tr>
      <th>Argentina</th>
      <td>0.936845</td>
      <td>0.527632</td>
      <td>0.866136</td>
      <td>0.621142</td>
      <td>0.193546</td>
      <td>-1.042257</td>
      <td>0.546624</td>
      <td>1.367958</td>
      <td>0.077797</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Venezuela</th>
      <td>0.944963</td>
      <td>0.429584</td>
      <td>1.026807</td>
      <td>0.296688</td>
      <td>-0.342879</td>
      <td>-1.286749</td>
      <td>0.207632</td>
      <td>1.190270</td>
      <td>-0.672139</td>
    </tr>
    <tr>
      <th>Vietnam</th>
      <td>-0.082030</td>
      <td>-0.574517</td>
      <td>0.198462</td>
      <td>0.448484</td>
      <td>1.100508</td>
      <td>0.089020</td>
      <td>0.202390</td>
      <td>-0.749403</td>
      <td>-0.809898</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>-1.294360</td>
      <td>-0.808532</td>
      <td>-0.693534</td>
      <td>-0.938572</td>
      <td>-0.774178</td>
      <td>-0.899352</td>
      <td>0.487271</td>
      <td>-1.713444</td>
      <td>0.445918</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>-0.638579</td>
      <td>-0.886655</td>
      <td>-0.488949</td>
      <td>-1.480281</td>
      <td>0.164061</td>
      <td>-0.093591</td>
      <td>0.479918</td>
      <td>0.172524</td>
      <td>0.111138</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>-1.207287</td>
      <td>-1.441962</td>
      <td>0.067210</td>
      <td>-1.876408</td>
      <td>-1.244086</td>
      <td>-0.453956</td>
      <td>0.578926</td>
      <td>0.141747</td>
      <td>-0.744916</td>
    </tr>
  </tbody>
</table>
<p>152 rows × 9 columns</p>
</div>



### Step 2.

The ```X_scaled``` dataframe contains, for each country listed, a group of 9 numerical indicators.  The 'region' column from ```df2``` has been removed because that is categorical rather than numerical.  (Since we have scaled the data to have zero mean, any numerical entry that is greater than zero indicates a value above average, and any entry that is less than zero indicates a value below average.)  Therefore, we can think of each country as being "defined" by this group of 9 indicators.

We are interested in how similar different countries are to each other, based on their indicator data.  Are there natural groupings or clusters of countries based upon similarity of their indicators?  This is the kind of question that the machine learning technique of clustering addresses.

To begin, let's just have a visual look at the data, which consists of 152 rows x 9 columns.  We've previously used the ```heatmap``` function from seaborn (sns) to visualize datasets of this sort.  Note that the seaborn package has already been imported at the top of this notebook.

In the code cell below:

* Use the heatmap function in sns to make a heatmap of ```X_scaled```

You might notice that the default rendering of the heatmap is not ideal, being somewhat short and squat when the dataset is much longer.  Edit the code you have entered in the code cell below to first create a figure with a size that is better suited to this plot, and then make the call to heatmap.  In particular, one way to create this figure is with the following code:

* `plt.figure(figsize = (6,30))`

You'll note that this is a call to ```plt``` (part of the matplotlib package).  Since seaborn sits on top of matplotlib to do its basic plotting, we can freely mix seaborn and matplotlib commands to customize the figures we generate.  Since we have requested a large figure size, it is possible that the figure might be embedded in a scrollable sub-window rather than rendered in its entirety in the notebook as is usually the case. If you'd like to be able to expand the sub-window and get the figure embedded fully within the notebook, you can click on the panel to the left of the figure (under the Out[] indicator, i.e., to the left but still within the notebook). If you decide you want to convert it back again to a scrollable sub-window, you can click in that left panel again.


```python
plt.figure(figsize = (10,80))
ax = sns.heatmap(X_scaled, annot=True, square=True)
ax.set_ylim(len(X_scaled), -0.5)
```




    (152.0, -0.5)




![png](output_6_1.png)


### Step 3.

The countries in the heatmap you have just created are ordered alphabetically, leading to what looks like a more or less random pattern of indicator values as you scan down the heatmap.  The point of clustering is to pull out subgroups (clusters) that share similar indicator profiles.

The first clustering algorithm we will examine is KMeans (sometimes written as k-means or K-means), which is described in more detail in the [scikit-learn documentation](https://scikit-learn.org/stable/modules/clustering.html#k-means).  With k-means, one specifies in advance how many clusters they would like to group the data into, and this value is the number k (or K), hence the name of the method.  Sometimes one needs to experiment with different values of k to see what best reflects the nature of the data.  k-means works by finding a set of "centroid" points at the center of each cluster, so that every data point within a cluster is closer to the center of its own cluster than to the centroid of a different cluster.

In a hypothetical dataset with N data points, a "perfect but meaningless" clustering of the data would involve making as many clusters as there are data points, that is, setting k = N.  In such a scenario, every data point (e.g., every country in our dataset) would be in its own cluster, perfectly identical to itself, but meaningless in terms of revealing structure and patterns in the data.  In the opposite limit, k = 1, all the data points would be in the same cluster, which leaves us no better than where we started.  The point of clustering is to find a number of clusters k (somewhere between 1 and N) that captures substructure within the data.

In the case of our WHR data, a useful guess for k might reflect the number of different regions that are contained in the ```df2``` dataframe.  You might recall that in the previous classification exercise, we built a classifier in order to try to predict the world region that a country is associated with based on its WHR indicators.  In this exercise, we want to cluster countries just based on the WHR indicators, and might be interested in how well the clustering reflects the region data.  Thus, a useful place to start here is to set k to be the number of unique regions contained in the ```df2``` dataframe.

Let's first figure out how many clusters we want to find.

In the code cell below:

* compute the number of unique region labels in ```df2``` (hint: look for information in pandas about the ```nunique``` method), and assign this value to the variable ```k```
* print the value of ```k```, so that you know how many clusters you are looking for

## Graded Cell

This cell is worth 20% of the grade for this assignment.


```python
k = df2.region.nunique()
k
```




    10



## Self-Check

Run the cell below to test the correctness of your code above before submitting for grading.



```python
# Run this self-test cell to check your code; do not add code or delete code in this cell
from jn import testK

try:
    print(testK(df2, k))    
except Exception as e:
    print("Error!\n" + str(e))
```

    Correct!


### Step 4.

Having identified the number of clusters we want to look for, let's continue with k-means.  (If you did not succeed above in finding the number of unique regions, set k = 10.)

In the code cell below:

* import the ```KMeans``` class from the ```sklearn.cluster``` submodule
* initialize a `KMeans` cluster object to identify ```k``` clusters, and assign this object to the variable ```kcluster``` &mdash; the relevant option to pass to ```KMeans``` is called ```n_clusters```
* call the ```fit``` method on ```kcluster``` so that you can fit the data in the ```X_scaled``` dataframe


```python
from sklearn.cluster import KMeans
kcluster = KMeans(n_clusters=10, random_state=0).fit(X_scaled)
```

### Step 5.

The output from the code cell above, if entered and run correctly, should note some further information about the KMeans clusterer that you have created and fit to the data.  There are various other options that can in principle be specified in constructing the object; the only option we specified above was ```n_clusters```, and used the default values of everything else.  

You will notice an entry for ```n_init=10```.  This refers to the fact that the k-means algorithm starts from a initial guess for the centroid locations, and runs the algorithm repeatedly with different starting guesses (n_init times), choosing the best clustering from the group.

Once the KMeans clusterer has fit the data (as you have done above), it contains various data attributes that we can query. One of these attributes is the ```labels_``` object, which is an array of integers that assigns a cluster label to each entry in the dataset.  For our WHR data, therefore, the ```labels_``` object describes, in the same order in which the data appears in our ```X_scaled``` dataframe, which cluster each country belongs to.

In the code cell below, print the value of ```kcluster.labels_``` and examine the output.


```python
kcluster.labels_
```




    array([9, 2, 2, 4, 1, 5, 8, 8, 2, 1, 0, 2, 1, 3, 9, 7, 3, 5, 6, 1, 2, 4,
           9, 7, 4, 8, 9, 4, 3, 3, 0, 4, 1, 2, 3, 1, 8, 3, 3, 5, 3, 2, 0, 8,
           1, 5, 0, 1, 6, 2, 3, 9, 9, 3, 8, 2, 8, 0, 7, 5, 5, 8, 1, 2, 0, 3,
           1, 2, 2, 6, 6, 1, 6, 7, 2, 5, 6, 9, 3, 2, 8, 5, 4, 0, 3, 6, 7, 6,
           3, 1, 2, 6, 5, 2, 4, 7, 6, 6, 8, 8, 3, 0, 6, 8, 9, 5, 1, 3, 3, 3,
           1, 2, 8, 2, 2, 0, 1, 6, 5, 9, 8, 2, 1, 6, 2, 9, 1, 7, 4, 8, 8, 5,
           1, 6, 6, 7, 9, 3, 5, 5, 4, 2, 8, 8, 1, 1, 1, 1, 6, 4, 6, 4],
          dtype=int32)



### Step 6.

The actual numbers associated with the cluster labels are meaningless, and will change each time you run the clustering algorithm.  (By this we mean that we could permute the labels of all the clusters, and the underlying clustering of the data would remain unchanged.)  What is meaningful, however, is which countries *share* the same cluster label, since that means they are assigned to the same cluster (regardless of what cluster label number that is).  Since the cluster labels printed above contain no information about the countries they correspond to, it is useful to combine the cluster labels with the dataframes that they originated from.  We'll do that by creating a copy of both the ```df2``` and ```X_scaled``` dataframes, and adding information about the cluster labels.

In the code cell below:

* make a copy of the ```df2``` dataframe using its ```copy``` method and assign the result to a new variable named ```df2_clustered```
* add a new column named 'klabel' to ```df2_clustered``` so that it is filled with the data in ```kcluster.labels_``` (hint: you can just assign the labels to a new column called ```df2_clustered['klabel']```)
* make a copy of the ```X_scaled``` dataframe and assign it to ```X_scaled_clustered```
* add a new column named 'klabel' to ```X_scaled_clustered``` so that it is filled with the data in ```kcluster.labels_```

Once you've done so, examine the new ```df2_clustered``` dataframe.  You should see the 'klabel' column now &mdash; any two countries with the same label have been assigned to the same cluster.


```python
df2_clustered = df2.copy()
df2_clustered['klabel'] = kcluster.labels_
X_scaled_clustered = X_scaled.copy()
X_scaled_clustered['klabel'] = kcluster.labels_
df2_clustered
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
      <th>Happiness</th>
      <th>Positive</th>
      <th>Negative</th>
      <th>LogGDP</th>
      <th>Support</th>
      <th>Life</th>
      <th>Freedom</th>
      <th>Generosity</th>
      <th>Corruption</th>
      <th>region</th>
      <th>klabel</th>
    </tr>
    <tr>
      <th>country</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Afghanistan</th>
      <td>3.806614</td>
      <td>0.580873</td>
      <td>0.301283</td>
      <td>7.419697</td>
      <td>0.517146</td>
      <td>50.838271</td>
      <td>0.544895</td>
      <td>0.118428</td>
      <td>0.826794</td>
      <td>South Asia</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Albania</th>
      <td>4.988791</td>
      <td>0.642628</td>
      <td>0.303256</td>
      <td>9.247059</td>
      <td>0.723204</td>
      <td>68.027213</td>
      <td>0.626155</td>
      <td>-0.105019</td>
      <td>0.859691</td>
      <td>Central and Eastern Europe</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Algeria</th>
      <td>5.555004</td>
      <td>0.616524</td>
      <td>0.265460</td>
      <td>9.501728</td>
      <td>0.804633</td>
      <td>64.984461</td>
      <td>0.536398</td>
      <td>-0.208236</td>
      <td>0.661478</td>
      <td>Middle East and North Africa</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Angola</th>
      <td>4.420299</td>
      <td>0.613339</td>
      <td>0.351173</td>
      <td>8.713935</td>
      <td>0.737973</td>
      <td>51.729801</td>
      <td>0.455957</td>
      <td>-0.077940</td>
      <td>0.867018</td>
      <td>Sub-Saharan Africa</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Argentina</th>
      <td>6.406131</td>
      <td>0.840998</td>
      <td>0.273187</td>
      <td>9.826051</td>
      <td>0.906080</td>
      <td>66.764205</td>
      <td>0.753122</td>
      <td>-0.154544</td>
      <td>0.844038</td>
      <td>Latin America and Caribbean</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Venezuela</th>
      <td>6.414997</td>
      <td>0.823428</td>
      <td>0.219652</td>
      <td>9.706075</td>
      <td>0.925062</td>
      <td>64.120754</td>
      <td>0.682923</td>
      <td>-0.192087</td>
      <td>0.782355</td>
      <td>Latin America and Caribbean</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Vietnam</th>
      <td>5.293268</td>
      <td>0.631631</td>
      <td>0.209818</td>
      <td>8.477400</td>
      <td>0.827200</td>
      <td>65.357492</td>
      <td>0.871811</td>
      <td>0.019168</td>
      <td>0.781401</td>
      <td>Southeast Asia</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Yemen</th>
      <td>3.969106</td>
      <td>0.536306</td>
      <td>0.299466</td>
      <td>8.191046</td>
      <td>0.721817</td>
      <td>54.056593</td>
      <td>0.626482</td>
      <td>-0.132600</td>
      <td>0.833238</td>
      <td>Middle East and North Africa</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Zambia</th>
      <td>4.685380</td>
      <td>0.722792</td>
      <td>0.275567</td>
      <td>8.095450</td>
      <td>0.745987</td>
      <td>49.643073</td>
      <td>0.749263</td>
      <td>-0.008872</td>
      <td>0.831900</td>
      <td>Sub-Saharan Africa</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Zimbabwe</th>
      <td>4.064211</td>
      <td>0.719749</td>
      <td>0.214457</td>
      <td>7.415946</td>
      <td>0.811693</td>
      <td>46.415665</td>
      <td>0.564987</td>
      <td>-0.064208</td>
      <td>0.849916</td>
      <td>Sub-Saharan Africa</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>152 rows × 11 columns</p>
</div>



### Step 7.

Recall that each cluster is approximately defined by its centroid, which we can think of as a typical or average indicator profile for that cluster.  Our data points actually live in a 9-dimensional space (9 elements in ```key_vars```), so it's a little hard to visualize the data.  But if we want to see what each of the clusters approximately "looks like," we can just plot the coordinates of the cluster centroids, which are stored in the attribute ```kcluster.cluster_centers_```.

Execute the code cell below to make a plot of the cluster centers and their associated label numbers.  Note that the cluster centers are all distinct from one another, although clusters are somewhat closer to each other.  This might be indicative of the fact that k=10 might be too many clusters to properly represent this dataset; if k were reduced, some of the nearby clusters would probably collapse into a larger metacluster reflecting their approximately common profile.  We'll just examine the k=10 case in this exercise, but if you're interested in investigating further on your own, you could try some other values of k to see how the results change.

Feel free to modify the code in the cell below if you want to tweak the plot, or to understand what each of the commands there is doing.


```python
for i in range(10):
    plt.plot(kcluster.cluster_centers_[i], label=i)
plt.xticks(range(10), key_vars, rotation=45)
plt.legend()
```




    <matplotlib.legend.Legend at 0x7fc6d016d2b0>




![png](output_19_1.png)


### Step 8.

In the plot above, each line represents the centroid of one cluster (for clusters labeled 0 through 9).  For each cluster, there is a group of countries whose indicator profiles lie near to these centroids.

First examine, and then execute, the code cell below.  

The code cell below defines a function called ```plot_cluster_and_centroid```, which takes as input an integer cluster label, and plots all country profiles within the cluster (in different colors) along with the centroid profile (plotted with a black dashed line and black point markers).

After the function definition, the function is called to produce a plot for cluster label 0.

Once you've examined the plot for cluster 0, modify the cluster label being passed to the function in order to view each of the other 9 clusters that have been produced (10 clusters in all, since we set k = 10).  In other words, modify the input to the function one at a time, and re-execute the code cell, or &mdash; if you prefer &mdash; open up additional code cells below to plot each of the clusters in turn. At present, the plot turns off the legend indicating the names of the countries in each cluster (```legend=False```), since the legend clutters the figure for large clusters and is difficult to reposition.  But if you're curious, try turning the legend back on to see the contents of each cluster.

Take some time to examine these plots to understand what they are conveying.  Some clusters represents countries that might have greater Happiness and lower Corruption, for example, whereas others might represent different combinations of attributes.


```python
def plot_cluster_and_centroid(label):
    X_scaled_clustered[X_scaled_clustered.klabel==label][key_vars].T.plot(legend=False)
    plt.plot(kcluster.cluster_centers_[label], 'ko--')
    plt.xticks(range(9), key_vars, rotation=45)

plot_cluster_and_centroid(0)
```


![png](output_21_0.png)


### Step 9.

We might be interested in how the results produced by k-means clustering relate to the region information that is stored in the ```df2_clustered``` dataframe.  As we discussed above, the cluster labels themselves are meaningless, but we can easily examine how each cluster label (klabel) aligns with different world regions.  For example, we might want to know how many countries from each region are associated with cluster number 0, cluster number 1, etc.

In the code cell below, write an expression to group the data in ```df2_clustered``` by both 'klabel' and 'region', and compute the size of each (klabel, region) pair.  You can do this in one line using the ```groupby``` method on dataframes that we have studied previously, along with the ```size()``` method that is applied to each group produced by the groupby operation.  An operation of this sort will produce a new dataframe with a two-level MultiIndex (i.e., each row described by its ('klabel', 'region') pair), with the corresponding column indicating how many countries are associated with that pair.

## Graded Cell

This cell is worth 40% of the grade for this assignment. <i>Note: a self-check will not accompany this assignment.</i><br>
Your output should look similar to this (your results may be different): <br><img src="clusteringStep9.png" width=400 height=400  align="left"/>


```python
df2_clustered.groupby(['klabel','region']).size()
```




    klabel  region                            
    0       Commonwealth of Independent States     1
            South Asia                             2
            Sub-Saharan Africa                     6
    1       Central and Eastern Europe             3
            Commonwealth of Independent States     1
            East Asia                              2
            Latin America and Caribbean            7
            Middle East and North Africa           4
            North America and ANZ                  1
            Western Europe                         4
    2       Central and Eastern Europe             9
            Commonwealth of Independent States     6
            East Asia                              1
            Middle East and North Africa           3
            Western Europe                         3
    3       Latin America and Caribbean           14
            Middle East and North Africa           1
            Southeast Asia                         2
            Sub-Saharan Africa                     1
            Western Europe                         1
    4       Middle East and North Africa           1
            Sub-Saharan Africa                    10
    5       Central and Eastern Europe             4
            Commonwealth of Independent States     1
            Middle East and North Africa           8
            Sub-Saharan Africa                     1
    6       Central and Eastern Europe             1
            Commonwealth of Independent States     2
            East Asia                              1
            South Asia                             1
            Southeast Asia                         1
            Sub-Saharan Africa                    12
    7       South Asia                             2
            Southeast Asia                         5
            Western Europe                         1
    8       East Asia                              1
            Middle East and North Africa           2
            North America and ANZ                  3
            Southeast Asia                         1
            Western Europe                        11
    9       Latin America and Caribbean            1
            South Asia                             2
            Sub-Saharan Africa                     8
    dtype: int64



### Step 10.

The k-means algorithm is just one of many clustering algorithms supported by sklearn.  A colorful overview of different clustering methods is provided in the [sklearn documentation](https://scikit-learn.org/stable/modules/clustering.html).

Another widely used clustering method is known as [Hierarchical clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering), some variants of which are known as agglomerative clustering.  This method takes a slightly more nuanced approach to the process of clustering.  Whereas k-means clustering specifies a fixed number of clusters to group data into, hierarchical clustering develops a "hierarchy" of clustering relationships where data points are grouped more closely together if they are more similar to each other.  It's somewhat like the way that ancestry works.  If someone were to ask you how many people you are related to, you might reply that it depends on how far back they want to go in time to define "relatedness." Presumably we are all related to each other (however remotely) if we go back far enough in time to a common evolutionary ancestor, but that fact might not be so useful in defining "relatedness" or "clusters" of people.  Nonetheless, hierarchical clustering does provide insight into these hierarchical relationships among clusters, and lends itself to useful visualization techniques that reveal those relationships.

The sklearn package provides objects and methods for `AgglomerativeClustering` that operate similarly to the way that the KMeans object worked in the exercises above, by creating a clustering object and then fitting it to the dataset of interest.  If you're interested, you can investigate this further below by following along with the sklearn documentation.  Unfortunately, sklearn does not provide great support for plotting the results of hierarchical clustering, generally referred to as dendograms.  There is some code showing a [simple example](https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html).

Instead, we will work with seaborn (sns), which provides a useful function called ```clustermap``` that performs a hierarchical clustering and displays the results.  The clustermap function is described in the [seaborn documentation](https://seaborn.pydata.org/generated/seaborn.clustermap.html#seaborn.clustermap).  The function actually uses a version of the clustering algorithm that is included as part of [scipy](http://scipy.org), a Python package that provides a wealth of useful tools for scientific computing, but which we have not emphasized in this course material.

In the code cell below, enter and execute a call to ```sns.clustermap``` to operate on the ```X_scaled``` dataframe, providing the following additional options:

* ```method = 'average'```
* ```metric = 'euclidean'```
* ```figsize = (15,40)```

Note that you are instructed to cluster the data in ```X_scaled```.  You wouldn't want to cluster the data in the augmented dataframe that you created above (```X_scaled_clustered```), because that contains additional information about the k-means cluster labels that you don't want to include here.

Your code should construct and display a figure that looks a bit like the heatmap that we created earlier in this exercise, but with some differences.  As was discussed above, if the figure is in a sub-window that you'd like to expand, you can click on the panel to the left of the figure to do so.

After you have produced the figure, proceed to the material below the figure to read further about what is plotted.

## Graded Cell

This cell is worth 40% of the grade for this assignment. <i>Note: a self-check will not accompany this assignment.</i><br>
Your plot should look like this: <br><img src="clusteringStep10.png" width=200 height=400  align="left"/>


```python
new_frame = sns.clustermap(X_scaled, method = 'average', metric = 'euclidean', figsize = (15,40))
```


![png](output_27_0.png)


## Step 11.

There are several things you should notice about the plot produced by the clustermap.  First, whereas our original heatmap ordered the countries alphabetically, with a more or less random pattern of indicator values as a result, this clustermap has reordered the rows to reflect the clustering.

You should also notice a tree-like structure running along the left-hand side of the heatmap.  This tree, also known as a dendogram, is what is providing information about the clustering.  It is a tree, because it starts from a broad trunk at the far left of the dendogram down to finer and finer sub-branches and finally down to individual "leaves" that represent individual countries.  The clustering algorithm works from the bottom up: It finds several pairs of countries that are highly similar within each pair (smallest euclidean distance between them, in this version of the analysis), and then finds other countries that are similar to each pair.  Thus the algorithm grows clusters by accreting (or agglomerating) onto groupings that have already been identified.  The similarity between two countries in the tree is reflected by how far you need to go "up" the tree from one country and then back "down" to the other one.  If you go far enough up the tree, all countries are similar enough to each other to be grouped in one big cluster, similar to how all people are related to one another if we go back far enough in time.  Two countries that are near each other vertically in the reordered heatmap tend to be more similar to each other, but that is not strictly the case.  You should notice that at particular parts of the dendogram different branches end up getting placed nearby each other in this 2D representation, but their distance from each other up and back down the tree could be very far.

There are some other things to notice in this plot.  

First, despite the fact that nearby ordering in the heatmap does not always reflect close similarity in the tree, you should be able to discern some clustering visually in the reordered heatmap, that is, groups of countries with similar WHR indicator profiles.  If you see a group of countries with similar indicator profiles (similar patterns of colors in the heatmap), you should be able to identify the sub-tree on the left that group is associated with.

Second, you should notice that the columns of the dataset have also been clustered, with their own dendogram running along the top.  This is indicative of the fact that some groups of indicator variables are more closely associated among themselves, such as 'LogGDP' and 'Life' (life expectancy) which are clustered more closely together.  Clustering along both axes of a dataset is known as "biclustering", and is turned on by default in ```clustermap```.  If you want to cluster only along one axis, you could modify either the `row_cluster` or `col_cluster` options to the function.

Finally, we have chosen just one set of criteria to carry out this clustering (```method='average'``` and ```metric='euclidean'```).  In order to identify groups of similar items in a dataset, we need to specify mathematically what we mean by "similar."  In this case, we have defined the similarity of two data points based on their euclidean distance from each other (such that two identical items would be separated by zero distance).  But we could have chosen some other criterion instead, such as the correlation between two data points.  In addition, in hierarchical clustering, one needs to specify not only how similar two *data points* are, but also to specify how similar two *clusters* are (since it is building up clusters of clusters).  This is what the `method` parameter is about (or more specifically, what is called the "linkage method").  The similarity between two clusters might be based on how similar their two closest items are, or their two most distant items, or the average distance between all pairs of points in each cluster.

If you're interested, you can consult the documentation for clustermap and experiment with some different options to explore the effect of different clustering metrics and methods.  There is no one right answer, but generally you'd like to find clustering results that exhibit some degree of robustness to variations in these sorts of options.

### Step 12.

Congratulations!  You've worked through some interesting examples in using clustering to identify substructure and patterns in datasets, a key element in the suite of unsupervised machine learning techniques.  Feel free to explore these datasets some more to improve your mastery of machine learning methods and the scikit-learn package.
