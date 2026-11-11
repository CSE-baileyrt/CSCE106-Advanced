# Assignment 2: functions
# In Lab 7, we created an app that allows the user to manage flashcard decks.
# Expand that lab to allow the user to create and manage recipes.
# Each file will contain a category of recipes (e.g., "Desserts", "Breads", etc.). The file name is the category name.
# Every recipe has a name and a list of ingredients. Store the pair in a dictionary (by category).
#   Example fruits.txt file structure: { "Applesauce":["apples"], "Strawberry compote":["strawberries", "sugar"] }
# Create the following functions:
# 1. A function to create a new category of recipes (one .txt file per category, one dictionary per file)
#    Create a subfolder specific to your program to store the recipe files.
# 2. A function to add a new recipe to an existing category (ask the user for a name and a list of ingredients)
# 3. A function to remove a recipe from an existing category (remove by name)
# 4. A function to view all categories (list all .txt files in the folder)
# 5. A function to view all recipes in a category (list all recipe names in the file)
# 6. A function to view the details of a specific recipe (display the name and list of ingredients)
# The user menu should offer the following options:
# Create a new category, add a recipe, remove a recipe, view all categories, view all recipes in a category, and view the details of a specific recipe.
# Call the appropriate function based on the user's choice. The program should loop until the user chooses to exit.
