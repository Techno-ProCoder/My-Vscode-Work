### PYTHON(INTERPRETER LANGUAGE)(LEGB(Local,Enclosing,Global,Built-in) RULE)(DYNAMICALLY TYPED)###

# Working With Basic Modules:-

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello World")
# engine.runAndWait()

# import os
# contents = os.listdir('/Windows')
# print(f'The contents of the Windows directory will be printed {len(contents)} times.')
# for item in contents: print('\n'.join(os.listdir('/Windows')))

# import pyjokes
# print(pyjokes.get_joke())

# import math
# print(math.sqrt(25))

# split()
# The split() method splits a string into a list. By default, it will use whitespace to separate the items, but you can also set another character of choice:
# >>> 'My name is Simon'.split()
# ['My', 'name', 'is', 'Simon']
# >>> 'MyABCnameABCisABCSimon'.split('ABC')
# ['My', 'name', 'is', 'Simon']
# >>> 'My name is Simon'.split('m')
# ['My na', 'e is Si', 'on']
# >>> ' My  name is  Simon'.split()
# ['My', 'name', 'is', 'Simon']
# >>> ' My  name is  Simon'.split(' ')
# ['', 'My', '', 'name', 'is', '', 'Simon']

# Justifying text with rjust(), ljust() and center()
# >>> 'Hello'.rjust(10)
# '     Hello'
# >>> 'Hello'.rjust(20)
# '               Hello'
# >>> 'Hello World'.rjust(20)
# '         Hello World'
# >>> 'Hello'.ljust(10)
# 'Hello     '
# >>> 'Hello'.center(20)
# '       Hello       '
# An optional second argument to rjust() and ljust() will specify a fill character apart from a space character:
# >>> 'Hello'.rjust(20, '*')
# '***************Hello'
# >>> 'Hello'.ljust(20, '-')
# 'Hello---------------'
# >>> 'Hello'.center(20, '=')
# '=======Hello========'

# Removing whitespace with strip(), rstrip(), and lstrip()
# >>> spam = '    Hello World     '
# >>> spam.strip()
# 'Hello World'
# >>> spam.lstrip()
# 'Hello World     '
# >>> spam.rstrip()
# '    Hello World'
# >>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
# >>> spam.strip('ampS')
# 'BaconSpamEggs'

# Escape Sequences:- \n,\b,\v,\f,\r,\a,\t and \\
# Types Of Ways To Write Hello World
# print("'hello world'")//for single,triple,till infinite quotes with hello world
# print("hello 'world'")//for single,triple,till infinite quotes with world only
# print("Hello World")//normal way to print hello world
# print('Hello World')//normal way to print hello world
# print('''Hello World''')//normal way to print hello world
# print('''Hello World''''')//normal way to print hello world
# print("""Hello World""")//normal way to print hello world
# print("""Hello World""""")//normal way to print hello world
# print('"Hello World"')//for double quotes with hello world
# print("Hello \"World\"")//for double quotes with world only
# print("Hello \'World\'")
# print("Hello \"World\'")
# print("Hello \'World\"")
# print("Hello \"World\'s\"")
# print("Hello \"World\"s\"")
# print("Hello \'World\'s\"")
# print("Hello \'World\"s\"")
# print("hello / world")
# print("hello \\ world")
# print(r"hello \ world")
# print(rf"hello \ world")
# name = "World"
  # name1 = "Hello"
  # print(f"{name1}, {name}!") //fstrings
# print(f"Hello, World!")

# a=int(input())
# b=float(input())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# number = int(input())
# z = int(input())
# print("Square Of number is:",number**2)

# a=54
# print(id(a)) # Prints The Memory address of 'a'

# Round Function(Inbuilt)
# a = 3.4555555555576784
# print(round(a,3))

# String(Immutable) Functions
# name="Aarpit"
# print(name)
# print(name[:]) # Slicing the string
# print(name[0:6:2]) # Slicing the string with skip value
# print(name[::-1]) # Reverse the string(with -ve skip value)
# String concatenation:-
# >>> 'Alice' 'Bob'
# 'AliceBob'
# String replication:-
# >>> 'Alice' * 5
# 'AliceAliceAliceAliceAlice'
# Sep Keyword:-
# print('cats', 'dogs', 'mice', sep=',')
# cats,dogs,mice
# print(len(name))
# print(len(input()))
# print(name.endswith("t"))
# print(name.startswith("Aa"))
# print(name.count("a"))
# print(name.capitalize())
# print(name.find("r"))
# print(name.lower())
# print(name.upper())
# print(name.replace("A","B"))
# print(name.title())
# print(name.swapcase())
# print(name.isalnum())
# print(name.isalpha())
# print(name.isnumeric())
# print(name.islower())
# print(name.isupper())
# print(name.isspace())
# print(name.istitle())
# print(name.join("A"))
# print(name.split("a"))
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())
# print(name.partition("r"))
# print(name.rpartition("r"))
# print(name.encode('utf-8'))
# print(name.decode('utf-8'))
# print(name.format())
# print(name.format_map("A"))
# print(name.index("r"))
# print(name.isprintable())
# print(name.isidentifier())
# print(name.isdecimal())
# print(name.isascii())
# print(name.isidentifier())
# print(name.removeprefix("A"))
# print(name.removesuffix("t"))
# print(name.zfill(10))
# print(name.center(10))
# print(name.ljust(10))
# print(name.rjust(10))
# print(name.expandtabs(4))
# print(name.casefold(10))
# print(name.maketrans("A","B"))
# print(name.translate("A","B"))
# print(name.rfind("r"))
# print(name.rindex("r"))
# print(name.rsplit("r"))

# name = """Aarpit is Bad"""
# print(name.replace(input(),input()).replace("Aarpit","Amit").replace("Amit","Aarpit").replace("Good","Bad")) # Chaining Of Functions

# Switch-Case Statements(Use Match In Python)

# Matching single values
# >>> response_code = 201
# >>> match response_code:
# ...     case 200:
# ...         print("OK")
# ...     case 201:
# ...         print("Created")
# ...     case 300:
# ...         print("Multiple Choices")
# ...     case 307:
# ...         print("Temporary Redirect")
# ...     case 404:
# ...         print("404 Not Found")
# ...     case 500:
# ...         print("Internal Server Error")
# ...     case 502:
# ...         print("502 Bad Gateway")
# ...     case _:
# ...         print("Invalid Code")
# Created
# Matching Builtin Classes
# >>> response_code = "300"
# >>> match response_code:
# ...     case int():
# ...             print('Code is a number')
# ...     case str():
# ...             print('Code is a string')
# ...     case _:
# ...             print('Code is neither a string nor a number')
# Code is a string
# Guarding Match-Case Statements
# >>> response_code = 300
# >>> match response_code:
# ...     case int():
# ...             if response_code > 99 and response_code < 500:
# ...                 print('Code is a valid number')
# ...     case _:
# ...             print('Code is an invalid number')
# Code is a valid number
# Matching by the length of an Iterable
# >>> today_responses = [200, 300, 404, 500]
# >>> match today_responses:
# ...     case [a]:
# ...             print(f"One response today: {a}")
# ...     case [a, b]:
# ...             print(f"Two responses today: {a} and {b}")
# ...     case [a, b, *rest]:
# ...             print(f"All responses: {a}, {b}, {rest}")
# All responses: 200, 300, [404, 500]
# Matching with the or Pattern
# >>> response_code = 502
# >>> match response_code:
# ...     case 200 | 201:
# ...         print("OK")
# ...     case 300 | 307:
# ...         print("Redirect")
# ...     case 400 | 401:
# ...         print("Bad Request")
# ...     case 500 | 502:
# ...         print("Internal Server Error")
# Internal Server Error

# Lists(Mutable)(1-D)

# Multiple Assignment Trick:-
# >>> furniture = ['table', 'chair', 'rack', 'shelf']
# >>> table, chair, rack, shelf = furniture
# >>> table
# 'table'
# >>> chair
# 'chair'
# >>> rack
# 'rack'
# >>> shelf
# 'shelf'
# >>> a, b = 'table', 'chair'
# >>> a, b = b, a
# >>> print(a)
# chair
# >>> print(b)
# table

# friends1 = ["Amit","Aarpit","Rahul",34,56.7,True]
# print(friends1[1])
# print(friends1[1][2])
# friends1[1]="Ghost"
# print(friends1)
# Lists(1-D) Can Be Sliced In The Same Manner As Strings
# print(friends1[1:3])
# print(friends1[1:3:2])
# print(friends1[1:3:2][0]) # For Row 1(Row Slicing with skip value and then Slicing)(Output = Ghost)
# print(friends1[1:3:2][0][0]) # For Row 1(Row Slicing with skip value and then Slicing)(Output = G and futher slicing's = G)

# Lists(Multidimensional)
# friends = [["Amit","Aarpit","Rahul",34,56.7,True],["Amt","Aarit","Raul",38,56.9,False]]
# print(friends[1][2][0])
# friends[1][2]="Ghost"
# print(friends)
# list(Multidimensional) can be sliced in the same manner as 1-D list
# print(friends[1][2:4]) # For Row 1(Row Slicing)
# print(friends[1][2:4:2]) # For Row 1(Row Slicing with skip value)
# print(friends[1][2:4:2][0]) # For Row 1(Row Slicing with skip value and then Slicing)(Output = Raul)
# print(friends[1][2:4:2][0][0]) # For Row 1(Row Slicing with skip value and then Slicing and then Slicing)(Output = R and futher slicing's = R)

