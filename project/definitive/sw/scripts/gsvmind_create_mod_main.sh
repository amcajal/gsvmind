#!/bin/bash
################################################################################
#   Project: GSVmind
#
#   File: gsvmind_create_mod_main.sh
#
#   Description: Creates a modified version of the python entry point file
#		(gsvmind.py). Basically, it modifies its relative paths so
#		a copy of the file can be launched from the root directory of
#		the project, insted of launch the one in the /src directory.
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
	echo "	gsvmind_create_mod_main.sh has finished successfully!"
	echo "##############################"
}

SRC_DIR=./project/definitive/sw/dev/src
MAIN_FILE=gsvmind.py
CURRENT_DIR=$(pwd)
ROOT_DIR=../../../../
################################################################################
cd $ROOT_DIR
rm $MAIN_FILE # Delete previous files with same name 
cp $SRC_DIR/$MAIN_FILE ./
sed -i 's/import gsv_web_scrapper/import sys\nsys.path.append(".\/project\/definitive\/sw\/dev")\nfrom src import gsv_web_scrapper/' $MAIN_FILE
sed -i 's/import gsv_nlp/from src import gsv_nlp/' $MAIN_FILE
python $MAIN_FILE -v
if [ $? -ne 0 ]; then
	exit 1
fi
################################################################################
print_success_message
exit 0