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





#series data method:
# s= pd.Series([0,10,20,30,40,50,60,70,80,90,100])

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
# s= pd.Series([0,10,20,30,40,50,60,70,80,90,100,None])
# .isna() → True for NaN
# .notna() → True for non-NaN
# print(s.isna()) 

# # .astype() Change data type 
# Can convert to str, category, bool
# Useful before computations that require specific types
# print(s.astype(float))

# # .copy() Create independent copy
# copyS= s.copy() 
# print(copyS)

# # .map() Apply a function element-wise to the Series.Can map dicts or Series to replace values:
# A lambda is a one-line function. lambda input : output eg lambda input : output 
# series.map(lambda x: expression)
# s = pd.Series([1, 2, None, 4])
# print(s.map(lambda x: x * 2))
# output :
# 0    2.0
# 1    4.0
# 2    NaN
# 3    8.0
# dtype: float64
# Differen ways of using map
# 1️⃣ Using a named function:
# Step 1: Define a function
# def double(x):
#     return x * 2
# Step 2: Pass function to map
# s.map(double)

# 2️⃣ Using lambda
# s.map(lambda x: x * 2)

# 3️⃣ Using a dictionary (lookup / replace)
# s = pd.Series(['low', 'medium', 'high'])
# s.map({
#     'low': 1,
#     'medium': 2,
#     'high': 3
# })

# 4️⃣ Using another Series (lookup table)
# keys = pd.Series(['a', 'b', 'c'])

# values = pd.Series(
#     [10, 20, 30],
#     index=['a', 'b', 'c']
# )
# keys.map(values)

# 5️⃣ Function with condition (named, not lambda)
# def even_or_odd(x):
#     if x % 2 == 0:
#         return 'even'
#     return 'odd'
# s.map(even_or_odd)

# 6️⃣ Function returning different data type
# def to_string(x):
#     return f"Value: {x}"

# s.map(to_string)

# 7️⃣ Mapping strings (common real use)
# s = pd.Series([' apple ', ' banana '])
# def clean(text):
#     return text.strip().upper()

# s.map(clean)

# 8️⃣ Handling missing values explicitly
# def safe_double(x):
#     if pd.isna(x):
#         return 0
#     return x * 2
# s.map(safe_double)



# # .apply() Apply a function element-wise (more flexible than map).
# Difference from .map()
# .map() → element-wise, simpler
# .apply() → works with functions returning more complex outputs 
# s = pd.Series([1,2,3])
# s2 = s.apply(lambda x: x**2)
# print(s2)


# # .replace() : Replace specific values with new ones.
# s = pd.Series([1,2,3,2])
# s2 = s.replace(2, 20)
# print(s2)
# 0     1
# 1    20
# 2     3
# 3    20
# dtype: int64

# # .duplicated() Detect duplicate values. Returns boolean Series.
# s = pd.Series([1,2,2,3])
# print(s.duplicated())
#output :
# 0    False
# 1    False
# 2     True
# 3    False
# dtype: bool
 

# # .drop_duplicates() Remove duplicates, keep first (or last).
# Useful for data cleaning and removing repeated entries
# s2 = s.drop_duplicates()
# print(s2)
#output :
# 0    1
# 1    2
# 3    3
# dtype: int64


# # .reset_index() Reset Series index to default integers.
# s = pd.Series([10,20,30], index=['a','b','c'])
# s_reset = s.reset_index(drop=True)
# print(s_reset)
# drop=True removes old index entirely
# Returns new Series by default


# # .set_axis() Assign a new index (or axis labels) to the Series.
# s = pd.Series([10,20,30])
# s_new = s.set_axis(['x','y','z'], axis=0)
# print(s_new)

# # .rename() Rename Series or its index labels. 
# s = pd.Series([10,20,30], index=['a','b','c'])
# s2 = s.rename({'a':'x','b':'y'})
# print(s2)




# Dataframe methods
#A. Creating & Structure

# pd.DataFrame()
# create a Dataframe
df= pd.read_csv('files/final.csv')
# print(df) #output: give table but not all data

# .copy()
# Creates an independent copy.
# df2 = df.copy()

