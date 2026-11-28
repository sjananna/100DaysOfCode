# ============================================================
# PYTHON FOR LOOPS
# ============================================================

# WHAT IS A FOR LOOP?
#
# A for loop is a control flow statement in Python.
#
# It allows us to repeat a block of code by going through
# the elements of an iterable, one item at a time.
#
# An iterable is an object that Python can go through
# element by element.
#
# Examples of iterables:
# 1. Strings - sequences of characters
# 2. Lists - collections of items
# 3. Tuples - ordered, immutable collections
# 4. Dictionaries - collections of key-value pairs
# 5. Sets - collections of unique elements
# 6. Ranges - sequences of integers
#
# WHY DO WE USE FOR LOOPS?
#
# Imagine having 100 students in a classroom.
#
# If we want to print every student's name, we could
# write 100 individual print() statements.
#
# However, this would make our code unnecessarily long.
#
# A for loop allows us to perform the same operation
# on every student without repeating the code manually.
#
# For loops are commonly used for:
#
# 1. Printing items from lists.
# 2. Processing characters in strings.
# 3. Repeating operations a specific number of times.
# 4. Accessing elements using their indexes.
# 5. Performing calculations on collections.
# 6. Searching for specific information.
# 7. Filtering data using conditional statements.
# 8. Processing records in larger applications.
#
#
# ============================================================
# DIFFERENCE BETWEEN FOR, WHILE, AND IF
# ============================================================
#
# 1. IF STATEMENT
#
# An if statement checks whether a condition is True.
#
# If the condition is True, Python executes the
# corresponding block of code.
#
# An if statement does not automatically repeat itself.
#
# Example:
#
# age = 24
#
# if age >= 18:
#     print("You are an adult.")
#
# Python checks the condition once.
#
# Since 24 >= 18 is True, Python prints:
#
# You are an adult.
#
#
# 2. WHILE LOOP
#
# A while loop repeatedly executes a block of code
# as long as its condition remains True.
#
# Example:
#
# number = 1
#
# while number <= 5:
#     print(number)
#     number += 1
#
# Output:
# 1
# 2
# 3
# 4
# 5
#
# HOW DOES IT WORK?
#
# Python checks whether number <= 5.
#
# If True:
# - It prints the number.
# - It increases the number by 1.
# - It checks the condition again.
#
# The loop stops when number becomes 6.
#
# IMPORTANT:
# If we forget number += 1, the condition will
# remain True and the loop may run forever.
#
#
# 3. FOR LOOP
#
# A for loop goes through the items of an iterable.
#
# Example:
#
# for number in range(1, 6):
#     print(number)
#
# Output:
# 1
# 2
# 3
# 4
# 5
#
# Python automatically retrieves the next number
# from the range during each iteration.
#
# We do not need to write number += 1.
#
#
# MAIN DIFFERENCES:
#
# IF:
# Checks a condition and decides which code to execute.
#
# WHILE:
# Repeats code while a condition remains True.
#
# FOR:
# Repeats code by retrieving items from an iterable.
#
# IMPORTANT:
# A for loop and a while loop are repetition structures.
# An if statement is a conditional structure.
#
# We can also use if statements INSIDE loops.
#
#
# ============================================================
# IMPORTANT TERMINOLOGY
# ============================================================
#
# ITERATION:
# One complete execution of a loop's body.
#
# ITERABLE:
# An object whose elements can be accessed one at a time
# during iteration.
#
# LOOP VARIABLE:
# A variable that receives the current item during
# each iteration.
#
# LOOP BODY:
# The indented instructions executed during each iteration.
#
# INDEX:
# The position of an element in a sequence.
#
# Python uses zero-based indexing.
#
# This means the first item has index 0.
#
#
# ============================================================
# PART 1: FOR LOOP WITH STRINGS
# ============================================================

for letter in "Giraffe Academy":
    print(letter)  # Prints each character from G through y.

