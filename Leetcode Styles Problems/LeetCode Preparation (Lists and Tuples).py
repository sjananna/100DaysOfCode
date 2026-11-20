# ============================================================
# 100 DAYS OF CODE — PYTHON LISTS AND TUPLES
# LeetCode-Style Coding Challenges
# Difficulty: Beginner to Intermediate
# Topic: Lists, Tuples, Mutability, Indexing, Loops, Functions
# ============================================================


# ============================================================
# PROBLEM 1: ONLINE SHOPPING CART
# Difficulty: Easy
# Concepts: Lists, append(), remove(), indexing, len()
# ============================================================

# Real-World Scenario:
# You are developing a shopping cart for an online store.
# Customers need to add, remove, and replace products.
#
# Initial Data:
# cart = ["Laptop", "Mouse", "Keyboard"]
#
# Your Tasks:
# 1. Add "Headphones" to the shopping cart.
# 2. Remove "Mouse" from the cart.
# 3. Replace "Keyboard" with "Mechanical Keyboard".
# 4. Count the total number of products.
# 5. Print the final shopping cart.
#
# Expected Output:
# Final Cart: ['Laptop', 'Mechanical Keyboard', 'Headphones']
# Total Products: 3
#
# Thinking Question:
# Why is a list more suitable than a tuple for a shopping cart?
# What happens if you try to use append() on a tuple?
#
# Write Your Solution Below:

cart = ["Laptop", "Mouse", "Keyboard"]
cart.append("Headphones")
print(cart)

cart.remove("Mouse")
print(cart)

cart[1] = "Mechanical Keyboard"
print(cart)

print(len(cart))

print(cart)



# ============================================================
# PROBLEM 2: BANK TRANSACTION HISTORY
# Difficulty: Easy
# Concepts: Lists, append(), sum(), max(), min()
# ============================================================

# Real-World Scenario:
# You are building a banking application that records transactions.
# Positive numbers represent deposits.
# Negative numbers represent withdrawals.
#
# Initial Data:
# transactions = [500, -200, 1000, -150, 300]
#
# Your Tasks:
# 1. Add a deposit of $700.
# 2. Add a withdrawal of $250.
# 3. Calculate the net change in the account balance.
# 4. Find the largest deposit.
# 5. Find the largest withdrawal amount.
#
# Expected Output:
# Transactions: [500, -200, 1000, -150, 300, 700, -250]
# Net Change: 1900
# Largest Deposit: 1000
# Largest Withdrawal: 250
#
# Thinking Question:
# Why is a list useful for storing an ongoing transaction history?
# Why would a real banking application also need a database?
#
# Write Your Solution Below:

transactions = [500, -200, 1000, -150, 300]

transactions.append(700)  # Adds a deposit of $700.
print(transactions)

transactions.append(-250)  # Adds a withdrawal of $250.
print(transactions)

print(sum(transactions))  # Calculates the net change: 1900.

print(max(transactions))  # Finds the largest deposit: 1000.

print(abs(min(transactions)))  # Finds the largest withdrawal amount: 250.

# ============================================================
# PROBLEM 2 - LESSONS LEARNED
# ============================================================

# 1. append() adds a new element to the end of a list.
# 2. remove() removes the first occurrence of a specified value.
# 3. Positive numbers represent deposits.
# 4. Negative numbers represent withdrawals.
# 5. sum() calculates the total of all numeric elements.
# 6. max() returns the largest value in a list.
# 7. min() returns the smallest value in a list.
# 8. abs() returns the absolute value of a number.
#
# IMPORTANT:
# To record a new withdrawal, use append() with a negative number.
# Example: transactions.append(-250)
#
# To find the largest withdrawal amount:
# abs(min(transactions))
#
# NOTE:
# This works when the list contains negative withdrawals.
# In a real application, filter withdrawals first because a list
# containing only deposits has no withdrawal to report.
#
# LESSON:
# Removing a transaction is not the same as recording a withdrawal.
# A withdrawal should be added as a new transaction.



# ============================================================
# PROBLEM 3: GPS LOCATION TRACKING
# Difficulty: Easy
# Concepts: Tuples, indexing, unpacking, immutability
# ============================================================

# Real-World Scenario:
# You are developing a GPS navigation application.
# A location is represented using latitude and longitude.
#
# Initial Data:
# toronto = (43.6532, -79.3832)
#
# Your Tasks:
# 1. Print the latitude.
# 2. Print the longitude.
# 3. Unpack the tuple into two separate variables.
# 4. Print the coordinates in a readable format.
#
# Expected Output:
# Latitude: 43.6532
# Longitude: -79.3832
# Location: Toronto
# Coordinates: 43.6532, -79.3832
#
# Extra Challenge:
# Try changing the first element of the tuple:
#
# toronto[0] = 50.0000
#
# What error does Python produce?
#
# Thinking Question:
# Why might a tuple be useful for representing one GPS location?
# How could you represent a new location without modifying the tuple?
#
# Write Your Solution Below:

