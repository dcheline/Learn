#!/usr/local/bin/python3 -tt

#importing the debugger
import pdb
import sys


def countWords (filename):

	f = open (filename, 'r')
	
	word_dict = {}
	words = []
	
	all_lines = f.readlines()
	for line in all_lines:
#		print ( line )					 # read a line at a time

		line_of_words = line.split ()    # split up all the words from the newly read line
#		print ( line_of_words )		
		
		for word in line_of_words:
			words.append ( word )   # take all the words from the newly read line and add it to the words list
		
#	print (words)
	
#	print ( sorted (words) )
#	sorted_words = sorted (words)
	
	for single in words:		
		if single in word_dict:
			word_dict [single] += 1
		else:
			word_dict [single] = 1
	
#	for key in word_dict:
#		print ( key, word_dict[key] )

				
#	print (word_dict)

	print ()
	print ( sorted (word_dict.keys()) )
	print ()

	for key in sorted (word_dict.keys()):   # print dictionary sorted by keys
		print ( key, word_dict[key] )
	
	print ()
	print ( sorted (word_dict.values()) )
	print ()

	for value in sorted (word_dict.values()):   # print dictionary sorted by values
		print ( value, word_dict[value] )






	f.close ()


def main ():
	
	countWords (sys.argv[1])
	
	
#	start debugging session
#	pdb.set_trace()



# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main ()
	