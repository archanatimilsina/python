# #list
# fruitList= ["Apple", "banana","mango","watermeleon"]
# print(fruitList)

# #looping through list
# for fruit in fruitList:
#     print(fruit)
#     # print(fruit+"is")


#all built-in lists of python
#append(x)
# fruitList= ["Apple", "banana","mango","watermeleon"]
# fruitList.append("Pomegranate")
# print(fruitList)

#extend(iterable)
# fruitList= ["Apple", "banana","mango","watermeleon"]
#extending list
# listy= ["shine","brighter"]
# fruitList.extend(listy)
# print(fruitList)
#output: ['Apple', 'banana', 'mango', 'watermeleon', 'shine', 'brighter']

#extending sets
# sets={1,2,3,4}
# fruitList.extend(sets)
# print(fruitList)
#output: ['Apple', 'banana', 'mango', 'watermeleon', 1, 2, 3, 4]

# #extending tuples
# tuples= ('a','b','c','d')
# fruitList.extend(tuples)
# print(fruitList)
#output: ['Apple', 'banana', 'mango', 'watermeleon', 'a', 'b', 'c', 'd']

# #extending dictionaries
# userData={
#     'Name': 'Archana',
#     'Surname':'Timilsina',
#     'Address': 'Bhaktapur'
# }
# fruitList.extend(userData)
# print(fruitList)
#output:  ['Apple', 'banana', 'mango', 'watermeleon', 'Name', 'Surname', 'Address']

#insert(index, x)
# fruitList.insert(0,"Hello")
# print(fruitList)
#output:['Hello', 'Apple', 'banana', 'mango', 'watermeleon']

#remove(x)
# fruitList.remove("Apple")
# print(fruitList)
#output: ['banana', 'mango', 'watermeleon']


#pop(index) or pop()
# fruitList.pop()
# print(fruitList)
# #output: ['Apple', 'banana', 'mango']

# fruitList.pop(0)
# print(fruitList)
#output: ['banana', 'mango', 'watermeleon']


# #clear()
# fruitList.clear()
# print(fruitList)
# #output: [] (empty)


# #index(x, start, end) => Returns the index of the first occurrence of a value.
# Optional start and end limit the search.
# print(fruitList.index("Apple"))
# #output: 0


# #count(x) => Counts how many times a value appears in the list.

# print(fruitList.count("Apple"))
# #output: 1
# print(fruitList.count()) #gives err


# #sort(*, key=None, reverse=False)
# fruitList.sort()
# print(fruitList)
# #output: ['Apple', 'banana', 'mango', 'watermeleon']
# fruitList.sort(reverse=True)
# print(fruitList)
#output: ['watermeleon', 'mango', 'banana', 'Apple']
# fruitList.sort(key=len) #the list is sorted by word length
# print(fruitList)
#output: ['mango', 'Apple', 'banana', 'watermeleon']


# #reverse()
# fruitList.reverse()
# print(fruitList)
# #output:  ['watermeleon', 'mango', 'banana', 'Apple']


# #copy()
# fruitlist3= fruitList.copy()
# print(fruitlist3)
# #output: ['Apple', 'banana', 'mango', 'watermeleon']


#len()
# print(len(fruitList))
# output: 4

#slicing 
# print(fruitList) #output: ['Apple', 'banana', 'mango', 'watermeleon']
# print(fruitList[1:2]) #output: ['banana']

# print("Apple" in fruitList) #output: True

# #inserting into the list
# fruitList[4:6]=["Hello","world"]
# print(fruitList) #output: ['Apple', 'banana', 'mango', 'watermeleon', 'Hello', 'world']

#remove from the list using del keyword
# del fruitList[3]
# print(fruitList) #output: ['Apple', 'banana', 'mango']

#looping through the list
# for fruits in fruitList:
#     print(fruits)
    #output: 
# Apple
# banana
# mango
# watermeleon

# #loop through index number
# for i in range(len(fruitList)):
#     print(fruitList[i])
        #output: 
# Apple
# banana
# mango
# watermeleon


#while loop
# i=0
# while i<len(fruitList):
#     print(fruitList[i])
#     i+=1
 #output: 
# Apple
# banana
# mango
# watermeleon

# [print(x) for x in fruitList]
 #output: 
# Apple
# banana
# mango
# watermeleon

#concatenate two lists
# list1=["alr","blr","clr"]
# list2=["dlr","elr","flr"]
# print(list1 + list2)
#output: ['alr', 'blr', 'clr', 'dlr', 'elr', 'flr']
