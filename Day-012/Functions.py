# ============================================================
# DAY 011 — PYTHON FUNCTIONS, PARAMETERS, AND ARGUMENTS
# ============================================================


# ============================================================
# 1. CREATING A SIMPLE FUNCTION
# ============================================================

def say_hi():  # 'def' defines a function named say_hi. No parameters are required.
    print("Hello User")  # This statement executes when the function is called.

say_hi()  # Calls the function and prints "Hello User".


# NOTES:
# A function is a reusable block of code designed to perform a task.
# 'def' is the Python keyword used to define a function.
# 'say_hi' is the function's name.
# () contains the function's parameters, if any.
# The colon (:) indicates the beginning of the function body.
# Indentation tells Python which statements belong to the function.
#
# IMPORTANT:
# Defining a function does not automatically execute its code.
# We must call the function using its name followed by parentheses.
#
# OUTPUT:
# Hello User


# ============================================================
# 2. CREATING A FUNCTION WITH A PARAMETER
# ============================================================

def sayhi(name):  # 'name' is a parameter that receives a value.
    print("Hello " + name)  # Concatenates "Hello " with the value of name.

sayhi("Mike")   # Passes "Mike" as an argument to the function.
sayhi("Steve")  # Passes "Steve" as an argument to the same function.


# NOTES:
# A parameter is a variable declared inside a function's parentheses.
# An argument is the actual value passed when calling the function.
#
# In this example:
# name = Parameter
# "Mike" = Argument
# "Steve" = Argument
#
# When sayhi("Mike") executes:
# Python assigns "Mike" to the parameter name.
# The function prints "Hello Mike".
#
# When sayhi("Steve") executes:
# Python assigns "Steve" to the parameter name.
# The function prints "Hello Steve".
#
# IMPORTANT:
# We can reuse the same function with different arguments.
# Since "Mike" and "Steve" are strings, they can be
# concatenated with "Hello " using the + operator.
#
# OUTPUT:
# Hello Mike
# Hello Steve


# ============================================================
# 3. FUNCTIONS WITH STRINGS AND INTEGERS
# ============================================================

def sayhi(name):  # Redefines the existing sayhi function.
    print("Hello " + name)

def age(age2):  # 'age2' is a parameter that receives the age.
    print("My age is " + age2)  # Works when age2 is a string.

age("24")  # Passes "24" as a string argument.


# NOTES:
# Here, we passed "24" instead of 24.
#
# WHY?
#
# "24" = String (str)
# 24   = Integer (int)
#
# Python does not allow direct concatenation between
# a string and an integer using the + operator.
#
# INCORRECT:
# print("My age is " + 24)
#
# This produces a TypeError because Python cannot
# concatenate a string and an integer directly.
#
# CORRECT:
# print("My age is " + "24")
#
# Both values are strings, so concatenation works.
#
# OUTPUT:
# My age is 24
#
# IMPORTANT:
# Although "24" and 24 look identical when printed,
# Python treats them as different data types.


# ============================================================
# 4. WHY KEEPING AGE AS AN INTEGER IS MORE USEFUL
# ============================================================

def age_next_year(age2):  # Receives an integer representing someone's age.
    print("My age next year will be " + str(age2 + 1))

age_next_year(24)  # Passes 24 as an integer.


# NOTES:
# Keeping age as an integer allows mathematical calculations.
#
# STEP-BY-STEP:
#
# 1. age_next_year(24) passes the integer 24.
#
# 2. The parameter age2 receives 24.
#
# 3. Python calculates age2 + 1.
#    24 + 1 = 25
#
# 4. str(age2 + 1) converts the result into a string.
#
# 5. The string is concatenated with "My age next year will be ".
#
# OUTPUT:
# My age next year will be 25
#
# IMPORTANT:
# If we passed "24" instead of 24, the expression
# age2 + 1 would produce a TypeError.
#
# WHY?
# Because Python cannot add an integer to a string.
#
# If the age is received as a string, we can use int()
# to convert it into an integer.
#
# Example:
# int("24") = 24
#
# BEST PRACTICE:
# Keep numbers as integers or floats when performing calculations.
# Convert them into strings when necessary for text concatenation.


# ============================================================
# 5. FUNCTIONS WITH MULTIPLE PARAMETERS
# ============================================================

def store(name, age):  # Defines a function with two parameters: name and age.
    print("My name is " + name + ". I am " + str(age) + " years old.")

store("Mike", 24)   # name receives "Mike", and age receives 24.
store("Steve", 70)  # name receives "Steve", and age receives 70.


# NOTES:
# A function can receive multiple parameters.
# Each parameter is separated by a comma.
#
# In this example:
#
# PARAMETERS:
# name
# age
#
# ARGUMENTS:
# "Mike", 24
# "Steve", 70
#
# STEP-BY-STEP:
#
# When store("Mike", 24) executes:
#
# 1. Python assigns "Mike" to name.
# 2. Python assigns 24 to age.
# 3. The print statement combines the values.
# 4. str(age) converts 24 into "24".
# 5. Python prints the complete sentence.
#
# OUTPUT:
# My name is Mike. I am 24 years old.
# My name is Steve. I am 70 years old.
#
# IMPORTANT:
# Python assigns positional arguments according to their order.
#
# First argument  -> First parameter
# Second argument -> Second parameter
#
# The str(age) conversion is necessary here because
# the + operator cannot concatenate strings with integers.


# ============================================================
# 6. USING F-STRINGS INSTEAD OF str()
# ============================================================

def store_details(name, age):
    print(f"My name is {name}. I am {age} years old.")

store_details("Mike", 24)
store_details("Steve", 70)


# NOTES:
# An f-string is a formatted string literal.
#
# The letter f is placed before the opening quotation mark.
# Variables and expressions are placed inside curly brackets {}.
#
# Python automatically formats the values as text.
#
# Therefore, we do not need to use str(age) explicitly.
#
# COMPARISON:
#
# Using concatenation:
# print("My name is " + name + ". I am " + str(age) + " years old.")
#
# Using an f-string:
# print(f"My name is {name}. I am {age} years old.")
#
# Both produce the same output.
#
# F-strings are generally easier to read and maintain.
#
# IMPORTANT:
# Using an f-string does not change the original
# data type of the variable.
#
# OUTPUT:
# My name is Mike. I am 24 years old.
# My name is Steve. I am 70 years old.


# ============================================================
# 7. SUMMARY — IMPORTANT PYTHON FUNCTION CONCEPTS
# ============================================================

# FUNCTION:
# A reusable block of code that performs a specific task.
#
# def:
# The keyword used to define a function.
#
# PARAMETER:
# A variable defined in a function's parentheses.
#
# ARGUMENT:
# The actual value passed when calling a function.
#
# FUNCTION CALL:
# Executes the function using its name and parentheses.
#
# STRING (str):
# A data type used to represent text.
# Example: "Mike", "24", "Hello"
#
# INTEGER (int):
# A data type used to represent whole numbers.
# Example: 24, 70, 100
#
# str():
# Converts a value into a string.
# Example: str(24) -> "24"
#
# int():
# Converts a compatible value into an integer.
# Example: int("24") -> 24
#
# CONCATENATION:
# Combining strings using the + operator.
# Example: "Hello " + "Mike" -> "Hello Mike"
#
# F-STRING:
# A formatted string that allows variables to be
# inserted directly using curly brackets {}.
#
