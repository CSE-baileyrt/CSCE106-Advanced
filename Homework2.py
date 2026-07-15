# NOTE: Homework 1 was a quiz that you completed the first week of class, in Blackboard

# Your assignment is to create a random password generator
# This assignment makes use of: random, lists, strings, loops, nested loops

# Start with a list of letters (upper and lower), a list of numbers, and a list of symbols. For example: 
lowers = ['a', 'b', 'c'] # (TODO: fill in the rest of the lowercase letters)
uppers = ['A', 'B', 'C'] # etc.
nums = ['0', '1', '2'] # etc. (only single digits are necessary)
specials = ['*', '&', '%'] # etc.
# TODO: If you choose to leave out any letters or numbers, include an explanation in comments
#   It might be good to leave a comment about which symbols you choose to include or exclude

# TODO: Ask the user how many characters long to make the password
# Start with an empty password string
# TODO: Repeat the following steps as many times as needed until the password is long enough
#   1. Randomly select a character from one of the lists above
#   2. Add that random character to the password string

# Print "Here are 3 random passwords of that length. Choose any that you like."
# TODO: Print the password generated above (matching the requested length)
# Generate a second password and print it
# Generate a third password and print it
# NOTE: It might be helpful to put the code to generate one password into a function

# TODO: Ask the user if they want to generate another or quit
#   If they want another, loop all the way back up to asking them how many characters
#   (They might want one longer or shorter the next time around)

# You’ll use the "random" library so be sure to look over what it can do on the Python docs:
# https://docs.python.org/3/library/random.html
# NOTE: There are many ways to "randomly select a character".
