# ============================================================
# DAY 014: PYTHON COMPARISON OPERATORS
# ============================================================

# ============================================================
# 1. WHAT ARE COMPARISON OPERATORS?
# ============================================================

# Comparison operators are used to compare two values.
#
# They evaluate a condition and return a Boolean result:
#
# True  = The comparison is correct.
# False = The comparison is incorrect.
#
# Comparison operators are commonly used with:
#
# 1. if statements
# 2. elif statements
# 3. while loops
# 4. Functions
# 5. Boolean expressions
#
# Python supports six main comparison operators:
#
# ==   Equal to
# !=   Not equal to
# >    Greater than
# <    Less than
# >=   Greater than or equal to
# <=   Less than or equal to
#
# IMPORTANT:
# Comparison operators can work with different data types.
#
# Examples include:
# - Integers (int)
# - Floating-point numbers (float)
# - Strings (str)
# - Booleans (bool)
#
# However, not every comparison is supported between
# every combination of data types.
#
# For example:
# 10 > 5       is valid.
# "Apple" == "Apple" is valid.
# 10 > "5"     raises a TypeError in Python 3.


# ============================================================
# 2. EQUAL TO OPERATOR (==)
# ============================================================

# The == operator checks whether two values are equal.
#
# It returns True if both values are equal.
# Otherwise, it returns False.
#
# IMPORTANT:
# =  is an assignment operator.
# == is a comparison operator.
#
# Do not confuse these two operators.

num1 = 10
num2 = 10

print(num1 == num2)

# OUTPUT:
# True
#
# EXPLANATION:
# num1 contains 10.
# num2 contains 10.
#
# Python compares:
# 10 == 10
#
# Since both values are equal, the result is True.


# ============================================================
# 3. NOT EQUAL TO OPERATOR (!=)
# ============================================================

# The != operator checks whether two values are different.
#
# If the values are different, it returns True.
# If the values are equal, it returns False.

num1 = 10
num2 = 20

print(num1 != num2)

# OUTPUT:
# True
#
# EXPLANATION:
# Python evaluates:
# 10 != 20
#
# Since 10 is different from 20, the result is True.


# ============================================================
# 4. GREATER THAN OPERATOR (>)
# ============================================================

# The > operator checks whether the value on the left
# is greater than the value on the right.
#
# It returns True only when the left value is larger.

print(50 > 30)

# OUTPUT:
# True
#
# EXPLANATION:
# 50 is greater than 30.
#
# Therefore:
# 50 > 30 = True
#
# IMPORTANT:
# If both numbers are equal, > returns False.
#
# Example:
# 50 > 50 = False


# ============================================================
# 5. LESS THAN OPERATOR (<)
# ============================================================

# The < operator checks whether the left value
# is smaller than the right value.

print(20 < 40)

# OUTPUT:
# True
#
# EXPLANATION:
# 20 is smaller than 40.
#
# Therefore:
# 20 < 40 = True


# ============================================================
# 6. GREATER THAN OR EQUAL TO OPERATOR (>=)
# ============================================================

# The >= operator checks whether the left value
# is greater than OR equal to the right value.
#
# The comparison is True when:
#
# 1. The left value is greater.
# 2. Both values are equal.
#
# This operator is particularly important
# in your max_num() function.

print(50 >= 40)
print(50 >= 50)
print(30 >= 50)

# OUTPUT:
# True
# True
# False
#
# EXPLANATION:
#
# 50 >= 40 = True
# Because 50 is greater than 40.
#
# 50 >= 50 = True
# Because both numbers are equal.
#
# 30 >= 50 = False
# Because 30 is neither greater than nor equal to 50.


# ============================================================
# 7. LESS THAN OR EQUAL TO OPERATOR (<=)
# ============================================================

# The <= operator checks whether the left value
# is less than OR equal to the right value.

print(20 <= 30)
print(20 <= 20)
print(40 <= 20)

# OUTPUT:
# True
# True
# False
#
# EXPLANATION:
#
# 20 <= 30 = True
# 20 <= 20 = True
# 40 <= 20 = False


# ============================================================
# 8. USING COMPARISON OPERATORS WITH STRINGS
# ============================================================