# List(Multidimensional) Methods(For 1-D List just remove the index after friends)
# 1. Append
# Append an element to a specific row
# friends[0].append("NewElement")
# print(friends)
# Output: [['Amit', 'Aarpit', 'Rahul', 34, 56.7, True, 'NewElement'], ['NewAmit', 'NewAarpit', 'NewRahul', 40, 60.0, True], ['Amt', 'Aarit', 'NewFriend', 'Raul', 38, 56.9, False]]
# 2. Remove
# Remove an element from a specific row
# friends[0].remove("NewElement")
# print(friends)
# Output: [['Amit', 'Aarpit', 'Rahul', 34, 56.7, True], ['NewAmit', 'NewAarpit', 'NewRahul', 40, 60.0, True], ['Amt', 'Aarit', 'NewFriend', 'Raul', 38, 56.9, False]]
# 3. Pop
# Pop an element from a specific row
# popped_element = friends[2].pop(2)
# print(popped_element)  # Output: NewFriend
# print(friends)
# Output: [['Amit', 'Aarpit', 'Rahul', 34, 56.7, True], ['NewAmit', 'NewAarpit', 'NewRahul', 40, 60.0, True], ['Amt', 'Aarit', 'Raul', 38, 56.9, False]]
# 4. Extend
# Extend a specific row with another list
# friends[1].extend(["Extra1", "Extra2"])
# print(friends)
# Output: [['Amit', 'Aarpit', 'Rahul', 34, 56.7, True], ['NewAmit', 'NewAarpit', 'NewRahul', 40, 60.0, True, 'Extra1', 'Extra2'], ['Amt', 'Aarit', 'Raul', 38, 56.9, False]]

# Tuple(Immutable)(Just Like Lists But Immutable and with small brackets)(More Memory Efficient Than Lists)
# friends = (bool(input()),"Aarpit","Rahul",34,56.7,True)
# print(friends[0])
# friends1 = (1,) # Tuple with single element
# A Tuple can be converted into a list by typecasting it like we do with input() function

# Tuple Methods
# .count(), .index(), etc.
# Both 1-D and Multidimensional Tuples (access and slicing) are same as that in Lists just we cannot change any tuple element like in strings and the tuple methods are little different from Lists as they are immutable

# Dictionaries(Mutable)(Multi Or Single Dimensional Lists, tuples and dictionaries can be declared + modified inside it)(Represented by curly braces{})(Consists primarly of multiple key value pairs)(Key and value can be of any data type)(Key should be unique)(Value can be repeated)(Key can be equal to value also)(If Keys are duplicate then the last key value pair will overwrite all others)
# marks = {} # Empty Dictionary
# my_cat = {}
# my_cat['age_years'] = 2
# print(my_cat)
# marks = {"student1":{"Amit": 100, "Aarpit": 99, "Rahul": 98}, "student2": {"Amit": 22, "Aarpit": 93, "Rahul": 45}} # Multidimensional Dictionary(2-D)
# print(len(marks)) # Output = 2(Length of the dictionary)(As there are 2 key value pairs)(student1 and student2 are keys and the values are the dictionaries inside them)
# print(marks["student1"]["Aarpit"]) # Accessing the value of a key in a dictionary(Multidimensional)
# A Dictionary's(key(use .keys() with name of dictionary),values(use .values() with name of dictionary) and key-value pairs(use .items() with name of dictionary)) can be converted into a list by typecasting it like we do with input() function

# Dictionary Methods
# .items(), .keys(), .values(), .clear(), .copy(), .fromkeys(), .get(), .pop(), .popitem(), .setdefault(), .update()
# marks = {"student1":{"Amit": 100, "Aarpit": 99, "Rahul": 98}, "student2": {"Amit": 22, "Aarpit": 93, "Rahul": 45}}
# print(marks.items())
# print(marks["student1"].items())
# print(marks["student2"].items())
# print(marks.keys())
# print(marks["student1"].keys())
# print(marks["student2"].keys())
# print(marks.values())
# print(marks["student1"].values())
# print(marks["student2"].values())
# print(marks.clear()) # Output = None
# Imp Question Asked in Interview:- What will be the output of the following codes?
# print(marks.get("student3")) # Output = None
# print(marks["student3"]) # Output = Key Error

# Sets(Mutable)(Not Hashable)(Just Like Lists But Little Difference)(Unordered Collection of Unique Elements)(Represented by curly braces{})(Can be of any data type)(Cannot be sliced)(Cannot be accessed by index)(Cannot be repeated)(Can be modified)(Can be used to remove duplicates from a list)(Elements should be immutable and hashable)
# s = set() # Empty Set
# print(s) # Output = set()
# s1 = {1,2,3,4,5,5,5,5}
# print(s1) # Output = {1, 2, 3, 4, 5}
# A Set can be converted into a list by typecasting it like we do with input() function
# To Define Multidimensional Sets We Need to use frozensets()(immutable and hashable unlike sets themselves) function as we can not directly create multidimensional sets as illustrated below:-
# frozenset1 = frozenset([1, 2, 3])
# frozenset2 = frozenset([4, 5, 6])
# multidimensional_set = {frozenset1, frozenset2}
# print(multidimensional_set)

# Set Methods
# .add(), .remove(), .discard(), .clear(), .copy(), .pop(), .popitem(), .update(), .union(), .intersection(), .difference(), .symmetric_difference(), .issubset(), .issuperset(), .isdisjoint()
# s = {1,2,3,4,5}
# s1 = {4,5,6,7,8}
# print(s.union(s1)) # Output = {1, 2, 3, 4, 5, 6, 7, 8}
# print(s.intersection(s1)) # Output = {4, 5}
# print(s.difference(s1)) # Output = {1, 2, 3}
# print(s.symmetric_difference(s1)) # Output = {1, 2, 3, 6, 7, 8} # Or print(s^s1)
# print(s.issubset(s1)) # Output = False
# print(s.issuperset(s1)) # Output = False
# print(s.isdisjoint(s1)) # Output = False
# print(s.clear()) # Output = set()
# print(len(s)) # Output = 5(Length of the set)
# s.add(6) # Most commonly(widely) used method in sets
# print(s) # Output = {1, 2, 3, 4, 5, 6}
# s.remove(2)
# print(s) # Output = {1, 3, 4, 5, 6}
# s.discard(3)
# print(s) # Output = {1, 4, 5, 6}
# s = {"18",18,18.0}
# print(s) # Output = {18, '18'}(As Python treats 18 and 18.0 same)

# Conditional Statements
# a = int(input())
# If elif else ladder
# if a > 3:
#     print("Good")
#     if a == 5:
#         print("5")
#     elif a == 7:
#         print("7")
#     else:
# pass # Pass is used to skip the current iteration and move to the next iteration
# elif a == 3:
#     print("Medium")
# else:
#     print("Bad")
# In statement usage
# p1 = "harry"
# a = input()
# if(p1 in a.lower()):
#     print("Equal")
# else:
#     print("Not Equal")

# Loops(No do-while loop in Python)

# print ("range(-10,-20,-2)--> ", list(range(-10,-20,-2)))
# While Loop(We can use Conditional statements,Relational operators whenever required inside While loop)
# i = 1 # Initial Value
# while(i<6): # Condition-Checking(Use bool Keyword 'True' or any other 'always true' expression to print infinite loop)
#     print(i)
#     i += 1 # Incrementing 'i'
# Use Of Break,Continue And Pass Statements In While Loop:-
# i = 0
# while i < 10:
    # if i == 3:
        # i += 1
        # continue  # Skip the rest of the loop when i is 3
    # if i == 5:
        # pass  # Do nothing when i is 5(Pass is a null statement in Python)
    # if i == 7:
        # break  # Exit the loop when i is 7
    # print(i)
    # i += 1  # Output = 0,1,2,4,5,6
# 1. Iterating over a list(1-D):-
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
# 2. Iterating over a list(Multidimensional)(2-D only)(Or n-D and we want reverse of the list):-
# my_list = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]]
# my_list.reverse()
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
# 2(a). Iterating over a list(Multidimensional)(More Than Two Lists)(Generalised Method):-
# my_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
# order = [2, 0, 1]
# order_index = 0
# while order_index < len(order):
#     inner_list = my_list[order[order_index]]
#     i = 0
#     while i < len(inner_list):
#         print(inner_list[i])
#         i += 1
#     order_index += 1
# 3. Iterating over a Tuple(1-D)(Without converting into List):-
# my_tuple = (1, 2, 3, 4, 5)
# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1
# 4. Iterating over a Tuple(Multidimensional)(Without converting into List)(2-D only)(Or n-D and we want reverse of the Tuple):-
# my_tuple = ((1, 2, 3, 4, 5),(6, 7, 8, 9, 10))
# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i += 1
# 4(a). Iterating over a Tuple(Multidimensional)(Without converting into List)(More Than Two Tuples)(Generalised Method):-
# my_tuple = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15))
# order = [2, 0, 1]
# order_index = 0
# while order_index < len(order):
#     inner_tuple = my_tuple[order[order_index]]
#     i = 0
#     while i < len(inner_tuple):
#         print(inner_tuple[i])
#         i += 1
#     order_index += 1
# 5. Iterating over a Tuple(1-D)(Converting into List):-
# my_tuple = (1, 2, 3, 4, 5)
# tuple_list = list(my_tuple)
# tuple_list.reverse()
# i = 0
# while i < len(tuple_list):
#     print(tuple_list[i])
#     i += 1
# 6. Iterating over a Tuple(Multidimensional)(Converting into List)(2-D only)(Or n-D and we want reverse of the Tuple):-
# my_tuple = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10))
# tuple_list = list(my_tuple) 
# tuple_list.reverse()
# i = 0
# while i < len(tuple_list):
#     print(tuple_list[i])
#     i += 1
# 6(a). Iterating over a Tuple(Multidimensional)(Converting into List)(More Than Two Tuples)(Generalised Method):-
# my_tuple = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15))
# tuple_list = list(my_tuple)
# order = [2, 0, 1]
# order_index = 0
# while order_index < len(order):
#     inner_tuple = tuple_list[order[order_index]]
#     i = 0
#     while i < len(inner_tuple):
#         print(inner_tuple[i])
#         i += 1
#     order_index += 1
# 7. Iterating over a Set(1-D):-
# my_set = {1, 2, 3, 4, 5}
# set_list = list(my_set)
# set_list.reverse()
# i = 0
# while i < len(set_list):
#     print(set_list[i])
#     i += 1
# 8. Iterating over a Set(Multidimensional)(2-D only)(Or n-D and we want reverse of the Set)(Frozen Set):-
   # (a). Print second frozen sets content first:-
     # (i). Method 1(Typecasting)(Without lambda() function):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = {frozenset1, frozenset2}