toronto = (43.6532, -79.3832)
print(toronto[0])

print(toronto[1])

latitude, longitude = toronto
print(latitude, longitude)

latitude, longitude = toronto
print(latitude, longitude)

# ============================================================
# NOTES ON TUPLE UNPACKING AND ABSOLUTE VALUE
# ============================================================

# 1. TUPLE UNPACKING:
# Unpacking means assigning elements of a tuple to separate variables.
# We use commas (,) to separate the variable names.
# Python automatically assigns the values according to their order.
# We do not need to specify indexes [0] or [1] when unpacking.
#
# MY MISTAKE:
# I used latitude[0] and longitude[1] instead of just variable names.
# This tells Python to assign values to indexed elements inside
# latitude and longitude rather than unpack into new variables.
# If those variables are undefined, Python raises a NameError.
#
# IMPORTANT:
# Indexing = Accessing an element using its position.
# Unpacking = Assigning multiple elements to separate variables.
# Unpacking does not modify the original tuple.


# 2. ABSOLUTE VALUE — abs():
# abs() is a built-in Python function that returns the absolute value.
# Absolute value represents a number's distance from zero.
# It removes the negative sign from negative numbers.
# Positive numbers remain positive, and zero remains zero.
#
# WHY DO WE USE abs()?
# We use it when we need the magnitude of a number
# without considering whether it is positive or negative.
#
# REAL-WORLD EXAMPLE:
# In banking, a withdrawal may be represented by -250.
# The absolute value is 250, representing the withdrawal amount.
#
# IMPORTANT FOR GPS:
# Negative latitude represents South.
# Negative longitude represents West.
# Using abs() removes the negative sign and loses direction information.
# Therefore, abs() should not be used when preserving GPS coordinates.
#
# REMEMBER:
# abs() does not modify the original variable.
# It returns a new nonnegative value.



# ============================================================
# PROBLEM 4: EMPLOYEE IDENTIFICATION SYSTEM
# Difficulty: Easy
# Concepts: Tuples, indexing, unpacking
# ============================================================

# Real-World Scenario:
# You are developing an employee management system.
# Each employee has an ID, name, and job title.
#
# Initial Data:
# employee = (1025, "Sarah", "Data Analyst")
#
# Your Tasks:
# 1. Print the employee ID.
# 2. Print the employee name.
# 3. Print the job title.
# 4. Unpack the tuple into three separate variables.
# 5. Display the employee information.
#
# Expected Output:
# Employee ID: 1025
# Employee Name: Sarah
# Position: Data Analyst
#
# Thinking Question:
# What happens if an employee receives a promotion?
# Would a tuple always be the best choice for employee records?
# When might a dictionary be more convenient?
#
# Write Your Solution Below:

employee = (1025, "Sarah", "Data Analyst")
employee_ID = employee[0]
print(employee_ID)

employee_name = employee[1]
print(employee_name)

job_title = employee[2]
print(job_title)

employee_ID, employee_name, job_title = employee
print(str(employee_ID) + ", " +employee_name + ", "  +job_title)

# ============================================================
#  NOTES ON EMPLOYEE IDENTIFICATION SYSTEM
# ============================================================

# 1. TUPLE INDEXING:
# We use square brackets [] to access individual tuple elements.
# Indexing starts at 0, not 1.
# Indexing allows us to retrieve specific values from a tuple.

# 2. TUPLE UNPACKING:
# We can assign multiple tuple elements to separate variables.
# We separate the variable names using commas.
# Python assigns the values according to their positions.
# Unpacking is useful when we need all the values at once.

# 3. MY PREVIOUS MISTAKE:
# I tried using int(employee_ID) while concatenating strings.
# However, employee_ID was already an integer.
# int() does not convert an integer into a string.
# Using + between an integer and a string raises a TypeError.

# 4. WHAT I LEARNED:
# str() converts an integer into a string.
# This allows us to concatenate it with other strings using +.
# Tuple unpacking does not change the original data types.

# 5. IMPORTANT DIFFERENCE:
# Indexing retrieves individual elements using their positions.
# Unpacking assigns multiple elements to variables simultaneously.

# 6. REAL-WORLD APPLICATION:
# Tuples can group related employee information into one record.
# Indexing allows us to retrieve specific employee details.
# Unpacking makes it easier to work with all the fields.
# A tuple is useful for a fixed snapshot of employee information.
# If employee details change frequently, a dictionary may be better.

