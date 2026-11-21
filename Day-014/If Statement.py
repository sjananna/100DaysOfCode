# ============================================================
# DAY 012: PYTHON IF STATEMENTS AND CONDITIONAL LOGIC
# ============================================================

# ============================================================
# 1. WHAT IS AN IF STATEMENT?
# ============================================================

# An if statement is used to make decisions in Python.
# It allows Python to execute a block of code only when
# a specific condition is True.

# BASIC SYNTAX:
#
# if condition:
#     code to execute

# IMPORTANT RULES:
# 1. The keyword "if" starts a conditional statement.
# 2. The condition is evaluated as either True or False.
# 3. A colon (:) must be placed after the condition.
# 4. The code inside the if statement must be indented.
# 5. Python executes the indented code only if the condition is True.
# 6. If the condition is False, Python skips that block of code.
# 7. Python uses indentation to identify which statements
#    belong to the if block.

# ============================================================
# EXAMPLE 1: SIMPLE IF STATEMENT WITH TRUE
# ============================================================

is_male = True
if is_male:
    print("You are a male.")

# EXPLANATION:
# is_male is a variable containing the Boolean value True.
# Boolean values can only be True or False.
#
# The statement "if is_male:" checks whether is_male is True.
#
# Since is_male = True, the condition is satisfied.
# Python executes the indented print() statement.
#
# OUTPUT:
# You are a male.
#
# IMPORTANT:
# Writing "if is_male:" is equivalent to writing:
# if is_male == True:
#
# However, "if is_male:" is simpler and preferred in Python.


# ============================================================
# EXAMPLE 2: SIMPLE IF STATEMENT WITH FALSE
# ============================================================

is_female = False
if is_female:
    print("You are a male.")

# EXPLANATION:
# is_female is assigned the Boolean value False.
#
# Python checks the condition:
# if is_female:
#
# Since the condition is False, Python skips the print statement.
#
# OUTPUT:
# Nothing is printed.
#
# IMPORTANT:
# Python does not automatically execute another statement
# when an if condition is False.
#
# If we want Python to perform an alternative action,
# we can use the else statement.
#
# NOTE:
# The printed message says "You are a male."
# However, the variable being checked is is_female.
# These are logically inconsistent names/messages.
# Python does not detect this because the message is just text.


# ============================================================
# 2. WHAT IS AN ELSE STATEMENT?
# ============================================================

# The else statement provides an alternative action
# when the if condition evaluates to False.
#
# BASIC SYNTAX:
#
# if condition:
#     code executed when condition is True
# else:
#     code executed when condition is False
#
# IMPORTANT:
# An else statement does not require its own condition.
# It executes only when the preceding if/elif conditions
# in the same conditional chain are False.


# ============================================================
# EXAMPLE 3: IF AND ELSE
# ============================================================

is_female = False
if is_female:
    print("You are a male.")
else:
    print("You are a female.")

# EXPLANATION:
# Step 1: Python assigns False to is_female.
#
# Step 2: Python evaluates:
# if is_female:
#
# Step 3: Since is_female is False, the if block is skipped.
#
# Step 4: Python moves to the else block.
#
# Step 5: The else block executes.
#
# OUTPUT:
# You are a female.
#
# IMPORTANT:
# Python does not examine whether the printed sentence
# is factually correct.
#
# It only checks the Boolean condition.
#
# In this example, the output is logically inconsistent
# with the variable name because is_female is False.
#
# A more logically consistent example would be:
#
# if is_female:
#     print("You are a female.")
# else:
#     print("You are not female.")


# ============================================================
# 3. WHAT IS THE OR OPERATOR?
# ============================================================

# The "or" operator is a logical operator.
#
# It combines two or more conditions.
#
# The entire condition becomes True if AT LEAST ONE
# of the conditions is True.
#
# It becomes False only when ALL conditions are False.
#
# OR TRUTH TABLE:
#
# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False
#
# IMPORTANT:
# With "or", only one condition needs to be True.
#
# Python also uses short-circuit evaluation.
# If the first condition is True, Python does not need
# to evaluate the second condition to determine the result.


# ============================================================
# EXAMPLE 4: OR OPERATOR WITH TWO TRUE CONDITIONS
# ============================================================

is_male = True
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are female and short.")

