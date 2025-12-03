# import sys 
# print(sys.version)

#indentation
# i get err here bcz of indentation
# x="Hello World"
#   print(x)

#casting variable type
# x=int(3.56)
# print(x)

# x=float(3)
# print(x)

# x=str(3)
# print(x)
#output:
# 3
# 3.0
# 3
#why it doesn't throw the err assigning three times different data types it is bcz
# Python uses dynamic typing.The variable name doesn’t have a fixed type. The value you assign to it has a type.


#use of type(x)
# x=int(3.56)
# print(type(x))

# x=float(3)
# print(type(x))

# x=str(3)
# print(type(x))

# output
# <class 'int'>
# <class 'float'>
# <class 'str'>


#use of single quote and double quote
# x="Hello World"
# print(type(x))
# x='Hello World'
# print(type(x))
#output
# <class 'str'>
# <class 'str'>


#Python is case-sensitive
# class_name= "sign" #snake case 
# ClassName= "sign" #pascalcase
# className= "sign" #camelcase
# print(class_name)
# print(ClassName)
# print(className)
#lower camelCase => studentName
# Upper CamelCase (also called PascalCase) =>StudentName
# Snake Case =>student_name

#variable name can start with a letter or an underscore
# _pynam= "Hello world"
# print(_pynam)
# If you see:
# _var   => Internal use, but accessible.
# __var => A bit more strongly internal—name-mangled.
# _   => Value not meant to be used.
# __var__  => A Python-defined “magic” name.


#many values to multiple variables
# x,y,z=1,2,3
# print(x)
# print(y)
# print(z)
# Output:
# 1
# 2
# 3
# By default, print() ends with a newline character (\n).
# How to print in a single line
# Option 1: One print statement for all
# print(x, y, z) #Output: 1 2 3
# Option 2: Change the end parameter
# print(x, end=" ")
# print(y, end=" ")
# print(z)
# Output: 1 2 3
# Option 3: Format them into a string
# print(f"{x} {y} {z}") 
# Output: 1 2 3

#one value to multiplw variable
# x=y=z=1
# print(x)
# print(y)
# print(z)

# unpack a collection
#unpacking list
# fruits= ["apple", "banana", "mango"]
# x,y,z= fruits
# print(x)
# print(y)
# print(z)
# #unpacking tuple
# fruits= ("apple", "banana", "mango")
# x,y,z= fruits
# print(x)
# print(y)
# print(z)
# #unpacking set
# fruits= {"apple", "banana", "mango"}
# x,y,z= fruits
# print(x)
# print(y)
# print(z)

#printing multiple variables
# fruits= {"apple", "banana", "mango"}
# x,y,z= fruits
# print(x,y,z)
# when i was printing it multiple times i get a magic called unordered set magic 
# i get different result whenever i try to run it 
# output:
# 1st run
# apple mango banana
# 2nd run
# mango banana apple
# 3rd run
# apple mango banana
# Python sets are unordered. A set does not maintain any fixed order. The order of a set changes between program runs. Each time you start Python, it uses a new random hash seed (for security).
# Sets use these hash values internally to decide where each element goes. Because the hash seed changes each run, the internal arrangement of the set also changes. Sets should not be used when order matters.
# x, y, z = sorted(fruits) If you need a guaranteed order for unpacking, convert the set to a list or sort it: 
# x, y, z = sorted(fruits)
# print(x,y,z)
# Ouptut : it works => gives same no matter how many times you run 


#concatenate multiple variables
# fruits= {"apple", "banana", "mango"}
# x,y,z= fruits
# print(x+ y+ z)
#output: 

#global and local scope of a variable
# x="I am a global variable"
# def helloWorld():
#     y="I am a Local variable"
#     print(x)
#     print(y)
# helloWorld()
# x is a global var and y is local variable 

# x="I am a global variable"
# def helloWorld():
#     y="I am a Local variable"
#     print(x)
#     print(y)
# helloWorld()
# print(y) gives err bcz y is local-scoped
# but we can make it global using global keyword
# x="I am a global variable"
# def helloWorld():
#    global y
#    y= "I am a Local variable"
# #    You cannot write global y = "something"
#    print(x)
#    print(y)
# helloWorld()
# print(y) => gives I am a global variable
# I am a Local variable
# I am a Local variable