# REMEMBER:
# Lists are mutable, while tuples are immutable.
# We can access tuple elements but cannot replace them directly.


# ============================================================
# PROBLEM 5: UNIVERSITY STUDENT RECORDS
# Difficulty: Easy to Medium
# Concepts: Lists containing tuples, loops, indexing
# ============================================================

# Real-World Scenario:
# You are building a student management application.
# Each student has an ID, name, and grade.
#
# Initial Data:
# students = [
#     (101, "Alice", 85),
#     (102, "Bob", 92),
#     (103, "Charlie", 78),
#     (104, "Diana", 95)
# ]
#
# Your Tasks:
# 1. Print all student names.
# 2. Find the student with the highest grade.
# 3. Add a new student: (105, "Emma", 88).
# 4. Count the total number of students.
# 5. Print the names of students scoring above 90.
#
# Expected Output:
# Student Names:
# Alice
# Bob
# Charlie
# Diana
#
# Highest Grade: Diana - 95
# Total Students: 5
#
# Students Above 90:
# Bob
# Diana
#
# Thinking Question:
# Why is the outer collection a list?
# Why are individual student records represented as tuples?
# What would change if each student record were a list?
#
# Write Your Solution Below:

students = [
    (101, "Alice", 85),
    (102, "Bob", 92),
    (103, "Charlie", 78),
    (104, "Diana", 95)
]

Stu_Name = students[0][1], students[1][1], students[2][1], students[3][1]
print(Stu_Name)

Stu_Grade = students[0][2], students[1][2], students[2][2], students[3][2]
Highest_Grade = max(Stu_Grade)
Highest_index = Stu_Grade.index(Highest_Grade)
print("Highest Grade:", Stu_Name[Highest_index], "-", Highest_Grade)

students.append((105, "Emma", 88))
print(students)

Stu_Len = len(students)
print(Stu_Len)



for student in students:
    if student[2] > 90:
        print(student[1])

# ============================================================
# PROBLEM 5: UNIVERSITY STUDENT RECORDS
# MISTAKES, SOLUTIONS, AND LESSONS LEARNED
# ============================================================

# 1. UNDERSTANDING A LIST CONTAINING TUPLES
#
# Initially, I needed to understand how to access information
# when multiple tuples are stored inside a single list.
#
# The outer list contains all student records.
# Each tuple represents one student and contains three values:
# Student ID, Student Name, and Student Grade.
#
# The first index selects a student from the list.
# The second index selects specific information from that student's tuple.
#
# WHAT I LEARNED:
# Double indexing allows us to access elements inside nested collections.
# Lists can contain tuples, and each tuple counts as one list element.


# 2. FINDING THE STUDENT WITH THE HIGHEST GRADE
#
# WHERE I GOT STUCK:
# I successfully extracted student names and grades into
# separate collections and used max() to find the highest grade.
#
# However, max() returned only the highest numerical value.
# I did not know how to retrieve the corresponding student's name.
#
# WHY:
# max() identifies the largest value but does not automatically
# retrieve related information from another collection.
#
# SOLUTION LEARNED:
# First, find the highest grade using max().
# Next, use index() to identify the position of that grade.
# Finally, use the same position to retrieve the student's name.
#
# WHAT I LEARNED:
# max() returns the highest value.
# index() returns the position of the first matching value.
# Indexing retrieves an element from a specific position.
#
# IMPORTANT:
# This approach works because student names and grades
# are stored in the same order.
#
# If multiple students share the highest grade,
# index() identifies only the first matching position.


# 3. PRINTING THE HIGHEST GRADE WITH THE STUDENT'S NAME
#
# WHERE I GOT STUCK:
# I tried displaying a text label and a variable together
# without separating them correctly.
#
# WHY:
# Python requires valid syntax when combining text and variables.
#
# SOLUTION LEARNED:
# We can separate values inside print() using commas.
# Python automatically inserts spaces between the values.
#
# WHAT I LEARNED:
# Commas allow print() to display strings and integers together.
# Using + for string concatenation requires compatible string types.
# F-strings provide another way to format text and variables.
#
# IMPORTANT:
# Python variable names are case-sensitive.
# A variable written with a capital letter is different
# from the same name written with a lowercase letter.


# 4. ADDING A NEW STUDENT TO THE LIST
#
# MY MISTAKE:
# I tried using add with an assignment operator
# instead of calling the appropriate list method.
#
# WHY:
# I confused the methods used by lists and sets.
# Lists do not have an add() method.
#
# SOLUTION LEARNED:
# append() adds a new element to the end of a list.
# add() is used to add elements to a set.
#
# WHAT I LEARNED:
# A list can contain tuples as individual elements.
# Adding a tuple to a list does not change the existing tuples.
#
# IMPORTANT:
# The parentheses used to call a method are different
# from the parentheses used to group tuple values.
#
# Method calls use parentheses to pass arguments.
# Tuples group related values into one record.


