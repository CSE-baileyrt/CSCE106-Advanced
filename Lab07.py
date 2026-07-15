# The purpose of this lab is to demonstrate mastery of file IO

# The rest of the class built this for Lab 5:
# Create a program that allows a user to write flashcards and then test their own knowledge.
# Build the deck of flashcards
#   1. Start with an empty dictionary
#   2. Ask for a card term (key), then ask for the definition/answer (value)
#   3. Store that key-value pair in the dictionary
#   4. Loop until the user is done entering flashcards
# Quiz the user from that deck
#   1. Randomly pick a term, show it, and ask "Ready?"
#   2. When they hit Enter, show the definition.
#   3. Repeat the testing until the user chooses to quit.

# You will start by implementing the code for that lab and then enhance it as follows:
# Instead of making 1 deck of flashcards and then quizzing from that 1 deck,
#   allow the user to create as many decks as they want or quiz from any deck they have made
# As usual, display a menu of options and put users into a loop.
# The menu tree looks something like this:
# New subject?
#       Enter the subject name
#       Create the dictionary of flashcards (loop)
#       Save the entire dictionary to "<subject name>.txt"
# Saved subject?
#       Look in the folder, find all ".txt" files, display the list
#       Allow the user to pick one (type the name, pick a number, whatever you think is best)
#       Open the file "<subject name>.txt", read the entire string
#       Reconstruct the string into a dictionary (hint: Python "eval" function)
#       Quiz the user on the flashcards (loop)
# Quit?
#       Have a nice day, end the program