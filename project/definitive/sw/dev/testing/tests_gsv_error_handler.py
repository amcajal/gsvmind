################################################################################
#   Project: GSVMind
#
#   File: tests_gsv_error_handler.py
#
#   Description: Test definitions for gsv_error_handler module,
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

from src import gsv_error_handler


################################################################################
# Utility functions: These functions contains functionality required to perform
# the tests, but cannot be include as TestCase class methods because they are
# executed as tests itselfs, so they are added as stand-alone functions.
################################################################################

# Text file where stdout is redirected
file_with_stdout = "tests_gsv_error_handler_stdout.txt"

# Error message format, as defined in LLR_003
error_message_format = "\n\n*****\nERROR\n*****\n<Description>\nGSV could not be awaken...\n\n"

# Part of the message format to be replaced
to_replace_part = "<Description>"

# Error codes as defined in LLR_004
valid_error_codes = [100, 200, 300]
non_valid_error_codes = ['', 0, 1, 9999] # code 9999, more than non_valid, is "reserved"
all_error_codes = valid_error_codes + non_valid_error_codes

# As defined in LLR_003
def get_expected_message(error_code):
	if (error_code == 100):
		error_description = "Application could not retrieve content from internet." \
			" This may be due to internet connection issues or Wikipedia issues."
	elif (error_code == 200):
		error_description = "Application could not obtain a valid english phrase."
	elif (error_code == 300):
		error_description = "Application could not write the output log."
	else:
		error_description= "Application finished due to an unknown error."

	expected_message = error_message_format.replace(to_replace_part, error_description)
	return expected_message

def get_stdout_content():
	reader = open(file_with_stdout, 'r')
	content = reader.read()
	reader.close()
	return content

################################################################################

class TestGsvErrorHandler(unittest.TestCase):
	'''
	Tested requirements:
		LLR_001, 002, 003, 004
	Description:
		Test gsv_error_handler module behaves as specified.
	Preconditions:
		Stdout redirected to a file to process the output.
	Input:
		- List of error codes to trigger all possible paths.
		- Path to file to save stdout.
		- Template with error message format in order to be compared and processed.
	Procedure:
		For all relevant ERROR_CODEs defined in LLR_004:
		- Feed it as input to the gsv_error_handler module, handle_error function. 
		- Check execution exits, and return code of module is 1.
		- Check Message printed (saved in a file) is the correct one.
		- Check format of the message is the correct one.
		Finally, check all iterations caused an SystemExit exception.
	Output:
		N/A (if correct, the gsv_error_handler shall exit execution)
	Postconditions:
		Stdout redirected again to default stdout.
	Expected results:
		In all cases, the execution exits, the return code is not '0', the message format
		is correct, and the message is the correct one related
		to the input ERROR_CODE.
		All executions are aborted properly.
	Errors:
		One or more executions are not aborted, or return a code '0'.
		Message format is incorrect, or message returned is not the correct one.
	Side effects:
		N/A
	Notes:
		N/A
	'''
	def test_error_handling_process(self):
		stdout = sys.stdout
		n_exits = 0

		for ec in all_error_codes:
			try:
				sys.stdout = open(file_with_stdout, 'w')
				gsv_error_handler.handle_error(ec)

			except SystemExit:
				self.assertTrue(sys.exc_value != 0, "Expected a return value different from 0")
				n_exits += 1

			finally:
				sys.stdout.close()
				sys.stdout = stdout
				stdout_content = get_stdout_content()
				expected_message = get_expected_message(ec)
				self.assertTrue(stdout_content == expected_message, "Stdout generated is not correct when checking code " + str(ec))

		self.assertTrue(n_exits == len(all_error_codes), "One or more executions did not exit as expected")

################################################################################

if __name__ == '__main__':
	print "*"*20 + "\nRUNNING TESTS FOR MODULE: GSV_ERROR_HANDLER\n" + "*"*20 + "\n"
	suite = unittest.TestLoader().loadTestsFromTestCase(TestGsvErrorHandler)
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
