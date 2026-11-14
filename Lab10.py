# The purpose of this lab is to demonstrate understanding of basic web scraping
# NOTE: This assignment is identical to the one the rest of the class will do
# NOTE: Web scraping is extremely common. Code that performs web scraping is called a "bot".
#       Many websites (StackOverflow included) block bots. We have been able to complete this lab for several years.
#       However, if SO blocks our traffic more aggressively, I will assign a different objective (website).
#       Email me if you run into trouble with the SO site.
#       UPDATE Fall 2026: use GitHub instead (SO blocks bots aggressively now)
#       It is possible to use StackOverflow's API, but GitHub is simpler

# Instructions: complete the tasks below (marked To-Do)
# Use the BeautifulSoup library (version 4): https://www.crummy.com/software/BeautifulSoup/
# Connect to the StackOverflow website, download details about some questions, and display those details


import requests
from bs4 import BeautifulSoup

# TODO: download the page using requests:
#       GitHub website, top 45 repositories that are tagged as Python

# TODO: using BeautifulSoup, extract the following from the list of repos: user, repo, stars, desc

# NOTE: you might need to get page 2 and page 3, to get to 45 (use the "?page=" query string parameter)

# TODO: print all 45 repos in the format "{user} / {repository} ({stars}):\n{description}"
