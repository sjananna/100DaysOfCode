secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("Enter Guess: ")
print("You win!")


# ============================================================
# WHILE LOOP - GUESSING GAME EXECUTION FLOW
# ============================================================

# START
#   |
#   v
# Secret word = "giraffe"
#   |
#   v
# Guess = "" (Empty string)
#   |
#   v
# Is guess different from "giraffe"?
#   |
#   | YES (Condition is True)
#   v
# Ask the player to enter a guess
#   |
#   v
# Check the guess again
#   |
#   | WRONG → Condition remains True → Ask again
#   |
#   | CORRECT → Condition becomes False
#   v
# Stop the while loop
#   |
#   v
# Print "You win!"
#   |
#   v
#  END

# NOTE:
# The while loop keeps repeating as long as guess != secret_word.
# Every incorrect guess makes the loop repeat.
# Once the player enters "giraffe", the condition becomes False.
# Python exits the loop and executes print("You win!").
# This game allows unlimited guesses because there is no guess limit.


secret_word_one = "Tiger"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word_one and not out_of_guesses:
    if guess_count < guess_limit:
     guess = input("Enter Guess: ")
     guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("You lose!")
else:
    print("You win this game!")

# ============================================================
# PYTHON WHILE LOOP - GUESSING GAME WITH LIMITED ATTEMPTS
# ============================================================

# WHAT IS THIS PROGRAM?
# This program creates a guessing game where the player must
# guess a secret word within a maximum of 3 attempts.
#
# If the player guesses correctly, Python prints "You win this game!"
# If the player uses all 3 attempts incorrectly, Python prints "You lose!"
#
# CONCEPTS USED:
# 1. Variables
# 2. Strings
# 3. Integers
# 4. Booleans
# 5. While loops
# 6. Conditional statements (if and else)
# 7. Comparison operators (!= and <)
# 8. Logical operators (and and not)
# 9. Assignment operators (+=)
# 10. User input using input()


# ============================================================
# PART 1: INITIALIZING VARIABLES
# ============================================================

# secret_word_one = "Tiger"
# Stores the correct answer as a string.
# Python compares the player's guess against this variable.
# IMPORTANT: Python is case-sensitive.
# "Tiger" and "tiger" are NOT considered equal.


# guess = ""
# Creates an empty string to store the player's answer.
# Initially, the player has not entered anything.
# Each time input() executes, the previous value is replaced.


# guess_count = 0
# Creates an integer variable to count the number of guesses.
# Initially, the player has made 0 guesses.
# This variable increases by 1 after each attempt.


# guess_limit = 3
# Sets the maximum number of allowed guesses.
# The player can enter a maximum of 3 answers.
# This variable remains unchanged throughout the game.


# out_of_guesses = False
# Creates a Boolean variable.
# Boolean values can only be True or False.
#
# False = The player has NOT been marked as out of guesses.
# True  = The player HAS been marked as out of guesses.
#
# Initially, this variable is False because the game
# has not started and the player still has 3 attempts.


# ============================================================
# PART 2: UNDERSTANDING THE WHILE LOOP CONDITION
# ============================================================

