i = 1
while i <= 10:
    print(i)
    i = i + 1 #i+=1 same as this
print("Done with loop!")

# ============================================================
# PYTHON WHILE LOOP - NOTES
# ============================================================

# WHAT IS A WHILE LOOP?
# A while loop is a control flow statement in Python.
# It repeatedly executes a block of code as long as a
# specified condition remains True.

# HOW DOES A WHILE LOOP WORK?
# 1. Python checks the condition after the "while" keyword.
# 2. If the condition is True, Python executes the indented code.
# 3. After executing the code, Python checks the condition again.
# 4. If the condition remains True, the loop repeats.
# 5. If the condition becomes False, Python exits the loop.
# 6. Python then continues executing code outside the loop.

# ============================================================
# MY CODE EXPLANATION
# ============================================================

# i = 1
# We initialize a variable called "i" with the value 1.
# This variable acts as a counter for the while loop.

# while i <= 10:
# "while" is a Python keyword used to create a loop.
# "i <= 10" is the condition.
# <= means "less than or equal to".
# The loop continues as long as i is less than or equal to 10.

#     print(i)
#     Prints the current value of i during each iteration.
#     The first iteration prints 1.
#     The second iteration prints 2.
#     This continues until the loop prints 10.

#     i = i + 1
#     Increases the value of i by 1 after each iteration.
#     This process is called incrementing.
#     Example: i = 1 + 1 = 2
#              i = 2 + 1 = 3
#              i = 3 + 1 = 4

#     i += 1
#     This is the shorter version of i = i + 1.
#     Both statements perform the same operation.
#     The += operator is called an augmented assignment operator.

# print("Done with loop!")
# This statement is outside the while loop.
# It executes only after the loop condition becomes False.
# When i becomes 11, the condition 11 <= 10 is False.
# Python exits the loop and prints "Done with loop!".

# ============================================================
# HOW PYTHON PROCESSES EACH ITERATION
# ============================================================

# Iteration 1:  i = 1  -> 1 <= 10  -> True -> Prints 1
# Iteration 2:  i = 2  -> 2 <= 10  -> True -> Prints 2
# Iteration 3:  i = 3  -> 3 <= 10  -> True -> Prints 3
# Iteration 4:  i = 4  -> 4 <= 10  -> True -> Prints 4
# Iteration 5:  i = 5  -> 5 <= 10  -> True -> Prints 5
# Iteration 6:  i = 6  -> 6 <= 10  -> True -> Prints 6
# Iteration 7:  i = 7  -> 7 <= 10  -> True -> Prints 7
# Iteration 8:  i = 8  -> 8 <= 10  -> True -> Prints 8
# Iteration 9:  i = 9  -> 9 <= 10  -> True -> Prints 9
# Iteration 10: i = 10 -> 10 <= 10 -> True -> Prints 10

# After iteration 10:
# i increases from 10 to 11.
# Python checks the condition again.
# 11 <= 10 -> False
# The while loop stops executing.

# IMPORTANT:
# The loop executes 10 times.
# However, Python evaluates the condition 11 times.
# The first 10 evaluations return True.
# The 11th evaluation returns False.

# ============================================================
# EXPECTED OUTPUT
# ============================================================

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Done with loop!

# ============================================================
# IMPORTANT CONCEPT - INFINITE LOOP
# ============================================================

# An infinite loop occurs when the condition never becomes False.

# Example:

# i = 1
# while i <= 10:
#     print(i)

# In this example, i always remains 1.
# Since 1 <= 10 is always True, the loop never stops.
# This happens because we forgot to increment i.

# To prevent this problem, we can use:
# i = i + 1
# OR
# i += 1

# ============================================================
# KEY POINTS TO REMEMBER
# ============================================================

# 1. A while loop repeats code while a condition remains True.
# 2. Python checks the condition before every iteration.
# 3. If the condition is initially False, the loop never executes.
# 4. A counter variable can track the progress of a loop.
# 5. i += 1 is equivalent to i = i + 1 for an integer counter.
# 6. Python does not automatically increment the counter.
# 7. Forgetting to update the counter may cause an infinite loop.
# 8. Indentation determines which statements belong to the loop.
# 9. The loop terminates when its condition becomes False.
# 10. Code outside the loop executes after the loop finishes.