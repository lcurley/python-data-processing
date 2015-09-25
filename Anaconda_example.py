# Anaconda example: data parsing, tables and images

# using pandas to read in some data and quickly remove NA rows
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd
from pandas import DataFrame, Series
from __future__ import division
import seaborn as sns
from sklearn.cross_validation import train_test_split
sns.set(style='ticks', palette='Set2')
%matplotlib inline

# read in data
data = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data-original",
                   delim_whitespace = True, header=None,
                   names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration',
                            'model', 'origin', 'car_name'])
print(data.shape)
data = data.dropna()
data.head()
# returns (406, 9)

# modeling with scikit-learn
# split data into test and training
# choose a model, fit the training data, and predict the test data
indep_vars = ['cylinders', 'displacement', 'horsepower', 'weight', 'acceleration']
dep_vars = ['mpg']
indep_data = data[indep_vars]
dep_data = data[dep_vars]
indep_train, indep_test, dep_train, dep_test = train_test_split(indep_data, dep_data, test_size=0.33, random_state=42)

regr = linear_model.LinearRegression()
regr.fit(indep_train, dep_train)
print('Coefficients: {0}'.format(zip(indep_vars,np.squeeze(regr.coef_))))
# returns coefficients: .......

regr_predict = regr.predict(indep_test)
print("Residual sum of squares: %.2f"
      % np.mean((regr_predict - dep_test) ** 2))
# returns "Residual sum of squares: 19.71" 

# using pandas to create summary statistics and tables
data.groupby(['cylinders']).mpg.describe()

# gives table of 5 rows x 95 columns
pivot_table = data.pivot_table(index='cylinders', columns='acceleration', values='mpg', aggfunc=np.mean)
pivot_table.head()

# plotting using matplotlib and seaborn
# despine function removes chart "junk"

#histogram
p = plt.hist(data.mpg)
plt.title("MPG")
p
sns.despine()

#linear fit scatterplot
sns.lmplot("mpg", "weight", data);

#nonlinear fit scatterplot
sns.lmplot("mpg", "weight", data, order=2);

# linear fit scatterplot with histogram on outer edges
sns.jointplot("mpg", "weight", data, kind="reg")

# boxplot
sns.boxplot(data[['displacement', 'horsepower']])

#violin plot
sns.violinplot(data[['displacement', 'horsepower']])

# facet grid
g = sns.FacetGrid(data, col="cylinders")
g.map(plt.hist, "mpg");