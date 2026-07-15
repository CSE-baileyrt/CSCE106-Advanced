# The purpose of this lab is to demonstrate mastery of both the while loop and the for loop

# The FIZZBUZZ challenge (see Lab 1) is well-known. You're going to create the Ultimate FIZZBUZZ Solver

# Step 1: the inputs
# Welcome the user, explain what the program is built to do
# Prompt the user to enter the start and end numbers (e.g. 1 to 100, 50 to 199, -100 to +100, etc.)
#       Validate that the first number is less than the second number
#       Positive and negative numbers are all valid (so is zero)
#       Decimal numbers are not valid, but you don't need to handle that (the user will only enter ints)
# Prompt the user to enter two integers as the divisors
#       Validate that the two divisors are not the same number, and are both positive (>0, not >=0)
#       In the original version, the two divisors are 3 and 5
#       Each number in the range is evaluated to see if it is evenly divisible by the first, second, or both
#       Assume that the two inputs are integers (the user will not enter decimals)
# Prompt the user to enter two replacement strings for those divisors
#       Validate that the first and second replacement strings are not the same and not empty
# NOTE: You may collect the divisors and replacements as sets (int+string then int+string) if you wish
#       i.e. You may have the user enter 2 ints followed by 2 strings or 1 int-string pair and then another
# Prompt the user to select the loop type: for loop or while loop
#       Validate that the input is one of those 2 options
# If any inputs fail validation, you must prompt the user to enter a valid input
#       Do not continue to Step 2 until all inputs are valid

# Once all inputs are valid, summarize the challenge (for the user):
# Step 2: print the following text, replacing the [brackets] with the inputs given above
# Print the numbers [start] to [end], one line each, using a [while/for] loop
# If any number is evenly divisible by [first int], replace that with [first replacement]
# If any number is evenly divisible by [second int], replace that with [second replacement]
# If any number is evenly divisible both [first int] and [second int], replace that with [both replacements]
# Otherwise, print the number (no replacements)

# Step 3: run the challenge
# Write the code to solve the challenge with the given inputs
# You'll need to create 2 solutions: for loop and while loop versions
# I recommend creating 2 functions, one for each loop type, and then passing the inputs to its function
# Execute the FIZZBUZZ solver for the given inputs (the code should print the desired output)

# Tests: run the program with the following inputs
# a) 1, 100, 3, 5, "FIZZ", "BUZZ", "while"      # The OG challenge
# b) 500, 750, 10, 17, "FOZZY", "BEAR", "for"   # bigger numbers
# c) -100, -1, 3, 5, "FOO", "BAR", "while"      # all negative
# d) -50, 50, 4, 7, "FFFF", "BBBB", "for"       # make sure this prints the correct entry for 0
# NOTE: You do NOT need to send me screenshots of the tests. They are for your benefit only