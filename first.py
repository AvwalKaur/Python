#To see the list of all keywords
'''
import keyword
#keyword module is used to see all keywords in python
print(keyword.kwlist)
#count all the keywords
print(len(keyword.kwlist))
'''
import keyword

'''value=float(input("Enter the floating point number :"))
print(value)
print(type(value))'''

#by default, input() function will only accept
#string values
# We have to do typecasting using methods such as
#int(), str(), float()


#print() function


# smaplefile is a file object open for writing
# samplefile=open('C:/Users/rajin/Desktop/Python/demo.txt','w')
# Two modes to open file -->
#'r' mode is for reading
#'w' mode is for writing something in file
# during runtime

# print(4,5,6,7,8,sep='%',end='*',file=samplefile)

#instead of printing on screen
# it will print on demo.txt samplefile

# using format() method in output formatting

# print("Hello all {} people in class !".format("beautiful"))
'''str=input("Input your answer :")  #beautiful
print("Hello all {} people in the class".format(str))'''

#variable concatenation
'''str1 = "Hello "
str2 = "Welcome"
str3 = str1 + str2
print(str3)'''
# + operator is an overloaded operator that can combine
# two or more similar type of objects
# i.e it is having differnt definitions in diff scenarios

'''i=10
j=20
print(i+j)'''  # adding numbers
'''str1="Hello"
num=10
print(str1+(str)(10))''' #Type casting

# num=10
# print("The number is : ",num,".The type is : ",type(num))

# num1=10.77
# print("The number is : ",num1,".The type is : ",type(num1))

#complex numbers
# real part --> 10
# imaginary part --> 5 j(iota is replaced by j)
# num2=10+5j
# print("The number is : ",num2,".The type is : ",type(num2))


#Number system
#Integer base 10
# Binary number system --> base2 --> Prefix 0b or 0B
#Declaring binary numbers

# print(0b101)
# print(0B1011)

#Octal numbers --> base8 --> Prefix 0o or 0O
# octal --> decimal --> binary
# print(0o156)

#Hexadecimal 16 --> prefix 0x or 0X
# print(0x1FB)
#0 -9 , 10-A, 11-B, 15-

#Typecasting in numbers is automatically or implicit
#Explicit typecasting is forced one

#Implicit --> smaller datatype to big datatype

# print(100+15.67)  #Integer+floating numbers
                  #small datatype + bigger datatype
#implicitly integer is converted to floating number
# 100.00+15.67

# explicit typecasting
#forcing large datatype to fit in the size of small datatype
# fitting float in int datatype
# no round off take place
'''print(int(15.789))
print(int(-15.425875))

val="10+3j"
print(type(val))
comp=complex(val)
print(type(comp))'''



#Number based modules -->2
# random and math modules


#Random module
#To generate values randomly on the fly
'''
import random

print(random.randrange(20,50))
# to print any random number
print(random.random())
# Use random to pick a value randomly from any sequence

list1=["hello","bye","hey",'a','c',3,5,6,67]
print(random.choice(list1))
# to shuffle the sequence of a list or any collection
print(random.shuffle(list1))
print((list1))
'''
#Aliases means nickname
# like giving nickname to any module
# for example
# import module_name as nickname
#import random as rn


# Math module
# for mathematical calculations
'''
import math as mt
print(mt.factorial(4))
print(mt.pow(4,2))
print(mt.pi)
print(mt.log10(1000))
print(mt.remainder(42,10))
'''


#Sequence data
# 3 types --> list, string, tuples

#List --> very flexible sequence of data as it allows
#all sorts of modification
# data in list can be of different datatypes
# not possible in arrays and arraylists in Java
# starts with index 0 --> ordered by position
# mutable --> can be modified easily
# repeated or duplicate values are allowed

'''list=["apple","mango",'a','b',1,3,9,14.56,13.24,True,False]
print(list[0])  # first element
print(list[1])  # second element
print(list[-1]) # last element
print(list[-2])''' # second last element
#if we access list from left to right, index starts from 0
# if we access list from right to left, index starts from -1
#0 1 2 3 4 ----->
#-1,-2,-3,-4 <-----


#Tuples
# () --> parenthesis are used to denote tuples
# index starts from 0 from left to right
# and it starts from -1 from right to left
# it may contain any type of data

'''tup1=(1,2,"Hello","Bye",True,12.556)
print(tup1[0]) #First element
print(tup1[-1])''' #last element

#Difference
'''list=[1,2,3,"Hello","Bye",14.355,True]
tup=(4,5,6,"New","Old",67.89,False)

#Lists
print(list)
list[-1]="Go"
print(list)
#Python lists are mutable
print(tup)
tup[-1]="GoNow"
print(tup)'''
#error
#does not support item assignment
# Python tuples are immutable

# Collections type data --> with no index or position
# Dictionary & Sets

#Dictionary
# values are in form of key:value pairs
# each value is recognised by key
# values can be repeated
# dictionaries are mutable

'''dict={'name':"avwal",'age':19,'house number':20}
print(dict)
print(dict['house number'])
print(dict.keys())     # only keys
print(dict.values())   # only values
print(dict.items())    # only items
dict['name']="Avwal"
print(dict)'''


#Sets
# no duplicate elements are allowed
'''# can give output as unordered elements
set={1,2,5,3,6,6,2,"Hello",85,100}
print(set)
'''

