# ============================================================
# PYTHON LIST METHODS
# ============================================================

# A list is an ordered and changeable (mutable) collection of elements.
# Lists are created using square brackets [].
# Lists can contain strings, integers, floats, Boolean values, and other data types.
# Python uses zero-based indexing, meaning the first element is at index 0.


# 1. CREATING LISTS

lucky_number = [4, 8, 7, 18, 22, 28, 40]  # Creates a list containing seven integers.
print(lucky_number)  # Displays all the elements inside the lucky_number list.

friends_name = ["Heina", "Reith", "Duck", "Rick", "Emmanuel"]  # Creates a list containing five strings.
print(friends_name)  # Displays all the names stored in the list.


# 2. extend() METHOD

# extend() adds all the elements from another iterable to the end of an existing list.
# Unlike append(), extend() adds each element individually.
# The original list is modified, but the list supplying the elements remains unchanged.

friends_name.extend(lucky_number)  # Adds all seven numbers from lucky_number to friends_name.
print(friends_name)  # Displays the updated list containing both strings and integers.


# 3. append() METHOD

# append() adds a single element to the END of an existing list.
# It does not replace or remove any existing elements.
# If we append another list, that entire list becomes one nested element.

friends_name.append("Andy")  # Adds "Andy" as the last element of friends_name.
print(friends_name)  # Displays the updated list.


# 4. insert() METHOD

# insert() adds an element at a specific index position.
# Syntax: list.insert(index, value)
# The first argument specifies the index, and the second specifies the value.
# Existing elements at that index and afterward move one position to the right.
# Remember that Python indexing starts at 0.

friends_name.insert(1, "Jack")  # Inserts "Jack" at index 1, which is the second position.
print(friends_name)  # Displays the list after inserting "Jack".


# 5. remove() METHOD

# remove() deletes an element based on its VALUE rather than its index.
# If the value appears multiple times, only its FIRST occurrence is removed.
# If the specified value does not exist, Python raises a ValueError.
# remove() modifies the original list and returns None.

friends_name.remove("Rick")  # Searches for "Rick" and removes it from the list.
print(friends_name)  # Displays the list without "Rick".


# 6. pop() METHOD

# pop() removes an element from a list and returns the removed value.
# If no index is provided, pop() removes the LAST element.
# If an index is specified, it removes the element at that index.
# Example: friends_name.pop(2) removes the element at index 2.
# Unlike remove(), pop() works with index positions.

friends_name.pop()  # Removes the last element, which is "Andy".
print(friends_name)  # Displays the list after removing the last element.


# 7. index() METHOD

# index() searches for a specified value and returns its index position.
# Python starts counting index positions from 0.
# If duplicate values exist, index() returns the position of the FIRST occurrence.
# If the value does not exist, Python raises a ValueError.
# index() does not modify the original list.

print(friends_name.index("Reith"))  # Returns 2 because "Reith" is currently at index 2.


# 8. count() METHOD

# count() calculates how many times a specified value appears in a list.
# It returns an integer representing the number of occurrences.
# If the value does not exist, count() returns 0.
# count() does not change the original list.

friends_name = ["Heina", "Reith", "Duck", "Jim", "Jim", "Emmanuel"]  # Reassigns the variable to a new list.
print(friends_name.count("Jim"))  # Returns 2 because "Jim" appears twice.


# 9. sort() METHOD — STRINGS

# sort() arranges the elements of a list in ascending order.
# For strings, sorting is lexicographical, based on Unicode character values.
# For names with the same capitalization, this usually appears alphabetical (A to Z).
# sort() modifies the ORIGINAL list instead of creating a new one.
# To sort in descending order, use list.sort(reverse=True).
# Python 3 cannot directly sort a list containing both integers and strings.

friends_name.sort()  # Arranges the names alphabetically from A to Z.
print(friends_name)  # Displays ['Duck', 'Emmanuel', 'Heina', 'Jim', 'Jim', 'Reith'].


# 10. sort() METHOD — NUMBERS

# When sort() is applied to numbers, it arranges them from smallest to largest.
# The default sorting order is ascending.
# IMPORTANT: sort() modifies the existing list and returns None.
# Therefore, print(lucky_number.sort()) prints None instead of the sorted numbers.
# To print the sorted list, first call sort() and then print the variable.
# Alternatively, sorted(lucky_number) returns a NEW sorted list.
# Example: print(sorted(lucky_number)) prints the sorted numbers directly.

lucky_number.sort()  # note that you can not automate this sort into the print function directly like print(lucky_number.sort())
print(lucky_number)  # Displays [4, 7, 8, 18, 22, 28, 40].


# 11. reverse() METHOD

# reverse() reverses the CURRENT order of elements in a list.
# It does not automatically arrange numbers from largest to smallest.
# Since lucky_number was previously sorted in ascending order,
# reversing it now produces descending order.
# reverse() modifies the original list and returns None.
# To sort directly in descending order, use list.sort(reverse=True).

lucky_number.reverse()  # Reverses the order of the lucky_number list.
print(lucky_number)  # Displays [40, 28, 22, 18, 8, 7, 4].


# 12. copy() METHOD

# copy() creates a NEW list containing the elements of an existing list.
# The copied list is stored in a separate variable.
# Changes to the outer structure of the original list do not affect the copied list.
# However, copy() creates a SHALLOW copy, so nested mutable objects remain shared.
# Example: friends2 = friends_name.copy()
# friends2 now contains the same names as friends_name.
# Printing friends_name displays the original list, not the copied variable.

friends2 = friends_name.copy()  # Creates a separate shallow copy and stores it in friends2.
print(friends_name)  # Displays the original friends_name list.


# 13. clear() METHOD

# clear() removes ALL elements from an existing list.
# The variable itself is not deleted; it simply contains an empty list.
# An empty list is represented by [].
# clear() modifies the original list and returns None.
# Since friends2 is a separate copy, clearing friends_name does not empty friends2.
# Example: print(friends2) would still display the copied names.

friends_name.clear()  # Removes all elements from friends_name.
print(friends_name)  # Displays [] because the list is now empty.


# ============================================================
# IMPORTANT DIFFERENCES BETWEEN LIST METHODS
# ============================================================

# append()  -> Adds ONE element to the end of a list.
# extend()  -> Adds EACH element from another iterable.
# insert()  -> Adds an element at a specified index.
# remove()  -> Removes the FIRST occurrence of a specified VALUE.
# pop()     -> Removes and RETURNS an element using its INDEX.
# index()   -> Returns the index of the FIRST matching value.
# count()   -> Returns the number of occurrences of a value.
# sort()    -> Sorts the original list in ascending order by default.
# reverse() -> Reverses the existing order of elements.
# copy()    -> Creates a separate SHALLOW copy of a list.
# clear()   -> Removes every element from an existing list.


# ============================================================
# IMPORTANT — RETURN VALUES
# ============================================================

# The following methods modify the original list and return None:
# append(), extend(), insert(), remove(), sort(), reverse(), clear()

# The following methods return useful values:
# pop()   -> Returns the removed element.
# index() -> Returns the index position.
# count() -> Returns the number of occurrences.
# copy()  -> Returns a new shallow copy of the list.

# sorted() is a built-in function, NOT a list method.
# sorted() returns a new sorted list without changing the original list.

