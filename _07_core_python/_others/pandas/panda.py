"""
Pandas is a Python library.
Pandas is used to analyze data.

Pandas:
Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis"
and was created by Wes McKinney in 2008.

Use Pandas:
Pandas allows us to analyze big data and make conclusions based on statistical theories.
Pandas can clean messy data sets, and make them readable and relevant.
Relevant data is very important in data science.

What Can Pandas Do?
Panda gives you answers about the data.
Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?
Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values.
This is called cleaning the data.



"""

# how to import pandas
import pandas as pd

# check panda version
print("pandas Version:", pd.__version__)

x = {
    'bikes': ["Duke", "splendor", "pulsar", "yamaha rx100"],
    'mileage': [25, 65, 45, 50]
}
y = pd.DataFrame(x)

print(y)

"""
Series in pandas:
A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.
"""
print("Series in Pandas")
x = [1, 2, 3, 4, 5]
y = pd.Series(x)
print(y)

"""
Labels:
     the values are labeled with their index number. First value has index 0, second value has index 1 etc.
This label can be used to access a specified value.
"""
print("specific value")
print(y[3])

"""
Create Labels
With the index argument, you can name your own labels.
"""
print("assigning index name to value")
y = pd.Series(x, index=['a', 'b', 'c', 'd', 'e'])
print(y)
print(y['c'])

"""
Key/Value Objects as Series
You can also use a key/value object, like a dictionary, when creating a Series.

"""
# Dictionary
x = {'Name': 'Amarnath', 'Age': 30, 'Education': 'B.Tech', 'job': 'Technical Engineer'}
y = pd.Series(x)
print(y)

y = pd.Series(x, index=['Name', 'job'])
print("Requesting Dictionary Keys \n", y)

"""
DataFrames
Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
Series is like a column, a DataFrame is the whole table
"""

print("***** DataFrames *****")
x = {
    'Name': ['Amarnath', 'Viveka', 'Lavi', 'Vani', 'Shanwik'],
    'Age': [30, 27, 22, 25, 1]
}
y = pd.DataFrame(x)

print(y)

"""
Locate Row:
the DataFrame is like a table with rows and columns.
Pandas use the loc attribute to return one or more specified row(s)
"""
print("***** Locate Row *****")
print(y.loc[2])
print(y.loc[2:4])

"""
Read CSV Files:
A simple way to store big data sets is to use CSV files (comma separated files).
CSV files contains plain text and is a well know format that can be read by everyone including Pandas.
"""
print("\n\n\n****** Read CSV file ******")
x = pd.read_csv('QFI_AP Master sheet.csv')
print(x)

"""
Viewing the Data:
One of the most used method for getting a quick overview of the DataFrame, is the head() method.
The head() method returns the headers and a specified number of rows, starting from the top.
"""
print("\n\n\n******* Head Method ******")
print(x.head(10))
"""
The tail() method returns the headers and a specified number of rows, starting from the bottom.
"""
print("\n\n\n******* tail Method ******")
print(x.tail(10))


