# ============================================================
# PYTHON TUPLES
# ============================================================

# DEFINITION:
# A tuple is a built-in Python data type used to store multiple
# values in a single variable.

# Tuples are ordered, indexed, and immutable.
# Immutable means that once a tuple is created, its elements
# cannot be changed, added, or removed.

# Tuples are created using commas, usually enclosed in parentheses ().
# Lists are created using square brackets [].


# ------------------------------------------------------------
# 1. CREATING A TUPLE
# ------------------------------------------------------------

coordinates = (4, 5)

# Here, "coordinates" is a variable containing a tuple.
# The tuple stores two integer values: 4 and 5.
# Indexing starts at 0, just like Python lists.


# ------------------------------------------------------------
# 2. ACCESSING TUPLE ELEMENTS
# ------------------------------------------------------------

print(coordinates[0])  # Output: 4
print(coordinates[1])  # Output: 5

# coordinates[0] accesses the first element.
# coordinates[1] accesses the second element.
# We use square brackets [] to access elements by index.


# ------------------------------------------------------------
# 3. TUPLES ARE IMMUTABLE
# ------------------------------------------------------------

# coordinates[1] = 6
# print(coordinates[1])

# The above code will produce a TypeError if uncommented.
# This happens because tuples do not support item assignment.
# Once a tuple is created, we cannot modify its individual elements.


# ------------------------------------------------------------
# 4. DIFFERENCE BETWEEN LISTS AND TUPLES
# ------------------------------------------------------------

# LIST EXAMPLE:

numbers = [4, 5]
numbers[1] = 6
print(numbers)  # Output: [4, 6]

# Lists are mutable, meaning their elements can be modified.


# TUPLE EXAMPLE:

coordinates = (4, 5)
# coordinates[1] = 6  # TypeError!

# Tuples are immutable, meaning their elements cannot be modified.


# ------------------------------------------------------------
# 5. WHEN SHOULD WE USE TUPLES?
# ------------------------------------------------------------

# Use tuples when you want to store a collection of values
# that should remain unchanged.

# Examples:
# - Geographic coordinates (latitude, longitude)
# - RGB color values (red, green, blue)
# - Fixed dimensions (width, height)
# - Days of the week

rgb_color = (255, 0, 0)
dimensions = (1920, 1080)

print(rgb_color)
print(dimensions)

# ============================================================
# 6. PYTHON: LISTS CONTAINING TUPLES
# ============================================================

# A list can contain multiple tuples as its elements.
# Lists are mutable, while tuples are immutable.

numbers = [(4, 5), (7, 9), (2, 5), (8, 9)]

# The outer square brackets [] indicate a list.
# The parentheses () indicate tuples stored inside the list.

# Index 0 = (4, 5)
# Index 1 = (7, 9)
# Index 2 = (2, 5)
# Index 3 = (8, 9)

numbers[1] = 10

# Here, numbers[1] accesses the second element of the list.
# The tuple (7, 9) is replaced entirely with the integer 10.
# This is possible because the outer structure is a mutable list.

print(numbers)
# Output: [(4, 5), 10, (2, 5), (8, 9)]

# IMPORTANT:
# Replacing an entire tuple inside a list is allowed.
# However, modifying an individual element inside a tuple
# is NOT allowed because tuples are immutable.

# Example:
# numbers[0][1] = 10
# This would produce a TypeError because we are attempting
# to change the value 5 inside the tuple (4, 5).

# KEY TAKEAWAY:
# A list containing tuples is still mutable.
# The tuples themselves remain immutable.


# ============================================================
# 7. PYTHON: MUTABLE LISTS INSIDE IMMUTABLE TUPLES
# ============================================================

# A tuple is immutable, meaning its elements cannot be replaced.
# However, a tuple can contain mutable objects, such as lists.
# The contents of these nested lists can still be modified.

coordinates = (4, 5, [10, 20, 30])

# Here, coordinates is a tuple containing three elements.
# The outer parentheses () indicate a tuple.
# The inner square brackets [] indicate a list.

# Index 0 = 4
# Index 1 = 5
# Index 2 = [10, 20, 30]

print(coordinates)
# Output: (4, 5, [10, 20, 30])


# MODIFYING AN ELEMENT INSIDE THE NESTED LIST

coordinates[2][0] = 100

# coordinates[2] accesses the list [10, 20, 30].
# coordinates[2][0] accesses the first element of that list (10).
# The assignment = 100 replaces 10 with 100.
# This is allowed because lists are mutable.

print(coordinates)
# Output: (4, 5, [100, 20, 30])


# WHY DOES THIS WORK?

# Tuples are immutable, but lists are mutable.
# The tuple contains a reference to the nested list.
# We cannot replace that reference through tuple indexing.
# However, we can modify the contents of the referenced list.


# WHAT HAPPENS IF WE TRY TO REPLACE THE ENTIRE LIST?

# coordinates[2] = [40, 50, 60]

# This produces a TypeError.
# Tuples do not support item assignment.
# Replacing the entire list would modify an element of the tuple.


# IMPORTANT DIFFERENCE:

# coordinates[2][0] = 100
# ALLOWED: Modifies an element inside the nested list.

# coordinates[2] = [40, 50, 60]
# NOT ALLOWED: Attempts to replace an element of the tuple.


# KEY TAKEAWAY:

# A tuple can contain mutable objects, such as lists.
# We can modify the contents of a nested list.
# However, we cannot replace the list through tuple indexing.
# Tuple immutability does not make nested mutable objects immutable.


# ------------------------------------------------------------
# 8. IMPORTANT NOTES
# ------------------------------------------------------------

# 1. Tuples are ordered.
# 2. Tuples allow duplicate values.
# 3. Tuples support indexing and slicing.
# 4. Tuples can contain different data types.
# 5. Tuples cannot be modified after creation.
# 6. Lists are mutable, but tuples are immutable.
# 7. Tuples use () while lists use [].
# 8. Tuple elements are accessed using square brackets [].
# 9. A variable can be reassigned to a completely new tuple.
# 10. If a tuple contains a mutable object, such as a list,
#     the contents of that nested object can still be modified.




