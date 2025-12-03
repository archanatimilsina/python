
x="Hello world"
y="123"
z=" "
####case related methods
#str.upper(): Converts string to uppercase
# print(x.upper())
#str.lower():Converts string to lowercase
# print(x.lower())
# #str.capitalize(): Capitalizes first character
# print(x.capitalize())
# str.title() : Capitalizes first letter of each word
# print(x.title())
# str.swapcase(): Swaps case of each character
# print(x.swapcase())

####Search / Check methods
# str.startswith(prefix):  Check if string starts with prefix 
# print(x.startswith("Hel")) #output : True (STrats with Hel)
# # str.endswith(suffix):  Check if string ends with suffix
# print(x.endswith("rld")) #output: True (ends with rld)

# # str.find(sub): Returns lowest index of substring, -1 if not found
# print(x.find("o")) #output:4  4th position o

# # str.rfind(sub): Returns highest index of substring, -1 if not found
# print(x.rfind("o")) #output: 8  8th position o

# str.index(sub): Like find(), but raises ValueError if not found
# print(x.index("o")) #output:4

# str.rindex(sub): Like rfind(), but raises ValueError if not found
# print(x.rindex("o")) #output:7

# str.count(sub): Count occurrences of substring
# print(x.count("W")) #output:2




##### Check content / type methods
#str.isalpha() => All letters
# print(x.isalpha())
# # if there is space inbetween then it returns false

# #str.isdigit() => All digits
# print(y.isdigit())
# print(x.isdigit()) #returns false
# y="123" it returns true but if y=123 it gives err

#str.isalnum() => Letters or digits
# print(x.isalnum()) #space gives err here. It checks every item inside that variable so space is counted on it too

#str.islower() => All lowercase
# print(x.islower()) 

#str.isupper() => All uppercase
# print(x.isupper())

#str.isspace()=> Only whitespace
# print(z.isspace())  #return true if z=" "

#str.istitle()=> Title cased
# print(x.istitle()) #A string is title-cased only if every word in the string starts with
# an uppercase letter and the rest of the word is lowercase.




#### Modify / Transform methods
#str.strip().  #Removes whitespace from both ends.
# print(x.strip())

#str.strip([chars]) => strip("abc") does NOT trim the substring "abc"
# —it removes any individual character in "abc" from both ends.
# m = "llHello Worldoll"
# print(m.strip("lo"))  

#str.lstrip([chars]) => Remove from the left only
# Works like strip() but only affects the beginning.
# m = "....Hello..."
# print(m.lstrip("."))
# output: Hello...

#str.rstrip([chars]) — Remove from the right only
# Only affects the end.
# m = "....Hello..."
# print(m.rstrip("."))
# output: ....Hello

#str.replace(old, new, count)
# a) Replace all: do not give count value
# m="banana"
# print(m.replace("na","ma"))
# output: bamama

# b) Replace limited count:: give count
# m="banana"
# print(m.replace("na","ma",1)) #output: bamana
# print(m.replace("na","ma",2)) #output: bamama

#str.center(width, fillchar) => Centers a string inside a larger string.
# x1 = "Hi"
# print(x1.center(10, "*"))  #Output: ****Hi****
# # Total width = 10

#str.ljust(width, fillchar) => Places string on the left, pads the right.
# x1 = "Hi"
# print(x1.ljust(10, "*"))  #Output: Hi********


#str.rjust(width, fillchar) => Places string on the right, pads the left.
# x1 = "Hi"
# print(x1.rjust(10, "*"))  #Output: ********Hi


#str.zfill(width)=> Pads the left with zeros — works mostly for numeric strings.
# x1 = "Hi"
# print(x1.zfill(10))  #Output: 00000000Hi
# # Total width = 10



#### Split / Join methods
#str.split(sep=None, maxsplit=-1)
# This breaks a string into pieces and returns a list.
# If sep is not given, Python splits on any amount of whitespace (spaces, tabs, newlines).
# maxsplit controls how many splits happen; the rest stays as one piece.
# x = "apple mango banana orange"
# print(x.split())
# print(x.split("o")) #output: ['apple mang', ' banana ', 'range']
# print(x.split("o",1)) #output:['apple mang', ' banana orange']

# #str.rsplit(sep=None, maxsplit=-1) => Same as split, but splitting happens from the right side.
# x = "applemango-banana-orange- "
# print(x.rsplit("-")) #output: ['applemango', 'banana', 'orange', ' ']

#str.splitlines([keepends])
# x = "Hello\nWorld\r\nPython"
# print(x.splitlines()) # This splits the string wherever newline characters occur (\n, \r\n, etc.).
# # ['Hello', 'World', 'Python']
# # If keepends=True, it keeps the newline characters in the output.
# print(x.splitlines(True))
# # ['Hello\n', 'World\r\n', 'Python']


#str.join(iterable)
# This takes a list/tuple of strings and joins them into one string using the current string as a separator.
# The left side is the separator; the right side is the items.
# x=["apple","banana","mango"]
# print('-'.join(x))


####  Encoding / Decoding
#str.encode(encoding='utf-8', errors='strict')
# x = "नमस्ते"
# print(x.encode())  
# b'\xe0\xa4\xa8\xe0\xa4...'



####  Partitioning / Searching
#str.partition(sep)
# Splits the string into 3 parts:
# part before the separator
# the separator itself
# part after the separator
# print(x.partition(" ")) #output: ('Hello', ' ', 'world')
# #str.rpartition(sep) => Same as partition but splits at the last occurrence.
# print(x.rpartition("d")) #output: ('Hello worl', 'd', '')



#### Other useful methods
#str.format(*args, **kwargs)=> Classic Python formatting—replace {} placeholders with values.
# msg = "My name is {} and I am {} years old"
# print(msg.format("Archana", 20))


#str.format_map(mapping)
# Similar to .format(), but works with a dictionary directly.
# data = {"name": "Sita", "age": 22}
# print("Name: {name}, Age: {age}".format_map(data))


#str.maketrans()
# Creates a translation table used by str.translate().
# tbl = str.maketrans({"a": "1", "e": "2"})
# print(tbl)

#str.translate(table) => Applies the translation table.
# x = "apple"
# tbl = str.maketrans({"a": "1", "e": "2"})
# print(x.translate(tbl))
# 1ppl2


#concatenate
# print("A"+" "+ "Timilsina")

#format string f and the format method
# price= "Rs.59"
# print(f"Hello this is {price}")
# txt="this is {}"
# print(txt.format(price))


#input()
# name=input()
# print(f"hello {name}")
# name=input("Enter you Name:")
# print(f"hello {name}")


#using \" \"
# print("My name is \"Archana\" Timilsina")
# # using \' \'
# print('My name is \'Archana\' Timilsina')

# print("Archana \\ Timisina") #output: Archana \ Timisina
# print("Archana \nTimisina") #output:Archana 
#  Timisina
# print("Archana \r Timisina")
# Any characters printed after \r overwrite the characters at the start of the line.
 #output: Timisina
# print("Archana\tTimisina") #output: Archana Timisina (give tab)
# print("Archana\b Timisina") #\b represent backslash
 #output: Archan Timisina
# print("Archana \f Timisina") #output:
# Archana 
#          Timisina
#\f for form feed

