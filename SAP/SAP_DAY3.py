#!/usr/bin/env python
# coding: utf-8

# A quick recap of DAY2 discussions:
# - Control statements
#      - If... elif... else:<br>
#       If (condition is met):<br>
#         (perform operation)<br>
#      elif (another condition is met):<br>
#          (perform another operation)<br>
#              ...
#      else:              # that is, if none of the conditions stated above was met<br>
#          (perform this final operation)<br>
# 
#      - For...<br>
#      for (range of values or valid conditions):<br>
#          (perform operation)<br>
# 
#      - While...<br>
#      While (condition remains valid):<br>
#      (perform operation)
#  
# - Python List, Dictionaries and Sets

# # ..................................................................................
# ### Monday, 13th April, 2020
# # ..................................................................................
# 

# ####  Functions, Lambda Expressions, Time and DateTime in Python
# - Functions in Python 
#     - Defining a function 
#     - Passing Arguments
#     - Return values
#     - Passing a list
#     - Passing an arbitrary number of arguments 
#     - Storing your functions in Modules, styling functions.
# - Lambda Expressions
# - Time and DateTime in Python 
# 

# ### Functions

# #### Defining a Function: Syntax
# def <function_name>(optional paramenters/input(s)):
#     
#     statement1
#     statement2
#         :
#         :
#     statementn

# In[1]:


def func1():
    print('This is a python function')
    
#Optional input
def greet():
    print('Hello Stranger')

#Function call
greet()
func1()


# #### Passing Parameters / Arguments
# Data / Information can be passed as parameters into a function.
# 
# Parameters are specified inside the parentheses after the function name. Multiple parameters are separated with comma.
# 
# Arguments: are specified inside the parenthesis whenever a function is called
# 

# In[2]:


#One parameter
def greet1(name):
    print('Hello ', name)
    

#Function call with an argument
greet1('Jane')
greet1('Alex')


# In[3]:


#Multiple Parameters

#Function to greet a person with an identified gender
def greet2(name, gender):
    if gender in ['Male', 'M', 'm', 'male', 'MALE']:
        print("What's up bro? Good to see you, ", name)
    else:
        print('Hello lady, how are you doing %s?' %name)
        
greet2('Adedeji', 'm')
greet2('Victoria', 'f')


# In[4]:


def area_circle(radius):
    '''
    This function calculates the area of a circle given its radius
    input: Radius of the circle
    Output: Area of the circle
    '''
    import math
    area = math.pi * radius**2
    print('The area of a circle with radius %fcm is %fcm2' %(radius, area))

#function call
area_circle(23)


# In[5]:


def add(a, b):
    '''
    This function adds two given numbers
    inputs: number1, number2
    output: A print statement of the addition of the inputs
    '''
    return (a+b)


# In[6]:


#function call
add(4, 6)


# ### Parsing a list, Dictionary, tuple, set and other data structure
# The value of a parameter can as well be specified in the function definition. However, the value can be subjected to change in the function call

# In[7]:


#Passing a python function that print out all cars in list of cars 
def my_function(carlist):
    for car in carlist:
        print(car)

List_of_cars = ["Toyota", "Ford", "Honda"]

my_function(List_of_cars)


# In[8]:


#Passing a dictionary as a parameter

def Book_Stock_func(Books):
    for book, Quantity in Books.items():
    
        print("The Qty of {0} is {1}".format(book, Quantity))


    
Dict_of_books = {"Math": 4, "English": 5 , "Pysics": 8} #creating dictionar 

Book_Stock_func(Dict_of_books)


# ### Parsing a value
# The value of a parameter can as well be specified in the function definition. However, the value can be subjected to change in the function call

# In[9]:


# Python functions can also have default arguments which can be changed if the user inputs another, or retained if not

def greet(name, msg = 'Good morning!'):
    '''
    This function greets a person with the user's greeting
    If a greeting is not provided, it reverts to greeting
    the person with the default message, Good morning
    Inputs: name, mmessage (optional)
    output: Print statement greeting user
    '''
    print('Hello %s, %s' %(name, msg))
    
greet('Adeleye', 'How are you?')
greet('Adeleye')


# In[10]:


def greet(name = '', msg = 'Good morning!'):
    '''
    This is an extention of the greet function from above,
    to permit the user call the function without any input
    Inputs: name(optional), mmessage (optional)
    output: Print statement greeting user
    '''
    print('Hello %s, %s' %(name, msg))
greet()


# #### Passing an arbitrary number of arguments 

# In[11]:


# Python functions also allow arbitrary arguments, where the function allows the user input more input but of the same type
def greet(*names):
    '''
   This function greets all
   the person in the names tuple
   input: name(s)
   output: Greeting to the respective name(s)
   '''
   # names is a tuple with arguments
    for name in names:
        print("Hello",name)

greet('John')


