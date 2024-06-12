# decision-making conditional statements
# if-elif-else block
# Check if a number is positive, negative or zero

# number=int(input("Enter the number: "))
# if number>0 :
#     print("number",number, "is positive")
# elif number<0 :
#     print("number", number, "is negative")
# else :
#     print("number is zero")


# Nested if
# num=int(input("Enter the number"))
# if num>=0 :
#     if num==0 :
#         print("Number is zero")
#     else :
#         print("Number is positive")
# elif num<0 :
#     print("Number is negative")
# else :
#     print("Not the desired output")

# a = 10
# b = 150
# c = 2
# maximum of three numbers
# if a>b and a>c :
#     print("a is largest")
# else :
#     if b>c :
#         print("b is largest")
#     else :
#         print("c is largest")

# minimum of three numbers
# if a<b and a<c :
#     print("a is smallest")
# else :
#     if(b<c) :
#         print("b is smallest")
#     else :
#         print("c is smallest")

# count net payable amount
# amount=int(input("Enter the amount:"))
# if amount<1000:
#     discount=amount*0.05
# elif amount<5000:
#     discount=amount*0.10
# else :
#     discount=amount*0.15
# print("Net payable amount: ",amount-discount)


# For loop
# list=[1,2,3,"Hello", True,False,3+5j]
# for i in list:
#     print(i)

# range() --> generates numbers in a given range
# syntax: range(start. stop, steps)

#use for loop to print a range of numbers
'''
values=range(10)
# values will have numbers from 0 to 9
for i in values:
    print(i)
'''

'''
values=range(5,-5,-2)
# a range from 5 to -5 with back jumps or skips of 2
list1=list(values)
for i in list1 :
    print(i)
print("The list is:",list1)
'''

'''values=range(0,9,2)
list=list(values)
for i in list:
    print(i)
print(list)'''

# In python, we can accompany for loop with else
'''
for iter in seq:
    # statements
else:
    # message or computation
'''
# else block works when the for loop ends
'''
list=["Ajay","Vijay","Sanjay","Uday"]
count=0
for i in list:
    print("The name of employee is:",i)
    count=count+1
else:
    print("Total number of employees in company:",count)
    print("No more employees to display!")
'''
'''
list=[1,2,3,4]
for _ in list:
    print("Loop working test success")
# _(underscore) just indicates that loop is running correct no of times without actually accessing the values
'''
'''
# Nested for loop
for i in range(5):
    for j in range(5):
        print("The value of i:",i, "Value of j is:",j)

'''

# while-loop
# it checks if the user has entered the correct password for login
# else the user is asked to retry again.
# user can try infinite times
'''while True:
    userName=input("Enter your username:")
    passwordInput=input("Enter your password:")
    # using decision statements
    if passwordInput=="Password":
        print(userName,"You are welcome !")
        break  # exits or breaks the loop without continuing further
    elif passwordInput=="Quit":
        print("You are exiting the system")
        break
    else:
        print("You have entered wrong input")   # nothing happens, loop continues to run
'''

# Calculate sum of numbers till user enters 'Quit'
'''first_number=int(input("Enter a number..."))
sum=first_number
choice=input("You want to Yes or Quit ?....")
while True:
    if choice=='Quit' or choice =='quit':
        break
    elif choice.upper()=="YES":
        sec_number=int(input("Enter other number to add"))
        sum=sum+sec_number
        print("The sum is:",sum)
        choice = input("You want to continue or quit ?....")
    else :
        print("Enter a relevant choice :)")
        choice = input("You want to continue or quit ?....")'''

# Flow Control Statements
# break, continue, pass
'''for i in range(10):
    if i == 7:
        print("Limit to 7 reached")
        break
    elif i==5:
        print("Limit to 5 reached! Warning!")
        pass
    else:
        print("The value is:", i)
# out of loop
else:
    print("Loop ended at 7")
print("Out of for and else loop")'''

'''
list=["Ajay","Raman","Mona","Priya"]
salary=1000
for i in list:
    if i=="Priya":
        continue
    elif i=="Ajay" or i=="Mona":
        print("New User !",i)
    else:
        pass'''
