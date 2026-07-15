# The purpose of this assignment is to manage items in a Python list
# create a grocery shopping program

# Intro:
# 1. Begin with an empty grocery list, welcome the user
# 2. Before the main loop begins, prompt the user for the first grocery item (string) and add that to the list
# 3. Before the main loop begins, print the list so the user can see there's one item
# 4. Give instructions that the user may add multiple items at a time, comma-separated

# Main loop:
# With each iteration, display the menu options: add items, remove item (purchased), print list, exit
#       You may implement the menu however you wish.
#       For example: 1) add, 2) remove, 3) print, 4) exit                           [user types a number]
#       Another option: Add items (a), Remove item (r), Print list (p), Exit (x)    [user types a character]
#       Another option: "Add" items, "Remove" item, "Print" list, "Exit"            [the user types the string]
# "add items" details: the user may type one single string or a list of items, separated by commas
#       add the item(s) to the list, print the number of items in the list (e.g. "There are now _ items")
#       if the user enters multiple items, insert each. Example: "apple, soda, napkins" should add 3 items
#       do NOT print the list at this time; that feature has its own menu option
# "remove item" details: print the contents of the shopping list, as a numbered list (starting with 1)
#       prompt the user to enter the number to be removed
#       remove that item from the list, print the number of items in the list
#       do NOT print the list at this time; that feature has its own menu option
# "print list" details: print the contents of the shopping list
#       numbered list, bulleted list, one long string, whatever you think is best for the user
#       at the top, print "There are _ items in the list:"
# "exit" details: terminate the loop, bid the user farewell
