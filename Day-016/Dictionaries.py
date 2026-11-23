monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "March",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions)
print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a Valid Key"))



Here are your Python dictionary notes for PyCharm, written entirely as comments so you can paste them directly into your IDE.

I’ve also included an important correction: In your dictionary, "May" is incorrectly assigned "March" instead of "May".

# ======================================================================
# PYTHON DICTIONARIES - COMPLETE BEGINNER NOTES
# TOPIC: DICTIONARIES, KEYS, VALUES, GET(), IMMUTABILITY, AND PRINT()
# ======================================================================
# 1. WHAT IS A DICTIONARY IN PYTHON?
#
# A dictionary is a built-in Python data structure.
#
# Dictionaries store information in KEY-VALUE pairs.
#
# Each key is associated with a corresponding value.
#
# Dictionaries are useful when we want to look up information
# using a meaningful identifier instead of a numerical index.
#
# EXAMPLE:
#
# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March"
# }
#
# Here:
#
# "Jan" = KEY
# "January" = VALUE
#
# "Feb" = KEY
# "February" = VALUE
#
# "Mar" = KEY
# "March" = VALUE
#
# The key identifies the information we want to retrieve.
#
# The value contains the information associated with that key.
#
# GENERAL SYNTAX:
#
# dictionary_name = {
#     key1: value1,
#     key2: value2,
#     key3: value3
# }
#
# IMPORTANT:
# Dictionaries use curly braces {}.
#
# A colon : separates each key from its value.
#
# A comma , separates different key-value pairs.
#
# Dictionary keys must be unique.
#
# Dictionaries preserve insertion order in Python 3.7+.
#
# Unlike lists, dictionaries are accessed using keys
# rather than automatically assigned numerical indexes.
# ======================================================================
# 2. UNDERSTANDING YOUR MONTH CONVERSION DICTIONARY
# ======================================================================
#
# Your dictionary stores abbreviated month names as keys.
#
# The corresponding full month names are stored as values.
#
# EXAMPLE:
#
# "Jan": "January"
#
# KEY = "Jan"
# VALUE = "January"
#
# When Python receives the key "Jan",
# it can retrieve the associated value "January".
#
# IMPORTANT CORRECTION:
#
# Your original dictionary contains:
#
# "May": "March"
#
# This is a logical mistake.
#
# Python will NOT produce an error because the dictionary
# syntax is valid.
#
# However, the information associated with "May" is incorrect.
#
# The correct pair should be:
#
# "May": "May"
#
# IMPORTANT LESSON:
#
# Code can execute successfully while still producing
# incorrect results because of incorrect data.
#
# This is called a logical error.
# ======================================================================
# 3. PRINT FUNCTION 1: PRINTING THE ENTIRE DICTIONARY
# ======================================================================
#
# YOUR CODE:
#
# print(monthConversions)
#
# EXPLANATION:
#
# print() is a built-in Python function.
#
# monthConversions is the variable containing the dictionary.
#
# When we pass the dictionary to print(),
# Python displays the entire dictionary.
#
# The output includes all keys and their associated values.
#
# EXAMPLE OUTPUT:
#
# {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', ...}
#
# The actual output includes all 12 key-value pairs.
#
# IMPORTANT:
#
# Printing the dictionary does not modify its contents.
#
# It only displays the dictionary's current representation.
#
# The dictionary retains the order in which its keys
# were originally inserted.
# ======================================================================
# 4. PRINT FUNCTION 2: ACCESSING A VALUE USING SQUARE BRACKETS
# ======================================================================
#
# YOUR CODE:
#
# print(monthConversions["Nov"])
#
# BREAKDOWN:
#
# print() = Displays the result.
#
# monthConversions = The dictionary we want to access.
#
# ["Nov"] = The key used to retrieve a value.
#
# Python searches the dictionary for the key "Nov".
#
# It finds:
#
# "Nov": "November"
#
# Therefore, Python returns the corresponding value.
#
# OUTPUT:
#
# November
#
# GENERAL SYNTAX:
#
# dictionary_name[key]
#
# IMPORTANT:
#
# The square brackets [] contain the KEY.
#
# They do not represent a numerical index in this example.
#
# The key must match an existing dictionary key.
#
# Dictionary key lookups are case-sensitive.
#
# For example:
#
# "Nov" and "nov" are different keys.
#
# IMPORTANT WARNING:
#
# If we attempt to access a key that does not exist,
# Python raises a KeyError.
#
# EXAMPLE:
#
# print(monthConversions["Luv"])
#
# RESULT:
#
# KeyError: 'Luv'
#
# This happens because "Luv" is not a key in the dictionary.
# ======================================================================
# 5. PRINT FUNCTION 3: USING THE GET() METHOD
# ======================================================================
#
# YOUR CODE:
#
# print(monthConversions.get("Dec"))
#
# BREAKDOWN:
#
# monthConversions = The dictionary we want to search.
#
# . = The dot operator used to access a method.
#
# get() = A dictionary method used to retrieve a value.
#
# "Dec" = The key supplied as an argument.
#
# Python searches for the key "Dec".
#
# It finds:
#
# "Dec": "December"
#
# OUTPUT:
#
# December
#
# GENERAL SYNTAX:
#
# dictionary_name.get(key)
#
# IMPORTANT:
#
# get() retrieves the value associated with a key.
#
# It does not remove, update, or modify the dictionary.
#
# Unlike square bracket access, get() does not raise
# a KeyError when the requested key does not exist.
#
# Instead, it returns None by default.
# ======================================================================
# 6. PRINT FUNCTION 4: USING GET() WITH A NONEXISTENT KEY
# ======================================================================
#
# YOUR CODE:
#
# print(monthConversions.get("Luv"))
#
# EXPLANATION:
#
# Python searches the dictionary for the key "Luv".
#
# However, the dictionary does not contain that key.
#
# Because we are using get(),
# Python does not raise a KeyError.
#
# Instead, get() returns None.
#
# OUTPUT:
#
# None
#
# WHAT IS NONE?
#
# None is a special value in Python.
#
# It represents the absence of a value.
#
# None is not the same as:
#
# 0
# False
# ""
#
# None has its own data type called NoneType.
#
# IMPORTANT:
#
# get() returns None when the key is missing
# and no alternative default value is provided.
#
# However, an existing key can also have None
# explicitly stored as its value.
#
# Therefore, receiving None does not always prove
# that the requested key is missing.
# ======================================================================
# 7. PRINT FUNCTION 5: USING GET() WITH A DEFAULT VALUE
# ======================================================================
#
# YOUR CODE:
#
# print(monthConversions.get("Luv", "Not a Valid Key"))
#
# GENERAL SYNTAX:
#
# dictionary_name.get(key, default_value)
#
# BREAKDOWN:
#
# monthConversions = The dictionary being searched.
#
# get() = The dictionary method used to retrieve a value.
#
# "Luv" = The key Python attempts to find.
#
# "Not a Valid Key" = The default value to return
#                     when the requested key is missing.
#
# The get() method accepts two arguments:
#
# ARGUMENT 1:
# key
#
# The key we want to search for.
#
# ARGUMENT 2:
# default_value
#
# The value returned when the key does not exist.
#
# IMPORTANT:
#
# The second argument is optional.
#
# If we do not provide it, the default is None.
#
# WHAT HAPPENS INTERNALLY?
#
# STEP 1:
# Python searches for the key "Luv".
#
# STEP 2:
# Python determines that the key does not exist.
#
# STEP 3:
# Instead of returning None,
# Python returns the supplied default value.
#
# OUTPUT:
#
# Not a Valid Key
#
# IMPORTANT:
#
# The default value does not get inserted
# into the dictionary.
#
# The dictionary remains unchanged.
#
# If the requested key exists,
# get() returns its actual associated value
# instead of the default value.
# ======================================================================
# 8. DIFFERENCE BETWEEN [] AND GET()
# ======================================================================
#
# METHOD 1: SQUARE BRACKETS
#
# dictionary_name[key]
#
# Retrieves the value associated with the specified key.
#
# If the key exists:
# Returns the corresponding value.
#
# If the key does not exist:
# Raises a KeyError.
#
#
# METHOD 2: GET()
#
# dictionary_name.get(key)
#
# If the key exists:
# Returns the corresponding value.
#
# If the key does not exist:
# Returns None by default.
#
#
# METHOD 3: GET() WITH A DEFAULT VALUE
#
# dictionary_name.get(key, default_value)
#
# If the key exists:
# Returns the corresponding value.
#
# If the key does not exist:
# Returns the supplied default value.
#
#
# IMPORTANT DIFFERENCE:
#
# [] can raise a KeyError when a key is missing.
#
# get() allows us to handle missing keys
# without raising a KeyError.
#
# This makes get() useful when we are uncertain
# whether a key exists in a dictionary.
# ======================================================================
# 9. IMPORTANT CONCEPT: DICTIONARY KEYS MUST BE HASHABLE
# ======================================================================
#
# Dictionary keys must be HASHABLE.
#
# A hashable object has a hash value that remains stable
# during its lifetime and supports equality comparisons.
#
# Python uses hashing to efficiently locate dictionary keys.
#
# Most common immutable built-in types are hashable.
#
# IMMUTABLE means an object's value cannot be changed
# after the object has been created.
#
# COMMON IMMUTABLE TYPES:
#
# 1. int
# 2. float
# 3. str
# 4. bool
# 5. tuple (when all its elements are hashable)
#
# EXAMPLES OF VALID DICTIONARY KEYS:
#
# "Jan"             -> String
# 101               -> Integer
# 3.14              -> Float
# True              -> Boolean
# (10, 20)          -> Tuple containing integers
#
# All these examples can be used as dictionary keys.
#
# IMPORTANT:
#
# Immutability and hashability are related concepts,
# but they are not exactly the same.
#
# A custom immutable object is not automatically hashable.
#
# A tuple is hashable only if all its elements are hashable.
#
# The actual requirement for dictionary keys is hashability,
# not simply immutability.
# ======================================================================
# 10. WHY CAN'T WE USE A LIST AS A DICTIONARY KEY?
# ======================================================================
#
# Lists are mutable.
#
# MUTABLE means an object can be changed after creation.
#
# EXAMPLE:
#
# numbers = [10, 20, 30]
#
# We can change an element:
#
# numbers[0] = 100
#
# The list becomes:
#
# [100, 20, 30]
#
# Because lists are mutable and unhashable,
# Python does not allow them as dictionary keys.
#
# INVALID EXAMPLE:
#
# my_dictionary = {
#     [1, 2]: "Numbers"
# }
#
# RESULT:
#
# TypeError: unhashable type: 'list'
#
# IMPORTANT:
#
# Dictionary keys must have stable hash values.
#
# Built-in lists do not provide the hashability
# required for dictionary keys.
# ======================================================================
# 11. WHY CAN WE USE A TUPLE AS A DICTIONARY KEY?
# ======================================================================
#
# Tuples are immutable.
#
# Once a tuple is created, its elements cannot
# be replaced, added, or removed.
#
# EXAMPLE:
#
# coordinates = (43, -79)
#
# A tuple containing only integers is hashable.
#
# Therefore, it can be used as a dictionary key.
#
# VALID EXAMPLE:
#
# locations = {
#     (43, -79): "Toronto",
#     (45, -75): "Ottawa"
# }
#
# Python can use these coordinate tuples as keys.
#
# IMPORTANT EXCEPTION:
#
# A tuple containing a list is not hashable.
#
# EXAMPLE:
#
# invalid_key = ([1, 2], 3)
#
# Although the outer object is a tuple,
# it contains a mutable, unhashable list.
#
# Therefore, the tuple cannot be used as a dictionary key.
#
# MOST IMPORTANT LESSON:
#
# A tuple can be a dictionary key only when
# all its elements are hashable.
# ======================================================================
# 12. CAN DICTIONARY VALUES BE MUTABLE?
# ======================================================================
#
# YES!
#
# Dictionary VALUES do not need to be immutable.
#
# Values can contain:
#
# Strings
# Integers
# Floats
# Lists
# Tuples
# Dictionaries
# Other Python objects
#
# EXAMPLE:
#
# student = {
#     "name": "Alice",
#     "grades": [85, 90, 95]
# }
#
# "name" and "grades" are string keys.
#
# "Alice" is a string value.
#
# [85, 90, 95] is a list value.
#
# The list is mutable, but this is allowed
# because it is a dictionary VALUE, not a key.
#
# IMPORTANT:
#
# Dictionary keys must be hashable.
#
# Dictionary values can be mutable or immutable.
# ======================================================================
# 13. CAN WE CHANGE DICTIONARY KEYS?
# ======================================================================
#
# We cannot modify an existing string key in place
# because strings are immutable.
#
# However, dictionaries themselves are mutable.
#
# This means we can:
#
# Add new key-value pairs.
# Update values associated with existing keys.
# Remove existing key-value pairs.
#
# EXAMPLE:
#
# monthConversions["Jan"] = "January"
#
# This assigns a value to the key "Jan".
#
# If the key already exists, its value is updated.
#
# If the key does not exist, a new pair is inserted.
#
# IMPORTANT:
#
# A dictionary key cannot be modified in place
# when it is an immutable object.
#
# To effectively rename a key, we can create
# a new key-value pair and remove the old one.
#
# The dictionary itself remains mutable.
# ======================================================================
# 14. WHY ARE DICTIONARY KEYS UNIQUE?
# ======================================================================
#
# Every dictionary key must be unique.
#
# A dictionary cannot contain two separate entries
# with equal keys.
#
# EXAMPLE:
#
# months = {
#     "Jan": "January",
#     "Jan": "Another Value"
# }
#
# Python does not create two separate "Jan" entries.
#
# Instead, the later value replaces the earlier value.
#
# The resulting dictionary contains:
#
# {"Jan": "Another Value"}
#
# IMPORTANT:
#
# Dictionary values do not have to be unique.
#
# Different keys can refer to identical values.
#
# For example:
#
# "A": 100
# "B": 100
#
# This is completely valid.
# ======================================================================
# 15. FINAL OUTPUT OF YOUR ORIGINAL PROGRAM
# ======================================================================
#
# PRINT 1:
#
# Displays the entire monthConversions dictionary.
#
# Note that the original dictionary incorrectly maps
# "May" to "March".
#
#
# PRINT 2:
#
# November
#
# REASON:
# The key "Nov" exists and maps to "November".
#
#
# PRINT 3:
#
# December
#
# REASON:
# get("Dec") retrieves the value associated with "Dec".
#
#
# PRINT 4:
#
# None
#
# REASON:
# The key "Luv" does not exist.
# get() returns None when no default is provided.
#
#
# PRINT 5:
#
# Not a Valid Key
#
# REASON:
# The key "Luv" does not exist.
# get() returns the supplied default value.
# ======================================================================
# 16. MOST IMPORTANT LESSONS LEARNED
# ======================================================================
#
# 1. Dictionaries store data as key-value pairs.
#
# 2. Dictionaries use curly braces {}.
#
# 3. A colon : separates a key from its value.
#
# 4. Dictionary keys must be unique.
#
# 5. Dictionary keys must be hashable.
#
# 6. Strings, integers, and hashable tuples can be keys.
#
# 7. Lists cannot be dictionary keys because they are unhashable.
#
# 8. Dictionary values can be mutable or immutable.
#
# 9. Dictionary values do not need to be unique.
#
# 10. dictionary[key] retrieves a value using square brackets.
#
# 11. Square bracket access raises KeyError for missing keys.
#
# 12. get(key) retrieves a value without raising KeyError
#     when the key is missing.
#
# 13. get(key) returns None by default for a missing key.
#
# 14. get(key, default) returns the supplied default
#     when the key is missing.
#
# 15. get() does not modify the dictionary.
#
# 16. Dictionary keys are case-sensitive when using strings.
#
# 17. Dictionaries preserve insertion order in Python 3.7+.
#
# 18. Dictionaries are mutable even though their keys
#     must be hashable.
#
# 19. A tuple is hashable only if all its elements are hashable.
#
# 20. A program can run successfully while containing
#     incorrect information, such as "May": "March".
# ======================================================================
# FINAL TAKEAWAY
# ======================================================================
#
# DICTIONARY = A collection of key-value pairs.
#
# KEY = The identifier used to retrieve information.
#
# VALUE = The information associated with a key.
#
# HASHABLE = An object that supports stable hashing
#            and equality comparisons.
#
# IMMUTABLE = An object that cannot be changed after creation.
#
# MUTABLE = An object that can be modified after creation.
#
# [] = Retrieves a value but raises KeyError if the key is missing.
#
# get() = Retrieves a value and supports a fallback for missing keys.
#
# get(key, default) = Returns the default if the key is absent.
#
# MOST IMPORTANT:
#
# Dictionary keys must be HASHABLE.
# Dictionary values can contain ANY type of Python object.
