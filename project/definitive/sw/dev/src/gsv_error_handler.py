################################################################################
#   Project: GSVMind
#
#   File: gsv_error_handler.py
#
#   Description: Module in charge of printing error messages, finishing execution 
#		and performing shutdown operations when required.
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

import logging

# As defined by LLR_003, LLR_004
def generate_error_message(error_code):
	# The final NEW_LINE char shall be removed, because the "print" instruction already adds one
	error_message_template = "\n\n*****\nERROR\n*****\n<Description>\nGSV could not be awaken...\n"
	replace_this = "<Description>"

	if (error_code == 100):
		error_description = "Application could not retrieve content from internet." \
		" This may be due to internet connection issues or Wikipedia issues."

	elif (error_code == 200):
		error_description = "Application could not obtain a valid english phrase."

	elif (error_code == 300):
		error_description = "Application could not write the output log."

	else:
		error_description = "Application finished due to an unknown error."

	final_error_message = error_message_template.replace(replace_this, error_description)
	return final_error_message
	

def clean_and_exit():
	'''
	At this moment, this method is quite useless, as it only
	contains a single statement. However, in the future, more
	operations could be required before exit the application,
	so it is left in this way.
	'''
	exit(1)


# As defined by LLR_002
def handle_error(error_code):
	error_message = generate_error_message(error_code)
	print error_message
	# As defined by LLR_027, LLR_029
	logging.info("ERROR:"+error_message+"\n")
	clean_and_exit()
