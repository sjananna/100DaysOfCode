friends = ["Honey", "Karen", "Shimmer", "Samia", "Anny", "Harp", "Beatrice", "Kevin"]
Values = ["Name","21", "False" ]
Value = ["Name",21, False ]
print(friends)
print(friends[3])
print(friends[-1])
print(type(Values[2]))
print(friends[3:])
print(friends[3:5])

friends[1] = "Mike"
print(friends)


# ============================================================
# TOPIC: PYTHON LISTS
# Concepts: Lists, Indexing, Negative Indexing, Slicing,
# Data Types, type() Function, and Modifying List Elements
# ============================================================

# ------------------------------------------------------------
# 1. WHAT IS A LIST IN PYTHON?
# ------------------------------------------------------------

# Definition:
# A list is a built-in Python data structure used to store
# multiple values inside a single variable.

# Lists are created using square brackets [].
# Individual elements are separated by commas (,).

# Example:
# friends = ["Honey", "Karen", "Shimmer", "Samia",
#            "Anny", "Harp", "Beatrice", "Kevin"]

# Explanation:
# friends = The variable that stores the entire list.
# [] = Square brackets used to create a list.
# "Honey", "Karen", etc. = Individual elements of the list.
# , = Commas separate the elements.

# Important Properties of Lists:
# 1. Lists are ordered, meaning elements have specific positions.
# 2. Lists are mutable, meaning their elements can be changed.
# 3. Lists allow duplicate values.
# 4. Lists can contain different data types.
# 5. Lists use zero-based indexing, meaning counting starts at 0.


# ------------------------------------------------------------
# 2. PRINTING AN ENTIRE LIST
# ------------------------------------------------------------

# Example:
# print(friends)

# Explanation:
# The print() function displays the entire list.
# All elements appear inside square brackets.

# Output:
# ['Honey', 'Karen', 'Shimmer', 'Samia',
#  'Anny', 'Harp', 'Beatrice', 'Kevin']

# Note:
# Printing a list displays its representation, including
# square brackets, commas, and quotation marks around strings.


# ------------------------------------------------------------
# 3. ACCESSING LIST ELEMENTS USING INDEXING
# ------------------------------------------------------------

# Definition:
# Indexing allows us to access a specific element in a list
# using its position (index number).

# Python uses zero-based indexing.
# This means the first element has index 0, not 1.

# Example:
# friends = ["Honey", "Karen", "Shimmer", "Samia",
#            "Anny", "Harp", "Beatrice", "Kevin"]

# Index Positions:
#
# Index:       0        1         2         3
# Values:    Honey    Karen    Shimmer    Samia
#
# Index:       4        5         6         7
# Values:     Anny     Harp    Beatrice   Kevin

# Example:
# print(friends[3])

# Output:
# Samia

# Explanation:
# friends = The list variable.
# [3] = Accesses the element at index position 3.
# print() = Displays the selected element.


# ------------------------------------------------------------
# 4. NEGATIVE INDEXING
# ------------------------------------------------------------

# Definition:
# Negative indexing allows us to access elements
# starting from the end of a list.

# Positive indexing starts from 0.
# Negative indexing starts from -1.

# Example:
# friends = ["Honey", "Karen", "Shimmer", "Samia",
#            "Anny", "Harp", "Beatrice", "Kevin"]

# Negative Index Positions:
#
# Honey     = -8
# Karen     = -7
# Shimmer   = -6
# Samia     = -5
# Anny      = -4
# Harp      = -3
# Beatrice  = -2
# Kevin     = -1

# Example:
# print(friends[-1])

# Output:
# Kevin

# Explanation:
# [-1] accesses the last element of the list.
# [-2] accesses the second-to-last element.
# [-3] accesses the third-to-last element.

# Important:
# Negative indexing is useful when we want to access
# elements from the end without knowing the list's length.


# ------------------------------------------------------------
# 5. LISTS CAN STORE DIFFERENT DATA TYPES
# ------------------------------------------------------------

# Definition:
# Python lists can contain elements of different data types.

# Common Data Types:
#
# str   = String (text)
# int   = Integer (whole number)
# float = Floating-point number (decimal number)
# bool  = Boolean (True or False)

# Your Example:
# Values = ["Name", "21", "False"]

# Explanation:
# Although the list contains a word, a number-looking value,
# and a Boolean-looking value, all three are strings.

# Why?
# Because each value is enclosed in quotation marks ("").

# Python interprets values inside quotation marks as strings,
# regardless of whether they look like numbers or Booleans.

# Let's examine each element:

# Values[0] = "Name"
# Data Type = str
# Reason: Text enclosed in quotation marks.

# Values[1] = "21"
# Data Type = str
# Reason: The number 21 is enclosed in quotation marks.
# Therefore, Python treats it as text rather than an integer.

# Values[2] = "False"
# Data Type = str
# Reason: False is enclosed in quotation marks.
# Therefore, Python treats it as text rather than a Boolean.

# Example:
# print(type(Values[2]))

# Output:
# <class 'str'>

# Explanation:
# Values[2] accesses the third element, "False".
# type() checks the data type of the selected element.
# print() displays the result.

# Since "False" is enclosed in quotation marks,
# Python identifies its data type as str.