# 5. COUNTING THE TOTAL NUMBER OF STUDENTS
#
# WHAT I LEARNED:
# len() counts the number of elements in a collection.
#
# When a list contains tuples, each tuple counts as one element.
# Python does not count every individual value inside the tuples.
#
# For example:
# Five student tuples represent five students.
# Each student may contain three pieces of information,
# but the outer list still contains only five elements.
#
# IMPORTANT:
# len() returns an integer.
# It does not modify the original collection.


# 6. PRINTING STUDENTS WHO SCORED ABOVE 90
#
# WHERE I GOT STUCK:
# I needed to retrieve multiple student names based on their grades.
# Previously, I was manually accessing each student's information.
#
# WHY:
# Manual indexing works for a small number of records,
# but becomes inefficient when working with many students.
#
# SOLUTION LEARNED:
# A for loop examines each student tuple one at a time.
# An if statement checks whether the student's grade
# satisfies the required condition.
#
# If the grade is greater than 90,
# Python displays that student's name.
#
# WHAT I LEARNED:
# A for loop repeats instructions for every element.
# The loop variable temporarily represents the current student tuple.
# Python automatically assigns each tuple to the loop variable.
#
# The grade is stored at index 2.
# The student's name is stored at index 1.
#
# The if statement checks the grade before printing the name.
#
# IMPORTANT:
# Greater than (>) excludes the boundary value.
# Greater than or equal to (>=) includes the boundary value.
#
# A student scoring exactly 90 does not satisfy a condition
# requiring a grade strictly greater than 90.


# ============================================================
# FINAL LESSONS FROM PROBLEM 5
# ============================================================

# 1. A list can store multiple tuples representing related records.
#
# 2. Double indexing accesses information inside nested collections.
#
# 3. max() finds the highest value, not its corresponding name.
#
# 4. index() finds the position of a value within a collection.
#
# 5. Related collections must maintain matching positions
#    when we use an index from one to access another.
#
# 6. append() adds new records to a list.
#
# 7. len() counts the elements in the outer collection.
#
# 8. A for loop allows us to process multiple records automatically.
#
# 9. An if statement filters records based on specific conditions.
#
# 10. Combining loops, conditions, and indexing allows us
#     to search and filter information in real-world applications.
#
# MOST IMPORTANT LESSON:
# Instead of manually accessing every student,
# I can use loops to process an entire collection.
# I also learned that finding a value and finding
# the position of that value are two different operations.



# ============================================================
# PROBLEM 6: E-COMMERCE PRODUCT INVENTORY
# Difficulty: Medium
# Concepts: Lists, tuples, searching, loops
# ============================================================

# Real-World Scenario:
# You are building an inventory management system.
# Each product has an ID, name, and price.
#
# Initial Data:
# products = [
#     (101, "Laptop", 1200),
#     (102, "Mouse", 25),
#     (103, "Keyboard", 75),
#     (104, "Monitor", 300)
# ]
#
# Your Tasks:
# 1. Display all products.
# 2. Find products costing more than $100.
# 3. Find the most expensive product.
# 4. Add a new product: (105, "Webcam", 80).
# 5. Print the updated inventory.
#
# Expected Output:
# Products Above $100:
# Laptop
# Monitor
#
# Most Expensive Product:
# Laptop - $1200
#
# Total Products: 5
#
# Thinking Question:
# Why can we append a new tuple to the list?
# Can we directly modify the price inside an existing tuple?
# What data structure might be better for frequently changing prices?
#
# Write Your Solution Below:

products = [
    (101, "Laptop", 1200),
    (102, "Mouse", 25),
    (103, "Keyboard", 75),
    (104, "Monitor", 300)
]

print(products)


for product in products:
    if product[2] > 100:
        print(product[1])


Product_Price = products[0][2], products[1][2], products[2][2], products[3][2]
Exp_Product = max(Product_Price)
Max_Index = Product_Price.index(Exp_Product)
Product_Name = products[0][1], products[1][1], products[2][1], products[3][1]
print(Product_Name[Max_Index], "-"+" $" ,Exp_Product)


products.append((105, "Webcam", 80))
print(products)


# ======================================================================
# DAY 010 - PROBLEM 6: E-COMMERCE PRODUCT INVENTORY
# TOPIC: LISTS, TUPLES, INDEXING, LOOPS, MAX(), APPEND(), AND F-STRINGS
# ======================================================================


# ======================================================================
# 1. UNDERSTANDING THE PRODUCT INVENTORY
# ======================================================================

