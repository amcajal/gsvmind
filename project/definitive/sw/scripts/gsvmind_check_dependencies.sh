#!/bin/bash
################################################################################
#   Project: GSVmind
#
#   File: gsvmind_check_dependencies.sh
#
#   Description: Check if the required libraries, utilities, tools, etc,
#		are present in the system and thus, the application can be launched.
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
	echo "	gsvmind_check_dependencies.sh has finished successfully!"
	echo "##############################"
}


################################################################################

print_info_message "Checking for Python 2..."
python2 --version
if [ $? -ne 0 ]; then
	print_error_message "python --version"
	exit 1
fi


print_info_message "Checking for pip..."
pip --version
if [ $? -ne 0 ]; then
	print_error_message "pip --version"
	exit 1
fi


print_info_message "Checking for Python Requests library..."
python -c "import requests"
if [ $? -ne 0 ]; then
	print_error_message "python -c \"import requests\""
	exit 1
fi


print_info_message "Checking for Python BeautifulSoup library..."
python -c "from bs4 import BeautifulSoup"
if [ $? -ne 0 ]; then
	print_error_message "python -c \"from bs4 import BeautifulSoup\""
	exit 1
fi


print_info_message "Checking for Python TextBlob library..."
python -c "from textblob import TextBlob"
if [ $? -ne 0 ]; then
	print_error_message "python -c \"import TextBlob\""
	exit 1
fi


print_info_message "Checking for Coverage.py ..."
coverage --version
if [ $? -ne 0 ]; then
	print_error_message "coverage --version"
	exit 1
fi

################################################################################
print_success_message
exit 0