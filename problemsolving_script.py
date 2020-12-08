#!/usr/bin/env python3
#create dictionary
import io
import re
#find MFI in dictionary and store in variable
with open ("lyrics.txt", "r") as in_handle:
	lyrics = in_handle.read()
	lyrics = lyrics.replace(" ","")
#import needed packages
print(lyrics)
#create list of characters stored based on max key (MFI)
all_char = {}
#read the file and store it in a variable, then remove spaces
for item in lyrics:
	if item in all_char:
		all_char[item] += 1
	else:
		all_char[item] = 1

print(str(all_char))
#iterate over variable
#add values and keys to dictionary, increasing each time character is iterated over
key_max = max(all_char, key = all_char.get)
print(key_max)

final = re.split(key_max, lyrics)
print(final)