# multidimensional_list = list(multidimensional_set)
# i = 0
# while i < len(multidimensional_list):
#     inner_set = multidimensional_list[i]
#     inner_list = list(inner_set)
#     j = 0
#     while j < len(inner_list):
#         print(inner_list[j])
#         j += 1
#     i += 1
     # (ii). Method 2(Typecasting)(With lambda() function):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = {frozenset1, frozenset2}
# multidimensional_list = list(multidimensional_set)
# multidimensional_list.sort(key=lambda x: x!= frozenset2)
# i = 0
# while i < len(multidimensional_list):
#     inner_set = multidimensional_list[i]
#     inner_list = list(inner_set)
#     j = 0
#     while j < len(inner_list):
#         print(inner_list[j])
#         j += 1
#     i += 1
     # (iii). Method 3(Explicitly converting into List):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = [frozenset2, frozenset1]
# i = 0
# while i < len(multidimensional_set):
#     inner_set = multidimensional_set[i]
#     inner_list = list(inner_set)
#     j = 0
#     while j < len(inner_list):
#         print(inner_list[j])
#         j += 1
#     i += 1    
# (b). Print first frozen sets content first:-
     # (i). Method 1(Typecasting):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = {frozenset1, frozenset2}
# multidimensional_list = list(multidimensional_set)
# multidimensional_list.sort(key=lambda x: x!= frozenset1)
# i = 0
# while i < len(multidimensional_list):
#     inner_set = multidimensional_list[i]
#     inner_list = list(inner_set)
#     j = 0
#     while j < len(inner_list):
#         print(inner_list[j])
#         j += 1
#     i += 1
     # (ii). Method 2(Explicitly converting into List):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = [frozenset2, frozenset1]
# i = 0
# while i < len(multidimensional_set):
#     inner_set = multidimensional_set[i]
#     inner_list = list(inner_set)
#     j = 0
#     while j < len(inner_list):
#         print(inner_list[j])
#         j += 1
#     i += 1  
# 9. Iterating over a Set(Multidimensional)(More Than Two Sets)(Frozen Set)(Generalised Method)(Can be also be done by lambda() function and explicit conversion into List method like done in # 8):- 
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# frozenset3 = frozenset(["John", "Doe", "Smith"])
# multidimensional_set = {frozenset1, frozenset2, frozenset3}
# multidimensional_list = list(multidimensional_set)
# order = [2, 0, 1]
# order_index = 0
# while order_index < len(order):
#     inner_set = multidimensional_list[order[order_index]]
#     inner_list = list(inner_set)
#     i = 0
#     while i < len(inner_list):
#         print(inner_list[i])
#         i += 1
#     order_index += 1
# 10. Iterating over a Dictionary(1-D)(Keys):-
# my_dict = {"Amit": 100, "Aarpit": 99, "Rahul": 98}
# keys_list = list(my_dict.keys())
# keys_list.reverse()
# i = 0
# while i < len(keys_list):
#     key = keys_list[i]
#     print(key)
#     print(f"{key}:{my_dict[key]}")
#     i += 1
# 11. Iterating over a Dictionary(Multidimensional)(2-D only)(Or n-D and we want reverse of the Dictionary)(Keys):-
# my_dict = {"student1":{"Amit": 100, "Aarpit": 99, "Rahul": 98}, "student2":{"Amit": 102, "Aarpit": 96, "Rahul": 95}}
# keys_list = list(my_dict.keys())
# keys_list.reverse()
# i = 0
# while i < len(keys_list):
#     key = keys_list[i]
#     print(key)
#     print(f"{key}: {my_dict[key]}")
#     i += 1
# 11(a). Iterating over a Dictionary(Multidimensional)(More than two dictionares)(Generalised Method)(Keys):-
# my_dict = {
#     "student1": {"Amit": 100, "Aarpit": 99, "Rahul": 98},
#     "student2": {"Amit": 101, "Aarpit": 97, "Rahul": 96},
#     "student3": {"John": 95, "Doe": 94, "Smith": 93}
# }
# order = [2, 0, 1]
# keys_list = list(my_dict.keys())
# order_index = 0
# while order_index < len(order):
#     key = keys_list[order[order_index]]
#     print(key)
#     print(f"{key}: {my_dict[key]}")
#     order_index += 1
# 12. Iterating over a Dictionary(1-D)(Values):-
# my_dict = {"Amit": 100, "Aarpit": 99, "Rahul": 98}
# values_list = list(my_dict.values())
# values_list.reverse()
# i = 0
# while i < len(values_list):
#     value = values_list[i]
#     print(value)
#     i += 1
# 13. Iterating over a Dictionary(Multidimensional)(2-D only)(Or n-D and we want reverse of the Dictionary)(Values):-
# my_dict = {"student1":{"Amit": 100, "Aarpit": 99, "Rahul": 98}, "student2":{"Amit": 102, "Aarpit": 96, "Rahul": 94}}
# values_list = list(my_dict.values())
# values_list.reverse()
# i = 0
# while i < len(values_list):
#     value = values_list[i]
#     print(value)
#     i += 1
# 13(a). Iterating over a Dictionary(Multidimensional)(More than two dictionares)(Generalised Method)(Values):-
# my_dict = {
#     "student1": {"Amit": 100, "Aarpit": 99, "Rahul": 98},
#     "student2": {"Amit": 102, "Aarpit": 95, "Rahul": 96},
#     "student3": {"John": 95, "Doe": 94, "Smith": 93}
# }
# order = [2, 0, 1]
# values_list = list(my_dict.values())
# order_index = 0
# while order_index < len(order):
#     value = values_list[order[order_index]]
#     print(value)
#     order_index += 1
# 14. Iterating over a Dictionary(1-D)(Key-Value Pairs):-
# my_dict = {"Amit": 100, "Aarpit": 99, "Rahul": 98}
# items_list = list(my_dict.items())
# items_list.reverse()
# i = 0
# while i < len(items_list):
#     key, value = items_list[i]
#     print(f"{key}: {value}")
#     i += 1
# 15. Iterating over a Dictionary(Multidimensional)(2-D only)(Or n-D and we want reverse of the Dictionary)(Key-Value Pairs):-
# my_dict = {"student1":{"Amit": 100, "Aarpit": 99, "Rahul": 98}, "student2":{"Amit": 102, "Aarpit": 96, "Rahul": 95}}
# items_list = list(my_dict.items())
# items_list.reverse()
# i = 0
# while i < len(items_list):
#     key, value = items_list[i]
#     print(f"{key}: {value}")
#     i += 1
# 15(a). Iterating over a Dictionary(Multidimensional)(More than two dictionares)(Generalised Method)(Key-Value Pairs):-
# my_dict = {
#     "student1": {"Amit": 100, "Aarpit": 99, "Rahul": 98},
#     "student2": {"Amit": 102, "Aarpit": 95, "Rahul": 96},
#     "student3": {"John": 95, "Doe": 94, "Smith": 93}
# }
# order = [2, 0, 1]
# items_list = list(my_dict.items())
# order_index = 0
# while order_index < len(order):
#     key,value = items_list[order[order_index]]
#     print(f"{key}: {value}")
#     order_index += 1
# 16. Multidimensional Dictionary containing Multidimensional(2-D only)(lists, tuples, and sets (frozensets)):-
# Declaration:-
# multi_dict = {
#     "lists": {
#         "list1": [[1, 2, 3], [4, 5, 6]],
#         "list2": [["Amit", "Aarpit"], ["John", "Doe"]]
#     },
#     "tuples": {
#         "tuple1": ((1, 2, 3), (4, 5, 6)),
#         "tuple2": (("Amit", "Aarpit"), ("John", "Doe"))
#     },
#     "sets": {
#         "set1": {frozenset([1, 2, 3]), frozenset([4, 5, 6])},
#         "set2": {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}
#     }
# }
# Accessing and Printing(With While Loop):-
  # Access and print lists:-
# list_keys = list(multi_dict["lists"].keys())
# i = 0
# while i < len(list_keys):
#     key = list_keys[i]
#     print(f"{key}: {multi_dict['lists'][key]}")
#     i += 1
  # Access and print tuples:-
# tuple_keys = list(multi_dict["tuples"].keys())
# i = 0
# while i < len(tuple_keys):
#     key = tuple_keys[i]
#     print(f"{key}: {multi_dict['tuples'][key]}")
#     i += 1
  # Access and print sets:-
