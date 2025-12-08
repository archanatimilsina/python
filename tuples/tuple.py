
# #tuple
# tuples= (3.02,4.03)
# print(tuples)


# #methods of tuple
# #count(element) returns count of any element
# print(tuples.count(3.02))

# #index(element) returns the index of an element
# print(tuples.index(3.02))

#concatenate two tuples
# tuple1=("Hello","world")
# tuple2= ("This", "is","Archana")
# print(tuple1 + tuple2)

#Even though tuples only have two methods, Python gives you a toolkit outside the tuple object to work with them.
# t=("Apple", "banana","Mango","strawberry")

# • Indexing
# t[0]
# print(t[0]) #output: Apple

# # • Slicing
# # t[1:4]
# print(t[0:2]) #output:('Apple', 'banana')

# # • Concatenation
# print((1, 2) + (3, 4) )   #output: (1, 2, 3, 4)

# # • Repetition
# print(("a","b") * 3 )      #output: ('a', 'b', 'a', 'b', 'a', 'b')

# • Unpacking
# x, y = (10, 20)
# print(x)  #output:10
# print(y)  #output:20


# • Nested structures => # inner list is mutable, outer tuple is not
# t = (1, (2, 3), [4, 5])   
# x= t[2]
# x.append(6)
# print(t)
#output : (1, (2, 3), [4, 5, 6])


# (x,y,*z)= ("Apple", "banana","Mango","strawberry")
# print(x) #output:Apple
# print(y) #output:banana
# print(z) #output:['Mango', 'strawberry']

#way of changing the tuple even it is a immutable
# t=("Apple", "banana","Mango","strawberry")
# y= list(t)
# print(y) #output: ['Apple', 'banana', 'Mango', 'strawberry']
# y.append("watermeleon")
# t=tuple(y)
# print(y) #output: ['Apple', 'banana', 'Mango', 'strawberry', 'watermeleon']

#the way of adding item to any tuple by creating another tuple and joining them
