################################################################################
#   Project: GSVMind
#
#   File: tests_gsv_feedback.py
#
#   Description: Tests definition for gsv_feedback module.
#
#   Notes: N/A
#
#   Contact: Alberto Martin Cajal, amartin.glimpse23<AT>gmail.com
#
#   URL: https://github.com/amcajal/gsvmind
#
#   License: GNU GPL v3.0
#
#   Copyright (C) 2018 Alberto Martin Cajal
#
#   This file is part of GSVMind.
#
#   GSVMind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   GSVMind is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import unittest
import os
import sys

sys.path.append('../')

from src import gsv_feedback


################################################################################
# Utility functions: These functions contains functionality required to perform
# the tests, but cannot be include as TestCase class methods because they are
# executed as tests itselfs, so they are added as stand-alone functions.
################################################################################

stdout = sys.stdout
file_with_stdout = "tests_gsv_feedback_stdout.txt"

# As defined by LLR_035
# Note that the data index starts at 0, but requirements starts at 1
# The ascii_art_message, when printed in order, its equivalente to the
# following (it has been tested manually)
'''
 .d8888b.   .d8888b.  888     888               d8b               888
d88P  Y88b d88P  Y88b 888     888               Y8P               888
888    888 Y88b.      888     888                                 888
888         "Y888b.   Y88b   d88P 88888b.d88b.  888 88888b.   .d88888
888  88888     "Y88b.  Y88b d88P  888 "888 "88b 888 888 "88b d88" 888
888    888       "888   Y88o88P   888  888  888 888 888  888 888  888
Y88b  d88P Y88b  d88P    Y888P    888  888  888 888 888  888 Y88b 888
 "Y8888P88  "Y8888P"      Y8P     888  888  888 888 888  888  "Y88888
'''

ASCII_ART_MESSAGE = [

[' ', '.', 'd', '8', '8', '8', '8', 'b', '.', ' ', ' ', ' ', '.', 'd', '8', '8', '8', '8', 'b', '.', ' ', ' ', '8', '8',
 '8', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
 'd', '8', 'b', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8', '8'], # Row 0

['d', '8', '8', 'P', ' ', ' ', 'Y', '8', '8', 'b', ' ', 'd', '8', '8', 'P', ' ', ' ', 'Y', '8', '8', 'b', ' ', '8', '8',
 '8', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
 'Y', '8', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8', '8'], # Row 1

['8', '8', '8', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', 'Y', '8', '8', 'b', '.', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8',
 '8', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
 ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8', '8'], # Row 2

['8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', 'Y', '8', '8', '8', 'b', '.', ' ', ' ', ' ', 'Y', '8',
 '8', 'b', ' ', ' ', ' ', 'd', '8', '8', 'P', ' ', '8', '8', '8', '8', '8', 'b', '.', 'd', '8', '8', 'b', '.', ' ', ' ',
 '8', '8', '8', ' ', '8', '8', '8', '8', '8', 'b', '.', ' ', ' ', ' ', '.', 'd', '8', '8', '8', '8', '8'], # Row 3

['8', '8', '8', ' ', ' ', '8', '8', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', '"', 'Y', '8', '8', 'b', '.', ' ', ' ', 'Y',
 '8', '8', 'b', ' ', 'd', '8', '8', 'P', ' ', ' ', '8', '8', '8', ' ', '"', '8', '8', '8', ' ', '"', '8', '8', 'b', ' ',
 '8', '8', '8', ' ', '8', '8', '8', ' ', '"', '8', '8', 'b', ' ', 'd', '8', '8', '"', ' ', '8', '8', '8'], # Row 4

['8', '8', '8', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', '8', '8', '8', ' ', ' ', ' ',
 'Y', '8', '8', 'o', '8', '8', 'P', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ',
 '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8'], # Row 5

['Y', '8', '8', 'b', ' ', ' ', 'd', '8', '8', 'P', ' ', 'Y', '8', '8', 'b', ' ', ' ', 'd', '8', '8', 'P', ' ', ' ', ' ',
 ' ', 'Y', '8', '8', '8', 'P', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ',
 '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', 'Y', '8', '8', 'b', ' ', '8', '8', '8'], # Row 6

[' ', '"', 'Y', '8', '8', '8', '8', 'P', '8', '8', ' ', ' ', '"', 'Y', '8', '8', '8', '8', 'P', '"', ' ', ' ', ' ', ' ',
 ' ', ' ', 'Y', '8', 'P', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ',
 '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', ' ', '"', 'Y', '8', '8', '8', '8', '8'] # Row 7 

]

def generate_expected_ascii_message():
	expected_ascii_message=""
	
	for row in ASCII_ART_MESSAGE:
		row_to_print = ""
		for char in row:
			row_to_print += char
		expected_ascii_message += row_to_print + "\n"
	return expected_ascii_message # To delete last \n"
	

def redirect_stdout_to_file():
	try:
		sys.stdout = open(file_with_stdout, 'w')
	except IOError:
		stdout = sys.stdout
		print "Cannot redirect the stdou to a file. Test cannot continue"
		exit(1)

	
def restart_stdout():
	sys.stdout.close()
	sys.stdout = stdout
	

def read_stdout_file():
	try:
		reader = open(file_with_stdout, 'r')
		current_ascii_message = reader.read()
		reader.close()
	except IOError:
		print "Cannot open text with current_ascii_message. Test cannot continue"
		exit(1)
	return current_ascii_message
			
			
def write_content(file_name, content):
	writer = open(file_name, 'w')
	writer.write(content)
	writer.close()
	
	
################################################################################

class TestGsvFeedback(unittest.TestCase):
	'''
	Tested requirements:
	Description:
	Preconditions:
	Input:
	Procedure:
	Output:
	Postconditions:
	Expected results:
	Errors:
	Side effects:
	Notes:
	'''
	def test_ascii_message_printing(self):
		expected_ascii_message = generate_expected_ascii_message()
		# Writting the expected message is optional, but allows to debug the output
		write_content("expected_ascii_message.txt", expected_ascii_message)
		
		# Check message is properly generated when correct indexes are commanded
		redirect_stdout_to_file()
		for i in range(0, len(ASCII_ART_MESSAGE)):
			gsv_feedback.print_message_line(i+1)
		restart_stdout()
		current_ascii_message = read_stdout_file()
		write_content("current_ascii_message.txt", current_ascii_message)
		self.assertTrue(expected_ascii_message == current_ascii_message, "The generated ascii message is not correct.") 
		
		
		# Check message is generated wrong when incorrect indexes are commanded
		redirect_stdout_to_file()
		# The are a lot of possible combinations to generate a wrong message.
		# Due to the scope of the project, one of the most simple ones is forced.
		gsv_feedback.print_message_line(-1)
		gsv_feedback.print_message_line(0)
		gsv_feedback.print_message_line(9)
		gsv_feedback.print_message_line(100)
		restart_stdout()
		current_ascii_message = read_stdout_file()
		self.assertTrue(expected_ascii_message != current_ascii_message, "The generated ascii message should be wrong, but it printed well.") 

################################################################################

if __name__ == '__main__':
	print "*"*20 + "\nRUNNING TESTS FOR MODULE: GSV_FEEDBACK\n" + "*"*20 + "\n"
	print "WARNING: This requirement may need VISUAL checking"
	suite = unittest.TestLoader().loadTestsFromTestCase(TestGsvFeedback)
	unittest.TextTestRunner(verbosity=2).run(suite)


'''
Tested requirements:
Description:
Preconditions:
Input:
Procedure:
Output:
Postconditions:
Expected results:
Errors:
Side effects:
Notes:

def test_name_of_test(self):
'''