# set_keys = list(multi_dict["sets"].keys())
# i = 0
# while i < len(set_keys):
#     key = set_keys[i]
#     print(f"{key}: {multi_dict['sets'][key]}")
#     i += 1
  # Access and print the full dictionary:-
# keys = list(multi_dict.keys())
# i = 0
# while i < len(keys):
#     key = keys[i]
#     print(f"{key}: {multi_dict[key]}")
#     i += 1
# Accessing and Printing(Without While Loop):-
  # Access and print lists:-
# print(f"list1: {multi_dict['lists']['list1']}")
# print(f"list2: {multi_dict['lists']['list2']}")
  # Access and print tuples:-
# print(f"tuple1: {multi_dict['tuples']['tuple1']}")
# print(f"tuple2: {multi_dict['tuples']['tuple2']}")
  # Access and print sets:-
# print(f"set1: {multi_dict['sets']['set1']}")
# print(f"set2: {multi_dict['sets']['set2']}")
  # Access and print the full dictionary:-
# print(multi_dict)
# Modifying:-
  # Modify a list:-
# multi_dict["lists"]["list1"][0][0] = 10
  # Modify a tuple(tuples are immutable, so we need to create a new tuple):-
# multi_dict["tuples"]["tuple1"] = ((10, 2, 3), (4, 5, 6))
  # Modify a set(frozensets are immutable, so we need to create a new frozenset):-
# multi_dict["sets"]["set1"] = {frozenset([10, 2, 3]), frozenset([4, 5, 6])}
# 17. Multidimensional Dictionary containing Singledimensional(1-D)(lists, tuples, and sets):-
# Declaration:-
# multi_dict = {
#     "lists": {
#         "list1": [1, 2, 3],
#         "list2": ["Amit", "Aarpit", "John"]
#     },
#     "tuples": {
#         "tuple1": (1, 2, 3),
#         "tuple2": ("Amit", "Aarpit", "John")
#     },
#     "sets": {
#         "set1": frozenset([1, 2, 3]),
#         "set2": frozenset(["Amit", "Aarpit", "John"])
#     }
# }
# Accessing and Printing(With While Loop):-
  # Access and print lists:-
# list_keys = list(multi_dict["lists"].keys())
# i = 0
# while i < len(list_keys):
#     key = list_keys[i]
#     print(f"{key}: {multi_dict['lists'][key]}")
#     i += 1
  # Access and print tuples:-
# tuple_keys = list(multi_dict["tuples"].keys())
# i = 0
# while i < len(tuple_keys):
#     key = tuple_keys[i]
#     print(f"{key}: {multi_dict['tuples'][key]}")
#     i += 1
  # Access and print sets:-
# set_keys = list(multi_dict["sets"].keys())
# i = 0
# while i < len(set_keys):
#     key = set_keys[i]
#     print(f"{key}: {multi_dict['sets'][key]}")
#     i += 1
  # Access and print the full dictionary:-
# keys = list(multi_dict.keys())
# i = 0
# while i < len(keys):
#     key = keys[i]
#     print(f"{key}: {multi_dict[key]}")
#     i += 1
# Accessing and Printing(Without While Loop):-
  # Access and print lists:-
# print(f"list1: {multi_dict['lists']['list1']}")
# print(f"list2: {multi_dict['lists']['list2']}")
  # Access and print tuples:-
# print(f"tuple1: {multi_dict['tuples']['tuple1']}")
# print(f"tuple2: {multi_dict['tuples']['tuple2']}")
  # Access and print sets:-
# print(f"set1: {multi_dict['sets']['set1']}")
# print(f"set2: {multi_dict['sets']['set2']}")
  # Access and print the full dictionary:-
# print(multi_dict)
# Modifying:-
  # Modify a list:-
# multi_dict["lists"]["list1"][0] = 10
  # Modify a tuple(tuples are immutable, so we need to create a new tuple):-
# multi_dict["tuples"]["tuple1"] = (10, 2, 3)
  # Modify a set(frozensets are immutable, so we need to create a new frozenset):-
# multi_dict["sets"]["set1"] = frozenset([10, 2, 3])
# 18. Multidimensional Dictionary containing Multidimensional(lists, tuples, and sets (frozensets)) Methods:-
# 1. Append
# Append an element to a specific row
# multi_dict["lists"]["list1"].append([7, 8, 9])
# print(multi_dict)
# Output: {'lists': {'list1': [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 'list2': [['Amit', 'Aarpit'], ['John', 'Doe']]], 'tuples': {'tuple1': ((1, 2, 3), (4, 5, 6)), 'tuple2': (('Amit', 'Aarpit'), ('John', 'Doe'))}, 'sets': {'set1': {frozenset([1, 2, 3]), frozenset([4, 5, 6])}, 'set2': {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}}}
# 2. Remove
# Remove an element from a specific row
# multi_dict["lists"]["list1"].remove([4, 5, 6])
# print(multi_dict)
# Output: {'lists': {'list1': [[1, 2, 3], [7, 8, 9]], 'list2': [['Amit', 'Aarpit'], ['John', 'Doe']]], 'tuples': {'tuple1': ((1, 2, 3), (4, 5, 6)), 'tuple2': (('Amit', 'Aarpit'), ('John', 'Doe'))}, 'sets': {'set1': {frozenset([1, 2, 3]), frozenset([4, 5, 6])}, 'set2': {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}}}
# 3. Pop
# Pop an element from a specific row
# popped_element = multi_dict["lists"]["list1"].pop(1)
# print(popped_element)  # Output: [7, 8, 9]
# print(multi_dict)
# Output: {'lists': {'list1': [[1, 2, 3], [8, 9]], 'list2': [['Amit', 'Aarpit'], ['John', 'Doe']]], 'tuples': {'tuple1': ((1, 2, 3), (4, 5, 6)), 'tuple2': (('Amit', 'Aarpit'), ('John', 'Doe'))}, 'sets': {'set1': {frozenset([1, 2, 3]), frozenset([4, 5, 6])}, 'set2': {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}}}
# 4. Extend
# Extend a specific row with another list
# multi_dict["lists"]["list1"].extend([[10, 11, 12], [13, 14, 15]])
# print(multi_dict)
# Output: {'lists': {'list1': [[1, 2, 3], [8, 9], [10, 11, 12], [13, 14, 15]], 'list2': [['Amit', 'Aarpit'], ['John', 'Doe']]], 'tuples': {'tuple1': ((1, 2, 3), (4, 5, 6)), 'tuple2': (('Amit', 'Aarpit'), ('John', 'Doe'))}, 'sets': {'set1': {frozenset([1, 2, 3]), frozenset([4, 5, 6])}, 'set2': {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}}}
# 5. Update
# Update a specific row with another dictionary
# multi_dict["lists"]["list1"].update({"list1": [[16, 17, 18], [19, 20, 21]]})
# print(multi_dict)
# Output: {'lists': {'list1': [[1, 2, 3], [8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]], 'list2': [['Amit', 'Aarpit'], ['John', 'Doe']]], 'tuples': {'tuple1': ((1, 2, 3), (4, 5, 6)), 'tuple2': (('Amit', 'Aarpit'), ('John', 'Doe'))}, 'sets': {'set1': {frozenset([1, 2, 3]), frozenset([4, 5, 6])}, 'set2': {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}}}
# 6. Clear
# Clear all elements from a specific row
# multi_dict["lists"]["list1"].clear()
# print(multi_dict)
# Output: {'lists': {'list1': [], 'list2': [['Amit', 'Aarpit'], ['John', 'Doe']]], 'tuples': {'tuple1': ((1, 2, 3), (4, 5, 6)), 'tuple2': (('Amit', 'Aarpit'), ('John', 'Doe'))}, 'sets': {'set1': {frozenset([1, 2, 3]), frozenset([4, 5, 6])}, 'set2': {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}}}
# 7. Copy
# Copy a specific row
# copied_list = multi_dict["lists"]["list1"].copy()
# print(copied_list)
# Output: [[1, 2, 3], [8, 9], [10, 11, 12], [13, 14, 15]]
# 8. Reverse
# Reverse a specific row
# multi_dict["lists"]["list1"].reverse()
# print(multi_dict)
# Output: {'lists': {'list1': [[13, 14, 15], [10, 11, 12], [8, 9], [1, 2, 3]], 'list2': [['Amit', 'Aarpit'], ['John', 'Doe']]], 'tuples': {'tuple1': ((1, 2, 3), (4, 5, 6)), 'tuple2': (('Amit', 'Aarpit'), ('John', 'Doe'))}, 'sets': {'set1': {frozenset([1, 2, 3]), frozenset([4, 5, 6])}, 'set2': {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}}}
# 9. Sort
# Sort a specific row
# multi_dict["lists"]["list1"].sort()
# print(multi_dict)
# Output: {'lists': {'list1': [[1, 2, 3], [8, 9], [10, 11, 12], [13, 14, 15]], 'list2': [['Amit', 'Aarpit'], ['John', 'Doe']]], 'tuples':    {'tuple1': ((1, 2, 3), (4, 5, 6)), 'tuple2': (('Amit', 'Aarpit'), ('John', 'Doe'))}, 'sets': {'set1': {frozenset([1, 2, 3]), frozenset([4, 5, 6])}, 'set2': {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}}}
# 10. Index
# Find the index of a specific element in a specific row
# index = multi_dict["lists"]["list1"].index([10, 11, 12])
# print(index)  # Output: 2
# 11. Count
# Count the number of occurrences of a specific element in a specific row
# count = multi_dict["lists"]["list1"].count([10, 11, 12])
# print(count)  # Output: 1
# 12. Length
# Get the length of a specific row
# length = len(multi_dict["lists"]["list1"])
# print(length)  # Output: 4
# 13. Sum
# Get the sum of all elements in a specific row
# sum = sum(multi_dict["lists"]["list1"])
# print(sum)  # Output: 55
# 14. Minimum
# Get the minimum element in a specific row
# min_element = min(multi_dict["lists"]["list1"])
# print(min_element)  # Output: 1
# 15. Maximum
# Get the maximum element in a specific row
# max_element = max(multi_dict["lists"]["list1"])
# print(max_element)  # Output: 15
# 16. Average
# Get the average of all elements in a specific row
# average = sum(multi_dict["lists"]["list1"]) / len(multi_dict["lists"]["list1"])
# print(average)  # Output: 13.75
# 17. All
# Check if all elements in a specific row are True
# all_elements_true = all(multi_dict["lists"]["list1"])
# print(all_elements_true)  # Output: True
# 18. Any
# Check if any element in a specific row is True
# any_element_true = any(multi_dict["lists"]["list1"])
# print(any_element_true)  # Output: True
# 19. Zip
# Zip two or more lists into a list of tuples
# zipped_list = zip(multi_dict["lists"]["list1"], multi_dict["lists"]["list2"])
# print(list(zipped_list))  # Output: [(1, 'Amit'), (2, 'Aarpit'), (3, 'John'), (4, 'Doe')]
# 20. Unzip
# Unzip a list of tuples into two lists
# unzipped_list1, unzipped_list2 = zip(*zipped_list)
# print(list(unzipped_list1))  # Output: [1, 2, 3, 4]
# print(list(unzipped_list2))  # Output: ['Amit', 'Aarpit', 'John', 'Doe']
# 21. Flatten
# Flatten a list of lists into a single list
# flattened_list = [item for sublist in multi_dict["lists"]["list1"] for item in sublist]
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6, 'Amit', 'Aarpit', 'John', 'Doe']
# 22. Flatten with Depth
# Flatten a list of lists with a specified depth into a single list
# flattened_list = flatten(multi_dict["lists"]["list1"], depth=1)
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
# 23. Flatten with Depth and Skip None
# Flatten a list of lists with a specified depth and skip None values into a single list
# flattened_list = flatten(multi_dict["lists"]["list1"], depth=1, skip_none=True)
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
# 24. Flatten with Depth and Skip None and Skip Empty
# Flatten a list of lists with a specified depth and skip None and empty values into a single list
# flattened_list = flatten(multi_dict["lists"]["list1"], depth=1, skip_none=True, skip_empty=True)
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
# 25. Flatten with Depth and Skip None and Skip Empty and Skip Empty Lists
# Flatten a list of lists with a specified depth and skip None, empty, and empty lists into a single list
# flattened_list = flatten(multi_dict["lists"]["list1"], depth=1, skip_none=True, skip_empty=True, skip_empty_lists=True)
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
# 26. Flatten with Depth and Skip None and Skip Empty and Skip Empty Lists and Skip Empty Tuples
# Flatten a list of lists with a specified depth and skip None, empty, empty lists, and empty tuples into a single list
# flattened_list = flatten(multi_dict["lists"]["list1"], depth=1, skip_none=True, skip_empty=True, skip_empty_lists=True, skip_empty_tuples=True)
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
# 27. Flatten with Depth and Skip None and Skip Empty and Skip Empty Lists and Skip Empty Tuples and Skip Empty Sets
# Flatten a list of lists with a specified depth and skip None, empty, empty lists, empty tuples, and empty sets into a single list
# flattened_list = flatten(multi_dict["lists"]["list1"], depth=1, skip_none=True, skip_empty=True, skip_empty_lists=True, skip_empty_tuples=True, skip_empty_sets=True)
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
# 28. Flatten with Depth and Skip None and Skip Empty and Skip Empty Lists and Skip Empty Tuples and Skip Empty Sets and Skip Empty Dictionaries
# Flatten a list of lists with a specified depth and skip None, empty, empty lists, empty tuples, empty sets, and empty dictionaries into a single list
# flattened_list = flatten(multi_dict["lists"]["list1"], depth=1, skip_none=True, skip_empty=True, skip_empty_lists=True, skip_empty_tuples=True, skip_empty_sets=True, skip_empty_dictionaries=True)
# print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