# EXPLANATION:
#
# A string is a sequence of characters.
#
# "Giraffe Academy" contains 15 characters,
# including the space between the words.
#
# The for loop goes through the string one character
# at a time.
#
# BREAKING DOWN THE SYNTAX:
#
# for:
# A Python keyword used to start a for loop.
#
# letter:
# The loop variable that stores the current character.
#
# in:
# A Python keyword that tells the loop which
# iterable to retrieve its values from.
#
# "Giraffe Academy":
# The string that Python iterates through.
#
# print(letter):
# Prints the character currently stored in letter.
#
# HOW PYTHON EXECUTES THIS CODE:
#
# First iteration:
# letter = "G"
# Python prints G.
#
# Second iteration:
# letter = "i"
# Python prints i.
#
# Third iteration:
# letter = "r"
# Python prints r.
#
# Python continues until the last character, "y".
#
# The space between Giraffe and Academy is also
# considered a character.
#
# Therefore, Python prints an empty-looking line
# when it reaches the space.
#
# TOTAL ITERATIONS: 15
#
# IMPORTANT:
# The variable name "letter" is not a Python keyword.
#
# We could also write:
#
# for character in "Giraffe Academy":
#     print(character)
#
# Both examples work exactly the same way.
#
# We use meaningful variable names to make code
# easier to understand.
#
# WHEN IS THIS USEFUL?
#
# - Checking characters in passwords.
# - Counting letters in words.
# - Searching for particular characters.
# - Processing text.
# - Validating user input.


# ============================================================
# PART 2: FOR LOOP WITH LISTS
# ============================================================

friends = ["Jim", "Karen", "Ruby", "Amy", "Rouge", "Robert", "Ronnie", "Rim"]

for friend in friends:
    print(friend)  # Prints every name from Jim through Rim.

# EXPLANATION:
#
# A list stores multiple items inside one variable.
#
# Our list contains eight strings representing names.
#
# The variable friends stores the entire list.
#
# The variable friend stores one name at a time.
#
# BREAKING DOWN THE SYNTAX:
#
# for friend in friends:
#
# for:
# Starts the loop.
#
# friend:
# The loop variable that receives each name.
#
# in:
# Tells Python to retrieve values from the list.
#
# friends:
# The list containing the eight names.
#
# HOW PYTHON EXECUTES THE LOOP:
#
# Iteration 1:
# friend = "Jim"
# Output: Jim
#
# Iteration 2:
# friend = "Karen"
# Output: Karen
#
# Iteration 3:
# friend = "Ruby"
# Output: Ruby
#
# Iteration 4:
# friend = "Amy"
# Output: Amy
#
# Iteration 5:
# friend = "Rouge"
# Output: Rouge
#
# Iteration 6:
# friend = "Robert"
# Output: Robert
#
# Iteration 7:
# friend = "Ronnie"
# Output: Ronnie
#
# Iteration 8:
# friend = "Rim"
# Output: Rim
#
# TOTAL ITERATIONS: 8
#
# IMPORTANT DIFFERENCE:
#
# When iterating through a string:
# Python retrieves one character at a time.
#
# When iterating through this list:
# Python retrieves one complete name at a time.
#
# For example, "Karen" is treated as one list item.
#
# Python does not separate Karen into individual letters
# because we are iterating through the list, not the string.
#
# WHEN IS THIS USEFUL?
#
# - Displaying customer names.
# - Processing student records.
# - Displaying product lists.
# - Reading collections of information.
# - Performing operations on each list item.


# ============================================================
# PART 3: FOR LOOP USING range()
# ============================================================

for index in range(10):
    print(index)  # Prints numbers from 0 through 9.

