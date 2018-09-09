#!/bin/bash
################################################################################
#   Project: GSVmind
#
#   File: setup.sh
#
#   Description: Script to perform basic setup for GSVmind project.
#		In order, it checks if the dependencies are satisfied,
#		then run the tests of the application, and generates
#		the main python file to be launched from the root 
#		directory of the project. If any of the stepts fails
#		(except last one), scripts warns about it and exits.
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
#   This file is part of GSVmind
#
#   GSVmind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   GSVmind is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

print_info_message()
{
	echo "\n\n##############################"
	echo "	$1"
	echo "##############################\n\n"
}

print_error_message()
{
	echo "##############################"
	echo "	A COMMAND HAS FAILED --->"
	echo "			$1"
	echo "##############################"
}


print_success_message()
{
	echo "##############################"
	echo "	GSVmind setup has finished successfully!"
	echo "##############################"
}

CURRENT_DIR=$(pwd)
SCRIPTS_DIR=./scripts
################################################################################
print_info_message "GSVmind SETUP SCRIPT..."

cd $SCRIPTS_DIR

print_info_message "Checking dependencies..."
sh ./gsvmind_check_dependencies.sh
if [ $? -ne 0 ]; then
	print_error_message "sh gsvmind_check_dependencies.sh"
	echo "System has not the required software installed. It can be installed lanching /scripts/gsvmind_install_req_sw.sh"
	exit 1
fi
	

print_info_message "Running tests..."
sh ./gsvmind_run_tests.sh
if [ $? -ne 0 ]; then
	print_error_message "sh ./tests/gsvmind_run_tests.sh"
	exit 1
fi


print_info_message "COVERAGE REPORT IS NOT GENERATED BECAUSE OF THE DURATION OF SUCH OPERATION\n
	To generate it, launch project/def/sw/scripts/gsvmind_gen_coverage_info.sh"


print_info_message "Creating python file in main directory..."
sh ./gsvmind_create_mod_main.sh
if [ $? -ne 0 ]; then
	echo "COULD NOT CREATE A MODIFIED FILE. Application can be launch from /src directory"
fi

cd $CURRENT_DIR
################################################################################
print_success_message
exit 0