# For Loops(We can use Conditional statements,Relational operators whenever required inside For loop)
# for i in range(0,4,1): # Range syntax:- (start,end,skip value(optional))
    # print(i)
# We can also Use Skip Value To print a sequence in reverse order like illustated below:-
# n = int(input())
# for i in range(10, 0, -1):
#     print(f"{n} * {i} = {n * i}")
# import itertools
# for i in itertools.count(): # Infinite Loop
    # print(i)
# Use Of Break,Continue And Pass Statements In For Loop:-
# for i in range(10):
    # if i == 3:
        # continue  # Skip the rest of the loop when i is 3
    # if i == 5:
        # pass  # Do nothing when i is 5(Pass is a null statement in Python)
    # if i == 7:
        # break  # Exit the loop when i is 7
    # print(i)  # Output = 0,1,2,4,5,6
# Use Of For Loop With Else statement(Used when for loop is exhausted then the content of the else loop is printed):-
# l= [1,3,4]
# for i in l:
#     print(i)
# else:
#     print("Done") 
# If 'Break' statement is encountered inside the for loop then else will not be executed:-
# l = [1, 3, 4]
# for i in l:
    # if i == 3:
        # break
    # print(i)
# else:
    # print("Done") # Output = 1 

# Loop in Multiple Lists with zip()
# >>> furniture = ['table', 'chair', 'rack', 'shelf']
# >>> price = [100, 50, 80, 40]
# >>> for item, amount in zip(furniture, price):
# ...     print(f'The {item} costs ${amount}')
# The table costs $100
# The chair costs $50
# The rack costs $80
# The shelf costs $40

# 1. Iterating over a list(1-D):-
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# for i in range(len(my_list)):
#     print(my_list[i])
# 2. Iterating over a list(Multidimensional)(2-D only)(Or n-D and we want reverse of the list):-
# my_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
# my_list.reverse()
# for i in range(len(my_list)):
    # print(my_list[i])
# 2(a). Iterating over a list(Multidimensional)(More Than Two Lists)(Generalised Method):-
# my_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
# order = [2, 0, 1]
# for order_index in order:
#     inner_list = my_list[order_index]
#     for i in range(len(inner_list)):
#         print(inner_list[i])
# 3. Iterating over a Tuple(1-D)(Without converting into List):-
# my_tuple = (1, 2, 3, 4, 5)
# for i in range(len(my_tuple)):
#     print(my_tuple[i])
# 4. Iterating over a Tuple(Multidimensional)(Without converting into List)(2-D only)(Or n-D and we want reverse of the Tuple):-
# my_tuple = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10))
# for i in range(len(my_tuple)):
#     print(my_tuple[i])
# 4(a). Iterating over a Tuple(Multidimensional)(Without converting into List)(More Than Two Tuples)(Generalised Method):-
# my_tuple = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15))
# order = [2, 0, 1]
# for order_index in order:
#     inner_tuple = my_tuple[order_index]
#     for i in range(len(inner_tuple)):
#         print(inner_tuple[i])
# 5. Iterating over a Tuple(1-D)(Converting into List):-
# my_tuple = (1, 2, 3, 4, 5)
# tuple_list = list(my_tuple)
# tuple_list.reverse()
# for i in range(len(tuple_list)):
#     print(tuple_list[i])
# 6. Iterating over a Tuple(Multidimensional)(Converting into List)(2-D only)(Or n-D and we want reverse of the Tuple):-
# my_tuple = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10))
# tuple_list = list(my_tuple)
# tuple_list.reverse()
# for i in range(len(tuple_list)):
#     print(tuple_list[i])
# 6(a). Iterating over a Tuple(Multidimensional)(Converting into List)(More Than Two Tuples)(Generalised Method):-
# my_tuple = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15))
# tuple_list = list(my_tuple)
# order = [2, 0, 1]
# for order_index in order:
#     inner_tuple = tuple_list[order_index]
#     for i in range(len(inner_tuple)):
#         print(inner_tuple[i])
# 7. Iterating over a Set(1-D):-
# my_set = {1, 2, 3, 4, 5}
# set_list = list(my_set)
# set_list.reverse()
# for i in range(len(set_list)):
#     print(set_list[i])
# 8. Iterating over a Set(Multidimensional)(2-D only)(Or n-D and we want reverse of the Set)(Frozen Set):-
   # (a). Print second frozen sets content first:-
     # (i). Method 1(Typecasting)(Without lambda() function):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = {frozenset1, frozenset2}
# multidimensional_list = list(multidimensional_set)
# for i in range(len(multidimensional_list)):
#     inner_set = multidimensional_list[i]
#     inner_list = list(inner_set)
#     for j in range(len(inner_list)):
#         print(inner_list[j])
     # (ii). Method 2(Typecasting)(With lambda() function):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = {frozenset1, frozenset2}
# multidimensional_list = list(multidimensional_set)
# multidimensional_list.sort(key=lambda x: x != frozenset2)
# for i in range(len(multidimensional_list)):
#     inner_set = multidimensional_list[i]
#     inner_list = list(inner_set)
#     for j in range(len(inner_list)):
#         print(inner_list[j])
     # (iii). Method 3(Explicitly converting into List):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = [frozenset2, frozenset1]
# for i in range(len(multidimensional_set)):
#     inner_set = multidimensional_set[i]
#     inner_list = list(inner_set)
#     for j in range(len(inner_list)):
#         print(inner_list[j])
   # (b). Print first frozen sets content first:-
     # (i). Method 1(Typecasting):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = {frozenset1, frozenset2}
