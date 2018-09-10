#!/bin/bash
################################################################################
#   Project: GSVmind
#
#   File: gsvmind_gen_coverage_info.sh
#
#   Description: Script to automatically generate coverage data and an HTML report.
#
#   Notes: This script is basically a copy of gsvmind_run_tests.sh, but adding
#		the Coverage.py tool required commands to generate the coverage
#		info. Tests could be executed at the same time the coverage info
#		is retrieved. However, it has been considered better to separate
#		both goals. Because code coverage operations adds a penalty,
#		usually tests will be run first "as they are", to check functionality
#		only (check requirements are met). And if the functionality
#		is complete, then coverage data is obtained.
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
	echo "	gsvmind_gen_coverage_info.sh has finished successfully!"
	echo "##############################"
}

CURRENT_DIR=$(pwd)
SOURCE_DIR=../dev/src
################################################################################
print_info_message "GSVmind COVERAGE DATA GENERATION script..."

cd ../dev/test

# Delete all previous coverage data
coverage erase 
rm -r ./coverage_results

for gsv_test_file in $(find ./ -regex ^\./tests.*\.py$); 
do 
	coverage run --parallel-mode --source=$SOURCE_DIR --omit=/user/* $gsv_test_file
	if [ $? -ne 0 ]; then
		print_error_message "coverage run $gsv_test_file"
		exit 1
	fi

done;

coverage combine
coverage html -d ./coverage_results
if [ $? -ne 0 ]; then
	print_error_message "coverage html -d ./coverage_results"
	exit 1
fi
################################################################################
cd $CURRENT_DIR
print_success_message
exit 0