# B. Inspecting Data
# .head(n)
# print(df.head()) #shows first five rows
# print(df.head(7)) #shows first n rows
# .tail(n)
# print(df.tail()) #shows last 5 rows
# print(df.tail(7)) #shows last n rows
# .info() #Structure, dtypes, null counts.
# df.info()
#output:
# <class 'pandas.core.frame.DataFrame'>
# Index: 966 entries, 0 to 966
# Data columns (total 9 columns):
#  #   Column      Non-Null Count  Dtype 
# ---  ------      --------------  ----- 
#  0   Unnamed: 0  966 non-null    int64 
#  1   label       966 non-null    object
#  2   url         966 non-null    object
#  3   brand       966 non-null    object
#  4   name        966 non-null    object
#  5   price       966 non-null    object
#  6   skin type   966 non-null    object
#  7   concern     966 non-null    object
#  8   img         966 non-null    object
# dtypes: int64(1), object(8)
# memory usage: 75.5+ KB
#we can use column like df['price']
#object in pandas usually means text (string). 
# .describe() #Summary statistics.
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

# # .shape #Rows and columns count.
# print(df.shape)
#output:
# (966, 9)
# That means:
# 966 rows
# 9 columns
# # .columns #Column names.
# print(df.columns)
#output:
# Index(['Unnamed: 0', 'label', 'url', 'brand', 'name', 'price', 'skin type',
#        'concern', 'img'],
#       dtype='object')
# # .index #Row index.
# print(df.index)
#output:
# Index([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
#        ...
#        957, 958, 959, 960, 961, 962, 963, 964, 965, 966],
#       dtype='int64', length=966)
# # .dtypes #Data types of columns.
# print(df.dtypes)
#ouput:
# Unnamed: 0     int64
# label         object
# url           object
# brand         object
# name          object
# price         object
# skin type     object
# concern       object
# img           object
# dtype: object

# # C. Selection & Indexing
# # .loc[] #Label-based selection.
# # .loc[] is used to access rows and columns by their labels (names), not by their numerical position.
# # You can pass row labels, column names, slices of labels, or boolean conditions.
# #syntax: df.loc[row_label, column_label]

# # .iloc[]  #Position-based selection.
# # .iloc[] works like a normal Python index: by row and column positions, integers only.
# # Useful when you don’t know labels or they are not integers.
# # Syntax:
# # df.iloc[row_index, column_index]
# # eg: 
# # .at[]   #Fast scalar access (label).


# # .iat[]  #Fast scalar access (position).


# # D. Cleaning & Missing Data
# # .isna() / .notna() : Detect missing values.
# df.isna()
# df.notna()

# # .dropna() :Remove rows/columns with NaN.
# df.dropna()

# # .fillna(value) : Fill missing values.
# df.fillna("Shine")

# #.replace() : Replace values.
# df.replace(0, None)



# # 🔁 E. Sorting & Ordering
# # .sort_values() : Sort by column.
# df.sort_values('A')

# # .sort_index() : Sort by index.
# df.sort_index()

# # F. Filtering & Boolean Logic
# df[df['A'] > 10]

# # .query() : SQL-like filtering.
# df.query('A > 10')


# # 🔄 G. Applying Functions
# # .map() (Series-level)
# df['A'].map(lambda x: x * 2)
 
# # .apply() : Apply function row/column-wise.
# df.apply(sum)

# # .applymap()
# # Apply to every cell.
# df.applymap(str)


# # H. Aggregation & Statistics
# # .sum(), .mean(), .min(), .max()
# df.sum()
# df.mean()
# df.min()
# df.max()
# # .count() #Count non-null.
# df.count()
# # df.value_counts() : Frequency counts (Series).
# df['A'].value_counts()


# # 🧱 I. Grouping
# # .groupby() Split → Apply → Combine.
# df.groupby('category')['price'].mean()


# # 🔗 J. Combining DataFrames
# # .merge(): SQL-style join.
# # pd.merge(df1, df2, on='id')

# # .join(): Join on index.
# # df1.join(df2)

# # .concat():  Stack DataFrames.
# # pd.concat([df1, df2])

# # K. Index Management
# # .set_index() :Set column as index.
# df.set_index('id')

# # .reset_index() : Reset index.
# df.reset_index()

# # .rename() : Rename columns/index.
# df.rename(columns={'A':'age'})


# # L. Duplicates
# # .duplicated() :Detect duplicates.
# df.duplicated()

# # .drop_duplicates() : Remove duplicates.
# df.drop_duplicates()


# # M. Type Handling
# # .astype() : Change data type.
# # df['A'] = df['A'].astype(float)


# # N. Input / Output
# # .to_csv() : Save to CSV.
# # df.to_csv('data.csv')

# # pd.read_csv(): Load CSV
# # pd.read_csv('data.csv')


