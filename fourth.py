# Built-in methods of set()
# all() any() len() max() min() sum()--> generic methods
# i.e. used without dot operator

# all() --> checks for the True set of boolean values
# 0 --> False, 1 or any integer --> positively True value
# similar to AND operator
# If any iterable(list, set, tuples) is False or 0, then the answer comes out to be False
'''
set1={True, True, True, True}
res=all(set1)
print(res)

set2={True, False, True, True,1,1,0,0}
print(all(set2))

list1=[1,1,1,1]
print(all(list1))

list2=[0,0,0]
print(all(list2))

list3=[True, True, 1,2,4,8, 9+8j]
print(all(list3))

# any() --> it returns True if atleast one value in an iterable to be True
# similar to OR operator
set2={True, False, True, True,1,1,0,0}
print(any(set2))
# if all are False, then ans is False
list2=[0,0,0,False]
print(any(list2))

# len() --> checks for length of set
set2={True, False, True, True,1,1,0,0,False}
print(len(set2))
# all True values(True,1) are considered once and all false values(False,0) are considered once


# max() and min()
set1={1,3,77,4,49,55,-11,100}
print(max(set1))
print(min(set1))

# sum() method
set1={1,2,3,4,5}
print(sum(set1))

# Mathematical Set Operations
# Union, Intersection, Symmetric Difference, Subtraction
#(out of place operations)
# Union --> Combines unique elements from set A and set B
# union() and |(pipe operator)

set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}
print("Using union()", set1.union(set2))
print("using | operator", set1 | set2)

# takes 4 and 5 just once

# Intersection --> takes only the common elements present in both sets
# intersection() and &(ampersand) operator
set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}
print("Using intersection()", set1.intersection(set2))
print("using & operator", set1 & set2)

# Symmetric Difference
# difference() A-B : Result must contain the values of A which are not present in set B
# i.e. unique elements of set1
# creates difference in new set
# difference() method and -(minus) operator
set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}
print(set1.difference(set2))
print(set1 - set2)
print(set2.difference(set1))
print(set2 - set1)

# In-place update set operations --> if the original set is updated
# Out-of-place set operations
# a separate memory is allocated for output storage
# intersection_update(), update(), difference_update()

set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}
# set1.intersection_update(set2)
# print(set1)  # contains the intersection update
# # i.e. the intersection values are copied and kept in place of original set1
# print(set2)  # intact

# set2.intersection_update(set1)
# print(set1)
# print(set2)

# difference_update()..........
set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}
set2.difference_update(set1)
print(set1)
print(set2)

# update()...............
set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}
set2.update(set1)
print(set1)
print(set2)

# symmetric_difference()..............
# returns all the values present in given set data structures except the common values between them
set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}
print(set1.symmetric_difference(set2))
print(set1)
print(set2)

# symmetric_difference_update()......
# in place operations
# changes the set1 directly
set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}
print(set1.symmetric_difference_update(set2))
print(set1)
print(set2)
'''


# issuperset(), issubset(), isdisjoint()
# if there are no common values in two sets, it is a disjoint set
'''
set1={1,2,3,5,4}
set2={1,2,3,4,5,6,7,8,9,10}
set3={11,22,33,44,55}
# check for subset and superset
print("if set1 is a subset of set2: ",set1.issubset(set2))
print("if set1 is a superset of set2: ",set1.issuperset(set2))
print("if set2 is a subset of set1: ",set2.issubset(set1))
print("if set2 is a superset of set1: ",set2.issuperset(set1))
# check for disjoint sets
print("if set1 and set3 are disjoint: ",set1.isdisjoint(set3))
print("if set2 and set3 are disjoint: ",set2.isdisjoint(set3))

# pop() method: It randomly deletes a value from set
set1={78,2,'abc','vfg',11.58,5,4}
print(set1)
print(set1.pop())
# changes the original set --> in place operations
print(set1)
'''


# Dictionary
# contains key:value pairs
# {} braces are the brackets for dictionary
# both set and dictionary values are stored at any memory location, not stored at contiguous memory location
# both set and dictionary are collection types, so they have unordered values
# empty dictionary specified by {} and empty set denoted by set()

dict1={}
print("The dict1 values:",dict1, "Type is: ",type(dict1))
dict1={"name":"Ajay", "age":20, "Salary":10000, "House no":"CD 42E"}
print(dict1)

# How to access elements in dictionary
# with the help of keys
dict1={"name":"Ajay", "age":20, "Salary":10000, "House no":"CD 42E"}
print("Employee name:",dict1["name"])
print("Age is:",dict1["age"])

# Dictionary is mutable similar to lists and sets
# add new values to dictionary
dict1={"name":"Ajay", "age":20, "Salary":10000, "House no":"CD 42E"}
dict1["Degree"]=["BCA","MCA","Mtech"]
print(dict1)
print(dict1["Degree"])

# to update the existing value
# change the age from 20 to 22
dict1["age"]=22
print(dict1)

dict1={"name":"Ajay", "age":20, "Salary":10000, "House no":"CD 42E"}
# length of dictionary
print(len(dict1))
# Remove salary
# using del property
print(dict1)
del dict1["Salary"]
print(dict1)

# pop() method
res=dict1.pop("age")
print(dict1)
print("The popped value is:",res)
print("The keys are:",dict1.keys())  # stored in list
print("The values are:",dict1.values())  # stored in list
print("The items are:",dict1.items()) # stored as list of tuples


# get() --> to get a value corresponding to a key
print(dict1.get("House no"))