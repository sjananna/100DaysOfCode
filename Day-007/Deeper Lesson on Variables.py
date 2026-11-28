character_age = "35"
character_name = "Samia"
print("My name is " + character_name + ".")
print("My age is " + character_age + ". I am very strong.")
print("As I look forward to my future, my future will be exceptionally bright and people would know my name " + character_name + ".")

# ============================================================
# PYTHON BASICS - VARIABLES, STRINGS, AND STRING CONCATENATION
# ============================================================
# WHAT IS A VARIABLE?
# A variable is a name that refers to a value in Python.
# Variables allow us to store, access, update, and reuse data.
# Example:
# character_name = "Samia"
# character_name is the variable name.
# = is the assignment operator.
# "Samia" is the string value assigned to the variable.
#
# WHY DO WE USE VARIABLES?
# 1. To store information for later use.
# 2. To avoid repeatedly writing the same information.
# 3. To make programs easier to read and maintain.
# 4. To update information without rewriting multiple statements.
# 5. To perform operations using stored values.
#
# WHAT IS A STRING?
# A string is a sequence of characters enclosed in quotation marks.
# The Python data type for strings is str.
# Strings can contain:
# - Letters
# - Numbers
# - Spaces
# - Symbols
# - Punctuation
# Examples:
# "Samia" is a string.
# "35" is a string.
# "Python Programming" is a string.
# IMPORTANT:
# "35" is a string because it is enclosed in quotation marks.
# 35 is an integer because it is written without quotation marks.
#
# WHAT IS STRING CONCATENATION?
# String concatenation means joining two or more strings
# together to create a single string.
# Python uses the + operator for string concatenation.
# Example:
# "Hello " + "Samia"
# Result: "Hello Samia"
# IMPORTANT:
# When + is used between strings, it joins them.
# When + is used between numbers, it performs addition.
# For example:
# "10" + "5" produces "105".
# 10 + 5 produces 15.
# The operation depends on the data types involved.

# ============================================================
# PART 1: CREATING AND ASSIGNING VARIABLES
# ============================================================
# character_age = "35"
# EXPLANATION:
# character_age is the variable name.
# = is the assignment operator.
# It assigns the value on the right to the variable on the left.
# "35" is the value assigned to character_age.
# IMPORTANT:
# Although 35 looks like a number, Python treats "35"
# as a string because it is enclosed in quotation marks.
# DATA TYPE: str (string)
# If we wanted to store the age as an integer:
# character_age = 35
# The data type would be int (integer).
# DIFFERENCE:
# "35" = String
# 35 = Integer
# Strings are useful for displaying text.
# Integers are useful for mathematical calculations.
#
# character_name = "Samia"
# EXPLANATION:
# character_name is another variable.
# The assignment operator (=) assigns the string
# "Samia" to character_name.
# Python can retrieve this value whenever
# character_name is referenced later in the program.
# DATA TYPE: str (string)
# IMPORTANT:
# Variable names should describe the information they represent.
# character_name is more descriptive than x.
# Python variable names are case-sensitive.
# character_name and Character_Name are different names.

# ============================================================
# PART 2: PRINTING A VARIABLE WITH STRING CONCATENATION
# ============================================================
# print("My name is " + character_name + ".")
# EXPLANATION:
# print() is a built-in Python function.
# It displays information in the console.
# This statement combines three strings:
# 1. "My name is "
# 2. character_name
# 3. "."
# BREAKING DOWN EACH COMPONENT:
# "My name is " is a string containing text.
# Notice the space after "is".
# + is the string concatenation operator.
# It joins strings together.
# character_name stores the value "Samia".
# "." is another string containing a period.
# HOW PYTHON EXECUTES THIS STATEMENT:
# STEP 1: Python reads the first string, "My name is ".
# STEP 2: Python retrieves the current value of character_name.
# character_name = "Samia"
# STEP 3: Python concatenates the strings:
# "My name is " + "Samia" + "."
# STEP 4: print() displays the completed sentence.
# OUTPUT: My name is Samia.
# IMPORTANT CONCEPT: SPACING
# Python does not automatically insert spaces
# when concatenating strings.
# Example:
# "Hello" + "Samia" produces "HelloSamia".
# "Hello " + "Samia" produces "Hello Samia".
# Therefore, we must include spaces wherever necessary.

# ============================================================
# PART 3: CONCATENATING A VARIABLE CONTAINING A NUMBER
# ============================================================
# print("My age is " + character_age + ". I am very strong.")
# EXPLANATION:
# This statement uses string concatenation to combine
# a sentence with the value stored in character_age.
# The statement contains three components:
# 1. "My age is "
# 2. character_age
# 3. ". I am very strong."
# HOW PYTHON EXECUTES THIS STATEMENT:
# STEP 1: Python reads the first string, "My age is ".
# STEP 2: Python retrieves the value of character_age.
# character_age = "35"
# STEP 3: Python joins the three strings:
# "My age is " + "35" + ". I am very strong."
# STEP 4: print() displays the completed sentence.
# OUTPUT: My age is 35. I am very strong.
# WHY DOES THIS CODE WORK?
# Because character_age contains a string.
# The + operator can concatenate strings.
# However, consider:
# character_age = 35
# Now the variable contains an integer.
# If we attempt:
# print("My age is " + character_age)
# Python produces a TypeError.
# ERROR:
# TypeError: can only concatenate str (not "int") to str
# WHY DOES THIS ERROR OCCUR?
# Python cannot directly concatenate a string and an integer using +.
# String concatenation requires string operands.
# HOW CAN WE SOLVE THIS PROBLEM?
# We can convert the integer into a string using str().
# Example:
# character_age = 35
# print("My age is " + str(character_age))
# OUTPUT: My age is 35
# WHAT DOES str() DO?
# str() is a built-in Python function.
# It converts a value into its string representation.
# For example, str(35) produces "35".
# IMPORTANT:
# str() does not permanently change the original variable.
# If character_age contains the integer 35,
# str(character_age) produces a string representation.
# However, character_age itself remains an integer
# unless we assign a new value to it.

