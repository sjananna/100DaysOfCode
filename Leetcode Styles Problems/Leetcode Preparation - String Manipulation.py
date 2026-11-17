# ============================================================
# PYTHON: LEETCODE PREPARATION - STRING MANIPULATION
# ============================================================

# OBJECTIVE:
# We are starting our Python problem-solving journey to
# prepare for LeetCode coding challenges.
#
# The goal is to develop logical thinking, strengthen our
# understanding of Python, and learn how to solve coding
# problems independently.
#
# We will begin with beginner-friendly string manipulation
# problems using Python concepts we have already learned.
#
# TOPICS WE WILL PRACTICE:
#
# String concatenation (+)
# String indexing and negative indexing
# String slicing
# String length using len()
# Converting strings using .upper() and .lower()
# Checking strings using .isupper() and .islower()
# Finding characters using .index()
# Replacing text using .replace()
# Method chaining
# Comparing values using ==
#
# OUR PROBLEM-SOLVING APPROACH:
#
# Read the problem carefully and understand its requirements.
# Identify the input and expected output.
# Think about which Python concepts can solve the problem.
# Write the solution independently before checking the answer.
# Run the program and compare the output with the expected result.
# Debug any errors and understand why they occurred.
# Look for ways to make the solution simpler and more efficient.
#
# IMPORTANT:
# We will initially solve problems without using loops,
# conditional statements, or user-defined functions.
#
# As we learn more Python concepts, we will gradually
# introduce more challenging problems and algorithms.
#
# These exercises are designed to build the foundational
# skills needed to solve actual LeetCode problems.
#
# ============================================================
# BEGINNER STRING MANIPULATION CHALLENGES
# ============================================================


# PROBLEM 1: THE SECRET NAME

# Given a string containing a student's name with
# a mixture of uppercase and lowercase letters,
# perform the following operations:
#
# Convert the entire name to uppercase.
# Convert the entire name to lowercase.
# Print the total number of characters, including spaces.
# Print the first character of the name.
# Print the last character using negative indexing.
#
# RULES:
# Do not modify the original string.
# Do not use loops or conditional statements.
# Use only the Python concepts learned so far.
#
# EXPECTED OUTPUT:
# SAMIA JAHAN ANANNA
# samia jahan ananna
# 18
# s
# A

name = "sAmIa jAhAn aNaNnA"


# WRITE YOUR SOLUTION BELOW:

print(name.upper())
print(name.lower())
print(len(name))
print(name[0])
print(name[-1])

# ============================================================
# PROBLEM 2: FIND THE HIDDEN CHARACTER
# ============================================================

# OBJECTIVE:
# We are practicing string indexing and the .index() method
# to locate specific characters inside a string.
#
# Python uses zero-based indexing, meaning the first
# character of a string starts at index 0.
#
# The .index() method returns the index of the first
# occurrence of a specified character or substring.
#
# PROBLEM:
# Given the string "Python Programming", perform the
# following operations:
#
# Find the index of the first uppercase "P".
# Find the index of the first lowercase "g".
# Print the character located at index 7.
# Print the total number of characters in the string.
#

# HINT:
# Use .index() to find the position of a character.
# Use square brackets [] to access a character by index.
# Use len() to count the total number of characters.
#
# REMEMBER:
# Python indexing starts at 0, not 1.
# Spaces are also counted as characters.
# The .index() method is case-sensitive.
#
# WRITE YOUR SOLUTION BELOW:

message = "Python Programming"
print(message.index("P"))
print(message.index("g"))
print(message[7])
print(len(message))


# ============================================================
# PROBLEM 3: FIX THE SECRET MESSAGE
# ============================================================

# OBJECTIVE:
# Practice replacing text, converting strings to uppercase,
# calculating string length, and accessing characters.
#
# PROBLEM:
# You are developing a simple text correction system.
#
# A user submits the following message:
# "Java is the best programming language"
#
# Your task is to modify the message using Python.
#
# REQUIREMENTS:
# Replace the word "Java" with "Python".
# Convert the updated message to uppercase.
# Print the total number of characters in the updated message.
# Print the first character of the updated message.
#
# RULES:
# Do not use loops or conditional statements.
# Use only the Python concepts learned so far.
#
# BONUS CHALLENGE:
# Try solving the problem using method chaining.
#
# HINT:
# The .replace() method replaces specified text.
# The .upper() method converts text to uppercase.
# The len() function counts characters, including spaces.
# String indexing starts at 0.
#
# WRITE YOUR SOLUTION BELOW:

