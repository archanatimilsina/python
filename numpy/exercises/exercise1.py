# practicing 20 problems

# 1. Create an array
# Create a 1D NumPy array with values [1, 2, 3, 4, 5].
#answer
# import numpy as np
# one_d_array= np.array([
#     1,2,3,4,5
# ])
# print(one_d_array)



# 2. Check type and shape
# Print the type and shape of the array from #1.
#answer
# import numpy as np
# one_d_array= np.array([
#     1,2,3,4,5
# ])
# print(one_d_array)
# print(f"Shape of the one_d_array:{one_d_array.shape}")
# print(f"Type of the one_d_array{type(one_d_array)}")


# 3. Create a 2D array
# Create a 2x3 array:
# [[1, 2, 3],
#  [4, 5, 6]]
#answer
# import numpy as np
# two_d_Array= np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(f"2*3 array: {two_d_Array}")


# 4. Access elements
# From the array in #3, print the element in row 1, column 2.
# import numpy as np
# two_d_Array= np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# # print(f"Element in the row1, column2 is {two_d_Array[0,1]}") #row1 and column2 i.e 2
# print(two_d_Array[0,0]) #1
# print(two_d_Array[0,1]) #2
# print(two_d_Array[0,2]) #3
# print(two_d_Array[1,0]) #4
# print(two_d_Array[1,1]) #5
# print(two_d_Array[1,2]) #6
#note row indices 0 and 1
# column indices 0 1 2 


# 5. Slice rows
# From the array in #3, print the first row.
# import numpy as np
# two_d_Array= np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(f"First row is {two_d_Array[0 ,:]}") #output : First row is [1 2 3]
# print(f"Second row is {two_d_Array[1 ,:]}") #output : Second row is [4 5 6]


# eg two_d_array[row , column]
# two_d_array[ 0  ,   :   ]
# Read it as:
#     “Give me row 0, and give me all columns from that row.”
# 3 D slicing for that you should have 
# array[start:stop for row  , start:stop for column]
# print(two_d_Array[0:1, 0:1]) #output : [[1]]
# General slicing format:
# array[ row_start : row_stop , col_start : col_stop ]
# Rule you must lock into memory
# Start index is INCLUDED
# Stop index is EXCLUDED
# This rule applies to both rows and columns.
#         Col 0   Col 1   Col 2
# Row 0 →   1       2       3
# Row 1 →   4       5       6



### **6. Slice columns**
# - From the array in #3, print the **second column**.
# import numpy as np
# two_d_Array= np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(two_d_Array[:,1:2])
# #output:
# [[2]
#  [5]]


### **7. Shape and reshape**
# - Reshape the array `[1,2,3,4,5,6]` into a **2x3 array**.
# When reshaping, the total number of elements must stay the same.
# Original array → 6 elements
# Target shape → 2 x 3 = 6 elements ✅
# If the numbers don’t match, NumPy will raise an error.
# reshaped = arr.reshape(2, 3)
# print(reshaped)
# import numpy as np
# arar= np.array([1,2,3,4,5,6])
# reshaped_arar = arar.reshape(2,3)
# print(reshaped_arar)
# #output:
# [[1 2 3]
#  [4 5 6]]


### **8. Create zeros and ones**
# - Create a **3x3 array of zeros**.
# - Create a **2x4 array of ones**.

# np.full(shape, fill_value)
#     shape → tuple (rows, columns)
#     fill_value → the number you want every element to be
# arar_zeros= np.zeros((row,column))
# arar_zeros= np.zeros((row,column),dtype= int/float)
# arar_ones= np.ones((row,column))
# arar_ones= np.ones((row,column),dtype= int/float)

# - Create a **3x3 array of zeros**.
# import numpy as np
# arar_zeros= np.zeros((3,3))
# print(arar_zeros)
#output: 
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# arar_zeros= np.zeros((3,3),dtype = int)
# print(arar_zeros)
#output:
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]


# - Create a **2x4 array of ones**.
# arar_ones= np.ones((2,4))
# print(arar_ones)
# #output :
# # [[1. 1. 1. 1.]
# #  [1. 1. 1. 1.]]

# arar_ones= np.ones((2,4),dtype= int)
# print(arar_ones)
#output:
# [[1 1 1 1]
#  [1 1 1 1]]



### **9. Create random arrays**
# - Create a **3x3 array with random integers from 0 to 9**.
# import numpy as np
# rand_int_array = np.random.randint(low=0, high=10,size=(3,3))
# print(rand_int_array)
#output :
# [[8 9 2]
#  [0 8 1]
#  [4 6 5]]

