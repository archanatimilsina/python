
#set
# Unordered – Python does not keep the elements in the order you add them.
# Mutable – you can add or remove elements.
# A collection of unique elements (no duplicates allowed).

# set1= {"hello", "world"}
# print(set1) #output : {'world', 'hello'}
# # "hello" and "world" are stored in set1.
# # The set doesn’t remember the order in which they were added.

# set1= {"hello", "world","hello"} #gives {'world', 'hello'}

# Python sets are implemented as hash tables.
# The position of each element in a set depends on its hash value, not the order you typed them.
# So when Python prints a set, it shows the elements in an arbitrary order, which can seem random.

# set2={ "hello","World","Hello","world"}
# print(set2)

set1={"Apple","Banana","strawberry","watermeleon","mango"}
#lists of method of set

#add(x)
# set1.add('pomegranate')
# print(set1) #output: {'Banana', 'watermeleon', 'mango', 'strawberry', 'pomegranate', 'Apple'}

#update(iterable)
# This behaves like extend() for lists, but without preserving duplicates.
#extending with list
# listy= ["guava","litchii","orange"]
# set1.update(listy)
# print(set1) #output:{'Apple', 'litchii', 'orange', 'mango', 'Banana', 'guava', 'watermeleon', 'strawberry'}

#extending with tuple
# listy= ("guava","litchii","orange")
# set1.update(listy)
# print(set1) #output:{'Apple', 'litchii', 'orange', 'mango', 'Banana', 'guava', 'watermeleon', 'strawberry'}


#extending with dictionary
# listy={
#     'shine': ["guava","litchii","orange"]
# }
# set1.update(listy)
# print(set1) #output:{'watermeleon', 'strawberry', 'Apple', 'shine', 'mango', 'Banana'}


#remove(x) #If the element doesn’t exist, Python raises KeyError.
# set1.remove("Apple") 
# print(set1) #output: {'mango', 'strawberry', 'watermeleon', 'Banana'}


#discard(x)  Deletes an element, but silently does nothing if it doesn’t exist.
# s = {1, 2}
# s.discard(10) #no err
# print(s)

#pop()  Removes and returns a random element (not truly random — but unpredictable, because sets have no fixed order).
# print(s.pop())

#clear() Empties the entire set.
# s = {1, 2, 3}
# s.clear()
# print(s) #output: set()
 

 