# multidimensional_list = list(multidimensional_set)
# multidimensional_list.sort(key=lambda x: x != frozenset1)
# for i in range(len(multidimensional_list)):
#     inner_set = multidimensional_list[i]
#     inner_list = list(inner_set)
#     for j in range(len(inner_list)):
#         print(inner_list[j])
     # (ii). Method 2(Explicitly converting into List):-
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# multidimensional_set = [frozenset2, frozenset1]
# for i in range(len(multidimensional_set)):
#     inner_set = multidimensional_set[i]
#     inner_list = list(inner_set)
#     for j in range(len(inner_list)):
#         print(inner_list[j])
# 9. Iterating over a Set(Multidimensional)(More Than Two Sets)(Frozen Set)(Generalised Method)(Can be also be done by lambda() function and explicit conversion into List method like done in # 8):- 
# frozenset1 = frozenset(["Amit", "Aarpit", "Rahul"])
# frozenset2 = frozenset([1, 2, 3, 4, 5])
# frozenset3 = frozenset(["John", "Doe", "Smith"])
# multidimensional_set = {frozenset1, frozenset2, frozenset3}
# multidimensional_list = list(multidimensional_set)
# order = [2, 0, 1]
# for order_index in order:
#     inner_set = multidimensional_list[order_index]
#     inner_list = list(inner_set)
#     for i in range(len(inner_list)):
#         print(inner_list[i])
# 10. Iterating over a Dictionary(1-D)(Keys):-
# my_dict = {"Amit": 100, "Aarpit": 99, "Rahul": 98}
# keys_list = list(my_dict.keys())
# keys_list.reverse()
# for i in range(len(keys_list)):
#     key = keys_list[i]
#     print(key)
#     print(f"{key}: {my_dict[key]}")
# 11. Iterating over a Dictionary(Multidimensional)(2-D only)(Or n-D and we want reverse of the Dictionary)(Keys):-
# my_dict = {"student1": {"Amit": 100, "Aarpit": 99, "Rahul": 98}, "student2": {"Amit": 102, "Aarpit": 96, "Rahul": 95}}
# keys_list = list(my_dict.keys())
# keys_list.reverse()
# for i in range(len(keys_list)):
#     key = keys_list[i]
#     print(key)
#     print(f"{key}: {my_dict[key]}")
# 11(a). Iterating over a Dictionary(Multidimensional)(More than two dictionares)(Generalised Method)(Keys):-
# my_dict = {
#     "student1": {"Amit": 100, "Aarpit": 99, "Rahul": 98},
#     "student2": {"Amit": 101, "Aarpit": 97, "Rahul": 96},
#     "student3": {"John": 95, "Doe": 94, "Smith": 93}
# }
# order = [2, 0, 1]
# keys_list = list(my_dict.keys())
# for order_index in order:
#     key = keys_list[order_index]
#     print(key)
#     print(f"{key}: {my_dict[key]}")
# 12. Iterating over a Dictionary(1-D)(Values):-
# my_dict = {"Amit": 100, "Aarpit": 99, "Rahul": 98}
# values_list = list(my_dict.values())
# values_list.reverse()
# for i in range(len(values_list)):
#     value = values_list[i]
#     print(value)
# 13. Iterating over a Dictionary(Multidimensional)(2-D only)(Or n-D and we want reverse of the Dictionary)(Values):-
# my_dict = {"student1": {"Amit": 100, "Aarpit": 99, "Rahul": 98}, "student2": {"Amit": 102, "Aarpit": 96, "Rahul": 94}}
# values_list = list(my_dict.values())
# values_list.reverse()
# for i in range(len(values_list)):
#     value = values_list[i]
#     print(value)
# 13(a). Iterating over a Dictionary(Multidimensional)(More than two dictionares)(Generalised Method)(Values):-
# my_dict = {
#     "student1": {"Amit": 100, "Aarpit": 99, "Rahul": 98},
#     "student2": {"Amit": 102, "Aarpit": 95, "Rahul": 96},
#     "student3": {"John": 95, "Doe": 94, "Smith": 93}
# }
# order = [2, 0, 1]
# values_list = list(my_dict.values())
# for order_index in order:
#     value = values_list[order_index]
#     print(value)
# 14. Iterating over a Dictionary(1-D)(Key-Value Pairs):-
# my_dict = {"Amit": 100, "Aarpit": 99, "Rahul": 98}
# items_list = list(my_dict.items())
# items_list.reverse()
# for i in range(len(items_list)):
#     key, value = items_list[i]
#     print(f"{key}: {value}")
# 15. Iterating over a Dictionary(Multidimensional)(2-D only)(Or n-D and we want reverse of the Dictionary)(Key-Value Pairs):-
# my_dict = {"student1": {"Amit": 100, "Aarpit": 99, "Rahul": 98}, "student2": {"Amit": 102, "Aarpit": 96, "Rahul": 95}}
# items_list = list(my_dict.items())
# items_list.reverse()
# for i in range(len(items_list)):
#     key, value = items_list[i]
#     print(f"{key}: {value}")
# 15(a). Iterating over a Dictionary(Multidimensional)(More than two dictionares)(Generalised Method)(Key-Value Pairs):-
# my_dict = {
#     "student1": {"Amit": 100, "Aarpit": 99, "Rahul": 98},
#     "student2": {"Amit": 102, "Aarpit": 95, "Rahul": 96},
#     "student3": {"John": 95, "Doe": 94, "Smith": 93}
# }
# order = [2, 0, 1]
# items_list = list(my_dict.items())
# for order_index in order:
#     key, value = items_list[order_index]
#     print(f"{key}: {value}")
# 16. Multidimensional Dictionary containing Multidimensional(2-D only)(lists, tuples, and sets (frozensets)):-
# Declaration:-
# multi_dict = {
#     "lists": {
#         "list1": [[1, 2, 3], [4, 5, 6]],
#         "list2": [["Amit", "Aarpit"], ["John", "Doe"]]
#     },
#     "tuples": {
#         "tuple1": ((1, 2, 3), (4, 5, 6)),
#         "tuple2": (("Amit", "Aarpit"), ("John", "Doe"))
#     },
#     "sets": {
#         "set1": {frozenset([1, 2, 3]), frozenset([4, 5, 6])},
#         "set2": {frozenset(["Amit", "Aarpit"]), frozenset(["John", "Doe"])}
#     }
# }
# Accessing and Printing(With For Loop)(Using Enumerate function()):-
  # Access and print lists:-
# list_keys = list(multi_dict["lists"].keys())
# for i, key in enumerate(list_keys):
#     print(f"{key}: {multi_dict['lists'][key]}")
  # Access and print tuples:-
# tuple_keys = list(multi_dict["tuples"].keys())
# for i, key in enumerate(tuple_keys):
#     print(f"{key}: {multi_dict['tuples'][key]}")
  # Access and print sets:-
# set_keys = list(multi_dict["sets"].keys())
# for i, key in enumerate(set_keys):
#     print(f"{key}: {multi_dict['sets'][key]}")
  # Access and print the full dictionary:-
# keys = list(multi_dict.keys())
# for i, key in enumerate(keys):
#     print(f"{key}: {multi_dict[key]}")
# 17. Multidimensional Dictionary containing Singledimensional(1-D)(lists, tuples, and sets):-
# Declaration:-
# multi_dict = {
#     "lists": {
#         "list1": [1, 2, 3],
#         "list2": ["Amit", "Aarpit", "John"]
#     },
#     "tuples": {
#         "tuple1": (1, 2, 3),
#         "tuple2": ("Amit", "Aarpit", "John")
#     },
#     "sets": {
#         "set1": frozenset([1, 2, 3]),
#         "set2": frozenset(["Amit", "Aarpit", "John"])
#     }
# }
# Accessing and Printing(With For Loop)(Using Enumerate Function()):-
  # Access and print lists:-
# list_keys = list(multi_dict["lists"].keys())
# for i, key in enumerate(list_keys):
#     print(f"{key}: {multi_dict['lists'][key]}")
  # Access and print tuples:-
# tuple_keys = list(multi_dict["tuples"].keys())
# for i, key in enumerate(tuple_keys):
#     print(f"{key}: {multi_dict['tuples'][key]}")
  # Access and print sets:-
# set_keys = list(multi_dict["sets"].keys())
# for i, key in enumerate(set_keys):
#     print(f"{key}: {multi_dict['sets'][key]}")
  # Access and print the full dictionary:-
# keys = list(multi_dict.keys())
# for i, key in enumerate(keys):
#     print(f"{key}: {multi_dict[key]}")
# Star Patterns With For Loop:
'''
  *
 ***
*****
''' 
# n =int(input())
# for i in range(1,n+1):
  # print(" "* (n-i), end="") # end="" is to ensure we do not get a new line by default that we get after print function is executed
  # print("*"* (2*i-1), end="")
  # print("") # To get a new line do not put '/n' as that would produce another extra new line
'''
*
**
***
'''
# n =int(input())
# for i in range(1,n+1):
#   print("*"*i, end="")
#   print("")
'''
***
* *
***
'''
# n = int(input())
# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"* n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2),end="")
#         print("*", end="")
#     print("")

# Functions And Recursion:-

# Functions:-
# import sys
# def fun():
#     print("Hello")
#     return
#     sys.exit()
#     fun()
# fun()
# Function with Arguments:-
# def fun(name,ending = "Thank You"):
#   print("Hello " + name)
#   print(f"Hello {name}")
#   print(ending)
#   gr = "Hello " + name
#   return gr
# gr1 = fun(input())  
# print(gr1)
# def rem(l,word):
#   n=[]
#   for i in l:
#     if (i!=word):
#       n.append(i.strip(word))
#   return n
# l = ["Harry", "Rohan", "Divesh","an"]
# print(rem(l,"an"))