# In[12]:


print('Wait to see what it prints when given more names...')

greet("Monica","Luke","Steve","John")


# In[13]:


# Adding one minute interval between greetings using time module
import time

def greet(*names):
    '''
   This function greets all
   the person in the names tuple
   input: name(s)
   output: Greeting to the respective name(s)
   '''
   # names is a tuple with arguments
    for name in names:
        print("Hello",name)
        time.sleep(3)


print('Wait to see what it prints when given more names...')

greet("Monica","Luke","Steve","John")


# ### Assignment 1
# Create a function that accepts your Surname and other names and output your full name

# ### Assignment 2
# Create a function named Family and pass the dictionary below:
# 
# - Family_Age = {"Father":, 50, "Mother": 45, "Daughter": 25, "Son":20}

# #### Function variables
# - Global variables
# - Local variables <br>
# Before we go too deep into functions, it is important to note that variables used in functions STAY in the function unless they are declared as global variables in the function. This is because they are local to the function; hence, called local variables.
# However, variables used outside a function, can be used in a function within the same script because they are seen as global variables

# In[14]:


# Variables declared outside the function
a = 8
b = 12

def association():
    c = 5
    print((a + b)*c)
    
association()

# c is declared in the function, but not returned, so it will not be seen outside the function
print(c)


# #### Making Local Variables Reusable Outside the Function

# In[15]:


def mul(a):
    '''
    This function gives the multiples of a number 
    Input: Number
    Output: Number^2, Number^3
    '''
    global a_square
    global a_cube
    a_square = a**2
    a_cube = a**3
    print('The square of %d is %d, and the cube of %d is %d' %(a, a_square, a, a_cube))
    #return a_square

mul(2)

print('Using local variables outside the function.......\n ', a_square , '+', + a_cube, 'is', a_square + a_cube)


# In[17]:


def mult(a, a_range):
    '''
    This function gives the multiples of a number between a particular range
    Input: Number
    Output: Number^0, Number^1, Number^2, Number^a_range
    '''
    global a_mult
    a_mult = [] #A list container to store the multiples  
    for i in range(a_range):
        a_mult.append(a**i)
    print('The multiples of {} between 0 and {} is'.format(num, num_range), a_mult)


#Main Program        
num = int(input('What number are you interested in? ')) #The number whose multiples will be generated
num_range = int(input('what range are you interested in? ')) #The range within which the number should be generated eg between 0-20

mult(num, num_range) #Function call

print('Using local variables outside the function.......\n multiples of {} between 0 and {} is'.format(num, num_range), a_mult)


# ### Lambda functions
# Python also allows the creation of anonymous functions<br>
# Lambda functions can have any number of arguments, but only one expression.
# This function is used when we need a nameless function for a short period of time.

# In[18]:


# An anonymous function to double the given number
double = lambda x: x * 2
print('x^2 = ', double(5))

'''The lambda function can be used with an in-built python function called filter
The filter function takes in a function and a list as arguments,
and returns a new list which contains items (from the first list) for which the function conditions are True
'''

print('...................................Now to the combination of filter and lambda....................................')
time.sleep(4)
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# Output: [4, 6, 8, 12]
print(new_list)


# ### Time and Date in Python
# Date, time and datetime classes provides a number of function to deal with dates, times and time intervals

# In[19]:


#Importing time library
import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)


# In[20]:


#To import a calender
import calendar

cal = calendar.month(2019, 7)
print ("Here is the calendar for the specified month in the year 2019:")
print(cal)


# In[21]:


from datetime import datetime, date

# Getting the current time and date
time_now = datetime.now() 
print('The current time and date is ', time_now)

#Suppose we want to print just the current time without the date            
t = datetime.time(datetime.now())
print('The current time without the date is ', t)


# Getting the current date without time
todays_date = date.today()
print ('the current date without time is ', todays_date)


# ### Modules and Import
# Modules in python is a file that contain numerous codes, functions, variables, classes etc for specific functionalities. A module is a compilation of (often similar) functions under a general name. 
# 
# ### Python built-in Modules

# In[22]:


#importing a built-in module
import math 
print(math.pi)


# In[23]:


import datetime # This is a module used for date and time with some of its methods listed below
x = datetime.datetime(2020, 5, 4)
print('Conversion of "2020, 5, 4" to date format ', x)
time.sleep(5)

x = datetime.datetime.now()
print('The date and time at the meoment is ', x)

time.sleep(3)
print('The day of the week is ', x.strftime('%A'))


'''
%a... weekday in short form
%A... weekday in full
%w... weekday as a number
%d... Day of the month
%b... Month name in short
%B... Month in full
%m... Month as a number
%y... Year in short
%Y... Year in full
%H... Hour in 24-hr format
%I... Hour in 12-hr format
%p... am or pm
%M... Minute
%S... Second
%f... Microsecond
%Z... timezone
%j... day number of year
%U... week number of year with Sunday as first day of the week
%W... week number of year with Monday as first day of the week
%c... Local version of date and time
%x... Local version of date
%X... Local version of time
'''


