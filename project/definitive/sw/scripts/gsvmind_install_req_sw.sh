#!/bin/bash
################################################################################
#   Project: GSVmind
#
#   File: gsvmind_install_req_sw.sh
#
#   Description: Install required libraries, utilities, tools, etc,
#		to launch the application
#
#   Notes: Script needs to be launched with admin permissons
#	Script needs apt-get to install software.
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
	echo "	gsvmind_install_req_sw.sh has finished successfully!"
	echo "##############################"
}

################################################################################
print_info_message "THIS SCRIPT NEEDS TO BE LAUNCHED WITH ADMIN PERMISSIONS, OR IT WILL FAIL"

print_info_message "Installing Python 2..."
apt-get install python2
if [ $? -ne 0 ]; then
	print_error_message "apt-get install python2"
	exit 1
fi


print_info_message "Installing Python PIP..."
apt-get install python-pip
if [ $? -ne 0 ]; then
	print_error_message "apt-get install python-pip"
	exit 1
fi


print_info_message "Installing Python Requests library..."
pip install requests
if [ $? -ne 0 ]; then
	print_error_message "pip install requests"
	exit 1
fi


print_info_message "Installing Python BeautifulSoup library..."
apt-get install bs-4
if [ $? -ne 0 ]; then
	print_error_message "apt-get install bs-4"
	exit 1
fi


print_info_message "Installing Python TextBlob library..."
pip install -U textblob
if [ $? -ne 0 ]; then
	print_error_message "pip install -U textblob"
	exit 1
fi

# This command still related to TextBlob library
python -m textblob.download_corpora
if [ $? -ne 0 ]; then
	print_error_message "python -m textblob.download_corpora"
	exit 1
fi


print_info_message "Installing Coverage.py..."
pip install coverage
if [ $? -ne 0 ]; then
	print_error_message "pip install coverage"
	exit 1
fi
################################################################################
print_success_message
exit 0