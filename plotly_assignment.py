# -*- coding: utf-8 -*-
"""Plotly_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XHxzqhfJfbv79GZMIAHBVayEzrtCCvm-

Q1. Load the "titanic" dataset using the load_dataset function of seaborn. Use Plotly express to plot a
scatter plot for age and fare columns in the titanic dataset.
"""

'''Answer(1)'''
import seaborn as sns
titanic=sns.load_dataset("titanic")
titanic

'''Answer(1)'''
import plotly.graph_objects as go
fig=go.Figure()
fig.add_trace(go.Scatter(x=titanic.age,y=titanic.fare,mode='markers'))
fig.show()

"""Q2. Using the tips dataset in the Plotly library, plot a box plot using Plotly express."""

'''Answer(2)'''
tips=sns.load_dataset('tips')    #loading the tips dataset in tips variable
tips

'''Answer(2)'''
import plotly.express as px
import seaborn as sns

# Loading the tips dataset
tips = sns.load_dataset("tips")

# Creating a box plot using Plotly Express
fig = px.box(
    tips,
    x="day",          # x-axis: Days of the week
    y="total_bill",   # y-axis: Total bill amounts
    color="sex",      # Color the boxes by "sex"
    title="Box Plot of Total Bill Amounts by Day and Sex"
)

# Customizing the layout
fig.update_xaxes(title_text="Day of the Week")
fig.update_yaxes(title_text="Total Bill Amount")

# Showing the plot
fig.show()

"""Q3. Using the tips dataset in the Plotly library, Plot a histogram for x= "sex" and y="total_bill" column in
the tips dataset. Also, use the "smoker" column with the pattern_shape parameter and the "day"
column with the color parameter.
"""

'''Answer(3)'''
fig=px.histogram(tips,         #tips dataset
                 x='sex',    #giving x-axis to sex column of tips dataset
                 y='total_bill',#giving y-axis to total_bill column of tips dataset
                 pattern_shape='smoker',       #pattern shape as smoker
                 color='day', #colored by day
                 labels={'sex':'Sex','total_bill':'Total_bill'},   #change the labels as Sex and Total_bill
                title="Histogram of Total Bill by Sex (colored by day) and Smoking Status",)   #and  the title of the plot

fig.show()   #showing the plot

"""Q4. Using the iris dataset in the Plotly library, Plot a scatter matrix plot, using the "species" column for
the color parameter.
"""

'''Answer(4)'''

import plotly.express as px
import pandas as pd

# Load the iris dataset from Plotly
df = px.data.iris()
df.head()

# Creating a scatter matrix plot
fig = px.scatter_matrix(
    df,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species",  # Using the "species" column for coloring
    title="Scatter Matrix Plot of Iris Dataset",
)

# Show the plot
fig.show()

"""Q5. What is Distplot? Using Plotly express, plot a distplot.

answer(6):
A distplot, short for "distribution plot," is a graphical representation used to visualize the distribution of a univariate dataset. It combines a histogram with a kernel density estimate (KDE) and, optionally, rug plots. A distplot can be useful for understanding the underlying distribution of a dataset, including its central tendency, spread, and shape
"""

'''Answer(6)'''
import plotly.express as px
import pandas as pd

# Create a sample dataset
data = pd.Series([1.2, 2.3, 2.1, 3.5, 2.8, 3.2, 1.9, 2.5, 3.7, 2.4, 1.6, 2.0, 3.0, 3.1, 1.8, 2.6])

# Create a distplot using Plotly Express
fig = px.histogram(
    data,
    nbins=10,  # Number of bins for the histogram
    marginal="rug",  # Include rug plots on the sides
    title="Distplot Example",
)

# Shows the plot
fig.show()

