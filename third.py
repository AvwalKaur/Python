'''
# Lists
list1=[1,2,3,"abc","hello",True,False,11.89,4+5j]
print("The list is",list1)

# Creating a blank list
list2=[]
print(list2)
# list is created in memory but it is empty

# List in python is also a class.
# A list object can be also instantiated by list class
# constructor by invoking list()

str1="Hello all !"
# Create a list of all the characters
# To convert this string directly to list, we can invoke list constructor

New_list = list(str1)
print("The newly formed list is: ",New_list)
'''


# Properties of lists
# 1. Ordered --> Each element of list has an index position attached to it
# 2. Mutable
# 3. Allows repeated values i.e. duplicates

'''
# Ordered-------------
list1=[1,2,3,"Hello","Bye",3+7j,11.4]
#Start accessing from left to right
print("First element: ",list1[0])
print("Last element: ",list1[-1])
print("Second Last element: ",list1[-2])

# Slicing a list
list1=[1,2,3,"Hello","Bye",3+7j,11.4]
#      0 1 2  3        4    5    6
#     -7 -6 -5 -4      -3   -2   -1
# Slice list from index 1 to 6
# prints from index 1 to 5
print(list1[1:6:2])
print("Negative Slicing from second last position to second element: ",list1[1:-1])
print("Negative Slicing from second last position to second element: ",list1[-6:-1])
print(list1[-6:-1:-1])  # empty list

#Reverse a list
print("Reverse list: ",list1[::-1])
print(len(list1))


# 2. Mutable --->
# You can modify elements, add and remove elements from list
list1=[1,2,3,"Hello","Bye",3+7j,11.4]

# append() method
# To add a new element at the end of the list
print(list1)
list1.append("Bonjour")
print(list1)


# insert() method
# To add new element at a specific position in the list
print(list1.insert(3,"Bienvenue"))
print(list1)

# extend() method
# One can add new values from another list into original list
list1=[1,2,3,"Hello","Bye",3+7j,11.4]
list2=[7,8,9,"Go"]
list1.extend(list2)
print("List 2 will be extended in list 1: ",list1)

# List Concatenation
# elements are added in original order
print("List Concatenation :",list1 + list2)

# Operators common for sequences : + * [:]
# List Repeatition
print("List repeat: ",list1*3)

# Make modifications in a list
# We can change a particular list element
list1=[1,2,3,"Hello","Bye",3+7j,11.4]
print("Original list: ",list1)
# update the third element from 3 to 30
list1[2]=30
print("Updated list: ",list1)
# To change all elements in a range
list1[2:5]=[50,"Hello all","Bye all"]
print("Updated list: ",list1)
# If we add additional values, they simply get added
# No exception is thrown
list1[1:3]=[45,56,98]
print("Updated list: ",list1)


# Remove elements from list
list1=[1,2,3,"Hello","Bye",3+7j,11.4,"Hello"]
print("Original list",list1)
# Remove a particular element of value "Hello"
list1.remove("Hello")
print(list1)

list1.remove("Hello")
print(list1)

# If we try to remove a value that is not present
# error is thrown
# list1.remove("Hello")
# print(list1)

# Count occurence of elements
# using count() method
list1=[1,2,3,"Hello","Bye",3+7j,11.4,"Hello"]
print("Original list: ",list1)
print("Count of 'Hello' : ",list1.count("Hello"))

# Sort a list
# sorting works when we have elements of smae type
list3=[4,50,81,2,69,11]
# sorting in ascending order (by default)
list3.sort()
print("Sorted list: ",list3)

# sorting in descending order
list3.sort(reverse = True)
print("Reverse sorted list: ",list3)

# 3. Create duplicates or copy of list
# using copy() method
list3=[4,50,81,2,69,11]
print("Original list: ",list3)
New_list=list3.copy()
print("Copy of list3: ",New_list)

# Check if both lists are same
print(list3 == New_list)

# Tuples
# Tuple is a sequence similar to list but with some differnces
# 1. List is mutable but tuple is immutable
# 2. List starts with [] while tuple starts with ()
# 3. There is a fairly good number of methods in list while
#    there are only two methods for tuples


# Creating  a tuple
tup1=(1,2,3,"Hello","Bye",11.23,True, False,5+2j)
print(tup1)

# We have a tuple constructor tuple()
new_tuple=tuple(('Hello',1,2,3,"Go",22.5))
print(new_tuple)

# Creating a tuple from list elements
list4=['Hello',1,2,3,"Go",22.5]
new_tuple=tuple(list4)
print(new_tuple)
# Creating a tuple from list
# using list() constructor
tup1=(1,2,3,"Hello","Bye",11.23,True, False,5+2j)
list6=list(tup1)
print(list6)

# Creating tuple from string
# For collection  of values,
# Tuples is the default python data structure
str1="Hello all"
new_tuple=tuple(str1)
print("Tuple from list: ",new_tuple)

# Creating an empty tuple
tup1=()
print("The tup1 is :",tup1,"Type of tup1 :",type(tup1))

# Creating a tuple with a single element
# Singleton tuples
tup1=("Hello",)
# Python interpreter considers it as a normal string
# and does not print the ()
# because without , (comma), it does not consider it as a sequence
print("The tup1 is :",tup1,"Type of tup1 :",type(tup1))

tup2=(25,)
print("The tup2 is :",tup2,"Type of tup2 :",type(tup2))


# Default Data Structure
values=1,2,3,"Go"
print(values,"Type of values : ",type(values))
# Values are printed in tuples
'''