# Comparison operators can also compare strings.
#
# The == operator checks whether two strings have
# the same characters in the same order.
#
# Python string comparisons are case-sensitive.

print("Python" == "Python")
print("Python" == "python")
print("Apple" != "Banana")

# OUTPUT:
# True
# False
# True
#
# IMPORTANT:
# "Python" and "python" are not equal.
#
# This is because uppercase P and lowercase p
# are different characters.
#
# Strings can also be compared using <, >, <=, and >=.
#
# Python compares strings lexicographically
# using Unicode character values.

print("Apple" < "Banana")

# OUTPUT:
# True
#
# EXPLANATION:
# Python compares the characters from left to right.
#
# The Unicode value of "A" is smaller than "B".
# Therefore, "Apple" < "Banana" evaluates to True.


# ============================================================
# 9. USING COMPARISON OPERATORS WITH BOOLEANS
# ============================================================

# Boolean values can also be compared.
#
# True and False are Boolean values.
#
# In Python, bool is a subclass of int.
#
# For numeric comparisons:
#
# True behaves like 1.
# False behaves like 0.

print(True == True)
print(True == False)
print(True > False)
print(False < True)

# OUTPUT:
# True
# False
# True
# True
#
# IMPORTANT:
# Although Booleans can be compared numerically,
# they are primarily used to represent logical conditions.


# ============================================================
# 10. FINDING THE MAXIMUM NUMBER USING A FUNCTION
# ============================================================

# ORIGINAL CODE:

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(40, 78, 75))

# OUTPUT:
# 78


# ============================================================
# 11. UNDERSTANDING THE MAX_NUM FUNCTION STEP BY STEP
# ============================================================

# STEP 1: DEFINING THE FUNCTION
#
# def max_num(num1, num2, num3):
#
# The def keyword is used to define a function.
#
# max_num is the function name.
#
# num1, num2, and num3 are parameters.
#
# Parameters are variables that receive values
# when the function is called.
#
# In this example:
#
# max_num(40, 78, 75)
#
# num1 = 40
# num2 = 78
# num3 = 75


# ------------------------------------------------------------
# STEP 2: UNDERSTANDING THE FIRST IF CONDITION
# ------------------------------------------------------------

# if num1 >= num2 and num1 >= num3:
#
# This condition checks whether num1 is greater than
# or equal to BOTH num2 and num3.
#
# The >= operator performs the comparisons.
#
# The and operator combines the two conditions.
#
# IMPORTANT:
# The and operator requires BOTH comparisons to be True.
#
# Substitute the values:
#
# num1 >= num2
# 40 >= 78
#
# Result = False
#
# num1 >= num3
# 40 >= 75
#
# Result = False
#
# Therefore:
#
# False and False = False
#
# Python skips:
# return num1
#
# NOTE:
# Python uses short-circuit evaluation.
# Since 40 >= 78 is already False, Python does not
# actually need to evaluate the second comparison.
#
# We evaluated both above to understand the logic.


# ------------------------------------------------------------
# STEP 3: UNDERSTANDING THE ELIF CONDITION
# ------------------------------------------------------------

# elif num2 >= num1 and num2 >= num3:
#
# Since the first if condition was False,
# Python checks the elif condition.
#
# This condition checks whether num2 is greater than
# or equal to both num1 and num3.
#
# Substitute the values:
#
# num2 >= num1
# 78 >= 40
#
# Result = True
#
# num2 >= num3
# 78 >= 75
#
# Result = True
#
# Therefore:
#
# True and True = True
#
# Since both conditions are True,
# Python executes:
#
# return num2
#
# num2 contains 78.
#
# Therefore, the function returns 78.


# ------------------------------------------------------------
# STEP 4: UNDERSTANDING THE RETURN STATEMENT
# ------------------------------------------------------------

# return sends a value back to the place
# where the function was called.
#
# In this example:
#
# return num2
#
# returns the value 78.
#
# IMPORTANT:
# return does not automatically print a value.
#
# The print() function displays the returned value.
#
# Therefore:
#
# print(max_num(40, 78, 75))
#
# displays:
# 78
#
# Once Python executes a return statement,
# the function immediately stops executing.
#
# Any remaining statements inside that function
# are not executed.