# The products collection is a list containing multiple tuples.
#
# Each tuple represents one product with three pieces of information:
#
# Index [0] = Product ID
# Index [1] = Product Name
# Index [2] = Product Price
#
# IMPORTANT:
# Lists are mutable, meaning we can add, remove, or replace elements.
# Tuples are immutable, meaning their individual elements cannot
# be modified after creation.
#
# However, we can add new tuples to the outer list.
#
# WHAT I LEARNED:
# A list of tuples is useful for storing structured information,
# such as products, student records, employee details, and transactions.


# ======================================================================
# 2. DISPLAYING ALL PRODUCTS
# ======================================================================

# I successfully displayed the complete inventory using print().
#
# WHAT I LEARNED:
# Printing the entire list displays all the tuples inside it.
#
# However, if I want to display individual product information
# in a more readable format, I can use a for loop.
#
# A for loop processes each product automatically.
#
# This is particularly useful when working with hundreds
# or thousands of products.


# ======================================================================
# 3. FINDING PRODUCTS COSTING MORE THAN $100
# ======================================================================

# MY SOLUTION WAS CORRECT.
#
# I used a for loop to examine each product.
# I used an if statement to check whether its price exceeded $100.
#
# HOW THE LOOP WORKS:
#
# The loop variable temporarily represents one product tuple.
#
# During the first iteration, it represents the laptop.
# During the second iteration, it represents the mouse.
# During the third iteration, it represents the keyboard.
# During the fourth iteration, it represents the monitor.
#
# The loop continues until every product has been examined.
#
# HOW THE CONDITION WORKS:
#
# Index [2] retrieves the product's price.
# The greater-than operator checks whether the price exceeds 100.
#
# If the condition is True:
# Python displays the product name stored at index [1].
#
# If the condition is False:
# Python skips the print statement.
#
# EXPECTED RESULT:
# Laptop
# Monitor
#
# IMPORTANT:
# A for loop allows us to retrieve information automatically
# without manually accessing each product.
#
# This is called iterating through a collection.


# ======================================================================
# 4. FINDING THE MOST EXPENSIVE PRODUCT - MY ORIGINAL APPROACH
# ======================================================================

# WHAT I DID CORRECTLY:
#
# I manually extracted all product prices into a separate collection.
#
# I used max() to identify the highest price.
#
# I used index() to identify the position of that price.
#
# I then used the position to retrieve the corresponding product name.
#
# This approach was logically correct.
#
# WHAT I LEARNED:
#
# max() returns the largest value in a collection.
#
# index() returns the position of the first matching value.
#
# The same index can be used to retrieve related information
# when two collections contain elements in matching positions.


# ======================================================================
# 5. MY INDEXING MISTAKE
# ======================================================================

# WHERE I MADE A MISTAKE:
#
# While creating the collection of product names,
# I accidentally used index [2] for the fourth product.
#
# WHY THIS WAS WRONG:
#
# Index [1] represents the product name.
# Index [2] represents the product price.
#
# Therefore, I accidentally retrieved the monitor's price
# instead of its name.
#
# WHY MY PROGRAM STILL DISPLAYED THE CORRECT RESULT:
#
# The laptop was the most expensive product.
# Its name was stored correctly at position 0.
#
# Therefore, my mistake did not affect the displayed result.
#
# However, if the monitor had been the most expensive product,
# the program would have displayed its price instead of its name.
#
# WHAT I LEARNED:
#
# A program can produce the expected output even when
# another part of its logic contains an error.
#
# I should check the entire collection rather than assuming
# the program is correct because one result looks correct.
#
# IMPORTANT:
# Always verify which index represents the required information.


# ======================================================================
# 6. A BETTER APPROACH: FINDING THE MOST EXPENSIVE PRODUCT USING A LOOP
# ======================================================================

# Instead of manually extracting every product price,
# I can use a for loop to examine the products automatically.
#
# This approach is more efficient to write and easier to maintain.
#
# STEP 1: INITIALIZE THE MOST EXPENSIVE PRODUCT
#
# I start by assigning the first product tuple to a variable
# named most_expensive.
#
# This does not mean the first product is definitely the most expensive.
#
# It simply provides an initial product for comparison.
#
# At this stage, Python temporarily considers the first product
# to be the most expensive product found so far.


# STEP 2: ITERATE THROUGH THE PRODUCTS
#
# A for loop examines every product tuple in the list.
#
# During each iteration, the loop variable refers
# to the current product.
#
# Python automatically moves from one product to the next.
#
# I do not need to write separate indexing expressions
# for every product.


# STEP 3: COMPARE PRODUCT PRICES
#
# The if statement compares two prices:
#
# Current product price = product[2]
#
# Highest price found so far = most_expensive[2]
#
# The condition checks whether the current product
# costs more than the most expensive product found so far.
#
# If the condition is True:
# Python updates most_expensive to reference the current product.
#
# If the condition is False:
# Python keeps the existing most_expensive value.
#
# IMPORTANT:
# The comparison uses > rather than >=.
#
# If two products share the highest price,
# the first one encountered remains the selected product.


