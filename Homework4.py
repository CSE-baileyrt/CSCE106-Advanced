# The purpose of this assignment is to demonstrate mastery of dictionaries, requests, and adaptation

# In lesson 11, we wrote this code. During that lesson, I made the comment marked with the To-Do
##### BEGIN STARTER #####
import requests
response = requests.get(
    'https://raw.githubusercontent.com/krishnakt031990/Crawl-Wiki-For-Acronyms/master/AcronymsFile.csv'
)
text_lines = response.text.split("\n")
acronyms = {}

for line in text_lines:
    one_line = line.split("- ")
    if len(one_line) > 1:
        acro = one_line[0].strip()
        meaning = one_line[1].strip()
        acronyms[acro] = meaning
        
# full dictionary
# print(acronyms)
# print(len(acronyms))

# TODO: "These last 3 lines would make a nice lookup app"
# print("Hi there! I can look up acronyms for you!")
# u_acro = input('Enter an acronym: ')
# print("{} is short for {}".format(u_acro, acronyms[u_acro]))
##### END STARTER #####


# Your assignment is to start with that idea (an acronym lookup app) and make it better.
# TODO: Alter the code to make use of a different content file.
# https://raw.githubusercontent.com/priscian/nlp/master/OpenNLP/models/coref/acronyms.txt
# TODO: As usual, allow the user to look up multiple acronyms (keep offering until they choose to quit).

# == Similar elements ==
# 1. The user interaction is the same: Allow the user to enter an acronym, look it up in the dictionary, 
#   and display the corresponding meaning.
# 2. The procedure is also the same: Using the "requests" module, get the content at the URL, receive it 
#   as a string (response.text), parse the string into a dictionary one line at a time, and then move 
#   into the user interaction section.

# == Dissimilar elements ==
# 1. The data is formatted differently, details below
# 2. The user may search for an acronym that is NOT found in the dictionary, details below

# Data format
# The data from the in-class example was already condensed for us. Each acronym was only listed once, 
#   and the various meanings were all listed with that one entry. This time, each possible meaning has 
#   its own line in the file. You’ll first need to CHECK THE DICTIONARY (hint below) to see if that key 
#   already exists, and then add/append the second/third/Nth entry onto the end of the value. But a 
#   dictionary in Python may not have multiple entries with the same key. Example:
# AA	Administrative Assistant
# AA	Administrative Authority
# AA	Affirmative Action committee
# AA	Alcoholics Anonymous
# AA	American Airlines
# AA	Antiaircraft Artillery
# AA	Associate in Accounting
# AA	Astronomy and Astrophysics
# AA	Auto Answer
# AA	Automobile Association
# All of those lines need to end up in one dictionary entry. The Key should be "AA" and the Value should
#   be "Administrative Assistant, Administrative Authority, Affirmative..."

# There are some entries for which there are duplicate (identical) meanings. That’s okay- just add the 
#   meaning twice (pretend they are different in some subtle way)
# Example:
# A.I.	artificial intelligence
# A.I.	artificial intelligence
# Key = "A.I." (including the periods), Value = "artificial intelligence, artificial intelligence"

# Missing entries
# If the user searches for an acronym that is not found, you should display something helpful like 
#   "Acronym {} was not found in the list".
# Hint: 
#     if [key variable name] in [dictionary variable name]:
#         # code for what to do if it’s found
#     else:
#         # code for what to do if it’s NOT found
# (Optional) You might allow the user to ADD that acronym to the dictionary, if they provide a value
#   for the meaning.
