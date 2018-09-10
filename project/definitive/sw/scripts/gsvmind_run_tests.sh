#!/bin/bash
################################################################################
#   Project: GSVmind
#
#   File: gsvmind_run_tests.sh
#
#   Description: Script to run automatically all tests of /test directory
#		The script also generates coverage data and an HTML report.
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
	echo "	gsvmind_run_tests.sh has finished successfully!"
	echo "##############################"
}

CURRENT_DIR=$(pwd)
################################################################################
print_info_message "GSVmind RUN TEST SCRIPT..."

cd ../dev/testing

for gsv_test_file in $(find ./ -regex ^\./tests.*\.py$); 
do 
	python $gsv_test_file
	if [ $? -ne 0 ]; then
		print_error_message "python $gsv_test_file"
	exit 1
fi

done;

################################################################################
cd $CURRENT_DIR
print_success_message
exit 0