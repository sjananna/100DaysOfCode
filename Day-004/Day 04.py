# More on Strings

#Stripe String

name = "   Samia   "
name = name.strip()
print(name)

# Ask the user for their name
name = input("What's your name? ")
# Remove whitespace from the str
name = name.strip()
# Print the output
print(f"hello, {name}")

# Note:
# strip() removes whitespace from the beginning and end of a string.
# If there is no extra whitespace, strip() will not visibly change the string.


# title method:

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize the first letter of each word
name = name.title()

# Print the output
print(f"hello, {name}")

# Notes:
# title() converts the first letter of each word to uppercase
# and the remaining letters to lowercase.



## title() can also be combined directly with input() and strip().


name=input("what's your name? ").strip().title()
print(f"Hello, {name}")

# Notes:
# strip() removes extra whitespace from the beginning and end.
# title() capitalizes the first letter of each word.