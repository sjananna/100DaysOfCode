name = input("Enter Your name:")
print("Hello " + name + "!")

# Topic: Getting Input from the User in Python

# Definition:
# The input() function is a built-in Python function that allows a program
# to receive information entered by the user through the keyboard.

# How input() works:
# 1. First, we create a variable to store the user's input.
# 2. The input() function displays a prompt asking the user to enter information.
# 3. The program waits until the user types something and presses Enter.
# 4. The entered value is returned by input() and assigned to the variable.
# 5. We can use the stored value later in our program.

# Important Notes:
# - input() always returns the user's input as a string (str).
# - The text inside input() is called a prompt.
# - The = operator assigns the returned value to the variable.
# - The print() function displays the stored information.
# - The + operator joins strings together. This is called string concatenation.
# - To receive an integer, use int(input()).
# - To receive a decimal number, use float(input()).


# Example 2: Getting a user's age

age = input("Enter Your Age: ")    # Receives the user's age as a string.
print("Your age is " + age)        # Prints the entered age.

# Example 3: Getting an integer input

age = int(input("Enter Your Age: "))  # Converts the user's input from a string to an integer.
print(age)                            # Prints the integer value.
print(type(age))                      # Displays the data type: <class 'int'>.

# Example 4: Getting a decimal input

height = float(input("Enter Your Height: "))  # Converts the user's input into a float.
print("Your height is " + str(height) + " feet.")
# Key Concept:
# input() = Receives information from the user.
# Variable = Stores the information.
# print() = Displays the information.
# int() = Converts a valid numeric string into an integer.
# float() = Converts a valid numeric string into a floating-point number.
# + = Concatenates strings.