# ------------------------------------------------------------
# STEP 5: UNDERSTANDING THE ELSE STATEMENT
# ------------------------------------------------------------

# else:
#     return num3
#
# The else block executes when both the if
# and elif conditions evaluate to False.
#
# This means num3 must be greater than num1 and num2
# for this particular three-number comparison.
#
# Example:
#
# max_num(40, 50, 90)
#
# First condition:
# 40 >= 50 and 40 >= 90
# False
#
# Second condition:
# 50 >= 40 and 50 >= 90
# False
#
# Therefore, Python executes:
# return num3
#
# OUTPUT:
# 90


# ============================================================
# 12. WHAT HAPPENS IF TWO NUMBERS ARE EQUAL?
# ============================================================

# Your function uses >= instead of >.
#
# This is important because >= includes equality.
#
# Example:

print(max_num(80, 80, 50))

# OUTPUT:
# 80
#
# EXPLANATION:
#
# First condition:
#
# num1 >= num2
# 80 >= 80 = True
#
# num1 >= num3
# 80 >= 50 = True
#
# True and True = True
#
# Python returns num1.
#
# IMPORTANT:
# Using >= allows the function to handle equal numbers.
#
# If you used > instead of >=, the function could
# return an incorrect result when numbers are equal.
#
# Example:
#
# max_num(80, 80, 50)
#
# With > instead of >=:
#
# 80 > 80 = False
#
# Both the if and elif conditions would fail.
#
# Python would execute else and return 50.
#
# This would be incorrect because the maximum is 80.


# ============================================================
# 13. CAN THE MAX_NUM FUNCTION COMPARE OTHER DATA TYPES?
# ============================================================

# Yes, but only when the data types support
# the required comparison operators.
#
# Your function can compare integers and floats.
#
# It can also compare strings lexicographically.
#
# Example:

print(max_num("Apple", "Banana", "Cherry"))

# OUTPUT:
# Cherry
#
# EXPLANATION:
# Python compares strings using Unicode character order.
#
# "Cherry" is greater than "Apple" and "Banana"
# in this comparison.
#
# Therefore, the function returns "Cherry".
#
# IMPORTANT:
# Comparing strings does not measure their lengths.
#
# For example:
# "Z" > "Apple" evaluates to True,
# even though "Z" has fewer characters.
#
# The function can also compare Boolean values.
#
# However, the maximum of Boolean values is usually
# less useful than comparing numbers.
#
# Comparing incompatible types can raise TypeError.
#
# Example:
# max_num(10, "20", 30)
#
# This raises TypeError because Python 3 cannot
# order an integer and a string using >=.


# ============================================================
# 14. PYTHON HAS A BUILT-IN MAX() FUNCTION
# ============================================================

# Python already provides a built-in function called max().
#
# It returns the largest value from the supplied values.
#
# Example:

print(max(40, 78, 75))

# OUTPUT:
# 78
#
# Your custom max_num() function and Python's max()
# produce the same result for these three numbers.
#
# IMPORTANT:
# Writing your own max_num() function is useful
# because it teaches:
#
# 1. Function definitions
# 2. Parameters and arguments
# 3. Comparison operators
# 4. Logical operators
# 5. Conditional statements
# 6. Return statements
#
# In real-world Python programs, the built-in max()
# function is often more convenient.


# ============================================================
# 15. SUMMARY: WHAT I LEARNED
# ============================================================

# ==  Checks whether two values are equal.
#
# !=  Checks whether two values are different.
#
# >   Checks whether the left value is greater.
#
# <   Checks whether the left value is smaller.
#
# >=  Checks whether the left value is greater than or equal.
#
# <=  Checks whether the left value is less than or equal.
#
# COMPARISON OPERATORS:
# Return Boolean results: True or False.
#
# LOGICAL OPERATORS:
# Combine or reverse Boolean conditions.
#
# and = All conditions must be True.
#
# or = At least one condition must be True.
#
# not = Reverses a Boolean condition.
#
# if = Checks the first condition.
#
# elif = Checks another condition if previous ones were False.
#
# else = Executes when all preceding conditions are False.
#
# return = Sends a value back to the function caller
#          and immediately ends the function.
#
# max() = Python's built-in function for finding
#         the maximum value.