# EXPLANATION:
# Step 1: is_male = True
# Step 2: is_tall = True
#
# Step 3: Python evaluates:
# if is_male or is_tall:
#
# Step 4: Substitute the Boolean values:
# True or True
#
# Step 5: The result is True.
#
# Step 6: Python executes the if block.
#
# OUTPUT:
# You are a male or tall or both.
#
# IMPORTANT:
# Both conditions are True in this example.
# However, the or operator does not require both to be True.
# Only one True condition is sufficient.


# ============================================================
# EXAMPLE 5: OR OPERATOR WITH TWO FALSE CONDITIONS
# ============================================================

is_male = False
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both.")
else:
    print("You are female and short.")

# EXPLANATION:
# Step 1: is_male = False
# Step 2: is_tall = False
#
# Step 3: Python evaluates:
# False or False
#
# Step 4: Neither condition is True.
#
# Step 5: The overall condition evaluates to False.
#
# Step 6: Python skips the if block and executes else.
#
# OUTPUT:
# You are female and short.
#
# IMPORTANT:
# The or operator returns False only when
# every condition being checked is False.
#
# This is different from the and operator,
# which requires every condition to be True.


# ============================================================
# 4. WHAT IS THE AND OPERATOR?
# ============================================================

# The "and" operator combines multiple conditions.
#
# Unlike "or", the "and" operator requires ALL
# conditions to be True.
#
# If even one condition is False,
# the entire expression evaluates to False.
#
# AND TRUTH TABLE:
#
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False
#
# IMPORTANT:
# AND = ALL conditions must be True.
# OR  = AT LEAST ONE condition must be True.
#
# Python uses short-circuit evaluation with "and" too.
# If the first condition is False, Python does not need
# to evaluate the second condition.


# ============================================================
# EXAMPLE 6: AND OPERATOR WITH ONE FALSE CONDITION
# ============================================================

is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male.")
else:
    print("You are either not male or not tall or both.")

# EXPLANATION:
# Step 1: is_male = False
# Step 2: is_tall = True
#
# Step 3: Python evaluates:
# if is_male and is_tall:
#
# Step 4: Substitute the values:
# False and True
#
# Step 5: The result is False.
#
# Step 6: Python skips the if block.
#
# Step 7: Python executes the else block.
#
# OUTPUT:
# You are either not male or not tall or both.
#
# IMPORTANT:
# Even though is_tall is True,
# the entire expression is False because is_male is False.
#
# Both conditions must be True for the if block to execute.
#
# This is one of the most important differences
# between the "and" and "or" operators.


# ============================================================
# 5. WHAT IS AN ELIF STATEMENT?
# ============================================================

# The keyword "elif" means "else if".
#
# It allows Python to check another condition when
# the previous if or elif condition is False.
#
# BASIC SYNTAX:
#
# if condition1:
#     execute code if condition1 is True
# elif condition2:
#     execute code if condition2 is True
# else:
#     execute code if all previous conditions are False
#
# IMPORTANT RULES:
# 1. Python checks conditions from top to bottom.
# 2. If the if condition is True, its block executes.
# 3. If the if condition is False, Python checks elif.
# 4. You can use multiple elif statements.
# 5. The else statement is optional.
# 6. Once a condition is True, Python executes its block
#    and skips the remaining branches in that chain.
#
# NOTE:
# elif must come after an if or another elif.
# It cannot start a conditional chain by itself.


# ============================================================
# 6. WHAT IS THE NOT OPERATOR?
# ============================================================

# The "not" operator reverses the truth value
# of a Boolean expression.
#
# NOT TRUTH TABLE:
#
# not True  = False
# not False = True
#
# EXAMPLE:
#
# is_tall = False
#
# not is_tall evaluates to True.
#
# This is because not reverses False into True.
#
# Parentheses can be used to make conditions easier to read.
#
# not (is_tall)
#
# is equivalent to:
#
# not is_tall
#
# IMPORTANT:
# The not operator does not permanently change
# the original variable.
#
# If is_tall = False, evaluating not is_tall gives True,
# but the variable is_tall itself remains False.


# ============================================================
# EXAMPLE 7: IF, ELIF, ELSE, AND NOT
# ============================================================

is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not (is_tall):
    print("You are a male but short.")
else:
    print("You are a female and short.")

