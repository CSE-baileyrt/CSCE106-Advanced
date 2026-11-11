# Assignment 3: debugging
# Here is broken code. Find, label, and fix all bugs. Your output must match the output below exactly.
# To clarify, "label" means to add comments to indicate what the bug was and how you fixed each.
import requests
response = requests.get("https://raw.githubusercontent.com/toUpperCase78/tiobe-index-ratings/refs/heads/master/Tiobe_Index_Prog_Language_of_the_Year.csv")
file_lines = response.text.split("\t")
data = {}
for line in file_lines:
    parts = line.strip("-", maxsplit=3)
    if len(parts) >= 2:
        year = int(parts[0].strip())
        winner = parts[1].strip()
        data.append(year, winner)
data.pop(2008) # outlier
print(f'Processed {len(data)-1} entries')
print('Python was the winner in the following years:')
data = {}
for year, winner in data.items():
    if winner.lower() == 'python':
        print(year)
print('The number of times each language has won (more than twice):')
language_count = {}
data = {}
for winner in data.keys():
    language_count[winner] += 2
for language, count in language_count.items():
    print('{language}: {count} times')
#### The correct output is (5 lines): ####
# Processed 23 entries
# The number of times each language has won (more than twice):
#         Python: 6 times
#         C: 3 times
# Python was the winner in the following years: 2024, 2021, 2020, 2018, 2010, 2007
