#simple function in python
# def hello():
# #    print(hello) #output: <function hello at 0x10214d440>
#   print("hello") #output : hello
# hello()


# def hello(greeting , person_name):
#   print(f"{greeting}!! {person_name}")
# hello("Namaste","Archana") #output: Namaste!! Archana

#default arg
# def hello(greeting , person_name="saili"):
#   print(f"{greeting}!! {person_name}")
# # not passing second arg bcz there is default
# hello("Namaste") #output: Namaste!! saili
# # passing arg 
# hello("Namaste","Archana") #output: Namaste!! Archana
# conclusion: if we pass arg for default parameter then the passed value will be choosed if not passed default value will be used


#Default first argument, second mandatory
# 1> Keyword-only argument using *
# Python allows you to make arguments keyword-only after *.
# def hello(greeting="Namaste", person_name):returns err saying Non-default argument follows default argumentPylance bcz Python requires that all non-default arguments come before default arguments in the function definition.
# def hello(greeting="Namaste",*, person_name):
#     print(f"{greeting}!! {person_name}")

# hello(person_name="Archana")               # uses default greeting → Namaste!! Archana

# # 2. Using a placeholder value (None)
# def hello(greeting, person_name):
# # def hello(greeting, person_name): #None!! Archana
#     if greeting is None:
#         greeting = "Namaste"
#     print(f"{greeting}!! {person_name}")
# hello(None, "Archana")      # uses default greeting → Namaste!! Archana

# # 3. Using *args to simulate skipped arguments
# def hello(*args):
#     if len(args) == 1:
#         greeting = "Namaste"
#         person_name = args[0]
#     elif len(args) == 2:
#         greeting, person_name = args
#     else:
#         raise TypeError("Expected 1 or 2 arguments")
#     print(f"{greeting}!! {person_name}")

# hello("Archana")          # uses default greeting → Namaste!! Archana


# # 4. Using **kwargs with defaults
# def hello(**kwargs):
#     greeting = kwargs.get("greeting", "Namaste")
#     person_name = kwargs["person_name"]   # mandatory
#     print(f"{greeting}!! {person_name}")

# hello(person_name="Archana")               # default greeting → Namaste!! Archana



# *args allows a function to accept any number of positional arguments.
# print(args) #output : ('Archana',) a tuple so need to access args as args[0] as index
# function call can be like hello("Archana") no need to pass arg name 
# no need to use args always ;name can be anything
# **kwargs allows a function to accept any number of keyword arguments.
# Inside the function, kwargs is a dictionary (dict) with key-value pairs.
#  print(kwargs) #output : {'person_name': 'Archana'}
# function name should be like hello(person_name="Archana")



# # 5. Using functools.partial (advanced)
# from functools import partial

# def hello(greeting, person_name):
#     print(f"{greeting}!! {person_name}")

# hello_default = partial(hello, "Namaste")
# hello_default("Archana")  # Namaste!! Archana

# Explanation:
# partial creates a pre-filled function with default first argument
# You can still override both if you call the original function
# Useful if you want pre-configured functions




#passing the list as the argument
# listyarg= ["apple", "banana","mango"]
# def hello(listy):
#     print(listy)

# hello(listyarg) #output: ['apple', 'banana', 'mango']

#1. Positional Arguments: Arguments that are matched by position. Python assigns the value 
# you pass to the function parameter from left to right.

# 2. Keyword arguments: Keywords explicitly tell Python which value goes to which parameter 
# Order does not matter with keyword arguments


#3. Keyword-only Arguments
# Arguments that must be passed by keyword, even if they are defined in the function.
# Introduced using a * in the parameter list.
# Everything after * must be a keyword argument.

# In Python, / indicates that **all parameters before it must be passed positionally, not as keywords.
# def greet(title, /, name, *, greeting="Hello"):
# title → positional-only
# name → can be positional or keyword
# greeting → keyword-only (after *)