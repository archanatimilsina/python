
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
 
#set operation
# union(*others)  Returns a new set containing items from all sets.
# Equivalent to |
# a = {1, 2}
# b = {2, 3}
# print(a.union(b))        # {1, 2, 3}
# print(a|b)   # {1, 2, 3}


# intersection(*others) Common elements only.
# Equivalent to &.
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.intersection(b) )   # {2, 3}
# print(a&b)   # {2, 3}


# difference(*others) Elements in the first set but not in the others.
# Equivalent to -.
# a = {1, 2, 3}
# b = {2, 3}
# print(a.difference(b)) # {1}
# print(a-b) # {1}


# symmetric_difference(other) Elements that are in either set, but not in both.
# Equivalent to ^.
# a = {1, 2}
# b = {2, 3}
# print(a.symmetric_difference(b))     # {1, 3}
# print(a^b)     # {1, 3}


# update()
# Explained above (like union but modifies).
# intersection_update(*others)
# Keeps only the items that are also in the other sets.
# a = {1, 2, 3}
# b = {2, 3}
#print(a.intersection_update(b) )  # a becomes {2, 3}

# difference_update(*others)
# Removes elements found in the other sets.
# a = {1, 2, 3}
# b = {2}
#print(a.difference_update(b))      # {1, 3}


# symmetric_difference_update(other)
# Replaces the set with the symmetric difference.
# a = {1, 2}
# b = {2, 3}
# print(a.symmetric_difference_update(b))   # a becomes {1, 3}


# Relationship-checking methods
# These don’t modify anything. They answer structural questions.

# issubset(other)
# True if every element of one set appears in the other.
# print({1, 2}.issubset({1, 2, 3}))    # True

# issuperset(other)
# True if the set contains all elements of the other.
#print({1, 2, 3}.issuperset({1, 2}))   # True

# isdisjoint(other)
# True if the two sets share no elements.
#print({1, 2}.isdisjoint({3, 4}))    # True


# add, update, remove, discard, pop, clear, union, intersection, difference, symmetric_difference, 
# intersection_update, difference_update, symmetric_difference_update, issubset, issuperset, isdisjoint