# while guess != secret_word_one and not out_of_guesses:

    # The while loop contains TWO conditions:
    #
    # CONDITION 1:
    # guess != secret_word_one
    #
    # != means "not equal to".
    #
    # Python checks whether the player's guess is different
    # from the secret word.
    #
    # Example:
    # "Lion" != "Tiger"  --> True
    # "Tiger" != "Tiger" --> False
    #
    # If the guess is incorrect, this condition is True.
    # If the guess is correct, this condition is False.
    #
    #
    # CONDITION 2:
    # not out_of_guesses
    #
    # The 'not' operator reverses a Boolean value.
    #
    # not False --> True
    # not True  --> False
    #
    # Initially:
    # out_of_guesses = False
    #
    # Therefore:
    # not out_of_guesses --> not False --> True
    #
    #
    # UNDERSTANDING 'and':
    #
    # The 'and' operator requires BOTH conditions to be True.
    #
    # True  and True  --> True
    # True  and False --> False
    # False and True  --> False
    # False and False --> False
    #
    # The loop continues ONLY when:
    # 1. The player's guess is incorrect.
    # 2. The player has not been marked as out of guesses.
    #
    # If either condition becomes False, the loop stops.


    # ========================================================
    # PART 3: CHECKING THE NUMBER OF AVAILABLE GUESSES
    # ========================================================

    # if guess_count < guess_limit:

        # The '<' operator means "less than".
        #
        # Python checks whether the number of guesses used
        # is less than the maximum allowed guesses.
        #
        # Initially:
        # guess_count = 0
        # guess_limit = 3
        #
        # Python evaluates:
        # 0 < 3 --> True
        #
        # Therefore, Python enters this if block.
        #
        # After the first guess:
        # 1 < 3 --> True
        #
        # After the second guess:
        # 2 < 3 --> True
        #
        # After the third incorrect guess:
        # 3 < 3 --> False
        #
        # IMPORTANT:
        # The player is allowed to guess when the counter is
        # 0, 1, or 2 because all three values are less than 3.


        # guess = input("Enter Guess: ")

        # input() displays "Enter Guess:" to the player.
        #
        # Python pauses and waits for the player to type.
        #
        # Example:
        # Enter Guess: Lion
        #
        # Python stores:
        # guess = "Lion"
        #
        # IMPORTANT:
        # input() always returns a string.
        #
        # Every new guess replaces the previous guess.
        #
        # Example:
        # First attempt:  guess = "Lion"
        # Second attempt: guess = "Monkey"
        # Third attempt:  guess = "Tiger"


        # guess_count += 1

        # The += operator is an augmented assignment operator.
        #
        # guess_count += 1
        #
        # Is equivalent to:
        #
        # guess_count = guess_count + 1
        #
        # It increases the current value by 1.
        #
        # Example:
        #
        # Initially:     guess_count = 0
        # First guess:   guess_count = 1
        # Second guess:  guess_count = 2
        # Third guess:   guess_count = 3
        #
        # IMPORTANT:
        # The counter increases after EVERY entered guess,
        # regardless of whether the answer is correct.
        #
        # Once these statements finish executing, Python
        # returns to the beginning of the while loop.
        #
        # It checks both while conditions again.
        #
        # If the answer is correct, the loop stops.
        # If the answer is incorrect, the loop continues
        # as long as out_of_guesses remains False.


    # ========================================================
    # PART 4: WHAT HAPPENS WHEN THE GUESS LIMIT IS REACHED?
    # ========================================================

    # else:

        # This else belongs to:
        #
        # if guess_count < guess_limit:
        #
        # It executes when that condition becomes False.
        #
        # Example:
        # guess_count = 3
        # guess_limit = 3
        #
        # Python checks:
        # 3 < 3 --> False
        #
        # Therefore, Python enters this else block.
        #
        # IMPORTANT:
        # After the third incorrect guess, Python first
        # returns to the while condition.
        #
        # Since the guess is still incorrect and
        # out_of_guesses is still False, the loop enters
        # its body one final time.
        #
        # The if condition (3 < 3) is now False.
        # Therefore, Python executes this else block.
        #
        # No fourth guess is requested.


        # out_of_guesses = True

        # Changes the Boolean variable from False to True.
        #
        # Before:
        # out_of_guesses = False
        #
        # After:
        # out_of_guesses = True
        #
        # This tells Python that the player has exhausted
        # the maximum number of allowed attempts.
        #
        # Python returns to the while condition:
        #
        # guess != secret_word_one and not out_of_guesses
        #
        # Suppose the final guess was "Monkey".
        #
        # "Monkey" != "Tiger" --> True
        #
        # not out_of_guesses --> not True --> False
        #
        # Therefore:
        #
        # True and False --> False
        #
        # The while loop stops.


# ============================================================
# PART 5: DETERMINING WHETHER THE PLAYER WON OR LOST
# ============================================================

# if out_of_guesses:

    # Python checks whether out_of_guesses is True.
    #
    # Writing:
    # if out_of_guesses:
    #
    # Is equivalent to:
    # if out_of_guesses == True:
    #
    # If the player exhausted all attempts incorrectly,
    # out_of_guesses will be True.
    #
    # Therefore, Python executes the following statement.

    # print("You lose!")

    # Displays:
    # You lose!


# else:

    # This else executes when out_of_guesses is False.
    #
    # In this program, that means the player guessed
    # the correct word before running out of attempts.
    #
    # Example:
    # guess = "Tiger"
    #
    # Python evaluates:
    # "Tiger" != "Tiger" --> False
    #
    # The while loop stops because the guess is correct.
    #
    # Since out_of_guesses remains False,
    # Python executes this else block.

    # print("You win this game!")

    # Displays:
    # You win this game!


# ============================================================
# PART 6: COMPLETE PROGRAM EXECUTION FLOW
# ============================================================