# Recursion:-
# def factorial(n):
#   if(n==0 or n==1):
#     return 1
#   return n * factorial(n-1)
# n = int(input())
# print(factorial(n))  

### PROJECT 1:- SNAKE,WATER AND GUN GAME:-
'''
1 for snake
-1 for water
0 for gun
'''
# import sys
# import random
# print("WELCOME TO SNAKE,WATER AND GUN GAME\n")
# while(True):
#  print("Press 1 To Play or 2 To Exit")
#  choice = int(input())
#  if(choice==1):
#   computer = random.choice([1,0,1])
#   print("Choices Available: Snake(s),Water(w),Gun(g). Please Choose one from the text written in brackets")
#   youstr = (input("Please Enter your choice: "))
#   if(youstr == "s" or youstr == "w" or youstr == "g"):
#    youDict = {"s":1, "w":-1, "g":0}
#    reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
#    you = youDict[youstr]
#    print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
#    if(computer == -1 and you == 1):
#     print("You Won Congrats!\n")
#    if(computer == -1 and you == 0):
#     print("You Lose Better Luck Next Time!\n")
#    if(computer == 1 and you == 0):
#     print("You Won Congrats!\n")
#    if(computer == 1 and you == -1):
#     print("You Lose Better Luck Next Time!\n")
#    if(computer == 0 and you == -1):
#     print("You Won Congrats!\n")
#    if(computer == 0 and you == 1):
#     print("You Lose Better Luck Next Time!\n")
#    elif(computer == you):
#     print("Tie!\n")
#   else:
#    print("Wrong Choice Entered, Please Try Again")
#  elif(choice == 2):
#    print("Thanks for Playing, Hope You Liked The Game!")
#    sys.exit()
'''
Shortened Version:-
'''
# import sys
# import random
# print("WELCOME TO SNAKE,WATER AND GUN GAME\n")
# while(True):
#  print("Press 1 To Play or 2 To Exit")
#  userchoice = int(input())
#  if(userchoice==1):
#   computer = random.choice([1,0,1])
#   print("Choices Available: Snake(s),Water(w),Gun(g). Please Choose one from the text written in brackets")
#   youstr = (input("Please Enter your choice: "))
#   if(youstr == "s" or youstr == "w" or youstr == "g"):
#    youDict = {"s":1, "w":-1, "g":0}
#    reverseDict = {1:"Snake", -1:"Water", 0:"Gun"}
#    you = youDict[youstr]
#    print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
#    if(computer - you == -1 or computer - you == 2):
#     print("You Lose Better Luck Next Time!\n")
#    elif(computer - you != -1 or computer - you != 2):
#     print("You Won Congrats!")
#    elif(computer == you):
#     print("Tie!\n")
#   else:
#    print("Wrong Choice Entered, Please Try Again")
#  elif(userchoice == 2):
#    print("Thanks for Playing, Hope You Liked The Game!")
#    sys.exit()

# File I/O Operations:-

# f = open("file.txt", "r") # By default read mode
# print(f.read())
# f.close()
# st = "Hi I am Aarpit!"
# f =open("file.txt","r")
# f.write(st)
# print(f.readlines(),type(f.readlines())) # Read All Lines Together
# print(f.readline()) # Read Individual Lines
# line = f.readline()
# while(line!= ""):
#     print(line)
#     line = f.readline()
# f.close()
# With Statement(Removes the burden of closing the file explicitly):-
# with open("file.txt") as f:
#   print(f.read())
# import random
# def game():
#   print("You are Playing the Game...")
#   score = random.randint(1,62)
#   with open("hiscore.txt","r") as f:
#     hiscore = f.read()
#     if(hiscore!=""):
#       hiscore = int(hiscore)
#     else:
#       hiscore=0
#   print(f"Your score is {score}")
#   if(score>hiscore):
#     with open("hiscore.txt","w") as f:
#       f.write(str(score))
# game()      
# def generateTable(n):
    # table = "" # Declare Table as an Empty String Because we have to import it in file and file only accepts string format
    # for i in range(1,11):
        # table += f"{n} * {i} = {n*i}\n" '''The table += operation is used to concatenate each line of the multiplication table to the table string.This approach allows you to build the entire table as a single string, which can then be written to the file in one go.It ensures that the table is formatted correctly, with each line on a new line in the file.'''
#     with open(f"tables/table_{n}","w") as f:
#         f.write(table)
# for i in range(2,21):
#     generateTable(i)        
# To Wipe contents of any file just open it in write mode and write f.write("") done!!

### OBJECT ORIENTED PROGRAMMING IN PYTHON(OOP):-

# CLASS(Blueprint for creating object)(Mutable):- 
# class Employee:
    # name = "Aarpit"
    # language = "Python"
    # salary = 1200000 # Here name,language and salary are Attributes(Here, 'Class Attributes' as they are directly defined inside a class without any futher functions(methods))
    # def getInfo(self): # Methods(Functions)
      # print(f"The Language is {self.language} and the salary is {self.salary}")

    # @staticmethod # To skip the usage of 'self' parameter inside the function definition. It is used as a 'Decorator'(Explained Later)
    # def greet():
      # print("Good Morning")

# Aarpit = Employee() # Here Aarpit is an 'Object(Instance)'. Memory is allocated only after Object instantiation and not when class is defined
# print(Employee.name,Employee.language)
# print(Aarpit.name,Aarpit.language)  # Both give same result
# Aarpit.getInfo()
# Aarpit.greet()
# Employee.getInfo(Aarpit) # Both give the same result
# Rohan = Employee()
# Rohan.name= "Rohan Robinson"
# print(Rohan.name,Rohan.language) # Here 'name' is an 'Object Attribute(Instance Attribute)' as it is related to 'Objects(Instances)' like 'Aarpit' and 'Rohan'
# Instance Attributes take Preference(Dominate) over Class Attributes during Assignment and Retrieval.

# Constructors(Compiler Runs this the very first even before the main function or anything else):-
 # Use Of _init_ Method(Runs even if it is not called outside like any other normal function)(Dunder Method):-
# class Employee:
#     name = "Aarpit"
#     language = "Python"
#    salary = 1200000
    # print(language) # Here Python will be printed not javascript. Also anywhere inside the class only class attributes will be printed. Inside any function or outside the class Instance attributes if declared dominate over class attributes or else class attributes are used everywhere.
    # def getInfo(self):
      # print(f"The Language is {self.language} and the salary is {self.salary}") # Here Javascript will be printed not python. Because Constructor will run first and set the value of self.language and self.salary to the one given outside. If any other normal function was there and this function was called first then it would print the class's content.
    # def __init__(self,name,language,salary):
      #  self.name = name
      #  self.language = language 
      #  self.salary = salary
      #  print(f"{self.name},{self.language},{self.salary}")
      #  print("Good Morning") # Runs and prints Good Morning even if it is explicitly not called outside. Will be called that many of times as a new object is created like here only one object is there which is Aarpit so it will print only one time. Also if we call this method explicitly with different arguments than that we passed inside the Employee class it will run 2 times once by default and will print the class Employee's arguments then again print the arguments of the _init_ method that we explicitly passed outside.
# Aarpit = Employee("Aarpit","Javascript",120000)
# Aarpit.getInfo()
# Aarpit.__init__("Rohan","C#",130000)
# Aarpit.getInfo()
# print(Aarpit.name,Aarpit.language) # Here even though we have not defined the instance attribute outside we have defined it inside the _init_ function and still the output will be the instance attribute if we print it outside the class,inside that function,or inside any other function also. So Instance Attributes always dominate be it outside or passed as arguments to a function inside the class.
# Note1:- If Two Instance Attributes Conflict then Inside the class any function would print the main class instance's(Here Employee) attributes. But if it is called again after declaring the respective function's argument then it will print that function's argument and so on i.e. updated globally together. Also the respective function which is called will print the respective instance's attributes not main instance's attributes. Now Outside the class if we print the instances then the instance declared just above's attributes will be printed i.e. the latest function declared attributes.
# Note2:- Class and Instance Attributes both can be changed individually and changing them individually does not affect each other.

# Inheritance(Method Of Creating a new class from existing classes):-

# class Employee: # Base Or Parent Class
 # Code 
# class Programmer(Employee): # Derived Or Child Class
 # Code
# We can use Methods and Attributes Of Employee Class directly in Programmer class and can also overwrite or add new methods and attributes.

# Types Of Inheritance:-
 # Single Inheritance(Derived Class Directly From Base Class):-
  # example is above
 # Multiple Inheritance(Derived Class Inherits From More than one Parent class):-
# class Employee:
#      company = "ITC"
#      name = "Default name"
#      def show(self):
#        print(f"The name of the employee is {self.name} and the company is {self.company}")
# class Coder:
#    language = "Python"
#    def printLanguages(self):
#      print(f"Here is your Language {self.language}")
# class Programmer(Employee,Coder):
#    company = "ITC Infotech"
#    def showLanguages(self):
#      print(f"The name is {self.company} and he is good with {self.language} language")
# a = Employee()
# b = Programmer()
# b.show()
# b.printLanguages()
# b.showLanguages()
 # Multilevel Inheritance(When a child class becomes a parent for another child class):-
