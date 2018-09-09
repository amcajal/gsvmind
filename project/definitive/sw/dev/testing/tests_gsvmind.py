################################################################################
#   Project: GSVMind
#
#   File: tests_gsvmind.py
#
#   Description: Tests definition for the whole GSVmind project.
#				These tests can be considered as "integration tests",
#				as they check the proper behaviour of the whole system.
#				These tests can be used to obtain user acceptance; that
#				is, the solution developed meets the user requirements
#				and thus, the application meets its goals. 
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
import subprocess

################################################################################
# Utility functions: These functions contains functionality required to perform
# the tests, but cannot be include as TestCase class methods because they are
# executed as tests itselfs, so they are added as stand-alone functions.
################################################################################

################################################################################

class TestGSVmind(unittest.TestCase):
	'''
	Tested requirements:
		(All tests, but more directly):
		UR: 001, 002
		HLR: 001, 002, 003, 004, 006
		LLR: 040, 041, 042, 043, 044, 045
		
	Description:
		Test GSVmind fullfill all of its requirements. Its goal is
		to achieve the User Requirements: generate random english
		phrases, with a maximun length, suitable to be used like
		"GSV names" (The Cultre series by Ian M. Banks), and generated
		using Internet data (random too).
		Tests are performed trying to reproduce the user actions. Thus,
		the application is launched from command line, insted of call
		its main method in the test.
		
	Preconditions:
		All module tests should pass before attempt these ones.
		Output shall be redirected to a file, so it can be analyzed.
		
	Input:
		N/A
		
	Procedure:
		- Launch GSVmind application from a system console
		- Check it finishes correctly and it generates the expected output
		
	Output:
		- File with stdout output
		- Log
		 
	Postconditions:
		N/A
		
	Expected results:
		- Application finishes successfully (no errors arise)
		- Log is correct
		- Stdout captured is correct.
		
	Errors:
		- Application fails (see Notes section)
		- Log is incorrect
		- Stdout is incorrect
		
	Side effects:
		N/A
		
	Notes:
		As defined by requirements, application could fail but still
		successfull (if the error is detected and controled). A full
		test environment will include test cases to detect if the
		application "fails good". However, due to the scope of the
		project, it will be considered that only successfull executions
		are valid.
	'''
	def test_gsvmind(self):
		python_command = "python"
		gsvmind = "../src/gsvmind.py"
		h_param = "-h"
		v_param = "-v"
		invalid_param = "-a"
				
		working_commands = [
			[python_command, gsvmind, h_param], # Print application help message
			[python_command, gsvmind, v_param],  # print application version message
			[python_command, gsvmind] # Normal launch
		]
			
		failing_commands = [
			[python_command, gsvmind, invalid_param], # Invalid parameter.
		]
		
		
		for w in working_commands:
			ret_value = subprocess.call(w)
			self.assertTrue(ret_value == 0, "Application should work, but it failed when launching:" + str(w))
			
			
		for f in failing_commands:
			ret_value = subprocess.call(f)
			self.assertTrue(ret_value != 0, "Application should fail, but exit with code 0 while launching:" + str(f))
			
		
################################################################################

if __name__ == '__main__':
	print "*"*20 + "\nRUNNING TESTS FOR GSVmind (whole system)\n" + "*"*20 + "\n"
	suite = unittest.TestLoader().loadTestsFromTestCase(TestGSVmind)
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