# EXPLANATION:
#
# range() is a built-in Python function.
#
# It creates a range object representing a sequence
# of integers.
#
# We commonly use range() when we want a loop
# to execute a particular number of times.
#
# SYNTAX:
#
# range(stop)
#
# When only one argument is provided:
#
# 1. Python starts at 0.
# 2. Python increases the number by 1.
# 3. Python stops BEFORE the specified number.
#
# In our example:
#
# range(10)
#
# Represents the numbers:
#
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#
# HOW PYTHON EXECUTES THE LOOP:
#
# Iteration 1: index = 0
# Iteration 2: index = 1
# Iteration 3: index = 2
# Iteration 4: index = 3
# Iteration 5: index = 4
# Iteration 6: index = 5
# Iteration 7: index = 6
# Iteration 8: index = 7
# Iteration 9: index = 8
# Iteration 10: index = 9
#
# TOTAL ITERATIONS: 10
#
# IMPORTANT CORRECTION:
#
# range(10) does NOT produce 1 through 9.
#
# It produces 0 through 9.
#
# The stopping number, 10, is excluded.
#
# ALSO REMEMBER:
#
# range() does not directly create a list.
#
# print(range(10))
#
# Output:
# range(0, 10)
#
# To display the numbers as a list:
#
# print(list(range(10)))
#
# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# WHEN IS THIS USEFUL?
#
# - Repeating a task a fixed number of times.
# - Running simulations.
# - Creating numbered sequences.
# - Performing repeated calculations.
# - Controlling the number of loop iterations.


# ============================================================
# PART 4: FOR LOOP WITH A START AND STOP VALUE
# ============================================================

for index in range(12, 20):
    print(index)  # Prints numbers from 12 through 19.

# EXPLANATION:
#
# range() can accept two arguments.
#
# SYNTAX:
#
# range(start, stop)
#
# start:
# The number where the sequence begins.
#
# stop:
# The number where the sequence stops.
# The stopping number itself is excluded.
#
# In our example:
#
# range(12, 20)
#
# start = 12
# stop = 20
#
# Python generates:
#
# 12, 13, 14, 15, 16, 17, 18, 19
#
# HOW PYTHON EXECUTES THE LOOP:
#
# Iteration 1: index = 12
# Iteration 2: index = 13
# Iteration 3: index = 14
# Iteration 4: index = 15
# Iteration 5: index = 16
# Iteration 6: index = 17
# Iteration 7: index = 18
# Iteration 8: index = 19
#
# TOTAL ITERATIONS: 8
#
# WHY DOES IT STOP AT 19?
#
# Because Python excludes the stopping number.
#
# To include 20, we would write:
#
# range(12, 21)
#
# IMPORTANT DIFFERENCE:
#
# range(10):
# Starts at 0 automatically.
#
# range(12, 20):
# Starts at the number we specify.
#
# WHEN IS THIS USEFUL?
#
# - Processing a specific numerical interval.
# - Creating custom counting sequences.
# - Selecting particular index positions.
# - Performing calculations within a range.


# ============================================================
# PART 5: COMBINING range(), len(), AND LIST INDEXING
# ============================================================

friends = ["Jim", "Karen", "Ruby", "Amy", "Rouge", "Robert", "Ronnie", "Rim"]

for index in range(len(friends)):
    print(friends[index])  # Prints names from Jim through Rim.

# EXPLANATION:
#
# This example combines three Python concepts:
#
# 1. len()
# 2. range()
# 3. List indexing
#
# Let's understand them individually.
#
#
# STEP 1: len(friends)
#
# len() is a built-in Python function.
#
# It returns the number of items in a collection.
#
# Our friends list contains eight names.
#
# Therefore:
#
# len(friends) = 8
#
#
# STEP 2: range(len(friends))
#
# Python evaluates the inner expression first.
#
# range(len(friends))
#
# becomes:
#
# range(8)
#
# The loop iterates over:
#
# 0, 1, 2, 3, 4, 5, 6, 7
#
# These numbers correspond to the indexes
# of our eight list items.
#
#
# STEP 3: friends[index]
#
# List indexing allows us to retrieve an item
# using its position.
#
# For example:
#
# friends[0] = "Jim"
# friends[1] = "Karen"
# friends[2] = "Ruby"
#
# Here, index is a variable containing the
# current index number.
#
# Therefore:
#
# print(friends[index])
#
# retrieves the name at the current position.
#
#
# HOW PYTHON EXECUTES THE COMPLETE LOOP:
#
# First iteration:
#
# index = 0
# print(friends[0])
# Output: Jim
#
# Second iteration:
#
# index = 1
# print(friends[1])
# Output: Karen
#
# Third iteration:
#
# index = 2
# print(friends[2])
# Output: Ruby
#
# Python continues until index becomes 7.
#
# Last iteration:
#
# index = 7
# print(friends[7])
# Output: Rim
#
# TOTAL ITERATIONS: 8
#
#
# WHY DO WE USE len(friends) INSTEAD OF range(8)?
#
# Imagine adding another friend:
#
# friends.append("Alex")
#
# Now the list contains nine names.
#
# If we hardcode:
#
# range(8)
#
# Python will still process only eight positions.
#
# However:
#
# range(len(friends))
#
# automatically adjusts to the current list length.
#
# This makes the code more flexible and maintainable.
#
# IMPORTANT:
#
# Hardcoding means manually placing a fixed value
# directly into the code.
#
# Hardcoding is not always wrong, but it can make
# programs less adaptable when data changes.
#
#
# WHEN IS THIS USEFUL?
#
# - Accessing list elements by their indexes.
# - Updating list elements at specific positions.
# - Comparing neighboring elements.
# - Processing lists whose lengths may change.
# - Performing index-based calculations.