# STEP 4: UNDERSTANDING THE VARIABLE UPDATE
#
# When most_expensive is assigned the current product,
# the variable now refers to that entire tuple.
#
# It does not store only the product's price.
#
# It stores the product record containing:
#
# Product ID
# Product Name
# Product Price
#
# This is extremely useful because I can retrieve
# the product's name and price from the same tuple.
#
# I do not need to create separate collections
# for product names and product prices.


# STEP 5: UNDERSTANDING THE COMPARISON PROCESS
#
# Initial most expensive product:
# Laptop - $1200
#
# First iteration:
# Compare Laptop ($1200) with Laptop ($1200).
# The current price is not greater.
# Keep Laptop.
#
# Second iteration:
# Compare Mouse ($25) with Laptop ($1200).
# Mouse is cheaper.
# Keep Laptop.
#
# Third iteration:
# Compare Keyboard ($75) with Laptop ($1200).
# Keyboard is cheaper.
# Keep Laptop.
#
# Fourth iteration:
# Compare Monitor ($300) with Laptop ($1200).
# Monitor is cheaper.
# Keep Laptop.
#
# FINAL RESULT:
# Laptop - $1200
#
# IMPORTANT:
# If a more expensive product appeared later in the list,
# Python would automatically update most_expensive.
#
# This means the solution works regardless of the
# order in which the products appear.


# ======================================================================
# 7. WHY THE LOOP APPROACH IS BETTER THAN MANUAL INDEXING
# ======================================================================

# MY ORIGINAL APPROACH:
#
# I manually retrieved the prices of all four products.
# I manually retrieved the names of all four products.
# I used max() and index() to connect the highest price
# with the corresponding product name.
#
# THE PROBLEM:
#
# If the inventory contained 1,000 products,
# I would need to write many additional indexing expressions.
#
# If new products were added later,
# my manually created collections would not update automatically.
#
# THE IMPROVED APPROACH:
#
# A for loop examines every product in the list.
#
# It works with four products, 100 products,
# or even thousands of products.
#
# It also keeps the product name and price together
# inside the original tuple.
#
# WHAT I LEARNED:
#
# Avoid manually retrieving individual elements
# when the same task can be completed using iteration.
#
# Loops make programs easier to maintain and expand.
#
# IMPORTANT:
# The loop solution does not require creating
# separate collections of names and prices.
#
# It keeps track of the most expensive product directly.


# ======================================================================
# 8. UNDERSTANDING F-STRINGS
# ======================================================================

# An f-string is a formatted string literal.
#
# It allows us to insert variables and expressions
# directly into a string.
#
# An f-string begins with the letter f immediately
# before the opening quotation mark.
#
# Curly braces {} are used to insert values.
#
# Python evaluates the expression inside each pair
# of curly braces and inserts its result into the text.
#
# In this problem:
#
# most_expensive[1] retrieves the product name.
#
# most_expensive[2] retrieves the product price.
#
# The dollar sign is ordinary text placed before
# the expression containing the price.
#
# EXPECTED OUTPUT:
# Laptop - $1200
#
# IMPORTANT:
# The letter f must appear before the quotation marks.
#
# Without the f prefix, Python does not evaluate
# the expressions inside the curly braces.


# ======================================================================
# 9. MY PRINT FORMATTING MISTAKE
# ======================================================================

# WHERE I GOT STUCK:
#
# I wanted to display the product name and price
# with a dollar sign immediately before the number.
#
# However, my output contained an unwanted space
# between the dollar sign and the price.
#
# WHY THIS HAPPENED:
#
# By default, print() inserts a space between
# arguments separated by commas.
#
# The dollar sign and the price were passed
# as separate arguments.
#
# Therefore, Python inserted an automatic space.
#
# WHAT I LEARNED:
#
# Commas in print() separate arguments.
#
# The + operator joins strings without adding spaces.
#
# However, + cannot directly concatenate
# a string with an integer.
#
# str() can convert an integer into a string.
#
# F-strings allow strings and numbers to be combined
# without manually converting integers using str().
#
# ANOTHER USEFUL CONCEPT:
#
# The sep parameter controls the separator
# inserted between print() arguments.
#
# By default, sep is a single space.
#
# Setting sep to an empty string removes
# the automatic spaces.
#
# MY PREFERRED SOLUTION:
#
# Use an f-string for displaying product names and prices.
#
# F-strings make the output easier to read
# and give me greater control over formatting.


