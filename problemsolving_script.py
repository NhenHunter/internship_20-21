#!/usr/bin/env python3
#import needed packages
import io
import re

with open ("lyrics.txt", "r") as in_handle:
#read the file and store it in a variable, then remove spaces	
	lyrics = in_handle.read()
	lyrics = lyrics.replace(" ","")
print(lyrics)

#create dictionary
all_char = {}

#iterate over variable
for item in lyrics:
#add values and keys to dictionary, increasing each time character is iterated over	
	if item in all_char:
		all_char[item] += 1
	else:
		all_char[item] = 1

print(str(all_char))

#find MFI in dictionary and store in variable
key_max = max(all_char, key = all_char.get)

print(key_max)
#create list of characters stored based on max key (MFI)
final = re.split(key_max, lyrics)

print(final)