# ============================================================
# PART 6: PRINTING INDEX NUMBERS INSTEAD OF LIST ITEMS
# ============================================================

friends = ["Jim", "Karen", "Ruby", "Amy", "Rouge", "Robert", "Ronnie", "Rim"]

for index in range(len(friends)):
    print(index)  # Prints index numbers from 0 through 7.

# EXPLANATION:
#
# This example is almost identical to Part 5.
#
# However, there is one important difference.
#
# Previously, we wrote:
#
# print(friends[index])
#
# Now we are writing:
#
# print(index)
#
#
# WHAT IS THE DIFFERENCE?
#
# print(index):
#
# Prints the current index number.
#
# print(friends[index]):
#
# Retrieves and prints the list item stored
# at the current index.
#
#
# HOW PYTHON EXECUTES THIS CODE:
#
# len(friends) returns 8.
#
# range(8) provides the numbers 0 through 7.
#
# The loop variable index receives each number.
#
# First iteration:
#
# index = 0
# Output: 0
#
# Second iteration:
#
# index = 1
# Output: 1
#
# Third iteration:
#
# index = 2
# Output: 2
#
# Python continues until index becomes 7.
#
# FINAL OUTPUT:
#
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
#
#
# IMPORTANT:
#
# The loop does not print any friend's name
# because we never access friends[index].
#
# We only print the index variable.
#
# REMEMBER:
#
# index = position number
#
# friends[index] = value stored at that position
#
# WHEN IS THIS USEFUL?
#
# - Displaying index positions.
# - Tracking positions while processing lists.
# - Debugging loops.
# - Identifying where particular elements are stored.


# ============================================================
# PART 7: COMBINING FOR LOOPS WITH IF-ELSE STATEMENTS
# ============================================================

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")

# EXPLANATION:
#
# This example combines:
#
# 1. A for loop.
# 2. The range() function.
# 3. An if statement.
# 4. An else statement.
# 5. The equality comparison operator (==).
#
#
# STEP 1: range(5)
#
# Python generates:
#
# 0, 1, 2, 3, 4
#
# The loop executes five times.
#
#
# STEP 2: if index == 0
#
# The == operator checks whether two values are equal.
#
# It returns a Boolean value:
#
# True or False.
#
# IMPORTANT:
#
# = is an assignment operator.
#
# == is a comparison operator.
#
# Example:
#
# index = 0
#
# Assigns 0 to index.
#
# index == 0
#
# Checks whether index equals 0.
#
#
# STEP 3: EXECUTING THE CONDITION
#
# First iteration:
#
# index = 0
#
# Python checks:
#
# 0 == 0
#
# Result: True
#
# Output: First Iteration
#
#
# Second iteration:
#
# index = 1
#
# Python checks:
#
# 1 == 0
#
# Result: False
#
# Output: Not First
#
#
# Third iteration:
#
# index = 2
#
# 2 == 0 is False.
#
# Output: Not First
#
#
# Fourth iteration:
#
# index = 3
#
# 3 == 0 is False.
#
# Output: Not First
#
#
# Fifth iteration:
#
# index = 4
#
# 4 == 0 is False.
#
# Output: Not First
#
#
# FINAL OUTPUT:
#
# First Iteration
# Not First
# Not First
# Not First
# Not First
#
#
# WHY DOES PYTHON CHECK THE CONDITION FIVE TIMES?
#
# Because the if-else statement is inside the for loop.
#
# Every time the loop executes, Python checks
# the condition again.
#
# The if block executes when the condition is True.
#
# The else block executes when the condition is False.
#
#
# IMPORTANT: INDENTATION
#
# Python uses indentation to determine which
# instructions belong to a block of code.
#
# The if-else statement belongs to the for loop.
#
# The print statements belong to their respective
# if and else blocks.
#
# WHEN IS THIS USEFUL?
#
# - Identifying the first iteration.
# - Applying different rules to different items.
# - Filtering information.
# - Checking values during repeated operations.
# - Processing items based on conditions.