# ======================================================================
# 10. ADDING A NEW PRODUCT - MY APPEND() MISTAKE
# ======================================================================

# WHERE I MADE A MISTAKE:
#
# I initially tried to pass the product ID,
# product name, and product price as three
# separate arguments to append().
#
# WHY THIS WAS WRONG:
#
# The append() method accepts exactly one argument.
#
# Even though a product contains three values,
# those values must be grouped into one tuple.
#
# SOLUTION LEARNED:
#
# Create one tuple containing the product information.
#
# Pass that tuple as the single argument to append().
#
# UNDERSTANDING THE PARENTHESES:
#
# Outer parentheses belong to the method call.
#
# Inner parentheses group the product information
# into a single tuple.
#
# WHAT I LEARNED:
#
# append() adds one element to the end of a list.
#
# That element can be a string, integer, tuple,
# list, or another Python object.
#
# Adding a tuple increases the outer list's length by one.
#
# The original product tuples remain unchanged.


# ======================================================================
# 11. IMPORTANT DETAIL: WHEN THE INVENTORY IS UPDATED
# ======================================================================

# In my program, I searched for the most expensive product
# before adding the new webcam.
#
# Therefore, the search examined only the original products.
#
# After adding the webcam, the inventory contained five products.
#
# If I wanted to include the webcam in the search,
# I could perform the search after updating the inventory.
#
# IMPORTANT:
# The order in which Python executes instructions matters.
#
# Python normally executes statements from top to bottom.
#
# A result calculated before an update does not automatically
# recalculate itself when the original list changes.


# ======================================================================
# 12. FINAL LESSONS LEARNED FROM PROBLEM 6
# ======================================================================

# 1. Lists can contain tuples representing structured records.
#
# 2. Each tuple can store a product ID, name, and price.
#
# 3. Double indexing retrieves information from nested collections.
#
# 4. A for loop processes each product automatically.
#
# 5. An if statement filters products based on conditions.
#
# 6. max() retrieves the largest value in a collection.
#
# 7. index() retrieves the position of the first matching value.
#
# 8. Manual indexing can introduce mistakes and is difficult to scale.
#
# 9. A loop can find the most expensive product without
#    manually creating separate name and price collections.
#
# 10. A variable can store an entire tuple rather than
#     only one value from that tuple.
#
# 11. Updating the most expensive product during iteration
#     allows Python to keep track of the highest price found.
#
# 12. F-strings insert variables and expressions into strings.
#
# 13. Curly braces inside f-strings contain expressions
#     that Python evaluates.
#
# 14. print() inserts spaces between comma-separated arguments
#     unless a different separator is specified.
#
# 15. append() accepts one argument and adds one element to a list.
#
# 16. A tuple containing multiple values still counts
#     as one element when appended to a list.
#
# 17. The order of operations matters when modifying
#     and analyzing a collection.


# ======================================================================
# MOST IMPORTANT TAKEAWAY
# ======================================================================

# The biggest improvement I learned from this problem
# was how to retrieve information using loops
# instead of manually accessing every element.
#
# Initially, I created separate collections for
# product names and prices.
#
# Although this approach worked for a small inventory,
# it required unnecessary manual indexing.
#
# By using a for loop and keeping track of the
# most expensive product tuple, I can retrieve
# both the product name and price directly.
#
# I also learned how f-strings simplify formatting
# and how incorrect indexing can create hidden bugs.
#
# These concepts are useful for building inventory systems,
# analyzing product prices, and processing structured data.
#
# ======================================================================
# END OF PROBLEM 6 - REVISION NOTES
# ======================================================================




# ============================================================
# PROBLEM 7: REMOVE DUPLICATE CUSTOMER IDS
# Difficulty: Easy
# Concepts: Lists, loops, membership checking
# ============================================================

# Real-World Scenario:
# A customer registration system accidentally stores duplicate IDs.
#
# Initial Data:
# customer_ids = [101, 102, 103, 101, 104, 102, 105]
#
# Your Tasks:
# 1. Create a new list containing unique customer IDs.
# 2. Preserve the original order.
# 3. Print the new list.
# 4. Do not modify the original list.
#
# Expected Output:
# [101, 102, 103, 104, 105]
#
# Rules:
# Do not use set() for your first solution.
# Try solving the problem using a loop and a list.
#
# Bonus Challenge:
# Solve the same problem using set().
# Compare the results and consider whether order is preserved.
#
# Thinking Question:
# Why might duplicate customer IDs cause problems in a real application?
#
# Write Your Solution Below:




# ============================================================
# PROBLEM 8: FIND THE TWO HIGHEST SCORES
# Difficulty: Medium
# Concepts: Lists, sorting, indexing
# ============================================================

