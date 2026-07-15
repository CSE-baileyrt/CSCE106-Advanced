# The purpose of this lab is to demonstrate mastery of dictionaries in Python

# The Rolodex was invented in 1956. "Seasoned" professionals used to have them at their desks.
# A Rolodex worked by storing a stack of notecards, each with information about a specific person.
# You will create a Rolodex program, to help your favorite Boomer keep track of their contacts.

# Instructions:
# Allow the user to create a new card, edit a card, delete a card, and print the stack of cards
#       Those options should be available to them repeatedly, until they decide to quit
# The key of each card is the name of the contact person
#       If the user attempts to create a new card with the same contact, you must check with them:
#       If this is a new person, then they must alter the name to be unique
#       If this is an existing person, then this info will overwrite the stored info
# The value stored at that key is a Python List
#       The user can store as much info about the person as they want, just add it to the list
#       Each bit of info should be stored in the List as a string
#       For example, "Phone: 800-123-4567", "Address: 123 Sesame St"
# A card might look like this (JSON representation):
#       "Person 1" : ["info 1", "info 2", "info 3"]
# The full Rolodex (dictionary containing several people) might look like this:
#       { "Person 1" : ["info 1a", "info 2a", "info 3a"],
#       "Person 2" : ["info 1b", "info 2b", "info 3b"],
#       "Person 3" : ["info 1c", "info 2c", "info 3c"] }
# For clarity's sake, each List might have a different number of elements
#       i.e. One contact might have Phone, Address, and Birthday but another might have only have Phone
# "Edit a card" details:
#       The user has full control of what data they want to store on the card for that contact
#       Allow the user to add or delete strings from the List (value) for any contact they choose
# "Add a card" details:
#       Allow the user to enter the name of the contact (they key) and then create an empty List (the value)
#       Allow the user to add any details about the contact, store those strings in the List
#       When they are done adding details, insert the key-value pair into the dictionary
# "Delete a card" details:
#       Allow the user to select which card they wish to delete, then delete it from the dictionary
# "Print the stack" details:
#       Print all KEYS in the dictionary (names only, no details)
#       Ask the user if they want to see details for any of those contacts
#       If yes, print the details (List) for as many contacts as they want
#       If no, return to the menu

# Be user-friendly. Present instructions and feedback to the user as they make use of the program
#       Help the user feel informed about what's happening in the background
#       Craft the display carefully. The list of contacts plus the details might get messy
#       Consider using whitespace (tabs, newlines, spaces, etc.) to make the text more readable