# START
#   |
#   v
# secret_word_one = "Tiger"
#   |
#   v
# guess = ""
#   |
#   v
# guess_count = 0
#   |
#   v
# guess_limit = 3
#   |
#   v
# out_of_guesses = False
#   |
#   v
# CHECK WHILE CONDITION:
# Is the guess incorrect AND is out_of_guesses False?
#   |
#   | NO --------------------------> EXIT WHILE LOOP
#   |                                     |
#   | YES                                 v
#   v                               CHECK FINAL RESULT
# Is guess_count < guess_limit?           |
#   |                                     |
#   | YES                                 | out_of_guesses = True
#   v                                     v
# Ask player for a guess             Print "You lose!"
#   |
#   v
# Increase guess_count by 1
#   |
#   v
# Return to the while condition
#   |
#   | CORRECT GUESS
#   v
# Exit while loop
#   |
#   v
# out_of_guesses is False
#   |
#   v
# Print "You win this game!"
#
#
# ALTERNATIVE PATH:
#
# If guess_count < guess_limit is False:
#   |
#   v
# Execute the inner else block
#   |
#   v
# Set out_of_guesses = True
#   |
#   v
# Return to the while condition
#   |
#   v
# not out_of_guesses becomes False
#   |
#   v
# Exit the while loop
#   |
#   v
# Print "You lose!"


# ============================================================
# PART 7: EXAMPLE - PLAYER LOSES
# ============================================================

# Secret word: Tiger
#
# Attempt 1:
# Enter Guess: Lion
# guess_count = 1
# Incorrect answer --> Continue
#
# Attempt 2:
# Enter Guess: Elephant
# guess_count = 2
# Incorrect answer --> Continue
#
# Attempt 3:
# Enter Guess: Monkey
# guess_count = 3
# Incorrect answer --> Return to while condition
#
# The while condition is still True at this moment.
#
# Python enters the loop and checks:
# 3 < 3 --> False
#
# Therefore:
# out_of_guesses = True
#
# The while condition now becomes False.
#
# OUTPUT:
# You lose!


# ============================================================
# PART 8: EXAMPLE - PLAYER WINS
# ============================================================

# Secret word: Tiger
#
# Attempt 1:
# Enter Guess: Lion
# guess_count = 1
# Incorrect answer --> Continue
#
# Attempt 2:
# Enter Guess: Tiger
# guess_count = 2
# Correct answer!
#
# Python checks:
# "Tiger" != "Tiger" --> False
#
# The while loop stops.
#
# out_of_guesses remains False.
#
# OUTPUT:
# You win this game!


# ============================================================
# PART 9: IMPORTANT PYTHON CONCEPTS
# ============================================================

# 1. VARIABLE:
# A name that refers to a value stored in memory.
# Example: guess_count = 0


# 2. STRING:
# A sequence of characters enclosed in quotation marks.
# Example: secret_word_one = "Tiger"


# 3. INTEGER:
# A whole number without a decimal point.
# Example: guess_limit = 3


# 4. BOOLEAN:
# A data type representing True or False.
# Example: out_of_guesses = False


# 5. WHILE LOOP:
# Repeats a block of code while its condition remains True.


# 6. != OPERATOR:
# Checks whether two values are different.
# Example: 5 != 3 --> True


# 7. < OPERATOR:
# Checks whether the left value is smaller than the right.
# Example: 2 < 3 --> True


# 8. AND OPERATOR:
# Returns True only when both conditions are True.
# Example: True and False --> False


# 9. NOT OPERATOR:
# Reverses the Boolean value of a condition.
# Example: not False --> True


# 10. IF STATEMENT:
# Executes a block of code when its condition is True.


# 11. ELSE STATEMENT:
# Executes when the associated if condition is False.


# 12. AUGMENTED ASSIGNMENT (+=):
# Updates a variable by adding a value to its current value.
# Example: guess_count += 1


# 13. INPUT FUNCTION:
# Accepts user input and returns it as a string.
# Example: guess = input("Enter Guess: ")


# 14. LOOP TERMINATION:
# A while loop stops when its condition becomes False.


# 15. NESTED CONDITIONAL:
# An if-else statement placed inside another control structure.
# Here, the if-else statement is inside the while loop.


# 16. INDENTATION:
# Python uses indentation to identify blocks of code.
# Statements indented under while execute inside the loop.
# Statements indented under if or else belong to those blocks.
# Incorrect indentation can change the program's behaviour.


# ============================================================
# FINAL KEY TAKEAWAYS
# ============================================================

# 1. The while loop controls whether the game continues.

# 2. The if statement checks whether another guess is allowed.

# 3. The input() function receives the player's answer.

# 4. The guess_count variable tracks the number of attempts.

# 5. The guess_limit variable defines the maximum attempts.

# 6. The += operator increases the guess counter.

# 7. The out_of_guesses Boolean controls the losing condition.

# 8. The 'and' operator combines two conditions.

# 9. The 'not' operator reverses a Boolean value.

# 10. The final if-else statement determines the result.

# 11. A correct guess on the third attempt still wins.

# 12. The player cannot make a fourth guess.

# 13. The loop checks its condition BEFORE each iteration.

# 14. The inner else block runs after the third incorrect
#     guess when Python enters the loop again.

# 15. The final if-else statement is OUTSIDE the while loop.
#     Therefore, it executes only after the loop terminates.
