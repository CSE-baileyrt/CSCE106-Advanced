# The purpose of this lab is to demonstrate understanding of basic web scraping
# NOTE: This assignment is identical to the one the rest of the class will do
# NOTE: Web scraping is extremely common. Code that performs web scraping is called a "bot".
#       Many websites (StackOverflow included) block bots. We have been able to complete this lab for several years.
#       However, if SO blocks our traffic more aggressively, I will assign a different objective (website).
#       Email me if you run into trouble with the SO site.

# Instructions: complete the tasks below (marked To-Do)
# Use the BeautifulSoup library (version 4): https://www.crummy.com/software/BeautifulSoup/
# Connect to the StackOverflow website, download details about some questions, and display those details


import requests
from bs4 import BeautifulSoup

# TODO: download the page using requests:
#       StackOverflow website, top 45 unanswered questions that are tagged as Python
#       Alternatively, you can find the top 45 most recent Python questions (instead of unanswered)

# TODO: using BeautifulSoup, extract the following from the list of questions: title, user, text excerpt

# NOTE: you might need to get page 2 and page 3, to get to 45 (do lots of testing)

# TODO: print all 45 questions in the format "{title} ({user}):\n{excerpt}"