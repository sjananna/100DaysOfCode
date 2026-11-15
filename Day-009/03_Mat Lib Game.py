# Create a Mad Libs story

animal = input("Enter and animal name: ")
food = input("Enter a food name: ")
planet = input("Enter a planet name: ")

print("One day I found a " + animal +  " in my laboratory.\nIt was eating " + food +".\nSuddenly it escaped and ran to planet")



# ============================================================
# PROJECT: MAD LIBS GAME
# Topic: Variables, input(), print(), String Concatenation
# ============================================================

# Definition:
# A Mad Libs Game is a simple word-based game where the user
# enters different words, and the program uses those words
# to create a funny or unexpected story.

# Concepts Used:
# 1. Variables
# 2. input() Function
# 3. print() Function
# 4. String Concatenation (+)
# 5. Escape Character (\n)


# 1. PLANNING THE PROGRAM, VARIABLES, AND USER INPUT
# ------------------------------------------------------------

# My Approach to Building the Mad Libs Game:
#
# Instead of immediately writing Python code, I took a different
# approach by first planning and arranging the story.
#
# Step 1: I started by deciding what story I wanted the program
# to display using the print() function.
#
# Step 2: I arranged the sentences and identified the keywords
# that could be replaced with information entered by the user.
#
# Step 3: I selected three keywords: animal, food, and planet.
# These keywords became the variables for my program.
#
# Step 4: After identifying the variables, I used the input()
# function to ask the user to enter values for each variable.
#
# Step 5: I connected the variables to the story using the
# + operator (string concatenation) inside the print() function.
#
# Step 6: Finally, I used the \n escape character to arrange
# the sentences on separate lines.
#
# Key Learning:
# I focused on planning the structure and expected output
# before implementing the code. This helped me understand
# what information the program needed from the user and
# how the variables would be used to generate the story.


# ------------------------------------------------------------
# 2. VARIABLES AND USER INPUT
# ------------------------------------------------------------

# The input() function asks the user to enter information.
# The information entered by the user is always returned
# as a string (str).

# Example:
# animal = input("Enter an animal name: ")

# Explanation:
# animal = A variable that stores the user's answer.
# input() = A built-in Python function that receives user input.
# "Enter an animal name: " = A prompt displayed to the user.
# = = Assignment operator that assigns the input value to the variable.

# In this game, I created three variables:
# animal = Stores the animal entered by the user.
# food = Stores the food entered by the user.
# planet = Stores the planet entered by the user.


# ------------------------------------------------------------
# 3. STRING CONCATENATION (+)
# ------------------------------------------------------------

# String concatenation means joining two or more strings together.
# In Python, the + operator combines strings into one string.

# Example:
# print("One day I found a " + animal + " in my laboratory.")

# Explanation:
# "One day I found a " = First string.
# animal = Variable containing the user's input.
# " in my laboratory." = Second string.
# + = Joins the strings and variable values together.

# If the user enters Penguin:
# Output: One day I found a Penguin in my laboratory.

# Important:
# When concatenating strings, spaces must be added manually.
# Example: "Hello " + name
# Without the space, the words will appear joined together.


# ------------------------------------------------------------
# 4. NEWLINE ESCAPE CHARACTER (\n)
# ------------------------------------------------------------

# The \n escape character moves the following text to a new line.
# It allows us to display multiple sentences using one print() function.

# Example:
# print("Hello\nWorld")

# Output:
# Hello
# World

# In our Mad Libs Game, we used \n to separate
# the three sentences of our story.


# ------------------------------------------------------------
# 5. USING VARIABLES INSIDE PRINT()
# ------------------------------------------------------------

# Variables must be written outside quotation marks
# when we want Python to use their stored values.

# Example:
# print("The animal is " + animal)

# If animal = "Penguin":
# Output: The animal is Penguin

# Incorrect:
# print("The animal is animal")

# Output: The animal is animal

# Explanation:
# Python treats anything inside quotation marks as literal text.
# To display a variable's value, write its name outside the quotes.


# ------------------------------------------------------------
# 6. HOW THE MAD LIBS GAME WORKS
# ------------------------------------------------------------

# Step 1: The program asks the user to enter three words.
# Step 2: Each answer is stored in a separate variable.
# Step 3: The print() function creates a story using those variables.
# Step 4: The + operator joins strings with the user's answers.
# Step 5: The \n escape character separates the story into lines.
# Step 6: Python displays the completed story in the console.


# ------------------------------------------------------------
# KEY TAKEAWAYS
# ------------------------------------------------------------

# 1. input() collects information from the user.
# 2. Variables store the information for later use.
# 3. The + operator joins strings together.
# 4. print() displays the final result.
# 5. \n creates a new line within a string.
# 6. Variable names outside quotes display their stored values.
# 7. Variable names inside quotes are treated as ordinary text.
# 8. Mad Libs demonstrates how user input can create dynamic output.