# EXPLANATION:
# Step 1: is_male = True
# Step 2: is_tall = False
#
# FIRST CONDITION:
# if is_male and is_tall:
#
# Substitute the values:
# True and False
#
# Result = False
#
# Therefore, Python skips the first if block.
#
# SECOND CONDITION:
# elif is_male and not (is_tall):
#
# Break this condition into smaller parts:
#
# is_male = True
# is_tall = False
#
# not (is_tall) = not False = True
#
# Therefore:
# True and True = True
#
# Python executes the elif block.
#
# OUTPUT:
# You are a male but short.
#
# IMPORTANT:
# Python does not execute the else block because
# the elif condition has already evaluated to True.
#
# KEY CONCEPT:
# The not operator reverses the Boolean value.
#
# In this example:
# not False = True
#
# Combining "and" with "not" allows us to check
# whether one condition is True and another is False.


# ============================================================
# EXAMPLE 8: MULTIPLE ELIF STATEMENTS
# ============================================================

is_male = False
is_tall = True
if is_male and is_tall:
    print("You are a tall male.")
elif is_male and not (is_tall):
    print("You are a male but short.")
elif not (is_male) and (is_tall):
    print("You are a tall female.")
else:
    print("You are a female and short.")

# EXPLANATION:
# Step 1: is_male = False
# Step 2: is_tall = True
#
# Python checks each condition from top to bottom.
#
# ------------------------------------------------------------
# FIRST CONDITION:
# ------------------------------------------------------------
#
# if is_male and is_tall:
#
# Substitute:
# False and True
#
# Result = False
#
# Python skips the first if block.
#
# ------------------------------------------------------------
# SECOND CONDITION:
# ------------------------------------------------------------
#
# elif is_male and not (is_tall):
#
# is_male = False
# is_tall = True
#
# not (is_tall) = not True = False
#
# Therefore:
# False and False = False
#
# Python skips this elif block.
#
# ------------------------------------------------------------
# THIRD CONDITION:
# ------------------------------------------------------------
#
# elif not (is_male) and (is_tall):
#
# Break the condition into smaller parts:
#
# is_male = False
# not (is_male) = not False = True
#
# is_tall = True
#
# Therefore:
# True and True = True
#
# Python executes the third conditional block.
#
# OUTPUT:
# You are a tall female.
#
# ------------------------------------------------------------
# ELSE CONDITION:
# ------------------------------------------------------------
#
# The else block does not execute.
#
# REASON:
# The third condition already evaluated to True.
#
# Once Python finds the first True condition
# in an if/elif/else chain, it executes that block
# and skips the remaining branches.
#
# IMPORTANT:
# This example demonstrates how multiple elif statements
# can be used to evaluate different combinations of conditions.
#
# POSSIBLE COMBINATIONS:
#
# is_male = True,  is_tall = True
# OUTPUT: You are a tall male.
#
# is_male = True,  is_tall = False
# OUTPUT: You are a male but short.
#
# is_male = False, is_tall = True
# OUTPUT: You are a tall female.
#
# is_male = False, is_tall = False
# OUTPUT: You are a female and short.
#
# NOTE:
# These descriptions assume the simplified categories
# represented by the Boolean variables in this exercise.


# ============================================================
# 7. SUMMARY: WHAT I LEARNED
# ============================================================

# 1. if:
# Checks a condition and executes code if it is True.
#
# 2. else:
# Executes an alternative block when all preceding
# conditions in the same chain are False.
#
# 3. elif:
# Checks additional conditions after a previous
# if or elif condition evaluates to False.
#
# 4. and:
# Requires ALL conditions to be True.
#
# 5. or:
# Requires AT LEAST ONE condition to be True.
#
# 6. not:
# Reverses the truth value of a condition.
#
# 7. True and False:
# These are Boolean values, not strings.
# Python is case-sensitive, so True and False
# must begin with capital letters.
#
# 8. Indentation:
# Python uses indentation to determine which
# statements belong to each conditional block.
#
# 9. Colon (:):
# Required after if, elif, and else statements.
#
# 10. Execution order:
# Python checks if/elif conditions from top to bottom
# and executes only the first matching branch.
#
# 11. Multiple independent if statements:
# Each separate if statement is evaluated independently.
# Therefore, more than one independent if block
# can execute if their conditions are True.
#
# 12. Conditional chains:
# In a single if/elif/else chain, only one branch executes.
#
# 13. Short-circuit evaluation:
# With "or", Python can stop checking after finding True.
# With "and", Python can stop checking after finding False.
#
# 14. Boolean variables:
# Variables such as is_male and is_tall store True or False.
# Their names do not determine the result.
# Python evaluates the values assigned to them.
