#String literals
#single line strings
"""str="Hello I am Avwal"
print(str)"""

#multi line strings
# \ is auto generated connector
"""str1=("hello"
      "how are you"
      "I am fine")
print(str1)

#formatting multi line strings

str2='''Hello
all
Welcome
to my lecture in
session2'''
print(str2)"""


#String indexing
'''str="Hello"
print(str[0])
print(str[1])'''


'''str="Hello"
print("First character is",str[0])
print("Last character is",str[-1])

# Strings are immutable in python
# No modification is allowed in string characters

# Slicing
print(str[1:5])
#Slicing syntax
# str [start_index : end_index : number_of_jumps]
str1="hello all"
print(str1[1:7:2])
print(str1[0::2])

# Negative Slicing
# Indexing should be always oriented from left to right
print(str1[-5:-1])
print(str1[-1:-5])
# no syntax mistake
#logically incorrect
# therfore its not giving any error
#it is just not giving any answer
print(str1[-7::2])
# reverse a string without using any method
print(str1[: : -1])

print(str1[ : : -2])
# reverse by two jumps
#hello all  --> laolh
#starting from -1 index i.e. from the lat character

#String comparisions
# > < ==
# == --> checks for equality
# = --> assignment operator

s1="Hello"
s2="hello"
print(s1 == s2) #python is case sensitive
print(s1 > s2)
print(s1 < s2)  #72<104  --> True

#Ascii values
# A-Z = 65 to 90
# a-z = 97 to 122
# ord() method gives ascii codes for characters
# chr() method gives corresponding characters for a given ascii values

print(ord('H'))  #72
print(ord('h'))  #104
print(chr(65))
print(chr(97))

# String repitition
# using * operator, we can repeat string multiple times
str2="Hello "
print(str2 * 2)  #print str2 2 times
print(str2 * 5)  #prints str2 5 times

# Concatenation operator(+)
# + is an overloaded operator
str3="Hello"
str4=" "
str5="Bye"
print(str3+str4+str5)

# Find the number of characters in a string
print("The number of characters in 'Hello' are",len(str3))

# Test if a particular character of sub string is present in a string or not
# Membership Test is done by 'in' and 'not in' operator
# check if string 'friend' is present or not
str6="Hello dear friends, Welcome to class!"
print('welcome' in str6)  #check if present
print('!!' not in str6)   #check if not present
'''


# String Methods
str="Hello all"

# To convert to uppercase or lowercase
print(str.upper()) #another string with all uppercase letters will be formed in differnet memory location in RAM
#Strings are immutable
#original string is not changed
print(str)
print(str.lower())
print(str)

#Replace a particular substring to create a new string
str1="Hello all students"
new_str1=str1.replace('Hello','Good Morning')
print("Original String :",str1)
print("New String :",new_str1)


# How to find if a particular sub string is present or not
#find() --> returns the starting index of sub string if present else if the substring is not present then return -1

print(str1.find('people'))    #-1
print(str1.find('students'))  #starting index : 10
print(str1.find('students in class'))
#returns -1 as it will check the entire string

#index() --> finds the index of a substring.
# If substring is absent, then it will raise an error
# print(str1.index('people'))  #throws an error
print(str1.index('students'))  #starting index : 10

# To slice or split or cut the string
# Using split() method
# when the method finds the separaotor, it splits the string there
# default separator is space
str2="Hi, I am, learning Python"
print(str2.split())
print(str2.split(','))
print(str2.split(',',1)) #restricts splitting to 1 time
# Syntax : split(separator '',max number of splits)

# strip() method
# helps to remove spaces from text string (only leading or trailing)

str3="     Hello    I am      Avwal    "
print(str3.strip())
print(str3.lstrip())  #only from left
print(str3.rstrip())  #only form right
