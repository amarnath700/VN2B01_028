"""
Empty Cells:
Empty cells can potentially give you a wrong result when you analyze data.

Remove Rows:
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.

"""
import pandas as pd

x = pd.read_csv('family.csv')
print(x)

y = x.dropna()
print(y.to_string())

print("***** Remove Empty Cell *****")
x.dropna(inplace=True)  # the dropna(inplace = True) will NOT return a new DataFrame,
# but it will remove all rows containing NULL values from the original DataFrame.
print(x.to_string())

"""
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:
"""
print("*****  Replacing null field *****")
x = pd.read_csv('family.csv')
x.fillna(25, inplace=True)
print(x.to_string())

"""
Replace Only For Specified Columns:
The example above replaces all empty cells in the whole Data Frame.
To only replace empty values for one column, specify the column name for the DataFrame

"""
x = pd.read_csv('family.csv')
print("*****  Replacing specity column field *****")
x['Age'].fillna(25, inplace=True)
print(x.to_string())
"""
Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column

"""
x = pd.read_csv('family.csv')
print("*****  Replacing Mean Method *****")
y = x['Age'].mean()  # Mean = the average value (the sum of all values divided by number of values)
x['Age'].fillna(y, inplace=True)
print(x.to_string())


"""
Median
"""
x = pd.read_csv('family.csv')
print("*****  Replacing Median Method *****")
y = x['Age'].median()  #
x['Age'].fillna(y, inplace=True)
print(x.to_string())


"""
Mode
"""
x = pd.read_csv('family.csv')
print("*****  Replacing Mode Method *****")
y = x['Age'].mode()[5]  # Mode = it depends upon index given to the mode
x['Age'].fillna(y, inplace=True)
print(x.to_string())


"""
Data of Wrong Format:
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
"""
x = pd.read_csv('Date.csv')
print("*****  Wrong Method *****")
#x['Date'] = pd.to_datetime(x['Date'])
#print(x.to_string())
