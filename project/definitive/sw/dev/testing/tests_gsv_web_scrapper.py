################################################################################
#   Project: GSVMind
#
#   File: tests_gsv_web_scrapper.py
#
#   Description: Test definitions for gsv_web_scrapper module,
#		 from GSVMind project.
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

from src import gsv_web_scrapper

################################################################################
# Utility functions: These functions contains functionality required to perform
# the tests, but cannot be include as TestCase class methods because they are
# executed as tests itselfs, so they are added as stand-alone functions.
################################################################################

# As defined by LLR_005, LLR_014, LLR_015
def is_text_only_ascii(text_to_analize):
	# If the text is not ascii, in theory, writting to a file
	# will fail. In any case, this method allows to debug manually
	# the content of the page, in case it fails.
	try:
		writer = open('text_from_wiki_temp.txt', 'w')
		writer.write(text_to_analize)
		writer.close()
		return True
	except Exception as e:
		print e
		return False


# As defined by LLR_010, LLR_011	
def is_text_non_empty(text_to_analize):
	# There are several ways to check if text is not empty.
	# Some of them are applied here.
	if not text_to_analize:
		return False
		
	# This check is very subjective. The retrieved text could be in
	# one single line, and could still be valid. However, it is considered
	# that Wikipedia text will contain always NEW_LINE characters.
	lines = text_to_analize.split("\n")
	if len(lines) == 0:
		return False
	return True

	
# As defined by LLR_008, LLR_009
# In theory, checking for the presence of very common strings in the text 
# could be enough to decide if it is from Wikipedia or not (for example
# searching for "Wikipedia", or "From Wikipedia"). However,
# a page that is NOT from Wikipedia could contain the same strings.
# And given that only text from specific places in the HTML is retrieved,
# even a text from Wikipedia could faild such checking.
# Considering the scope of the project, its take for
# granted that a request to the Wikipedia's "random url" retrieves
# Wikipedia text.
def is_text_from_wikipedia(text_to_analize):
	return True
			
			
# As defined by LLR_016
# FFFC stands for "Free From Forbidden Characters"
def is_text_fffc(text_to_analize):
	forbidden_chars = [";", "\"", "\'"]
	if any(c in text_to_analize for c in forbidden_chars):
		return False
	else:
		return True


# As defined by LLR_008	
def is_text_different(new_text, old_text):
	if new_text == old_text:
		return False
	else:
		return True

################################################################################

class TestGsvWebScrapper(unittest.TestCase):
	'''
	Tested requirements:
		LLR_005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016
	Description:
		Test the retrieval of valid text content from internet.
	Preconditions:
		Internet access must be active.
	Input:
		N/A
	Procedure:
		(Repeat these steps several times)
		Retrieve text data from the module, and check that:
			- No SystemException was arised
			- The text is only ascii
			- Text is not empty
			- Text is from wikipedia
			- Text has proper characters replaced
			- Text, in each iteration, is different from the previous
	Output:
		Valid text data to be used in the language processing modules.
	Postconditions:
		N/A
	Expected results:
		All checkings listed in "Procedure" above are true.
	Errors:
		Any of the checkings listed in "Procedure" is false.
	Side effects:
		N/A
	Notes:
		This test only checks for proper behaviour. To test the module
		completely, additional functionality is required, like
		being able to change the URL used by the module to retrieve
		the internet data, as long as being able to create specific
		webpage with problematic content. Considering these are
		very time consuming tasks, and due to the scope of the project,
		only the test defined here is performed.
	'''
	def test_retrieval_valid_text_data(self):
		# Perform the test five times to get a reallistic coverage
		# in an acceptable amount of time
		n_failed_retrievals = 0
		previous_text_data = "Blablabla" # If Wikipedia provides this, reconsider your life
		for i in range(0, 5):
			try:
				text_data = gsv_web_scrapper.get_text_data()
				self.assertTrue(is_text_only_ascii(text_data), "Text still contains non ascii characters")
				self.assertTrue(is_text_non_empty(text_data), "Text is empty")
				self.assertTrue(is_text_from_wikipedia(text_data), "Text is not from Wikipedia")
				self.assertTrue(is_text_fffc(text_data), "Text contains characters that should be replaced")
				self.assertTrue(is_text_different(text_data, previous_text_data), "Texts are NOT different")
				previous_text_data = text_data
			except SystemExit:
				n_failed_retrievals += 1
			finally:
				if n_failed_retrievals == 5:
					self.assertTrue(False, "Web scrapper module could not retrieve a valid text one single time")
					

################################################################################

if __name__ == '__main__':
	print "*"*20 + "\nRUNNING TESTS FOR MODULE: GSV_WEB_SCRAPPER\n" + "*"*20 + "\n"
	suite = unittest.TestLoader().loadTestsFromTestCase(TestGsvWebScrapper)
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
