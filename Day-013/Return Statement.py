# ============================================================
# DAY 013: PYTHON FUNCTIONS — UNDERSTANDING THE RETURN KEYWORD
# ============================================================

# EXAMPLE 1: FUNCTION WITHOUT RETURN

def cube(num):
    num * num * num

print(cube(3))  # Output: None

# EXPLANATION:
# 1. We created a function named cube() with one parameter: num.
# 2. When we call cube(3), the value 3 is assigned to num.
# 3. Python calculates 3 * 3 * 3 = 27.
# 4. However, we did not use the return keyword.
# 5. Therefore, the calculated value (27) is not returned.
# 6. By default, Python functions return None if no return is specified.
# 7. None is a special Python value representing the absence of a value.
# 8. When print(cube(3)) executes, it prints None.

# IMPORTANT:
# Performing a calculation inside a function does not automatically
# return the calculated result.
# We must explicitly use the return keyword to send the result back.


# ============================================================
# EXAMPLE 2: FUNCTION WITH RETURN
# ============================================================

def cube(num):
    return num * num * num

print(cube(3))  # Output: 27

# EXPLANATION:
# 1. We created a function named cube() with one parameter: num.
# 2. We called the function using cube(3).
# 3. Python assigns the argument 3 to the parameter num.
# 4. The expression num * num * num calculates 3 * 3 * 3 = 27.
# 5. The return keyword sends the calculated value (27) back
#    to the location where the function was called.
# 6. Therefore, cube(3) evaluates to 27.
# 7. The print() function displays 27 on the screen.

# IMPORTANT:
# return does NOT automatically print anything.
# return sends a value back to the caller.
# print() displays a value on the screen.


# ============================================================
# EXAMPLE 3: STORING A RETURNED VALUE IN A VARIABLE
# ============================================================

def cube(num):
    return num * num * num

result = cube(3)
print(result)  # Output: 27

# EXPLANATION:
# 1. We created a function named cube() that accepts one parameter.
# 2. When cube(3) is called, num receives the integer 3.
# 3. Python calculates 3 * 3 * 3 = 27.
# 4. The return keyword sends 27 back to the caller.
# 5. The returned value is assigned to the variable result.
# 6. Therefore, result = 27.
# 7. print(result) displays the stored value: 27.

# IMPORTANT:
# We can store a function's returned value inside a variable.
# This allows us to reuse the result without calling the function again.

# Example:
# result = cube(3)
# print(result + 10)  # Output: 37
# print(result * 2)   # Output: 54


# ============================================================
# DIFFERENCE BETWEEN PRINT() AND RETURN
# ============================================================

# print():
# - Displays information on the screen.
# - Does not send the displayed value back to the caller.
# - Mainly used to show output to the user.

# return:
# - Sends a value from a function back to its caller.
# - Allows the returned value to be stored in a variable.
# - Allows the returned value to be used in further calculations.
# - Immediately ends the current function's execution.


# ============================================================
# KEY TAKEAWAYS
# ============================================================

# 1. A function without an explicit return statement returns None.
# 2. The return keyword sends a value back to the caller.
# 3. print() displays a value, while return provides a value.
# 4. Returned values can be assigned to variables.
# 5. Returned values can be reused in mathematical operations.
# 6. Any statements after an executed return inside the same
#    function will not run.
# 7. A function can return different data types, including:
#    int, float, str, bool, list, tuple, and dictionary.

# REMEMBER:
# print() = SHOW THE VALUE
# return  = GIVE BACK THE VALUE
# None    = NO VALUE RETURNED