# Real-World Scenario:
# You are developing a leaderboard for a programming competition.
#
# Initial Data:
# scores = [78, 95, 88, 92, 100, 85]
#
# Your Tasks:
# 1. Find the highest score.
# 2. Find the second-highest score.
# 3. Print both results.
# 4. Make sure the program works if the scores change.
#
# Expected Output:
# Highest Score: 100
# Second Highest Score: 95
#
# Rules:
# Do not manually enter the answers.
#
# Bonus Challenge:
# Solve the problem without using sort() or sorted().
#
# Thinking Question:
# Why is a list useful for a leaderboard?
# What happens if two players have the same highest score?
#
# Write Your Solution Below:




# ============================================================
# PROBLEM 9: RETURN MULTIPLE VALUES USING A TUPLE
# Difficulty: Medium
# Concepts: Functions, tuples, return, unpacking
# ============================================================

# Real-World Scenario:
# You are building a salary analysis tool.
#
# Initial Data:
# salaries = [45000, 52000, 60000, 48000, 75000]
#
# Your Tasks:
# 1. Create a function named analyze_salaries(salaries).
# 2. Calculate the minimum salary.
# 3. Calculate the maximum salary.
# 4. Calculate the average salary.
# 5. Return all three values from the function.
# 6. Unpack the returned values into three variables.
# 7. Print the results.
#
# Expected Output:
# Minimum Salary: 45000
# Maximum Salary: 75000
# Average Salary: 56000.0
#
# Hint:
# A function can return multiple values separated by commas.
# Python automatically packs these returned values into a tuple.
#
# Thinking Question:
# Why might returning a tuple be useful when a function
# needs to provide multiple related results?
#
# Write Your Solution Below:




# ============================================================
# PROBLEM 10: SHOPPING CART WITH PRODUCT RECORDS
# Difficulty: Medium
# Concepts: Lists, tuples, loops, functions
# ============================================================

# Real-World Scenario:
# You are developing a basic checkout system.
# Each product is represented by a tuple containing its name and price.
#
# Initial Data:
# cart = [
#     ("Laptop", 1200),
#     ("Mouse", 25),
#     ("Keyboard", 75),
#     ("Monitor", 300)
# ]
#
# Your Tasks:
# 1. Display every product and its price.
# 2. Calculate the original cart total.
# 3. Add a new product: ("Headphones", 150).
# 4. Remove "Mouse" from the cart.
# 5. Calculate the updated total.
# 6. Display the updated shopping cart.
#
# Expected Output:
# Original Total: $1600
#
# Updated Cart:
# Laptop - $1200
# Keyboard - $75
# Monitor - $300
# Headphones - $150
#
# Updated Total: $1725
#
# Thinking Question:
# Why is the shopping cart represented as a list?
# Why is each product represented as a tuple?
# What would happen if the entire shopping cart were a tuple?
#
# Write Your Solution Below:




# ============================================================
# FINAL REVISION NOTES: LISTS VS TUPLES
# ============================================================

# LIST:
# A list is an ordered, mutable collection of elements.
# Mutable means we can add, remove, or replace elements.
# Lists are created using square brackets [].
#
# Real-World Examples:
# Shopping carts, task lists, student collections, inventories.
#
# Common List Methods:
# append() = Adds an element to the end.
# insert() = Inserts an element at a specific position.
# remove() = Removes the first matching element.
# pop() = Removes and returns an element.
# sort() = Sorts the list in place.
# reverse() = Reverses the list in place.
# copy() = Creates a shallow copy of the list.


# TUPLE:
# A tuple is an ordered, immutable collection of elements.
# Immutable means its elements cannot be replaced, added, or removed.
# Tuples are commonly created using parentheses ().
#
# Real-World Examples:
# GPS coordinates, fixed record snapshots, function return values.
#
# Common Tuple Methods:
# count() = Counts occurrences of a value.
# index() = Finds the index of the first matching value.
#
# Important:
# Tuples can contain mutable objects, such as lists.
# Those objects can still be modified even though the tuple is immutable.


# ============================================================
# FINAL THINKING QUESTIONS
# ============================================================

# 1. What is the difference between mutable and immutable?
#
# 2. Why can we use append() with a list but not a tuple?
#
# 3. Can a tuple contain a list?
#
# 4. Can we modify a list stored inside a tuple?
#
# 5. Why might GPS coordinates be represented using a tuple?
#
# 6. Why is a shopping cart usually better represented using a list?
#
# 7. What happens when we use list.sort() inside print()?
#
# 8. Can a list contain multiple tuples?
#
# 9. Can a tuple contain multiple lists?
#
# 10. When would you choose a dictionary instead of a list or tuple?


# ============================================================
# END OF PRACTICE
# Goal: Understand how to choose between lists and tuples
# based on real-world programming requirements.
# ============================================================