# - Create a **2x2 array with random floats between 0 and 1**.
# rand_float_array = np.random.rand(2,2)
# print(rand_float_array)
#output:
# [[0.75579059 0.1925682 ]
#  [0.29822068 0.98105081]]

### **10. Array arithmetic**
# - Add 10 to every element in `[1,2,3,4]`.
# - Multiply every element by 2.
# import numpy as np
# given_array= np.array([1,2,3,4])

# # - Add 10 to every element in `[1,2,3,4]`.
# added_array = given_array + 10
# print(added_array)

# # - Multiply every element by 2.
# multiplied_array = given_array *2
# print(multiplied_array)
# Operation	        Example	          Output
# Addition	         arr + 5	       [6 7 8 9]
# Subtraction	     arr - 2	       [-1 0 1 2]
# Multiplication	 arr * 3	       [3 6 9 12]
# Division	         arr / 2	       [0.5 1.0 1.5 2.0]
# Floor division	 arr // 2	       [0 1 1 2]
# Modulus	         arr % 2	       [1 0 1 0]
# Exponentiation	 arr ** 2	       [1 4 9 16]
# Negation	         -arr	           [-1 -2 -3 -4]


### **11. Element-wise operations**
# - Create arrays `a = [1,2,3]` and `b = [4,5,6]`.
# - Compute `a + b`, `a * b`, and `a - b`.

# import numpy as np
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# add = a+b
# print(add)
# subtract = a - b
# print(subtract)
# multiply = a*b
# print(multiply)

# 2. Basic element-wise operations
# Operation	                         Syntax            	Result
# Addition	                        a + b	             [5 7 9]
# Subtraction	                    a - b	             [-3 -3 -3]
# Multiplication	                a * b	             [4 10 18]
# Division	                        a / b	             [0.25 0.4 0.5]
# Floor division	                a // b	             [0 0 0]
# Modulus	                        a % b	             [1 2 3]
# Exponent	                        a ** b	             [1 32 729]
# Negation	                        -a	             [-1 -2 -3]


### **12. Dot product**
# - Compute the **dot product** of `a` and `b`.

# Matrix multiplication (@ or np.dot)
# Matrix multiplication uses linear algebra rules:
# (m x n) @ (n x p) → result shape (m x p)
# Each element in the result is the dot product of a row from the first matrix and a column from the second
# import numpy as np

# a = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])

# b = np.array([[9,8,7],
#               [6,5,4],
#               [3,2,1]])

# matrix_mult = a @ b
# print(matrix_mult)


### **13. Sum, min, max**
# - For array `[1,2,3,4,5]`, find:
#     - Sum of elements
#     - Minimum value
#     - Maximum value
# import numpy as np
# araay= np.array([1,2,3,4,5])
# araay = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ])
# araay_sum= np.sum(araay)
# print(araay_sum) #output: 15
# araay_min = np.min(araay)
# print(araay_min) #o/p : 5
# araay_max= np.max(araay)
# print(araay_max) #o/p: 5





# 3. Compute the standard deviation
# Use np.std():
# std_value = np.std(arr)
# print("Standard Deviation:", std_value)
# How it’s calculated:
# Subtract mean from each element → deviations:
# [1-3, 2-3, 3-3, 4-3, 5-3] = [-2, -1, 0, 1, 2]
# Square each deviation:
# [-2^2, -1^2, 0^2, 1^2, 2^2] = [4, 1, 0, 1, 4]
# Compute mean of squared deviations:
# (4+1+0+1+4)/5 = 10/5 = 2
# Take square root → sqrt(2) ≈ 1.4142
# Output:
# Standard Deviation: 1.4142135623730951

### **14. Mean and standard deviation**
# - For array `[1,2,3,4,5]`, compute the **mean** and **standard deviation**.
# import numpy as np
# araay = [1,2,3,4,5]
# araay_mean= np.mean(araay)
# print(araay_mean)
# araay_std = np.std(araay)
# print(araay_std)

### **12. Dot product**
# - Compute the **dot product** of `a` and `b`.

import numpy as np
a= np.array([
    [1,2,3],
    [4,5,6]
]) #2*3 matrix
b= np.array([
    [1,2,3],
    [7,8,9],
    [1,2,3]
]) # 3*3 matrix
array_multiple = a @ b
print(array_multiple) 
#op:
# [[18 24 30]
#  [45 60 75]] #2*3 matrix