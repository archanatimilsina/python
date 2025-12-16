#import pandas here at top
import pandas as pd


#install pandas using: pip install pandas
#if you get err like this zsh: command not found: pip you can instead do this : python3 -m pip install pandas(mac)
# print(pd.__version__) #output : 2.3.3


#Series: A Series is essentially a one-dimensional labeled array capable of holding any data type: 
# integers, floats, strings, Python objects, even lists. “Series = data + index”
# series= pd.Series([10,20,30])
# print(series)
 #output:
# 0    10
# 1    20
# 2    30
# dtype: int64

# Custom index for series: 
# series =pd.Series([10,20,30],index= ['a','b','c'])
# print(series) 
#output:
# a    10
# b    20
# c    30
# dtype: int64 
#length should be matched

#Creating a Series: Different Methods
# Method 1: From a Python list
# s = pd.Series([1, 2, 3, 4])
# print(s)

# Method 2: From a NumPy array
# import numpy as np
# arr = np.array([5, 10, 15])
# s = pd.Series(arr)
# print(s)

# Method 3: From a dictionary
# data = {'x': 100, 'y': 200, 'z': 300}
# s = pd.Series(data)
# print(s)

# Method 4: Scalar value
# s = pd.Series(0, index=['a','b','c'])
# print(s)
#output:
# a    0
# b    0
# c    0
# dtype: int64

#DataFrame: A DataFrame is a two-dimensional labeled data structure with:
# Rows → each with a label (index)
# Columns → each a Series with a label (column name)
# Cells → values, can be mixed types (int, float, string, bool, datetime, objects)

# Creating a DataFrame
# Method 1: From a dictionary of lists
# import pandas as pd
# data = {
#     'name': ['Alice', 'Bob', 'Charlie'],
#     'age': [25, 30, 35],
#     'city': ['Kathmandu', 'Pokhara', 'Lalitpur']
# }
# df = pd.DataFrame(data)
# print(df)

#output:
#       name  age      city
# 0    Alice   25  Kathmandu
# 1      Bob   30    Pokhara
# 2  Charlie   35   Lalitpur
# Custom index:
# df = pd.DataFrame(data, index=['a','b','c'])
# print(df)

# Method 2: From a list of dictionaries
# data = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 30, 'city': 'Pokhara'},
#     {'name': 'Charlie', 'city': 'Lalitpur'}
# ]

# df = pd.DataFrame(data)
# print(df)
# Output:
#       name   age      city
# 0    Alice  25.0       NaN
# 1      Bob  30.0   Pokhara
# 2  Charlie   NaN   Lalitpur

# Method 3: From a dictionary of Series
# s1 = pd.Series([1,2,3], index=['a','b','c'])
# s2 = pd.Series([4,5,6], index=['a','b','c'])

# df = pd.DataFrame({'X': s1, 'Y': s2})
# print(df)

# Method 4: From a 2D NumPy array
# import numpy as np

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# df = pd.DataFrame(arr, columns=['A','B','C'])
# print(df)


# Method 5: From a scalar value
# df = pd.DataFrame(0, index=[0,1,2], columns=['A','B','C'])
# print(df)



# df= pd.read_csv('files/final.csv')
# print(df) #output: give table but not all data
# print(df.head()) #shows first five rows
# print(df.head(7)) #shows first n rows
# print(df.tail()) #shows last 5 rows
# print(df.tail(7)) #shows last n rows
# print(df.describe()) #Works on DataFrames, summarizing each numeric column.
#output:
#        Unnamed: 0
# count  966.000000
# mean   483.480331
# std    279.037927
# min      0.000000
# 25%    242.250000
# 50%    483.500000
# 75%    724.750000
# max    966.000000


#series data method:
s= pd.Series([0,10,20,30,40,50,60,70,80,90,100])

# .head(n) First n elements 
# print(s.head())
# print(s.head(7))

# .tail(n) Last n elements 
# print(s.tail())
# print(s.tail(7))

# # .describe() Summary statistics (numeric) 
# print(s.describe())

# # .unique() Unique values 
# print(s.unique())

# # # .nunique() Count of unique values 
# print(s.nunique())

# # # .value_counts() Frequency counts 
# print(s.value_counts())

# # .sort_values() Sort by values 
# print(s.sort_values())
# # .sort_index() Sort by index 
# print(s.sort_index())
# # .isna() / .notna() Detect missing values 
# print(s.isna())
# # .astype() Change data type 
# print(s.astype(float))
# # .copy() Create independent copy
# copyS= s.copy() 
# print(copyS)
# # .map() Apply function element-wise 

# # .apply() Apply function element-wise (more flexible) 

# # .replace() Replace specific values 

# # .duplicated() Detect duplicates 

# # .drop_duplicates() Remove duplicates 

# # .reset_index() Reset index to default integer index 

# # .set_axis() Assign new index 

# # .rename() Rename Series or its index labels explain all of these
