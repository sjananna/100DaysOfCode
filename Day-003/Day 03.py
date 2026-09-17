# Strings and Parameters

# String: A string in python described as 'str', is a sequence of text

#Ask the user for their name
name = input("What's your name? ")
print("Hello, " + name)
name="Samia"
print(name)


# The 'end' parameter

#print() has a built in default behavior
print("Hello")
print("Samia")
#Output:
#Hello
#Samia



# Formatting Strings


# end\n means a new line
print("Hello", end="\n")
print("Samia")
# Output:
# Hello
# Samia


# By default, print() ends with a new line
print("Hello\nSamia")# Output:
#Output:
# Hello
# Samia

# end=" "
print("Hello", end=" ")
print("Samia")
#Output: Hello Samia

# end=""
print("Hello", end="")
print("Samia")
#Output: HelloSamia

# end=" -> "
print("Hello", end=" -> ")
print("Samia")
#output: Hello -> Samia

#Notes:    end → controls what print() puts after it finishes printing.
#Notes:    \n -> means move to a new line
#Notes:    end=" " -> ends the print with a space instead of a new line
#Notes:    end="\n" -> ends the print with a new line; this is Python's default behavior



# Formatting Strings

#Ask the user for their name
name = input("What is your name? ")
print(f"Hello!, {name}")
# output: What is your name? Samia
#         Hello! Samia

# Notes:
#     Name → This is a variable, a named container used to store a value.
#     input() → This is a function that asks the user for input and returns what they type as a string.
#     f"Hello!, {name}" → This is an f-string (formatted string literal). It allows you to insert the value of a variable directly inside a string.
#     {name} → The curly braces tell the f-string to take the value stored in name and place it at that position.