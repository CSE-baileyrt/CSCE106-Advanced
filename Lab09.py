# The purpose of this lab is to demonstrate mastery of classes, IO, and debugging
# NOTE: this assignment is identical to the one the rest of the class will do
 
# Write a program to identify the longest and shortest lyrics in the Disney dataset file
# In Lecture 14 (see Blackboard for the recording), we built a program that downloads Disney songs, 
#   stores the data in classes, and prints the "best" songs. You will expand on that program.
# The attached code will download the file, read its contents, and store all fields (including the lyrics).
# Task #1: read through the code and make sure you understand what it's doing
# Task #2: complete the 5 code changes at the bottom, marked with TO-DO notation.
#   We have calculated the longest and shortest items in several exercises. Review the class code if needed.
#   Remember that the average is the sum of all lyric lengths divided by the number of songs in the list

import requests

class disney_song:
    def __init__(self, rank, title, movie, year, lyrics):
        self.rank = rank
        self.title = title
        self.movie = movie
        self.year = year
        self.lyrics = lyrics

response = requests.get('https://raw.githubusercontent.com/hxchua/datadoubleconfirm/master/datasets/DisneySongs25.csv')
text_lines = response.text.split('\n')

song_list = []
for song_record in text_lines:
    song_details = song_record.split(',', 4) # maxsplit for the lyrics
    if len(song_details) > 4:
        # we don't really care if the rank is an int or a string
        song_rank = song_details[0].strip() # strip out whitespace
        song_title = song_details[1].strip()
        song_movie = song_details[2].strip()
        # same for the year- it can be a string (simpler)
        song_year = song_details[3].strip()
        song_lyrics = song_details[4].strip()
        new_song = disney_song(song_rank, song_title, song_movie, song_year, song_lyrics)
        song_list.append(new_song)
# song_list is now full
print("Found {} songs in the list".format(len(song_list)))

# NOTE: use these variables to complete the tasks below
longest_lyrics = 0      # length of the longest lyrics
long_lyr_song = ''      # name of the song with the longest lyrics
shortest_lyrics = 0     # length of the shortest lyrics
short_lyr_song = ''     # name of the song with the shortest lyrics
lyr_char_count = 0      # total number of characters in all songs

# loop through the list
# for song in song_list:
#   TODO: skip the header line
#   TODO: find the SHORTEST lyrics
#   TODO: find the LONGEST lyrics
#   TODO: find the average length of the lyrics

# done with the loop
# print the song title for the longest lyrics
print('The longest song is: ' + long_lyr_song)
# print the song title for the shorted lyrics
print('The shortest song is: ' + short_lyr_song)
# TODO: print the average length of the lyrics (for all 25 songs)
# print('The average lyric length is: ')
