
# LeetCode-style mini problems using nput(), print(), end=, variables, and f-strings

# Problem 1 — Welcome User
# Ask the user for their name and print:
#                                        Enter your name: Samia
#                                        Welcome, Samia!

name = input("Enter your name: ")
print(f"Welcome, {name}")


# Problem 2 - First and Last Name
# Ask separately:   First name: Samia
#                   Last name: Jahan

name1 = input("First name: ")
name2 = input("Last name: ")



# Problem 3 — Learn end=
# You are given:  print("Python")
#                 print("is")
#                 print("fun")
#Currently it outputs:   Python
#                        is
#                        fun
# But we need:    Python is fun


print("Python", end=" ")
print("is", end=" ")
print("fun")



# Problem 5 — Name and Favourite Language
# Ask:   What is your name? Samia
#        What programming language are you learning? Python
# Output: Samia is learning Python!

name=input("What is your name? ")
programming=input("What is your programming language? ")
print(f"{name} is learning {programming}!")

# Problem 6 — Predict the Output

name = "Samia"
print("Hello", end=" ")
print(name, end="!")

# Ans: Hello Samia!


# Problem 7 — Find the Bug 🐛

name = input("What is your name? ")
print("Hello, {name}!")

#Ans: The f string is missing


# Problem 8 — Mini Challenge
# Create a Program that ask for :
#                                  Name:
#                                  City:
#                                  Dream job:
# Print                            Hello, Samia!
#                                  You live in Toronto.
#                                  Your dream job is Software Engineer.
#                                  Keep learning, Samia!


name=input("Name: ")
city=input("City: ")
job=input("Job: ")

print(f"Hello, {name}")
print(f"You live in {city}")
print(f"You are current a {job}")
print(f"Keep learning {name}")







# WHAT I LEARNED FROM THE CHALLENGES

# Learned how to take user input and store it inside a variable.

# Learned how to use multiple variables to store different user inputs.

# Learned how to use f-strings to insert variable values into sentences.

# Learned that variables inside an f-string must be placed inside {}.

# Learned that an f-string needs the letter f before the quotation marks.

# Learned how end=" " keeps the next print() output on the same line.

# Learned that print() normally uses end="\n", which moves the next output to a new line.

# Learned how multiple print() statements can be connected using end=.

# Learned how to combine input(), variables, f-strings, and print() to create a small interactive program.

# Basic pattern practiced:
# INPUT -> STORE IN VARIABLE -> USE THE VALUE -> PRINT THE RESULT