# Properties for tuples
# 1. Ordered
# 2. Immutable
# 3. Allows duplicate values

'''
# Ordered
tup1=(1,2,3,"Hello","Bye",11.23,True, False,5+2j)
print("Original tuple",tup1)
print(tup1[0])
print(tup1[-1])
print(tup1[-2])

# Slicing
print(tup1[0:6])
print(tup1[-6:-1])
# with 2 jumps
print(tup1[0:6:2])
# Reverse
print(tup1[::-1])
# Negative jumps are not allowed
print(tup1[1:7:-1])
'''

'''
# Tuple are immutable
# Real time application
# Storing the salaries of employess
# i.e. no modification needs to be made and store some security sensitive data
list1=[1,2,3,"Hello","Go",11.55]
tup1=(1,2,3,"Hello","Go",11.55)

# Try to modify 3 to 30 in both list1 and tup1
list1[2]=30
print(list1)
# tup1[2]=30 --> gives an error
# assignment of values cant be done in tuple
print(tup1)


# To find the number or count of elements in tuple
# using len() method
tup1=(1,2,3,"Hello","Go",11.55)
print(len(tup1))

# Check for membership in tuple (in and not in)
# Check if "Hello" exists in tuple
print("Hello" in tup1)
print("hello" in tup1)
print("Hello" not in tup1)

# To remove elements, we cant directly remove them
# But you can remove entire tuple in one go
# using del property
# del tup1
# print(tup1)

# Two methods in tuple
# 1. count(): count the number of times or frequency of elements
# 2. index(): Search and find index of an element otherwise throws an exception

tup2=(1,2,3,4,1,1,"Hello",4,"Hello")
print(tup2.count("Hello"))
print(tup2.count(1))
print(tup2.index(1))  # searches for first occurence of the element
print(tup2.index("Hello"))
'''

'''
# Set
# 1. Sets begin with {} braces
# 2. Sets don't allow duplicates i.e. no repeatition
# 3. Constructor call is set()
# 4. It is unordered
# 5. There is no slicing or indexing in a set

# Creating a set

set1={1,2,2,3,4,3,"Hello",11.58,"Bye",11.58,True, False,4+5j}
print(set1)
# If True and False are added in the set, it does not consider printing True value
# It considers only False values

# Empty set using set() method
set2=set()
print("Empty set is: ",set2,"Type of set2: ",type(set2))
list1=[]
print("Empty list is: ",list1,"Type of list1: ",type(list1))
tup1=()
print("Empty tuple is: ",tup1,"Type of tup1: ",type(tup1))
# If we use {} braces to create a set
# It creates a dictionary
# as dictionary is also a collection type
# {} by default are for dctionary
set3={}
print("Empty set is: ",set3,"Type of set3: ",type(set3))
'''

# Set is mutable
# add() update() remove() discard()
# For performing mathematical operations
# To add new elements in set, we use add()
set1={1,2,3,4,5,6,7,8,9,10}
print("Original set :",set1)
set1.add(99)
print("Updated set :",set1)
set1.add(100)
print("Updated set :",set1)
# Values can be added to any index in the set

# update() --> to add elements from another list of tuple in set
set1={1,2,3,4,5,6,7,8,9,10}
list1=[11,22,33,44,55]
set1.update(list1)
print(set1)

tup1=(999,888,666,111)
set1.update(tup1)
print(set1)

set2={454,875,965,125,324}
set1.update(set2)
print(set1)

# To remove values from set
set1={1,2,3,4,5,6,7,8,9,10,5}
print(set1)
# using discard() and remove() method
# remove() method removes a particular value of the set and throws error if value is not found
# set2=set1.remove(5)
# print(set1)
# since set does not consider duplicate values, it won't count second occurence of 5
# So remove() method throws a 'key error' exception if the value for deletion is not found
# set2=set1.remove(5) --> throws an error
# print(set1)
# set1.remove(11) --> throws an error
# print(set1)
set1={1,2,3,4,5,6,7,8,9,10,5}
set1.discard(5)
print(set1)
set1.discard(5)
print(set1)
# discard method does not throw an error even if we remove something which is not present in set