# In[24]:


import time
import calendar
ticks = time.time()

#All these examples has been done under Python date and time module
from time import localtime
todaytime = localtime(time.time())

more_readable_time = time.asctime(time.localtime(time.time()))
time.sleep(3)

cal = calendar.month(1900, 2)
print(cal)

print('Number of ticks since 1970: ', ticks)
print('The time is: ', todaytime)
print('A better version of the time is: ', more_readable_time)


# #### Creating a user defined module
# Follow these steps to create a new Module on your local machine:
# 
# - Create a new python file
# - Copy this code cell into a new the file
# - Save the notebook with myMod and download as myMod.py
# 
# Once the download completes, move the **myMod.py** into the same directory/folder with your active notebook
# - Run the next cell

# In[25]:


"""Module docstrings.

This module demonstrates how to create a python module that can be imported into python code for reusability

Available Functions: This module harbours 5 functions which are:

func1() :It takes one no parameter but 'Hello Stranger'
greet(name) :It takes one parameter which is name and return 'Hello + name_specified
greet2(name, gender): takes 2 parameter ie. name and gender of users
greet3(*names): Accepts arbitrary umber of parameters
calc(num): Returns the square of a number
student_age(dictionary): Accepts dictionary to return the age of students in the dictionary

Impoting the module:
        1. Make sure this module is saved in the same directory / folder with your currently running program
        2. type import myMod
"""

# A function without parameters/variable/arguments
def func1():
    print('Hello Stranger')
    
    
# A function with parameters/variable/arguments

#Function to greet someone whose name will be specified
def greet(name):
    print('Hello, ', name)
    
    
#Function to greet someone whose based on his or her gender   
def greet2(name, gender):
    if gender in ['Male', 'MALE', 'M', 'm', 'male']:
        print('Hi', name, 'we welcome you brother')
    else:
        print('Hi', name, 'we welcome you Sister')


# A function with arbitrary number of parameters with *
def greet3(*names):
    for name in names:
        print('Hello', name, 'Welcome to Python Class')
        import time
        time.sleep(1)
        

def calc(num):
    global square
    square = num**2
    print('the square of {} is {}'.format(num, square))


def student_age(dictionary):
    for student, age in dictionary.items():
        print('The Age of', student, 'is', age)


# ### Importing a user created module
# This could be done exactly as in-built modules will be imported. The syntax is 
#                     
#                     import module_name
#                     
# For instance; 
#     - a function that calculates the area and circumference of a circle called circle(area/circumference, radius)
#     - another function calculates the area and perimeter of a rectangle called rect(area/perimeter, length, breadth)
#     - another function calculates the area and perimeter of a triangle called triangle(area/perimeter, side1, side2, side3)
# These 3 functions can be stored in a module called plane_shapes, so that when we need to use the circle function, we simple:
#     - import plane_shapes
#     - plane_shapes.circle(circumference, radius)
#     - and we get the circumference of the said circle.
# 
# Alternatively, we could use the from keyword;
# - from plane_shapes import circle
# - circle(circumference, radius)
# 
# The above gives the same result

# ### Importing all functions from a module to the current workspace
# We may use the 
# 
# - import * 
# command to import all objects from a specific module
# - call each object or function as they are defined in the module

# In[26]:


#Lets import the myMod.py we created and store in the folder containing our active program

from myMod import *

greet2('Adebayo', 'M')


# ### Importing functions one by one from a module to the current workspace
# We may use the 
# 
# - import module_name 
# command to import the entire module
# - call each object or function as they are defined in the module with  dot(.) notation

# In[27]:


import myMod

myMod.greet2('David', 'M')


# ### Re-naming a Module
# You can create an alias when you import a module, by using the alias as keyword:
# 
# for Example:
#            
#            import myMod as m

# In[28]:


import myMod as m

m.student_age({"Monica":12, "Luke":30, "Steve": 33, "John": 23})


# #### Assignment 3
# - create a module called **plane_shapes** that contains:
#     - a function that calculates the area and circumference of a circle called circle(area/circumference, radius)
#     - another function calculates the area and perimeter of a rectangle called rect(area/perimeter, length, breadth)
#     - another function calculates the area and perimeter of a triangle called triangle(area/perimeter, side1, side2, side3)
# - Import the module 
# - Let users supply the values of parameters (radius, perimeter, length, breadth)
# - Use the circle and rectangle function
# 
# #### Assignment 4
# - Convert all the day2 exercises and assignments to functions
# - create a module containing all the functions you created 
# - import your modules and call various functions embeded in the module

# ### Remember, daily practice is key to your progress. Have fun!
