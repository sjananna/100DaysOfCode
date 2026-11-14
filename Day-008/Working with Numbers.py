#Writing a Number in Python
print(2.0987)
print(-2.9809)

#Adding and Subtracting in Python:
print(2+2)
print(2-2)
print(2*2+1)
print(2*2*(1+3))

#Using Modular Signs
print(10%3) #This gonna give the remainder

#Changing any integer to string
my_num = 5
print(my_num)
print(str(my_num)) #It will print string, it is very useful when you use it with other string
print(str(my_num) + " is a number.")

#Common Functions related to Python:
My_Num = -5
print(abs(My_Num)) #Absolute number
print(pow(3, 2)) #Power
print(pow(My_Num, 2))
print(max(4,6)) #max function should tell us which number is the higher
print(min(My_Num, 7))
print(round(4.5768))

#import python function

from math import *
print(sqrt(16)) #Python sqrt function always gives the decimal value.
print(int(sqrt(16)))
print(floor(2.87555)) #Round down to a lower number
print(ceil(2.87555)) #Round up to the highest number


# ==========================================
# PYTHON MATH MODULE AND IMPORT STATEMENT
# ==========================================

# math = A built-in Python module that provides mathematical functions and constants.
# It allows us to perform calculations such as square roots, rounding, logarithms, and trigonometry.
# Examples of math functions: sqrt(), floor(), ceil(), factorial().
# The math module is part of Python's standard library, so no additional installation is required.

# import = A Python keyword used to bring modules or specific functions into our program.
# It allows us to use functions and features defined in other modules.

# import math = Imports the entire math module.
# Example: math.sqrt(16) returns 4.0.

# from math import * = Imports all public functions and constants from the math module.
# The * (asterisk) means "import everything public" from the specified module.
# Example: sqrt(16) returns 4.0 without writing math. before the function.

# from math import sqrt = Imports only the sqrt() function from the math module.
# Example: sqrt(25) returns 5.0.

# Note: Using "import math" or importing specific functions is generally recommended
# because it makes the code easier to understand and avoids naming conflicts.