# ------------------------------------------------------------
# 6. DIFFERENCE BETWEEN STRINGS, INTEGERS, AND BOOLEANS
# ------------------------------------------------------------

# Example 1: All elements are strings.

# Values = ["Name", "21", "False"]

# print(type(Values[0]))  # <class 'str'>
# print(type(Values[1]))  # <class 'str'>
# print(type(Values[2]))  # <class 'str'>

# Example 2: Elements have different data types.

# Values = ["Name", 21, False]

# print(type(Values[0]))  # <class 'str'>
# print(type(Values[1]))  # <class 'int'>
# print(type(Values[2]))  # <class 'bool'>

# Explanation:
# "Name" = String because it is enclosed in quotation marks.
# 21 = Integer because it is a whole number without quotes.
# False = Boolean because it is written without quotes.

# Important:
# Boolean values must be written as True or False,
# with the first letter capitalized.

# "False" is a string.
# False is a Boolean.

# "21" is a string.
# 21 is an integer.

# A list does not automatically convert strings into
# integers or Booleans based on their appearance.

# Key Learning:
# The data type of each list element depends on how
# the value is written, not simply on its appearance.


# ------------------------------------------------------------
# 7. LIST SLICING
# ------------------------------------------------------------

# Definition:
# Slicing allows us to access a portion of a list
# instead of selecting only one element.

# General Syntax:
# list_name[start:stop]

# start = Index where slicing begins (included).
# stop = Index where slicing ends (excluded).

# Important:
# Python includes the starting index but excludes
# the stopping index.


# ------------------------------------------------------------
# 8. SLICING FROM A SPECIFIC INDEX TO THE END
# ------------------------------------------------------------

# Example:
# print(friends[3:])

# Output:
# ['Samia', 'Anny', 'Harp', 'Beatrice', 'Kevin']

# Explanation:
# [3:] means start at index 3 and continue to the end.

# Index 3 = Samia
# Index 4 = Anny
# Index 5 = Harp
# Index 6 = Beatrice
# Index 7 = Kevin

# Because no stopping index is provided,
# Python includes all remaining elements.

# Important:
# Leaving the stop position empty tells Python
# to continue slicing until the end of the list.


# ------------------------------------------------------------
# 9. SLICING BETWEEN TWO INDEX POSITIONS
# ------------------------------------------------------------

# Example:
# print(friends[3:5])

# Output:
# ['Samia', 'Anny']

# Explanation:
# [3:5] starts at index 3 and stops before index 5.

# Index 3 = Samia (included)
# Index 4 = Anny (included)
# Index 5 = Harp (excluded)

# Therefore, only Samia and Anny are returned.

# Important:
# The stopping index is NOT included in the result.

# Additional Examples:
#
# friends[0:3] = First three elements.
# friends[:3]  = Elements from the beginning to index 2.
# friends[3:]  = Elements from index 3 to the end.
# friends[:]   = A shallow copy of the entire list.


# ------------------------------------------------------------
# 10. MODIFYING ELEMENTS INSIDE A LIST
# ------------------------------------------------------------

# Definition:
# Lists are mutable, meaning we can change their elements
# after the list has been created.

# Original List:
# friends = ["Honey", "Karen", "Shimmer", "Samia",
#            "Anny", "Harp", "Beatrice", "Kevin"]

# Example:
# friends[1] = "Mike"

# Explanation:
# friends = The list variable.
# [1] = The index position of the element we want to change.
# = = Assignment operator.
# "Mike" = The new value assigned to index 1.

# Before Modification:
# Index 1 = Karen

# After Modification:
# Index 1 = Mike

# The original value "Karen" is replaced with "Mike".

# Example:
# print(friends)

# Output:
# ['Honey', 'Mike', 'Shimmer', 'Samia',
#  'Anny', 'Harp', 'Beatrice', 'Kevin']

# Important:
# Changing an element does not create a new list.
# It modifies the existing list.

# This is possible because Python lists are mutable.


# ------------------------------------------------------------
# 11. DIFFERENCE BETWEEN INDEXING AND SLICING
# ------------------------------------------------------------

# Indexing:
# Selects one element from a list.

# Example:
# print(friends[3])

# Output:
# Samia

# Data Type:
# str (because the selected element is a string).


# Slicing:
# Selects a portion of the list.

# Example:
# print(friends[3:5])

# Output:
# ['Samia', 'Anny']

# Data Type:
# list (because slicing returns a new list).

# Important:
# Indexing returns an individual element.
# Slicing returns a list containing the selected elements.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. Lists store multiple values inside a single variable.
# 2. Lists are created using square brackets [].
# 3. List elements are separated by commas.
# 4. Python lists use zero-based indexing.
# 5. Positive indexing starts from the beginning.
# 6. Negative indexing starts from the end.
# 7. Slicing extracts a portion of a list.
# 8. The starting index is included in slicing.
# 9. The stopping index is excluded in slicing.
# 10. Lists can contain different data types.
# 11. Values inside quotation marks are strings.
# 12. "21" is a string, while 21 is an integer.
# 13. "False" is a string, while False is a Boolean.
# 14. type() identifies the data type of a value.
# 15. Lists are mutable, so their elements can be modified.
# 16. Indexing returns an element; slicing returns a list.