# ============================================================
# PART 4: REUSING VARIABLES IN LONGER SENTENCES
# ============================================================
# print("As I look forward to my future, my future will be exceptionally bright and people would know my name " + character_name + ".")
# EXPLANATION:
# This statement demonstrates variable reusability.
# Variable reusability means using the same variable
# multiple times throughout a program.
# We previously assigned:
# character_name = "Samia"
# Python can retrieve this value whenever the variable is referenced.
# We do not need to type "Samia" repeatedly.
# BREAKING DOWN THE STATEMENT:
# FIRST COMPONENT:
# "As I look forward to my future, my future will be exceptionally bright and people would know my name "
# This is a string containing a sentence
# except for the name and final period.
# SECOND COMPONENT:
# character_name contains "Samia".
# THIRD COMPONENT:
# "." adds the final period.
# HOW PYTHON EXECUTES THIS STATEMENT:
# STEP 1: Python reads the first string.
# STEP 2: Python encounters the + operator.
# STEP 3: Python retrieves the current value of character_name.
# STEP 4: Python concatenates the first string with "Samia".
# STEP 5: Python adds the final period.
# STEP 6: print() displays the completed sentence.
# OUTPUT:
# As I look forward to my future, my future will be exceptionally bright and people would know my name Samia.
# WHY IS VARIABLE REUSABILITY IMPORTANT?
# Imagine using character_name in 100 print statements.
# If we wanted to change the name from Samia to Alex,
# we could update the variable assignment:
# character_name = "Alex"
# Any later statements using character_name would
# retrieve the updated value.
# We would not need to manually rewrite every sentence.
# This makes programs easier to maintain.
# IMPORTANT CONCEPT: DYNAMIC VALUES
# A variable's value can change during program execution.
# Example:
# character_name = "Samia"
# character_name = "Alex"
# After the second assignment, character_name refers to "Alex".
# Python uses the current value when executing a statement.
# NOTE:
# Changing a variable does not automatically change
# text that was already printed in the console.

# ============================================================
# PART 5: UNDERSTANDING THE + OPERATOR
# ============================================================
# The + operator behaves differently depending
# on the data types of its operands.
# EXAMPLE 1: INTEGER ADDITION
# print(10 + 5)
# OUTPUT: 15
# Both values are integers.
# Python performs mathematical addition.
#
# EXAMPLE 2: STRING CONCATENATION
# print("10" + "5")
# OUTPUT: 105
# Both values are strings.
# Python joins them instead of adding them mathematically.
#
# EXAMPLE 3: MIXING STRINGS AND INTEGERS
# print("Age: " + 35)
# RESULT: TypeError
# Python cannot concatenate a string and an integer
# directly using the + operator.
#
# EXAMPLE 4: CONVERTING AN INTEGER INTO A STRING
# print("Age: " + str(35))
# OUTPUT: Age: 35
# str(35) converts the integer into the string "35".
# Python can then concatenate both strings successfully.

# ============================================================
# PART 6: INTRODUCTION TO F-STRINGS
# ============================================================
# WHAT IS AN F-STRING?
# An f-string is a formatted string literal.
# It allows us to insert variables and expressions
# directly into strings.
# We place the letter f before the opening quotation mark.
# Variables or expressions are placed inside curly braces {}.
# EXAMPLE:
# character_name = "Samia"
# character_age = 35
# print(f"My name is {character_name}.")
# OUTPUT: My name is Samia.
# HOW DOES IT WORK?
# f tells Python to process the string as an f-string.
# {character_name} tells Python to evaluate the variable
# and insert its value into the resulting string.
# ANOTHER EXAMPLE:
# print(f"My age is {character_age}.")
# OUTPUT: My age is 35.
# WHY ARE F-STRINGS USEFUL?
# 1. They make code easier to read.
# 2. They reduce the need for multiple + operators.
# 3. They support inserting integers and other values.
# 4. They make longer sentences easier to construct.
# 5. They can evaluate expressions inside curly braces.
# IMPORTANT DIFFERENCE:
# STRING CONCATENATION:
# print("My age is " + str(character_age))
# F-STRING:
# print(f"My age is {character_age}")
# Both can produce the same output.
# However, f-strings are often easier to read,
# especially when working with multiple variables.

# ============================================================
# FINAL SUMMARY - WHAT WE LEARNED
# ============================================================
# 1. VARIABLES:
# Names that refer to values.
# Example: character_name = "Samia"
#
# 2. STRINGS:
# Sequences of characters enclosed in quotation marks.
# Example: "Samia"
#
# 3. ASSIGNMENT OPERATOR (=):
# Assigns a value to a variable.
#
# 4. PRINT FUNCTION:
# print() displays information in the console.
#
# 5. STRING CONCATENATION:
# The + operator joins strings together.
#
# 6. DATA TYPES:
# "35" is a string.
# 35 is an integer.
#
# 7. TYPEERROR:
# Can occur when an operation is applied
# to incompatible data types.
#
# 8. str() FUNCTION:
# Converts a