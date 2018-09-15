################################################################################
#   Project: GSVMind
#
#   File: gsvmind.py
#
#   Description: GSVMind main file (entry point). It parses
#	the input arguments, and if correct, call the proper modules
#	to request internet data, analyze it, and generate the random
#	english phrase.
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

import sys
import datetime
import logging
import argparse
import gsv_web_scrapper
import gsv_nlp


################################################################################

def print_version_message():
	print "\n"
	print "GSVMind"
	print "Version 1.0.0"
	print "Generate random GSV names (like the ones from Culture series of Ian M Banks!)"
	print "Copyright (C) 2018 Alberto Martin Cajal"
	print "Application released under license GNU GPL v3.0"
	print "This is free software; see the source for copying conditions."\
		"There is NO warranty; not even for MERCHANTABILITY"\
		"or FITNESS FOR A PARTICULAR PURPOSE."
	print "Project hosted at: https://github.com/amcajal/gsvmind"
	print "Contact: Alberto Martin Cajal, amartin.glimpse23<AT>gmail.com"
	print "\n"


def parse_arguments(args):
	parser = argparse.ArgumentParser(
		description='Generate random GSV names (like the ones from Culture series of Ian M Banks!)',
		epilog="Example: $ python gsvmind.py")
	parser.add_argument(
		'-v', '--version', 
		action='store_true', 
		default='store_false',
		help='Print version information and exit')
	parsed_arguments = parser.parse_args(args)
	return parsed_arguments
    
    
def check_arguments(parsed_arguments):
	if parsed_arguments.version == True:
		print_version_message()
		exit(0)

		
def configure_log():
	file_suffix = "_gsvmind_log.txt"
	file_preffix = datetime.datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
	log_name = file_preffix + file_suffix
	logging.basicConfig(filename=log_name,level=logging.INFO,format='%(message)s')


def main(args):
	# As defined by LLR_043
	parsed_arguments = parse_arguments(args)
	check_arguments(parsed_arguments)
	
	# As defined by LLR_045
	configure_log()
	
	# As defined by LLR_029
	logging.info("GSVNAME log\n###########")
	
	# As defined by LLR_043
	text_data = gsv_web_scrapper.get_text_data()
	gsv_name = gsv_nlp.generate_english_phrase(text_data)

	# As defined by LLR_044
	print "\nGSV operative! It decided to name itself:\"" + gsv_name.title() +"\"\n"
	
	
if __name__ == "__main__":
	main(sys.argv[1:])
	exit(0)