# ============================================================
# PART 8: STARTING FROM A SPECIFIC LIST INDEX
# ============================================================

friends = ["Jim", "Karen", "Ruby", "Amy", "Rouge", "Robert", "Ronnie", "Rim"]

for index in range(2, len(friends)):
    print(friends[index])  # Ruby, Amy, Rouge, Robert, Ronnie, Rim

# EXPLANATION:
#
# In this example, we do not start from index 0.
#
# Instead, we start from index 2.
#
# SYNTAX:
#
# range(start, stop)
#
# Here:
#
# start = 2
#
# stop = len(friends)
#
#
# STEP 1: CALCULATING THE LIST LENGTH
#
# len(friends) returns 8.
#
# Therefore:
#
# range(2, len(friends))
#
# becomes:
#
# range(2, 8)
#
#
# STEP 2: GENERATING INDEX NUMBERS
#
# Python iterates over:
#
# 2, 3, 4, 5, 6, 7
#
# Notice that indexes 0 and 1 are skipped.
#
#
# STEP 3: ACCESSING LIST ELEMENTS
#
# friends[2] = "Ruby"
# friends[3] = "Amy"
# friends[4] = "Rouge"
# friends[5] = "Robert"
# friends[6] = "Ronnie"
# friends[7] = "Rim"
#
#
# HOW PYTHON EXECUTES THE LOOP:
#
# First iteration:
#
# index = 2
# print(friends[2])
# Output: Ruby
#
# Second iteration:
#
# index = 3
# print(friends[3])
# Output: Amy
#
# Third iteration:
#
# index = 4
# print(friends[4])
# Output: Rouge
#
# Python continues until index becomes 7.
#
# Last iteration:
#
# index = 7
# print(friends[7])
# Output: Rim
#
#
# FINAL OUTPUT:
#
# Ruby
# Amy
# Rouge
# Robert
# Ronnie
# Rim
#
# TOTAL ITERATIONS: 6
#
#
# WHY DOES IT START WITH RUBY?
#
# Because Ruby is stored at index 2.
#
# Remember:
#
# Index 0 = Jim
# Index 1 = Karen
# Index 2 = Ruby
#
# Python begins at index 2 because we explicitly
# provided 2 as the starting argument.
#
#
# WHEN IS THIS USEFUL?
#
# - Skipping the first few items of a list.
# - Processing data from a particular position.
# - Working with selected sections of collections.
# - Ignoring elements that have already been processed.


# ============================================================
# PART 9: USING range() WITH START, STOP, AND STEP
# ============================================================

friends = ["Jim", "Karen", "Ruby", "Amy", "Rouge"]

for index in range(0, len(friends), 2):
    print(friends[index])  # Jim, Ruby, Rouge

