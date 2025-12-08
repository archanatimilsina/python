# student={
#     "name": "Archana",
#     "surname":"Timilsina",
#     "age":24,
#     "address":"Bhaktapur"
# }
# print(student)

#methods of dictionary
#.get(key)
# print(student.get("age")) #output: 24
# print(student.get("grade")) #output: None
# print(student.get("grade","N/A")) #output: N/A 


#.keys() Returns a special view object showing all keys
# print(student.keys()) #output : dict_keys(['name', 'surname', 'age', 'address'])

#values() Similar to keys() but for values.
# print(student.values()) #output: dict_values(['Archana', 'Timilsina', 24, 'Bhaktapur'])

#items() Gives pairs (key, value).
# print(student.items()) #output: dict_items([('name', 'Archana'), ('surname', 'Timilsina'), ('age', 24), ('address', 'Bhaktapur')])

#pop(key , default) Removes a key and returns its value.
# print(student.pop("address")) #output: Bhaktapur
# print(student) #output: {'name': 'Archana', 'surname': 'Timilsina', 'age': 24}

# print(student.pop("author","unknown")) #output:unknown 
# print(student) #output : {'name': 'Archana', 'surname': 'Timilsina', 'age': 24, 'address': 'Bhaktapur'}

#popitem() Removes and returns one key–value pair.
# In Python 3.7+, it removes the last inserted item.
# print(student.popitem()) #output: ('address', 'Bhaktapur')
# print(student) #output:  {'name': 'Archana', 'surname': 'Timilsina', 'age': 24}

#update(other_dictionary)
# marks= {
#     "nepali": 90,
#     "english": 77,
#     "math": 98
# }
# student.update(marks)
# print(student) #output: {'name': 'Archana', 'surname': 'Timilsina', 'age': 24, 'address': 'Bhaktapur', 'nepali': 90, 'english': 77, 'math': 98}

#setdefault(key , default)
# If the key exists, do nothing and return the value.
# If the key doesn’t exist, insert the default—and return it.
# student.setdefault("favFruit","mango")
# print(student) #output:  {'name': 'Archana', 'surname': 'Timilsina', 'age': 24, 'address': 'Bhaktapur', 'favFruit': 'mango'}

#dict.clear().  Empties the dictionary.
# student.clear()
# print(student) #output: {}

#copy()
# a={"nums":[1,2,3]}
# b= a.copy()
# b["nums"].append(5)
# print(a) #output: {'nums': [1, 2, 3, 5]}
# print(b)  #output: {'nums': [1, 2, 3, 5]}


#fromkeys(iterable, value) Creates a new dictionary with given keys and a single shared value.
# key=["name","surname","age","phoneNumber"]
# print(dict.fromkeys(key)) #output: {'name': None, 'surname': None, 'age': None, 'phoneNumber': None}
# print(dict.fromkeys(key,"unknown")) #output: {'name': 'unknown', 'surname': 'unknown', 'age': 'unknown', 'phoneNumber': 'unknown'}


#._contains_(key) Returns True if the key exist otherwise returns False
# print(student.__contains__("name"))  #output : True
# print(student.__contains__("squirrel"))  #output : False

#_len_() or len(dict_name)
# print(student.__len__()) #output: 4
# print(len(student)) #output: 4

#_getitem_(key) & _setitem_(key,value)
# print(student.__getitem__("name")) #output: Archana
# student.__setitem__("name","shine")
# print(student)  #output: {'name': 'shine', 'surname': 'Timilsina', 'age': 24, 'address': 'Bhaktapur'}


#_delitem_(key)
# student.__delitem__("name")
# print(student) #output: {'surname': 'Timilsina', 'age': 24, 'address': 'Bhaktapur'}

#__eq__(other) Allows equality comparison.
# student1={
#     "name": "Archana",
#     "surname":"Timilsina",
#     "age":24,
#     "address":"Bhaktapur"
# }
# print(student.__eq__(student1)) #ouput: Allows equality comparison.

#__iter__()
# it=student.__iter__()
# print(next(it)) #output: name
# print(next(it)) #output: surname