#  class Employee:
#          a = 1
# class Programmer(Employee):
#          b = 2
# class Manager(Programmer):
#          c = 3
# o = Employee()
# print(o.a)
# o = Programmer()
# print(o.a,o.b)
# o = Manager()
# print(o.a,o.b,o.c)

# Public, Private and Protected Class:-
# class Parent:
#     def __init__(self):
#         self.public = "Public"
#         self._protected = "Protected"
#         self.__private = "Private"

#     def show(self):
#         print(self.public)
#         print(self._protected)
#         print(self.__private)

# class Child(Parent):
#     def access(self):
#         print(self.public)        # ✅ Accessible
#         print(self._protected)    # ✅ Accessible (By convention)
#         # print(self.__private)   # ❌ AttributeError
#         print(self._Parent__private)  # ✅ Name mangling workaround

# c = Child()
# c.access()
# c.show()

# Super() Method(Used in multilevel and multiple inheritance cases when we want to run constructors of all derived classes inside the child class when we call a parameter inside the child class(By default only the child classes constructor will run not the parent classes which are included)):-
 #  class Employee:
  # def __init__(self):
  #  print("Constructor Of Employee")
  # a = 1
 # class Programmer:
  # def __init__(self):
  #  print("Constructor Of Programmer")
#  b = 2
 # class Manager:
  # def _init_(self):
  #   super().__init__()
  #   print("Constructor Of Manager")
  # c = 3
 # o = Employee()
 # print(o.a)
 # o = Programmer(Employee)
 # print(o.a,o.b)
 # o = Manager(Programmer)
 # print(o.a,o.b,o.c)


# Class Methods(By Default inside the class any function would print the instance attributes because they dominate over class but if we want them to forcibly print class attributes then we use @classmethod Decorator above them and cls instead of self as parameter inside the function()):-
# class Employee:
#   a = 1
#   @classmethod
#   def show(cls):
#     print(f"The class attributes of a is {cls.a}")
# e = Employee()
# e.a = 45
# e.show() # Here if we pass other parameters then also cls.a will print the class parameter only that is a = 1 in this case.

# Property Decorators + Getters + Setters (We use @property, getters,setters to convey the concept of 'Encapsulation' or in other words the process of hiding or packing(into a single unit class) the background logic or implementation or working of the object's components. Another concept called 'Abstraction' also almost conveys the same point of hiding the implementation of the object and exposing only the necessary details to the front-end user):-

# class Employee:
  # a = 1
  # @classmethod
  # def show(cls):
  #   print(f"The class attributes of a is {cls.a}")
  # @property
  # def name(self):
    # return Employee(self.fname, self.lname)
    # or return f"{self.fname} {self.lname}"
#   @name.setter
#   def name(self,value):
#     self.fname = value.split(" ")[0]
#     self.lname = value.split(" ")[1]
# e = Employee()
# e.a = 45
# e.name = "Aarpit Kumar" # Here name is an instance attribute but in the decorators(both property and setter) used here we use declare and use them as functions(methods) not attributes
# print(e.fname,e.lname)
# e.show()

# Types Of Overloading:-
 # Operator(Covered Below)
 # Function(Same Function with different parameters inside)
 # Method(Same Method With Different Parameters inside a Class Generally)
 # Constructor(Same Constructor name generally _init_ used with different parameters inside a class )

# # Operator Overloading in Python:-
# class Number:
#   def __init__(self,n):
#     self.n = n
#   def __add__(self,num): # Magic Or Dunder Method
#     return self.n + num.n
# n = Number(1)
# m = Number(2)
# print(n + m)

# Other Dunder/Magic Methods include:-
 # - use __sub__()
 # * use __mul__()
 # / use __truediv__()(Performs floating point division)
 # // use __floordiv__()(Performs division then rounds it off to the nearest integer i.e performs floor function)
 # __str__() # Used to set what gets displayed upon calling str(obj)
 # __len__() # Used to set what gets displayed upon calling __len__() or len(obj).

# PROJECT 2:- GUESS THE NO.(MAGIC NO.):-

# import random
# n = random.randint(1,100)
# num = -1
# guesses = 1
# while(n!=num):
#     num = int(input("Guess the no."))
#     if(num == n):
#         print("You guessed the no. correctly")
#         print(f"No. Of Guesses are {guesses}")
#         break
#     if(num > n):
#       print("The no. is lower than what you guessed")
#     guesses+=1
#     if(num<n):
#        print("The no. is higher than what you guessed")
#     guesses+=1

### ADVANCED PYTHON I ###:-

# Walrus Operator(Represented By :=):-

# if(n := len([1,2,3,4,5])) > 3:
#   print(f"The List is too long ({n} elements, expected <=3)")

# Type Definitions:-
# from typing import List,Tuple,Union,Dict,Sequence
# n: int = 5
# name: str = "Aarpit"
# def sum(a:int, b:int)- > int:
#   return a+b

# List Of Integers:-
# numbers: List[int] = [1,2,3,4,5]
# print(numbers)
# Tuple Of a String and an Integer:-
# person: Tuple[str,int] = ("Alice",30)
# print(person)
# Tuple Of a String and Multiple Int:-
# person1: Tuple[str,int, ...] = ("Alice",30,40,50,60)
# print(person1)
# Tuple Of Multiple String And Multiple Int(Union Type For Variables That Can Hold Multiple Types):-
# person2: Sequence[Union[str, int]] = ("Alice","Harry","Aarpit", 30, 40, 50)
# print(person2)
# Dictionary with String Keys And Integer Values:-
# scores: Dict[str,int] = {"Alice": 90, "Bob": 85}
# print(scores)

# Dictionary Merge(|) And Update Operators(|=):-
# dict1 = {'a':1,'b':2}
# dict2 = {'c':3,'d':4}
# merged = dict1|dict2
# print(merged)

# Multiple Context Managers:-
# with (open("file1.txt") as f1,open("file2.txt") as f2):
    
# Exception Handling(Prevents Program From Crashing If Any Error is Raised It Provides Viable Error Message Depending Upon The class Defined Like Exception here):-

# try:
#     print(int(input("Enter A No.")))
# except ValueError as v:
#     print(v)
# except Exception as e:
#     print(e)
# except: 
    # All Other Exceptions Are Handled Here

 # Raising An Error:-
# a = int(input("Enter a no."))
# b = int(input("Enter second no."))
# if(b==0):
#  raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
# else:
#  print(f"The Division Of a/b is = {a/b}")

 # Try with Else Clause:-
# try:
#     print(int(input("Enter A No.")))
# except Exception as e:
#     print(e)
# else:
#   print("I am inside else") # Runs Only if try is succesful otherwise goes inside the except Exception block.

 # Try With Finally:-
# def main():
#   try:
#       print(int(input("Enter A No.")))
#       return
#   except Exception as e:
#       print(e)
#       return
#   finally:
#     print("Hey I am inside of finally") # This Block Of Code Works Regardless Of Try Is Sucessful Or It Fails Even If return Is There In Both Try And Except Still Finally Will Run
# main()

# If __name__ == "__main()__":-

# from module import myFunc # For example there is a module named 'module.py' from which we import myFunc function defined inside it into a file named suppose 'main.py'.
# Module.py:-
# def myFunc():
#   print("Hello World")
# if __name__ == "__main__": # Runs only inside 'module.py' not 'main.py'. In Short checks whether code is directly run or imported into some other file.
  # If this code is directly run in the file it is present in
  # print("We are directly running this code")
  # myFunc()
  # print(__name__) # This will print '__main__' always if we run it inside the 'module.py' file and the code stays inside the 'module.py' file and now if we run in 'main.py' file we get output as name of the file from which it has been imported here 'module'.

# Global Keyword:-
# a = 89
# def fun():
    # global a # By Default the local variable a = 3 here will print a as 3 not 89 and the outside print statement will print a as 89. But if we declare the global keyword inside the function then in both print statements we get output as 3
#     a = 3
#     print(a)
# fun()
# print(a)

### ADVANCED PYTHON 2 ###:-

# Format Function(Used before f strings came in python):-
# a = "{} is a good {}".format("Aarpit", "Boy")
# print(a)
# You Can Also Specify The Order Inside The Brackets:-
# a = "{1} is a good {0}".format("Aarpit", "Boy")
# print(a)

# Map, Filter And Reduce:-
 # Map(Runs a Function For all Elements declared inside it):-
# l = [1,2,3,4,5]
# square = lambda x: x*x
# sqlist = map(square, l)
# print(list(sqlist))
 # Filter(Creates A list of items for which the function returns true):-
# def even(n):
#     if(n%2 == 0):
#         return True
#     return False
# onlyEven = filter(even,l)
# print(list(onlyEven))
 # Reduce(Applies a rolling computation to sequential pair of elements):-
# from functools import reduce
# def sum(a,b):
#     return a+b
# print(reduce(sum,l))

# Polymorphism:-
# There are 3 possible ways of polymorphism in python which are:-
# 1.Duck Typing(Dynamic Polymorphism)(Runtime)
# class Cat:
#     def speak(self):
#         print("Meow")

# class Dog:
#     def speak(self):
#         print("Bark")

# def animal_sound(animal): # animal_sound Function does not care if parameter Animal is present or not at all. But if it were a class not a function then we had have to Define Base Class Animal or else we get a namerror.
#     animal.speak()
# 2.Method Overriding(Inheritance-based Polymorphism)(Runtime):-
# class Animal:
#     def speak(self):
#         print("Some sound")

# class Dog(Animal):
#     def speak(self):
#         print("Bark")
# d = Dog()
# d.speak()
# 3.Operator Overloading(Special Method Polymorphism)(Compiletime Like):-
# Already Disscused Above

