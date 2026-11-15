num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 + num2
print(result)

# Topic: Getting Numeric Input from Users
# Concept: input(), int(), float(), Variables, and Arithmetic Operations

# Definition:
# The input() function always returns the user's input as a string (str),
# even if the user enters a number.

# Important Notes:
# 1. input() receives information from the user as a string.
# 2. int() converts a valid numeric string into an integer (whole number).
# 4. Without int(), the + operator joins two strings instead of adding numbers.
# 5. To perform mathematical calculations, we must convert string inputs into numeric types.
# 6. The = operator assigns a value to a variable.


# Example 2: What Happens Without int()?

num1 = input("Enter a number: ")                # Receives the first input as a string.
num2 = input("Enter another number: ")          # Receives the second input as a string.
result = num1 + num2                           # Concatenates the two strings instead of adding numbers.
print(result)                                  # Example: "10" + "20" produces "1020".


# Example 3: Adding Decimal Numbers Using float()

num1 = float(input("Enter a decimal number: "))          # Converts the first input into a float.
num2 = float(input("Enter another decimal number: "))    # Converts the second input into a float.
result = num1 + num2                                     # Adds the two floating-point numbers.
print(result)                                            # Example: 10.5 + 20.5 produces 31.0.


# Example 4: Checking the Data Type

number = input("Enter a number: ")              # Stores the user's input as a string.
print(type(number))                            # Output: <class 'str'>.

number = int(number)                           # Converts the string into an integer.
print(type(number))                            # Output: <class 'int'>.


# Key Concepts:
# input() = Receives user input as a string.
# int() = Converts a valid numeric string into an integer.
# float() = Converts a valid numeric string into a decimal number.
# + = Performs addition between numbers.
# + = Performs concatenation between strings.
# type() = Identifies the data type of a variable.

# Remember:
# "10" + "20" = "1020"  (String Concatenation)
# 10 + 20 = 30        (Integer Addition)
# 10.5 + 20.5 = 31.0 (Floating-Point Addition)

# Note:
# int() cannot directly convert a decimal string like "10.5" into an integer.
# Use float() for decimal inputs.
# Entering non-numeric text into int() or float() will cause a ValueError.