# EXPLANATION:
#
# This example introduces the third argument
# of the range() function.
#
# SYNTAX:
#
# range(start, stop, step)
#
#
# START:
#
# The number where the sequence begins.
#
# STOP:
#
# The stopping boundary, which is excluded.
#
# STEP:
#
# The amount by which the number changes
# during each iteration.
#
#
# STEP 1: CALCULATING THE LENGTH
#
# Our friends list contains five names.
#
# len(friends) returns 5.
#
# Therefore:
#
# range(0, len(friends), 2)
#
# becomes:
#
# range(0, 5, 2)
#
#
# STEP 2: UNDERSTANDING THE ARGUMENTS
#
# start = 0
#
# Python begins at index 0.
#
# stop = 5
#
# Python stops before index 5.
#
# step = 2
#
# Python increases the index by 2
# after each iteration.
#
#
# STEP 3: GENERATING THE INDEXES
#
# Python iterates over:
#
# 0, 2, 4
#
# It skips indexes 1 and 3.
#
#
# STEP 4: ACCESSING THE LIST ITEMS
#
# friends[0] = "Jim"
#
# friends[2] = "Ruby"
#
# friends[4] = "Rouge"
#
#
# HOW PYTHON EXECUTES THE LOOP:
#
# First iteration:
#
# index = 0
# print(friends[0])
# Output: Jim
#
# Python advances by 2.
#
# Second iteration:
#
# index = 2
# print(friends[2])
# Output: Ruby
#
# Python advances by 2.
#
# Third iteration:
#
# index = 4
# print(friends[4])
# Output: Rouge
#
# Python advances by 2 again.
#
# The next number would be 6.
#
# However, 6 is beyond the stopping boundary of 5.
#
# Therefore, the loop ends.
#
#
# FINAL OUTPUT:
#
# Jim
# Ruby
# Rouge
#
# TOTAL ITERATIONS: 3
#
#
# IMPORTANT:
#
# The step argument controls how the sequence
# progresses.
#
# range(0, 5, 1):
#
# 0, 1, 2, 3, 4
#
# range(0, 5, 2):
#
# 0, 2, 4
#
# range(0, 5, 3):
#
# 0, 3
#
# A positive step moves forward.
#
# A negative step can move backward.
#
# Example:
#
# range(4, -1, -1)
#
# Produces:
#
# 4, 3, 2, 1, 0
#
#
# WHEN IS THIS USEFUL?
#
# - Accessing every second item.
# - Skipping elements at regular intervals.
# - Processing alternating positions.
# - Creating custom numerical sequences.
# - Iterating backward through a collection.


# ============================================================
# FINAL SUMMARY - WHAT WE LEARNED
# ============================================================
#
# 1. FOR LOOP
#
# Repeats a block of code for each item in an iterable.
#
#
# 2. FOR LOOP WITH STRINGS
#
# for letter in "Python":
#
# Retrieves one character at a time.
#
#
# 3. FOR LOOP WITH LISTS
#
# for friend in friends:
#
# Retrieves one complete list item at a time.
#
#
# 4. range(stop)
#
# range(10)
#
# Produces numbers from 0 through 9.
#
#
# 5. range(start, stop)
#
# range(12, 20)
#
# Produces numbers from 12 through 19.
#
#
# 6. len()
#
# Returns the number of items in a collection.
#
#
# 7. range(len(friends))
#
# Allows us to iterate over the valid index
# positions of the friends list.
#
#
# 8. print(index)
#
# Prints the current index number.
#
#
# 9. print(friends[index])
#
# Prints the list item at the current index.
#
#
# 10. FOR LOOP WITH IF-ELSE
#
# Allows Python to make decisions during
# individual iterations.
#
#
# 11. range(2, len(friends))
#
# Starts processing the list from index 2.
#
#
# 12. range(0, len(friends), 2)
#
# Processes every second index, starting at 0.
#
#
# ============================================================
# IMPORTANT RULES TO REMEMBER
# ============================================================
#
# RULE 1:
# Python list indexing starts at 0.
#
# RULE 2:
# The stop argument of range() is excluded.
#
# RULE 3:
# The loop variable changes automatically
# as Python retrieves each new item.
#
# RULE 4:
# A for loop does not require us to manually
# increment the loop variable.
#
# RULE 5:
# len() returns the number of items.
#
# RULE 6:
# range() represents a sequence of integers.
#
# RULE 7:
# An index is a position, not the actual list value.
#
# RULE 8:
# Indentation determines which statements
# belong to the loop.
#
# RULE 9:
# A for loop can contain conditional statements.
#
# RULE 10:
# Use meaningful variable names to make
# your programs easier to understand.
#
#
# ============================================================
# END OF PYTHON FOR LOOP NOTES
# ============================================================