message = "Java is the best programming language"
message = message.replace("Java", "Python")
print(message)
print(message.upper())
print(len(message))
print(message[0])

# ============================================================
# IMPORTANT NOTE: STRING IMMUTABILITY AND VARIABLE REASSIGNMENT
# ============================================================

# MISTAKE:
# I used print(message.replace("Java", "Python")) expecting
# the original message variable to be updated.
#
# However, .replace() creates a new string without modifying
# the original string because strings are immutable in Python.
#
# The print() function only displays the modified result.
# It does not save the new string in the variable.
#
# Therefore, when I used message.upper(), len(message),
# and message[0], Python still accessed the original string.
#
# CORRECT APPROACH:
# message = message.replace("Java", "Python")
#
# The assignment operator (=) stores the new string
# in the message variable for future operations.
#
# We can also use method chaining:
# message = message.replace("Java", "Python").upper()
#
# KEY TAKEAWAY:
# String methods such as .replace(), .upper(), and .lower()
# return new strings instead of modifying the original.
#
# If I want to use the modified string later, I must
# assign the returned result to a variable.
#
# REMEMBER:
# Printing a result is NOT the same as storing a result.
# ============================================================


# ============================================================
# PROBLEM 4: USERNAME GENERATOR
# ============================================================

# OBJECTIVE:
# Practice string slicing, concatenation, and string methods
# to generate a username using personal information.
#
# PROBLEM:
# You are developing a username generator for a website.
#
# The program receives three pieces of information:
# A user's first name, last name, and birth year.
#
# Your task is to generate a username by combining
# specific characters from these variables.
#
# REQUIREMENTS:
# Extract the first three characters of the first name.
# Extract the first three characters of the last name.
# Combine both extracted strings with the birth year.
# Convert the entire username to lowercase.
# Print the final username.
#
# EXPECTED OUTPUT:
# samana2002
#
# HINT:
# String slicing allows us to extract specific characters.
# For example, name[0:3] extracts the first three characters.
#
# The + operator can concatenate multiple strings.
# The .lower() method converts a string to lowercase.
#
# BONUS CHALLENGE:
# Try generating the username using a single print() statement.
#
# WRITE YOUR SOLUTION BELOW:

first_name = "Samia"
last_name = "Ananna"
birth_year = "2002"

first_name = first_name[0:3]
print(first_name)

last_name = last_name[0:3]
print(last_name)

username = first_name+last_name+birth_year
print(username)

username = username.lower()
print(username.lower())
print(username)

# ============================================================
# PROBLEM 5: PASSWORD VALIDATION
# ============================================================

# OBJECTIVE:
# Practice string methods, indexing, length checking,
# and comparison operators to validate a password.
#
# PROBLEM:
# You are developing a basic password validation system
# for a website.
#
# The system receives a password from a user.
# Your task is to check whether the password meets
# specific conditions using Python.
#
# REQUIREMENTS:
# Check whether the password is entirely uppercase.
# Check whether the password is entirely lowercase.
# Check whether the password contains exactly 10 characters.
# Check whether the first character is "P".
# Check whether the last character is "6".
#
# EXPECTED OUTPUT:
# True
# False
# True
# True
# True
#

# HINT:
# The .isupper() method checks whether letters are uppercase.
# The .islower() method checks whether letters are lowercase.
# The len() function counts the total number of characters.
# The == operator compares two values and returns a Boolean.
# String indexing allows us to access individual characters.
# Negative indexing can access characters from the end.
#
# IMPORTANT:
# A Boolean value can be either True or False.
# Comparison expressions return Boolean values.
#
# BONUS CHALLENGE:
# Try completing all five requirements without
# creating any additional variables.
#
# WRITE YOUR SOLUTION BELOW:

password = "PYTHON2026"
print(password.isupper())
print(password.islower())
print(len(password) == 10)
print(password[0] == "P")
print(password[-1] == "6")

