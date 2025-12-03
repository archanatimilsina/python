# string type 
# x= "Hello World"
# print(type(x))
# # output: <class 'str'>


# x= 2
# print(type(x))
# print(x)
# # output:<class 'int'>


# x= 2.5
# print(type(x))
# print(x)
# # # output:<class 'float'>

#list
# x= ["apple", "banana", "mango"]
# print(type(x))
# print(x)
# # # output:<class 'list'>

# #set
# x= {"apple", "banana", "mango" }
# print(type(x))
# print(x)
# # # output:<class 'set'>

# #tuple
# x= ("apple", "banana", "mango")
# print(type(x))
# print(x)
# # # output:<class 'tuple'>

#range:  a lazy sequence of numbers
# x= range(6)
# print(type(x))
# print(x) #output : range(0, 6)
# # # output:<class 'range'>

#dictionary : key-value pair storage
# x= {"Name": "Archana", "Surname": "Timilsina"}
# print(type(x))
# print(x) #output: 
# # # output:<class 'dict'>

#frozenset: an immutable set
# Sometimes you need the set behavior (unique items, membership test), but also want
#  it to be locked so it’s safe to use as a dictionary key or part of another set.
# x= frozenset({"apple", "banana", "mango" })
# print(type(x))
# print(x)
# # # output:<class 'frozenset'>

#bytes :immutable raw byte data
# x= b"Hello World"
# print(type(x))
# print(x[1])
# output : 101
# # # output:<class 'bytes'>

#bool :True or False
# x= True
# print(type(x))
# print(x)
# # # output:<class 'bool'>

#bytearray :mutable raw byte buffer
# You need raw bytes but also want to modify them.
# x=b'Hello'
# ba= bytearray(x)
# print(ba[1])
# print(type(x))
# # # output:<class 'bytearray'>

#memoryview: a “window” into memory without copying
# x= memoryview(bytes(5))
# print(x)
# print(type(x))
# # # output:<class 'memoryview'>

#noneType: represents “no value”
# A special singleton object that means…
# no value
# empty
# not returned
# missing
# x= None
# print(type(x))
# # print(x)
# # # output:<class 'NoneType'>

#complex: A number with a real part and an imaginary part.
# x= 1j
# print(type(x))
# print(x)
# # output:<class 'complex'>
