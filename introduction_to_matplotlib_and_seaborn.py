# -*- coding: utf-8 -*-
"""Introduction To Matplotlib And Seaborn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VY70_Izj4VAK3l14bCow_SUN_P3PqZCO

# Introduction To Matplotlib And Seaborn
"""

pip install matplotlib

import matplotlib.pyplot as plt

# Data
x = [1,2,3,4,5]
y = [2,3,5,7,11]

# Create a line plot
plt.plot(x, y, ls = ':',color = '#BD4025', linewidth = '3', marker = '*', mec = 'r',ms = '10')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple line plot')
plt.show()

import numpy as np

y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])
plt.plot(y1)
plt.plot(y2)
plt.show()

import matplotlib.pyplot as plt

# Data
x = [1,2,3,4,5]
y = [2,3,5,7,11]

# Create a scatter plot
plt.scatter(x, y, color = 'r')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple line plot')
plt.show()

"""Creating simple bar plot with matplot lib"""

# Data
products = ['PC', 'TV', 'Ref', 'Micro']
sales = [4,7,1,8]

# Creating a bar plot
plt.barh(products, sales, color = 'black', height = 0.1)
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Simple bar plot')
plt.show()

"""Creating simple histogram with matplot lib"""

# Data
data = [1,2,2,3,3,3,4,4,4,4]

# Creating a histogram
plt.hist(data, bins = 4)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Simple Histogram')
plt.show()

"""Creating sub plots with Matplotlib"""

# Data
x = [1,2,3,4,5]
y1 = [2,3,5,7,11]
y2 = [1,4,6,8,10]

# Creating subplots
fig, axs = plt.subplots(2)

axs[0].plot(x, y1)
axs[0].set_title('First Plot')
axs[1].plot(x, y2, color = 'orange')
axs[1].set_title('Second Plot')

# Displaying the plot
plt.tight_layout()
plt.show()

"""Adding annotations with Matplotlib"""

# Data
x = [1,2,3,4,5]
y = [2,3,5,7,11]

# Creating a plot with annotations
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Annotations')
plt.annotate('Peak', xy=(5, 11), xytext=(4, 10),
             arrowprops=dict(color='black', shrink=0.05))
plt.show()

"""Create a Simple Line Plot with Seaborn

"""

import seaborn as sns
import matplotlib.pyplot as plt

# Data
x = [1,2,3,4,5]
y = [2,3,5,7,11]

# Creating a line plot
sns.lineplot(x=x, y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Scatter plot with Seaborn')
plt.show()

"""Creating a Simple Bar Plot with Seaborn"""

# Data
categories = ['A','B','C','D']
values = [4,7,1,8]

# Creating a bar plot
sns.barplot(x=categories, y=values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Simple Bar plot with Seaborn')
plt.show()

"""Creating a pair plot with Sea born"""

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
iris_data = sns.load_dataset("iris")

# Creating a pair plot
sns.pairplot(iris_data, hue = 'species')
plt.title('Pair Plot with Seaborn')
plt.show()

"""Create a asimple heatMap"""

import numpy as np

# Data
data = np.random.rand(10, 12)
sns.heatmap(data)
plt.title('Heatmap with Seaborn')
plt.show()